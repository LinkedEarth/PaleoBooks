import itertools, json, yaml, pathlib, subprocess, requests
import os
from textwrap import dedent, indent
from truncatehtml import truncate


# from tagged_card

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


# def _generate_status_badge_html(repo, github_url):
#     binder_root, binder_link = _grab_binder_link(repo)
#     github_id = _grab_github_id(repo)
#     return f"""
#     <a class="reference external" href="{github_url}/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="{github_url}/actions/workflows/nightly-build.yaml/badge.svg" /></a>
#     <a class="reference external" href="{binder_link}"><img alt="Binder" src="{binder_root}/badge_logo.svg" /></a>
#     <a class="reference external" href="https://zenodo.org/badge/latestdoi/{github_id}"><img alt="DOI" src="https://zenodo.org/badge/{github_id}.svg" /></a>
#     """


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


def _generate_tag_button(tag, tag_key, tag_type):
    tag_buttton_html = f"""<div class="{tag_key}"><input class=hidden name="{tag_type}" type="checkbox" value={tag.replace(" ", "-").lower()}><label onclick="change();">{tag}</label></div>"""

# <div id="{tag_key} pseudo-btn">
# <div id="pseudo-btn-{tag_type}">
# <label>
# <input type="checkbox" hidden='' value={tag.replace(" ", "-").lower()} onchange="change();"><span>{tag}</span>
# </label>
# </div>
# </div>

    return tag_buttton_html

def generate_repo_dicts(all_items):
    repo_dicts = []
    chapter_dicts = []
    for item in all_items:
        host = item['host'].strip()
        user = item['user'].strip()
        repo = item['repo_name'].strip()  # item.strip()
        github_url = item['repo_url'].strip()  # f"https://github.com/ProjectPythia/{repo}"
        cookbook_url = f"{host}/{repo}/README.html".strip()
        config_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"
        # print(item)
        master_tags = {}
        # Get information from _config (title, description, authors)
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
            # print('took the except through the title description author split')
            config = requests.get(config_url + '/_config.yml').content
            config_dict = yaml.safe_load(config)
            # with requests.get(config_url+'/_config.yml', 'r').content as file:
            #     config_dict = yaml.safe_load(file)
            cookbook_title = config_dict["title"]
            description = config_dict["description"] if 'description' in config_dict else ''
            authors = config_dict["author"] if 'author' in config_dict else ''

        # Get tags and thumbnail for repo
        try:
            gallery_info_url = config_url  # os.getcwd() + '/source/{}'.format(repo)
            # with open(gallery_info_url+'/meta_data/chapter_meta.yml', 'r') as file:
            #     gallery_info_dict = yaml.safe_load(file)

            gallery_info = requests.get(gallery_info_url + '/meta_data/chapter_meta.yml').content
            gallery_info_dict = yaml.safe_load(gallery_info)

            shortname = gallery_info_dict['shortname']
            thumbnail = gallery_info_dict["thumbnail"] if 'thumbnail' in gallery_info_dict else 'thumbnail.png'

            chapters = []
            for part in gallery_info_dict['parts']:
                type_tag = part['caption']
                type_stem = type_tag.lower().replace(' ', '_')
                for chapter in part['chapters']:
                    file_name = chapter['filename']
                    chapter_thumbnail = chapter['thumbnail'] if 'thumbnail' in chapter else ''
                    chapter_thumbnail = chapter_thumbnail if '.' in chapter_thumbnail else chapter_thumbnail + '.png' if len(
                        chapter_thumbnail) > 0 else chapter_thumbnail
                    chapter['type_tag'] = type_tag
                    chapter['tags']['formats'] = ['notebook', type_tag, shortname]
                    chapter['url'] = f'{host}/{repo}/notebooks/{type_stem}/{file_name}.html'
                    chapter['thumbnail_url'] = f'{gallery_info_url}/thumbnails/{chapter_thumbnail}'
                    tag_types = ['primary', 'secondary', 'info', 'caution']
                    tag_keys = ['formats', 'domains', 'packages']
                    _tag_html = '<div>'
                    for ip, tag_key in enumerate(tag_keys):
                        tag_type = tag_types[ip]
                        _tag_html += ''.join(
                            [_generate_tag_button(tag, tag_key, tag_type) for tag in chapter['tags'][tag_key]])
                    _tag_html += '</div>'
                    for tag_cat in chapter['tags'].keys():
                        if tag_cat not in master_tags:
                            master_tags[tag_cat] = []
                        master_tags[tag_cat] += chapter['tags'][tag_cat]

                    chapter['tags'] = {
                        k: v for k, v in chapter["tags"].items() if (v is not None and v[0] is not None)
                    }
                    chapter['tag_html'] = _tag_html
                    chapters.append(chapter)

            # meta_data_dir = '{}'.format(github_url.split('github.com/')[1])#https://raw.githubusercontent.com/{}/main/_gallery_info.yml'.format(github_url.split('github.com/')[1])
            # book_meta_loc = '/'.join([meta_data_dir, 'book_meta.yml'])
            # chapter_meta_loc = '/'.join([meta_data_dir, 'chapter_meta.yml'])
            # # f"https://raw.githubusercontent.com/ProjectPythia/{repo}/main/_gallery_info.yml"
            # book_meta_dict = yaml.safe_load(book_meta_loc)
            # chapter_meta_dict = yaml.safe_load(chapter_meta_loc)
            # print(gallery_info_dict["tags"])

        except:
            thumbnail = config_dict["thumbnail"] if 'thumbnail' in config_dict else 'thumbnail.png'
            master_tags = config_dict["tags"] if 'tags' in config_dict else {}

        thumbnail_url = f'{gallery_info_url}/thumbnails/thumbnail.png'
        # 'https://raw.githubusercontent.com/{}/main/{}'.format(github_url.split('github.com/')[1],
        #                                                                   thumbnail)

        for tag_cat in master_tags.keys():
            master_tags[tag_cat] = list(set(master_tags[tag_cat]))

        repo_tags = {
            k: v for k, v in master_tags.items() if (v is not None and v[0] is not None)
        }
        repo_tags['formats'].remove('notebook')
        # print('repo_tags', repo_tags['formats'].remove('notebook'))
        repo_dict = {
            "repo": repo,
            "github_url": github_url,
            "cookbook_url": cookbook_url,
            "cookbook_title": cookbook_title,
            "authors": authors,
            "thumbnail": thumbnail,
            "thumbnail_url": thumbnail_url,
            "description": description,
            "tags": repo_tags,
            'shortname': shortname
        }

        repo_dicts.append(repo_dict)
        chapter_dicts += chapters

    return {'repos': repo_dicts, 'chapters': chapter_dicts}


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
        f'<li><label class="dropdown-item checkbox {tag_key}"><input type="checkbox" rel={tag.replace(" ", "-").lower()} onchange="change();">&nbsp;{tag}</label></li>'
        for tag in tag_list
    )

    return f"""
<div class="dropdown">
<button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="{tag_key}Dropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
{tag_key.title()}</button>
<ul class="dropdown-menu" aria-labelledby="{tag_key}Dropdown">{options}</ul>
</div>\n
"""



def generate_menu(repo_dicts, submit_btn_txt=None, submit_btn_link=None):
    key_list = _generate_sorted_tag_keys(repo_dicts)

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
    panels_repos = []
    for repo_dict in repo_dicts['repos']:
        repo = repo_dict["repo"]
        github_url = repo_dict["github_url"]
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
        # tag_types = ['primary', 'secondary', 'info', 'caution']
        tags = []
        # _tag_html=''
        # for ip, tag_key in enumerate(tag_dict.keys()):
        #     tag_type = tag_types[ip]
        tag_types = ['primary', 'secondary', 'info', 'caution']
        tag_keys = ['formats', 'domains', 'packages']
        for ip, tag_key in enumerate(tag_keys):
                tag_type = tag_types[ip]
            # _tag_html += '\n'.join([_generate_tag_button(tag, tag_key, tag_type) for tag in tag_dict[tag_key]])
            # <button class ="sd-sphinx-override sd-btn sd-text-wrap sd-btn-{tag_type}" type="button" aria-pressed="false", rel = "{tag}", onchange = "change();">
            # {tag} </button > < input type = "button" rel = "{tag}" onchange = "change();" >
            # < a class ="sd-sphinx-override sd-btn sd-text-wrap sd-btn-info reference internal" href="#buttons" >
            # < span class ="std std-ref" > Buttons < /span > < /a >

            _tags = ', '.join([f':bdg-{tag_type}:`{tag}`' for tag in tag_dict[tag_key]])
            tags.append(_tags)
        tags = ', '.join(tags)
        # tags = ", ".join(tags)+'\n'
        tag_class_str = " ".join(tag_list_f).lower()

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
        # \t\t\t..raw:: html
        #
        # \t\t\t\t < img
        # src = "{thumbnail_url}"
        #
        # class ="gallery-thumbnail" / >
        panel = f"""\

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: {tag_class_str}
                    
                        .. card:: {cookbook_title}
                            :link: {cookbook_url}
                            :img-top: {thumbnail_url}
                            :img-alt: {thumbnail}
                               
                                
                            {tags}

            
        """
        panels_repos.append(panel)

    panels_chapters = []
    for repo_dict in repo_dicts['chapters']:
        repo = repo_dict["filename"]
        cookbook_url = repo_dict["url"]
        cookbook_title = repo_dict["shortname"]

        # authors = repo_dict["authors"]
        # authors_str = f"<strong>Author:</strong> {authors}"

        thumbnail = repo_dict["thumbnail"]
        thumbnail_url = (repo_dict["thumbnail_url"]
        )

        tag_dict = repo_dict["tags"]
        tag_list = sorted((itertools.chain(*tag_dict.values())))
        tag_list_f = [tag.replace(" ", "-") for tag in tag_list]
        tag_types = ['primary', 'secondary', 'info', 'caution']
        tags = []
        for ip, tag_key in enumerate(tag_dict.keys()):
            tag_type = tag_types[ip]
            _tags = ', '.join([f':bdg-{tag_type}:`{tag}`' for tag in tag_dict[tag_key]])
            tags.append(_tags)
        tags = ', '.join(tags)
        # tags = ", ".join(tags)+'\n'
        tag_class_str = " ".join(tag_list_f).lower()
        tag_html = '\t' * 5 + repo_dict['tag_html']

        description = repo_dict["description"] if 'description' in repo_dict else ''
        ellipsis_str = '<a class="modal-btn"> ... more</a>'
        short_description = truncate(description, max_descr_len, ellipsis=ellipsis_str)

        if ellipsis_str in short_description:
            modal_str = f"""
                    <div class="modal">
                    <div class="content">
                    <img src="{thumbnail_url}" class="modal-img" />
                    <h3 class="display-3">{cookbook_title}</h3>
                    # {authors_str}
                    <p class="my-2">{description}</p>
                    <p class="my-2">{tags}</p>
                    <p class="mt-3 mb-0"><a href="{cookbook_url}" class="btn btn-outline-primary btn-block">Visit Website</a></p>
                    </div>
                    </div>
                    """
        else:
            modal_str = ""
        print(tag_html)
        panel = f"""\


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: {tag_class_str}
                    
                        .. card:: {cookbook_title}

                            .. image:: {thumbnail_url}
                                :alt: {thumbnail}
                                :align: center
                                :target: {cookbook_url}
                                
                            {tags}
                            
                            .. raw:: html

                                {tag_html}   

        """
        print('panel', panel)
        panels_chapters.append(panel)

    print('survived?')

    panels_repos = "\n".join(panels_repos)
    panels_chapters = "\n".join(panels_chapters)

    title = title
    stitle = f"{subtitle}" if subtitle else ""
    stext = subtext if subtext else ""

    modal_html = '<div class="modal-backdrop"></div>'
    panels = f"""

{title}
=====================
{stitle}
{stext}

.. raw:: html

{indent(menu_html, '    ')}

+++++++++++++++
PaleoBooks
+++++++++++++++

.. grid:: 1 2 2 2

{panels_repos}

+++++++++++++++
Chapters
+++++++++++++++

.. grid:: 1 2 2 2

{panels_chapters}


.. raw:: html

{indent(modal_html, '    ')}


"""

    pathlib.Path(f"{filename}.rst").write_text(panels)
# {dedent(panels_body)}

# ```
#
# .. raw:: html
#
#     <div class="modal-backdrop"></div>
#     <script src="doc/_static/custom.js"></script>
