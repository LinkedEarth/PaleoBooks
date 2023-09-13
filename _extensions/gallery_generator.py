import itertools, json, yaml, pathlib, subprocess, requests
from textwrap import dedent, indent
from truncatehtml import truncate


def _grab_binder_link(repo):
    config_url = (
        f"https://raw.githubusercontent.com/ProjectPythia/{repo}/main/_config.yml"
    )
    config = requests.get(config_url).content
    config_dict = yaml.safe_load(config)
    root = config_dict["sphinx"]["config"]["html_theme_options"]["launch_buttons"][
        "binderhub_url"
    ]
    end = f"/v2/gh/ProjectPythia/{repo}.git/main"
    url = root + end
    return root, url


def _generate_status_badge_html(repo, github_url):
    binder_root, binder_link = _grab_binder_link(repo)
    github_id = _grab_github_id(repo)
    return f"""
    <a class="reference external" href="{github_url}/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="{github_url}/actions/workflows/nightly-build.yaml/badge.svg" /></a>
    <a class="reference external" href="{binder_link}"><img alt="Binder" src="{binder_root}/badge_logo.svg" /></a>
    <a class="reference external" href="https://zenodo.org/badge/latestdoi/{github_id}"><img alt="DOI" src="https://zenodo.org/badge/{github_id}.svg" /></a>
    """


def _grab_github_id(repo):
    github_api_url = f"https://api.github.com/repos/ProjectPythia/{repo}"
    response = requests.get(github_api_url)
    return response.json()['id']


def _run_cffconvert(command):
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        output_dict = json.loads(stdout.decode("utf-8"))
        return output_dict
    else:
        error_message = stderr.decode("utf-8").strip()
        raise RuntimeError(f"cffconvert command failed: {error_message}")


def generate_repo_dicts(all_items):
    repo_dicts = []
    for item in all_items:
        host = item['host'].strip()
        repo = item['repo_name'].strip()  # item.strip()
        github_url = item['repo_url'].strip()  # f"https://github.com/ProjectPythia/{repo}"
        cookbook_url = f"{host}/{repo}/README.html".strip()

        try:
            citation_url = f"https://raw.githubusercontent.com/ProjectPythia/{repo}/main/CITATION.cff"
            cffconvert_command = f"cffconvert -f zenodo -u {citation_url}"
            citation_dict = _run_cffconvert(cffconvert_command)

            cookbook_title = citation_dict["title"]
            description = citation_dict["description"]
            creators = citation_dict["creators"]
            names = [item.get("name") for item in creators]
            authors = ", ".join(names)

        except:
            config_url = 'https://raw.githubusercontent.com/{}/main/_config.yml'.format(github_url.split('github.com/')[1])
            # f"https://raw.githubusercontent.com/ProjectPythia/{repo}/main/_config.yml"
            config = requests.get(config_url).content
            config_dict = yaml.safe_load(config)
            cookbook_title = config_dict["title"]
            description = config_dict["description"] if 'description' in config_dict else ''
            authors = config_dict["author"] if 'author' in config_dict else ''

        try:
            gallery_info_url = 'https://raw.githubusercontent.com/{}/main/_gallery_info.yml'.format(github_url.split('github.com/')[1])
            # f"https://raw.githubusercontent.com/ProjectPythia/{repo}/main/_gallery_info.yml"
            gallery_info_dict = yaml.safe_load(requests.get(gallery_info_url).content)
            thumbnail = gallery_info_dict["thumbnail"] if 'thumbnail' in gallery_info_dict else 'thumbnail.png'
            # print(gallery_info_dict["tags"])
            tag_dict = {
                k: v for k, v in gallery_info_dict["tags"].items() if (v is not None and v[0] is not None)
            }
        except:
            thumbnail = config_dict["thumbnail"] if 'thumbnail' in config_dict else 'thumbnail.png'
            tag_dict = {
                k: v for k, v in config_dict["tags"].items() if (v is not None and v[0] is not None)
            } if 'tags' in config_dict else {}

        thumbnail_url = 'https://raw.githubusercontent.com/{}/main/{}'.format(github_url.split('github.com/')[1],
                                                                              thumbnail)

        repo_dict = {
            "repo": repo,
            "github_url": github_url,
            "cookbook_url": cookbook_url,
            "cookbook_title": cookbook_title,
            "authors": authors,
            "thumbnail": thumbnail,
            "thumbnail_url": thumbnail_url,
            "description": description,
            "tags": tag_dict,
        }
        repo_dicts.append(repo_dict)

    return repo_dicts


def _generate_sorted_tag_keys(repo_dicts):
    key_set = set(
        itertools.chain(*[repo_dict["tags"].keys() for repo_dict in repo_dicts])
    )
    return sorted(key_set)


def _generate_tag_set(repo_dicts, tag_key=None):
    tag_set = set()
    for repo_dict in repo_dicts:
        for k, e in repo_dict["tags"].items():
            if tag_key and k != tag_key:
                continue
            for t in e:
                tag_set.add(t)

    return tag_set


def _generate_tag_menu(repo_dicts, tag_key):
    tag_set = _generate_tag_set(repo_dicts, tag_key)
    tag_list = sorted(tag_set)

    options = "".join(
        f'<li><label class="dropdown-item checkbox {tag_key}"><input type="checkbox" rel={tag.replace(" ", "-")} onchange="change();">&nbsp;{tag}</label></li>'
        for tag in tag_list
    )
    print(options)

    return f"""
<div class="dropdown">
<button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="{tag_key}Dropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
{tag_key.title()}</button>
<ul class="dropdown-menu" aria-labelledby="{tag_key}Dropdown">{options}</ul>
</div>\n
"""


def generate_menu(repo_dicts, submit_btn_txt=None, submit_btn_link=None):
    key_list = _generate_sorted_tag_keys(repo_dicts)
    print(key_list)

    menu_html = '<div class="d-sm-flex mt-3 mb-4">\n'
    menu_html += '<div class="d-flex gallery-menu">\n'
    if submit_btn_txt:
        menu_html += f'<div><a role="button" class="btn btn-primary btn-sm mx-1" href={submit_btn_link}>{submit_btn_txt}</a></div>\n'
    menu_html += "</div>\n"
    menu_html += '<div class="ml-auto d-flex">\n'
    menu_html += '<div><button class="btn btn-link btn-sm mx-1" onclick="clearCbs()">Clear all filters</button></div>\n'
    for tag_key in key_list:
        menu_html += _generate_tag_menu(repo_dicts, tag_key) + "\n"
    menu_html += "</div>\n"
    menu_html += "</div>\n"
    menu_html += '<script>$(document).on("click",function(){$(".collapse").collapse("hide");}); </script>\n'
    return menu_html


def build_from_repos(
        repo_dicts,
        filename,
        title="Gallery",
        subtitle=None,
        subtext=None,
        menu_html="",
        max_descr_len=300,
):
    # Build the gallery file
    panels_body = []
    for repo_dict in repo_dicts:
        repo = repo_dict["repo"]
        print(repo)
        github_url = repo_dict["github_url"]
        status_badges = _generate_status_badge_html(repo, github_url)

        cookbook_url = repo_dict["cookbook_url"]
        cookbook_title = repo_dict["cookbook_title"]

        authors = repo_dict["authors"]
        authors_str = f"<strong>Author:</strong> {authors}"

        thumbnail = repo_dict["thumbnail"]
        thumbnail_url = (repo_dict["thumbnail_url"]
        )

        tag_dict = repo_dict["tags"]
        tag_list = sorted((itertools.chain(*tag_dict.values())))
        tag_list_f = [tag.replace(" ", "-") for tag in tag_list]
        print('tags', tag_list_f)
        tag_types = ['primary', 'secondary', 'info', 'caution']
        tags = []
        for ip, tag_key in enumerate(tag_dict.keys()):
            tag_type = tag_types[ip]
            _tags = ', '.join([f':bdg-{tag_type}:`{tag}`' for tag in tag_dict[tag_key]])
            print(_tags)
            tags.append(_tags)
        print('tags', tags)
        tags = ', '.join(tags)
        # tags = ", ".join(tags)+'\n'
        tag_class_str = " ".join(tag_list_f)

        description = repo_dict["description"]
        ellipsis_str = '<a class="modal-btn"> ... more</a>'
        short_description = truncate(description, max_descr_len, ellipsis=ellipsis_str)

        if ellipsis_str in short_description:
            modal_str = f"""
                    <div class="modal">
                    <div class="content">
                    <img src="{thumbnail_url}" class="modal-img" />
                    <h3 class="display-3">{cookbook_title}</h3>
                    {authors_str}
                    <p class="my-2">{description}</p>
                    <p class="my-2">{tags}</p>
                    <p class="mt-3 mb-0"><a href="{cookbook_url}" class="btn btn-outline-primary btn-block">Visit Website</a></p>
                    </div>
                    </div>
                    """
        else:
            modal_str = ""

        panel=f"""\

    
                \t.. grid-item::
                            
                \t\t.. card:: {cookbook_title}
                \t\t\t:link: {cookbook_url}
                \t\t\t:img-top: {thumbnail_url}
                \t\t\t:img-alt:
                            
                \t\t\t{tags}
            
            
        """
        panels_body.append(panel)
# ---
# :column: + tagged-card {tag_class_str}
#
# <div class="d-flex gallery-card">
# <img src="{thumbnail_url}" class="gallery-thumbnail" />
# <div class="container">
# <a href="{cookbook_url}" class="text-decoration-none"><h4 class="display-4 p-0">{cookbook_title}</h4></a>
# <p class="card-subtitle">{authors_str}</p>
# <br/>
# <p class="my-2">{short_description}</p>
# </div>
# </div>
# {modal_str}
#
# +++
# <div class="tagsandbadges">
# {tags}
# <div>{status_badges}</div>
# </div>
#
# """
#         )
    print(panels_body)
    panels_body = "\n".join(panels_body)

    stitle = f"{subtitle}" if subtitle else ""
    stext = subtext if subtext else ""

    panels = f"""
    
{title}
=====================
{stitle}
{stext}

.. raw:: html

{indent(menu_html, '    ')}


.. grid:: 2 3 3 4

{panels_body}


"""

    pathlib.Path(f"{filename}.rst").write_text(panels)
# {dedent(panels_body)}

# ```
#
# .. raw:: html
#
#     <div class="modal-backdrop"></div>
#     <script src="doc/_static/custom.js"></script>
