import itertools, json, yaml, pathlib, subprocess, requests
import os
from textwrap import dedent, indent
from truncatehtml import truncate
import requests


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

def extract_files(data, result=None):
    if result is None:
        result = {}
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "file":
                # Extract the file name after the last '/'
                file_name = value.split('/')[-1]
                result[file_name] = value
            elif isinstance(value, str):
                result[key] = value
            else:
                extract_files(value, result)
    elif isinstance(data, list):
        for item in data:
            extract_files(item, result)
    return result


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
    chapter_dicts = []
    logging = False

    for item in all_items:
        host = item['host'].strip()
        user = item['user'].strip()
        repo = item['repo_name'].strip()  # item.strip()
        print('repo: ', repo,'user', user, 'host', host)
        landingpage = item['landingpage'].strip()
        landingpage_url = item['landingpage_url'].strip()
        github_url = item['repo_url'].strip()  # f"https://github.com/ProjectPythia/{repo}"
        branch = item['branch'].strip()
        if len(item['branch']) == 0:
            branch = 'main'

        config_url = item['config_url'].strip()

        if len(config_url) > 0:
            config_url = config_url.replace('github.com', 'raw.githubusercontent.com').replace('blob/', '')

        if len(config_url) == 0:
            if 'tree' in github_url:
                config_url = f"https://raw.githubusercontent.com/{user}/{repo}/" + github_url.split('tree')[1].lstrip('/')
            elif 'blob' in github_url:
                config_url = f"https://raw.githubusercontent.com/{user}/{repo}/" + github_url.split('blob')[1].lstrip('/')
            else:
                config_url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}"
        #
            config_url = config_url.rstrip('/') + '/_config.yml'
        config_loc = config_url.split('_config')[0].rstrip('/')

        cookbook_loc = item['cookbook_loc'].strip().lstrip('/')
        if len(item['cookbook_loc']) == 0:
            cookbook_loc = f"{host}/{repo}".strip().lstrip('/')
        cookbook_url = landingpage_url if len(landingpage_url)>0 else  f"{cookbook_loc}/{landingpage}.html".strip()
        print('cookbook_loc', cookbook_loc, cookbook_url)
        master_tags = {}
        # Get information from _config (title, description, authors)
        # try:
        #     citation_url = f"https://raw.githubusercontent.com/ProjectPythia/{repo}/main/CITATION.cff"
        #     cffconvert_command = f"cffconvert -f zenodo -u {citation_url}"
        #     citation_dict = _run_cffconvert(cffconvert_command)
        #
        #     cookbook_title = citation_dict["title"]
        #     description = citation_dict["description"]
        #     creators = citation_dict["creators"]
        #     names = [item.get("name") for item in creators]
        #     authors = ", ".join(names)
        #
        # except:
            # print('took the except through the title description author split')
        try:
            config = requests.get(config_url).content
            config_dict = yaml.safe_load(config)
        except:
            config_dict = {}
        # print('config_dict', config_dict)
        # cookbook_title = config_dict["title"]
        # description = config_dict["description"] if 'description' in config_dict else ''
        # authors = config_dict["author"] if 'author' in config_dict else ''

        # Get tags and thumbnail for repo
        status = ''
        try:
            gallery_info_url = config_loc  # os.getcwd() + '/source/{}'.format(repo)
            gallery_info_raw = requests.get(gallery_info_url + '/meta_data/chapter_meta.yml').content
            try:
                encoding = 'utf-8'
                gallery_info = gallery_info_raw.decode(encoding, errors='replace')
            except:
                encoding = 'latin-1'
                gallery_info = gallery_info_raw.decode(encoding, errors='replace')
            status1 = f'first try {encoding}, length {len(gallery_info)} '
            if '404' in gallery_info:
                gallery_info_raw = requests.get(gallery_info_url + '/meta_data/chapter_meta.yaml').content
                try:
                    encoding = 'utf-8'
                    gallery_info = gallery_info_raw.decode(encoding, errors='replace')
                except:
                    encoding = 'latin-1'
                    gallery_info = gallery_info_raw.decode(encoding, errors='replace')
                status1 = f'second try {encoding}, length {len(gallery_info)} '
            if '404' in gallery_info:
                gallery_info_raw = requests.get(gallery_info_url + '/chapter_meta.yml').content
                try:
                    encoding = 'utf-8'
                    gallery_info = gallery_info_raw.decode(encoding, errors='replace')
                except:
                    encoding = 'latin-1'
                    gallery_info = gallery_info_raw.decode(encoding, errors='replace')
                status1 = f'third try {encoding}, length {len(gallery_info)} '
            if '404' not in gallery_info:
                try:
                    gallery_info_dict = yaml.safe_load(gallery_info)
                    status1 = f'parsed {encoding}, length {len(gallery_info)} '
                except yaml.YAMLError as exc:
                    print("Error parsing YAML:", exc)
                    status1 = f'failed parse {encoding}, length {len(gallery_info)} '


            status += status1+'; '
            # try:
            #     parsed_dict = ast.literal_eval(dict_str)

            # print('gallery_info_url', gallery_info_dict)
            # gallery_info_dict = yaml.safe_load(gallery_info)

            status2 = ''
            toc_url = gallery_info_url + '/_toc.yml'
            if logging is True:
                print('toc_url', toc_url)
            toc_info = requests.get(toc_url).content
            if logging is True:
                print('toc_info', toc_info)
            toc_info_dict__raw = yaml.safe_load(toc_info)
            tried1=False
            status2 = 'toc info dict raw loaded; '
            if 404 in toc_info_dict__raw.keys():
                # toc_url = 'https://raw.githubusercontent.com/croppers/cropper_ecs/refs/heads/main/_toc.yml?token=GHSAT0AAAAAADHBBOPZCYAZKLF3NPP6FPPA2DN5NBA'
                # toc_info = requests.get(toc_url).content
                print('tried 1', toc_url)
                tried1=True
                status2 = 'toc info dict tried 1; '
            if len(toc_info_dict__raw.keys())==1 and 404 in toc_info_dict__raw.keys():
                print('tried 2', toc_url)
            # toc_info_dict__raw = yaml.safe_load(toc_info)
            status += status2 +'; '
            if logging is True:
                print('toc_info_dict__raw', toc_info_dict__raw)

            if logging is True:
                print('gallery_info_dict', gallery_info_dict)
            status3 = ''
            if 'title' in gallery_info_dict.keys():
                cookbook_title = gallery_info_dict['title']
                status3 = 'title from gallery_info_dict; '
            else:
                cookbook_title = config_dict["title"]  if 'title' in config_dict.keys() else gallery_info_dict['shortname']
                status3 = 'title from config_dict; '

            status += status3 +'; '
            status4 = ''
            if 'author' in gallery_info_dict.keys():
                authors = gallery_info_dict['author']
                status4 = 'authors from gallery_info_dict; '
            else:
                authors = config_dict["author"] if 'author' in config_dict else ''
                status4 = 'authors from config_dict; '

            if 'description' in gallery_info_dict.keys():
                description = gallery_info_dict['description']
            else:
                description = config_dict["description"] if 'description' in config_dict else ''
            status += status4 +'; '

            status6 = ''
            content_type = 'PaleoBook'
            if 'type' in gallery_info_dict.keys():
                content_type = gallery_info_dict['type']
                if 'standalone' in content_type:
                    content_type = 'standalone'
            status6 = f'content_type {content_type}; '
            status += status6 +'; '

            status5 = ''
            if 'parts' not in toc_info_dict__raw.keys():
                if 'chapters' in toc_info_dict__raw.keys():
                    toc_info_dict__raw['parts']=[{'caption':'Missing', 'chapters': toc_info_dict__raw['chapters']}]
                    status5 = 'parts from chapters; '
                else:
                    toc_info_dict__raw['parts']=[{'caption':'Missing', 'chapters': [{'file': toc_info_dict__raw['root']}]}]
                    status5 = 'parts from root; '
            else:
                status5 = 'parts exist; '

            status += status5 +'; '
            toc_info_dict = {}
            for ip, content_type_category in enumerate(toc_info_dict__raw['parts']):

                toc_info_dict[content_type_category['caption']] = {}
                for chapter in content_type_category['chapters']:
                    name = chapter['file'].split('/')[-1].split('.')[0]
                    chapt_tail = chapter['file'].split('.')[0]
                    toc_info_dict[content_type_category['caption']][name] = chapt_tail
            if tried1 is True:
                print('toc_info_dict')

            shortname = gallery_info_dict['shortname']

            thumbnail = gallery_info_dict["thumbnail"] if 'thumbnail' in gallery_info_dict.keys() else 'thumbnail.png'
            if '.' not in thumbnail:
                thumbnail +='.png'
            print(shortname, 'thumbnail', thumbnail, 'in', gallery_info_url)
            # print('gallery_info_dict', gallery_info_dict)

            file_d = extract_files(toc_info_dict, result=None)
            if logging is True:
                print('file_d', file_d)

            chapters = []
            if 'parts' in gallery_info_dict.keys():
                content_type_label = 'parts'
            elif 'content_type' in gallery_info_dict.keys():
                content_type_label = 'content_type'
            else:
                content_type_label = 'content_type'
                gallery_info_dict[content_type_label] = [{key: gallery_info_dict[key] for key in ['chapters', 'caption'] if key in gallery_info_dict.keys()}]

            # if 'parts' not in gallery_info_dict.keys():
            #     gallery_info_dict['parts']=[{key: gallery_info_dict[key] for key in ['chapters', 'caption'] if key in gallery_info_dict.keys()}]# for 'chapters': toc_info_dict__raw['chapters']}]

            # if 'parts' in gallery_info_dict.keys():
            #     content_type_label = 'parts'
            # elif 'content_type' in gallery_info_dict.keys():
            #     content_type_label = 'content_type'

            content_types = gallery_info_dict[content_type_label]

            if logging is True:
                print('content_types', content_types)
            for content_type_category in content_types:
                content_type_tag = None
                if 'caption' in content_type_category.keys():
                    content_type_tag = content_type_category['caption']

                # if content_type_tag in toc_info_dict.keys():
                #     part_d = toc_info_dict[content_type_tag]
                # elif len(toc_info_dict.keys())==1:
                #     part_d = toc_info_dict[list(toc_info_dict.keys())[0]]
                #     content_type_tag = 'Science Workflows'
                # print(content_type_category)
                for chapter in content_type_category['chapters']:
                    if logging is True:
                        print('chapter', type(chapter))
                    file_name = chapter['filename']
                    if file_name in file_d.keys():
                        url_tail = file_d[file_name]#part_d[file_name]
                    else:
                        url_tail = file_name
                    chapter_thumbnail = chapter['thumbnail'] if 'thumbnail' in chapter else ''
                    # print('chapter_thumbnail', chapter_thumbnail)
                    chapter_thumbnail = chapter_thumbnail if '.' in chapter_thumbnail else chapter_thumbnail + '.png' if len(
                        chapter_thumbnail) > 0 else chapter_thumbnail
                    chapter['tags']['formats'] = ['notebook']
                    if content_type_tag is not None:
                        chapter['content_type_tag'] = content_type_tag
                        chapter['tags']['formats'] += [content_type_tag]
                    chapter['tags']['book'] = [shortname]

                    if 'language' in chapter.keys():
                        language = chapter['language']
                    else:
                        language = 'python'
                    if isinstance(language, str) == True:
                        language = [language]
                    chapter['tags']['language'] = language

                    # chapter['tags']['formats'] = ['notebook', content_type_tag]
                    # chapter['url'] = f'{cookbook_loc}/{url_tail}'
                    chapter['url'] = f'{cookbook_loc}/{url_tail}'# if file_name in file_d.keys() else f'{cookbook_loc}/{url_tail}'

                    chapter['thumbnail_url'] = f'{gallery_info_url}/thumbnails/{chapter_thumbnail}'

                    for tag_cat in chapter['tags'].keys():
                        if tag_cat not in master_tags:
                            master_tags[tag_cat] = []
                        master_tags[tag_cat] += chapter['tags'][tag_cat]

                    chapter['tags'] = {
                        k: v for k, v in chapter["tags"].items() if (v is not None and v[0] is not None)
                    }
                    # print(chapter)

                    chapters.append(chapter)

            # meta_data_dir = '{}'.format(github_url.split('github.com/')[1])#https://raw.githubusercontent.com/{}/main/_gallery_info.yml'.format(github_url.split('github.com/')[1])
            # book_meta_loc = '/'.join([meta_data_dir, 'book_meta.yml'])
            # chapter_meta_loc = '/'.join([meta_data_dir, 'chapter_meta.yml'])
            # # f"https://raw.githubusercontent.com/ProjectPythia/{repo}/main/_gallery_info.yml"
            # book_meta_dict = yaml.safe_load(book_meta_loc)
            # chapter_meta_dict = yaml.safe_load(chapter_meta_loc)
            # print(gallery_info_dict["tags"])
            if logging is True:
                print('reached end of try')

        except:
            thumbnail = config_dict["thumbnail"] if 'thumbnail' in config_dict else 'thumbnail.png'
            master_tags = config_dict["tags"] if 'tags' in config_dict else {}

        if logging is True:
            print('repo status', status)

        thumbnail_url = f'{gallery_info_url}/thumbnails/{thumbnail}'
        r = requests.get(thumbnail_url)
        if r.status_code in ['404', 404]:
            thumbnail_url = f'{gallery_info_url}/{thumbnail}'
            r = requests.get(thumbnail_url)
            if r.status_code in ['404', 404]:
                thumbnail_url = '/'.join([host, '_static', 'logo.png'])

        if logging is True:
            print('reached master tags', len(master_tags))
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

        if content_type != 'standalone':
            repo_dicts.append(repo_dict)
        # repo_dicts.append(repo_dict)
        chapter_dicts += chapters
        # print('chapter', chapters)

    if logging is True:
        print('\n\n\n\nchapter dicts', len(chapter_dicts))
    # print(chapter_dicts.keys())
    return {'repos': repo_dicts, 'chapters': chapter_dicts}


def _generate_sorted_tag_keys(repo_dicts):
    key_set = set(
        itertools.chain(*[repo_dict["tags"].keys() for repo_dict in repo_dicts])
    )
    # key_set.update(set(
    #     itertools.chain(*[repo_dict["shortname"] for repo_dict in repo_dicts])
    # ))
    # key_set.update(set(
    #     itertools.chain(*[repo_dict["type"] for repo_dict in repo_dicts])
    # ))
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
    # print(tag_list)

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
    # print('key_list', key_list)

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
    tag_types = ['emerald', 'success', 'primary', 'info', 'teal', 'warning', 'danger']

    # Build the gallery file
    panels_repos = []
    # print('repo_dicts', len(repo_dicts))
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

        hold_outs = []
        tag_type = 'danger'
        tags_book = [', '.join([f':bdg-{tag_type}:`{tag}`' for tag in tag_dict['book']])]
        tags_book = ', '.join(tags_book).lstrip(',').strip()
        hold_outs +=[f":`{_language}`" for _language in tag_dict['book']]  #[tag_dict['book']]
        tag_dict.pop('book')

        tag_language_dict = {'R':'mauve', 'python':'teal', 'missing':'gray'}
        if len(tag_dict['language']) == 1:
            language_color = tag_language_dict[tag_dict['language'][0]] if tag_dict['language'][0] in tag_language_dict.keys() else 'warning'
        else:
            language_color = 'light'

        tags_language = [', '.join([f':bdg-{language_color}:`{_language}`' for _language in tag_dict['language']])]
        tags_language = ', '.join(tags_language).lstrip(',').strip()
        hold_outs +=[f":`{_language}`" for _language in tag_dict['language']] #tag_dict['language'] +


        tag_dict.pop('language')

        tags = []
        for ip, tag_key in enumerate(tag_dict.keys()):
            # print('tag_key', tag_key)
            tag_type = tag_types[ip]
            _tags = ' '.join([f':bdg-{tag_type}:`{tag}`' for tag in tag_dict[tag_key] if f':`{tag}`' not in hold_outs])
            # print(tag_key, tag_dict[tag_key], _tags)

            tags.append(_tags)
        tags = ', '.join(tags)
        # tags = ", ".join(tags)+'\n'
        tag_class_str = " ".join(tag_list_f).lower()
        # print('tag_class_str', tag_class_str)

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

        panel = f"""\

                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: {tag_class_str}
                        :outline: {language_color}
                    
                        .. card:: {cookbook_title} {tags_book} {tags_language}
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
        thumbnail_url = (repo_dict["thumbnail_url"])

        tag_dict = repo_dict["tags"]
        tag_list = sorted((itertools.chain(*tag_dict.values())))
        tag_list_f = [tag.replace(" ", "-") for tag in tag_list]

        tag_language_dict = {'R':'mauve', 'python':'teal', 'missing':'gray'}
        if len(tag_dict['language']) == 1:
            language_color = tag_language_dict[tag_dict['language'][0]] if tag_dict['language'][0] in tag_language_dict.keys() else 'warning'
        else:
            language_color = 'light'

        # tag_type = tag_language_dict[language] if language in tag_language_dict.keys() else 'warning'
        tags_language = [', '.join([f':bdg-{tag_language_dict[_language] if _language in tag_language_dict.keys() else "warning"}:`{_language}`' for _language in tag_dict['language']])]
        tags_language = ', '.join(tags_language).lstrip(',').strip()
        tag_dict.pop('language')

        tag_type = 'danger'
        tags_book = [', '.join([f':bdg-{tag_type}:`{tag}`' for tag in tag_dict['book']])]
        tags_book = ', '.join(tags_book).lstrip(',').strip()
        tag_dict.pop('book')

        # tag_types = ['primary', 'secondary', 'success']
        tags = []
        tag_dict['formats'].remove('notebook')
        for ip, tag_key in enumerate(tag_dict.keys()):
            tag_type = tag_types[ip]
            _tags = ' '.join([f':bdg-{tag_type}:`{tag}`' for tag in tag_dict[tag_key]])
            tags.append(_tags)
        tags = ', '.join(tags)
        tag_class_str = " ".join(tag_list_f).lower()

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

        panel = f"""\


                .. grid-item::
                
                    .. tagged-card:: 
                        :tags: {tag_class_str}
                        :outline: {language_color}
                        
                        .. card:: {cookbook_title} {tags_book} {tags_language}
                            :link: {cookbook_url}
                            :img-top: {thumbnail_url}
                            :img-alt: {thumbnail}
                            
                            
                            
                            {tags}
                            

        """
        # print('panel', panel)
        panels_chapters.append(panel)

    # print('survived?')

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
