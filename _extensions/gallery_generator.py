import itertools, json, yaml, pathlib, subprocess, requests
import os
from doctest import master
from textwrap import dedent, indent
from truncatehtml import truncate
import requests
from urllib.parse import urlparse


# from tagged_card
def make_repo_panel(repo_dict, tag_types, max_descr_len=200):
    github_url = repo_dict["github_url"]
    cookbook_url = repo_dict["cookbook_url"]
    cookbook_title = repo_dict["cookbook_title"]
    print('repo', cookbook_title, cookbook_url)

    authors = repo_dict["authors"]
    authors_str = f"<strong>Author:</strong> {authors}"

    thumbnail = repo_dict["thumbnail"]
    thumbnail_url = (repo_dict["thumbnail_url"]
    )

    tag_dict = repo_dict["tags"]
    tag_dict['published'] = ['published'] if repo_dict['published'] is True else []
    tag_list = sorted((itertools.chain(*tag_dict.values())))
    tag_list_f = [tag.replace(" ", "-") for tag in tag_list]

    hold_outs = []
    tag_type = 'danger'
    tags_book = [', '.join([f':bdg-{tag_type}:`{tag}`' for tag in tag_dict['book']])]
    tags_book = ', '.join(tags_book).lstrip(',').strip()
    hold_outs += [f":`{_language}`" for _language in tag_dict['book']]  # [tag_dict['book']]
    tag_dict.pop('book')
    # print('build_from_repos', tag_dict.keys())
    tag_language_dict = {'R': 'mauve', 'python': 'teal', 'missing': 'gray'}
    if len(tag_dict['language']) == 1:
        language_color = tag_language_dict[tag_dict['language'][0]] if tag_dict['language'][
                                                                           0] in tag_language_dict.keys() else 'warning'
    else:
        language_color = 'light'

    tags_language = [', '.join([f':bdg-{language_color}:`{_language}`' for _language in tag_dict['language']])]
    tags_language = ', '.join(tags_language).lstrip(',').strip()
    hold_outs += [f":`{_language}`" for _language in tag_dict['language']]  # tag_dict['language'] +
    # print(tag_dict.keys(), hold_outs)
    tag_dict.pop('language')
    print('made it past language, hold_outs', hold_outs)
    tag_type = 'warning'
    tags_published = [', '.join([f':bdg-{tag_type}:`published`' for tag in tag_dict['published']])]
    tags_published = ', '.join(tags_published).lstrip(',').strip()
    hold_outs += [f":`{_language}`" for _language in tag_dict['published']]  # [tag_dict['book']]
    tag_dict.pop('published')

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

                            .. card:: {cookbook_title} {tags_book} {tags_published} {tags_language}
                                :link: {cookbook_url}
                                :img-top: {thumbnail_url}
                                :img-alt: {thumbnail}

                                {tags}


            """
    return panel, modal_str

def make_chapter_panel(_repot_dict, tag_types, max_descr_len=200, authors_str=''):
    repo = _repot_dict["filename"]
    cookbook_url = _repot_dict["url"]
    cookbook_title = _repot_dict["shortname"]
    print('chapter', cookbook_title, cookbook_url, _repot_dict['tags'].keys())

    thumbnail = _repot_dict["thumbnail"]
    thumbnail_url = (_repot_dict["thumbnail_url"])
    # print('thumbnail_url', thumbnail_url)

    _tag_dict = _repot_dict.get("tags", {'language': ['python'], 'formats': ['notebook']})
    print('make_chapter_panel', 'initial chapter tag_dict', _tag_dict.keys())
    # it remains baffling why this is still an issue, but this is a hedge
    if 'language' not in _tag_dict.keys(): _tag_dict['language'] = ['python']
    # print('make_chapter_panel', 'initial chapter tag_dict', tag_dict)
    tag_list = sorted((itertools.chain(*_tag_dict.values())))
    tag_list_f = [tag.replace(" ", "-") for tag in tag_list]

    tag_language_dict = {'R': 'mauve', 'python': 'teal', 'missing': 'gray'}
    # print(cookbook_title, 'language', tag_dict['language'])
    language = _tag_dict.get('language', ['python'])
    if isinstance(language, list) is True and len(language) == 1:
        language_color = tag_language_dict.get(language[0],
                                               'warning')  # if tag_dict['language'][0] in tag_language_dict.keys() else 'warning'
    else:
        language_color = 'light'
    # print('make_chapter_panel', 'chapter tag_dict', tag_dict)

    # tag_type = tag_language_dict[language] if language in tag_language_dict.keys() else 'warning'
    tags_language = [', '.join(
        [f':bdg-{tag_language_dict.get(_language, "warning")}:`{_language}`' for _language in _tag_dict['language']])]
    tags_language = ', '.join(tags_language).lstrip(',').strip()
    _tag_dict.pop('language')
    print('made it past language for chapter, hold_outs', _tag_dict.keys())

    tag_type = 'danger'
    tags_book = [', '.join([f':bdg-{tag_type}:`{tag}`' for tag in _tag_dict['book']])]
    tags_book = ', '.join(tags_book).lstrip(',').strip()
    _tag_dict.pop('book')

    # tag_types = ['primary', 'secondary', 'success']
    tags = []
    _tag_dict['formats'].remove('notebook')
    for ip, tag_key in enumerate(_tag_dict.keys()):
        tag_type = tag_types[ip]
        _tags = ' '.join([f':bdg-{tag_type}:`{tag}`' for tag in _tag_dict[tag_key]])
        tags.append(_tags)
    tags = ', '.join(tags)
    tag_class_str = " ".join(tag_list_f).lower()

    description = _repot_dict["description"] if 'description' in _repot_dict else ''
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


    return panel, modal_str


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


def _normalize_config_and_loc(config_url, github_url, user, repo, branch):
    config_url = config_url.strip()
    if len(config_url) > 0:
        config_url = config_url.replace('github.com', 'raw.githubusercontent.com').replace('blob/', '')
        parsed = urlparse(config_url)
        config_path = parsed.path.rstrip('/')
        has_yaml_file = config_path.endswith('.yml') or config_path.endswith('.yaml')
        config_loc = config_url.rsplit('/', 1)[0] if has_yaml_file else config_url.rstrip('/')
        if not has_yaml_file:
            config_url = config_loc.rstrip('/') + '/_config.yml'
        return config_url, config_loc.rstrip('/')

    if 'tree' in github_url:
        base = f"https://raw.githubusercontent.com/{user}/{repo}/" + github_url.split('tree')[1].lstrip('/')
    elif 'blob' in github_url:
        base = f"https://raw.githubusercontent.com/{user}/{repo}/" + github_url.split('blob')[1].lstrip('/')
    else:
        base = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}"
    base = base.rstrip('/')
    return base + '/_config.yml', base


def _fetch_yaml(url):
    try:
        response = requests.get(url)
    except Exception:
        return None
    if response.status_code != 200:
        return None
    try:
        return yaml.safe_load(response.content)
    except yaml.YAMLError:
        return None


def _iter_myst_toc_files(toc_items):
    if not isinstance(toc_items, list):
        return
    for item in toc_items:
        if not isinstance(item, dict):
            continue
        file_path = item.get("file")
        if isinstance(file_path, str) and file_path.strip():
            yield file_path.strip()
        children = item.get("children")
        if isinstance(children, list):
            yield from _iter_myst_toc_files(children)


def _normalize_myst_toc(myst_dict):
    project = myst_dict.get("project", {}) if isinstance(myst_dict, dict) else {}
    toc = project.get("toc", []) if isinstance(project, dict) else []
    parts = []
    if not isinstance(toc, list):
        return {"parts": parts}

    for item in toc:
        if not isinstance(item, dict):
            continue
        title = item.get("title", "Missing")
        files = list(_iter_myst_toc_files([item]))
        if not files:
            continue
        parts.append(
            {"caption": title, "chapters": [{"file": file_path} for file_path in files]}
        )
    return {"parts": parts}


def _normalize_legacy_toc(toc_dict):
    if not isinstance(toc_dict, dict):
        return {"parts": []}
    if "parts" in toc_dict and isinstance(toc_dict["parts"], list):
        return {"parts": toc_dict["parts"]}
    if "chapters" in toc_dict and isinstance(toc_dict["chapters"], list):
        return {"parts": [{"caption": "Missing", "chapters": toc_dict["chapters"]}]}
    if "root" in toc_dict:
        return {"parts": [{"caption": "Missing", "chapters": [{"file": toc_dict["root"]}]}]}
    return {"parts": []}

def sort_content_types(_gallery_info_dict):
    if 'parts' in _gallery_info_dict.keys():
        content_type_label = 'parts'
    elif 'content_type' in _gallery_info_dict.keys():
        content_type_label = 'content_type'
    else:
        content_type_label = 'content_type'
        _gallery_info_dict[content_type_label] = [
            {key: _gallery_info_dict[key] for key in ['chapters', 'caption'] if key in _gallery_info_dict.keys()}]


    return _gallery_info_dict[content_type_label], _gallery_info_dict

def fetch_thumbnail(_gallery_info_dict, gallery_info_url, fallback ='thumbnail.png', host='https://projectpythia.org'):
    thumbnail = _gallery_info_dict.get("thumbnail",
                                       fallback)  # if 'thumbnail' in gallery_info_dict.keys() else 'thumbnail.png'

    if '.' not in thumbnail:
        thumbnail += '.png'

    thumbnail_url = f'{gallery_info_url}/thumbnails/{thumbnail}'
    r = requests.get(thumbnail_url)
    if r.status_code in ['404', 404]:
        thumbnail_url = f'{gallery_info_url}/{thumbnail}'
        r = requests.get(thumbnail_url)
        if r.status_code in ['404', 404]:
            thumbnail_url = '/'.join([host, '_static', 'logo.png'])

    return thumbnail, thumbnail_url


def fetch_toc_structure(base_url):
    myst_data = _fetch_yaml(base_url.rstrip("/") + "/myst.yml")
    if isinstance(myst_data, dict):
        myst_toc = _normalize_myst_toc(myst_data)
        if myst_toc.get("parts"):
            return myst_toc

    toc_data = _fetch_yaml(base_url.rstrip("/") + "/_toc.yml")
    if isinstance(toc_data, dict):
        return _normalize_legacy_toc(toc_data)
    return {"parts": []}

def build_toc_info_dict(toc_info_dict__raw):
    toc_info_dict = {}
    for content_type_category in toc_info_dict__raw.get('parts', []):
        caption = content_type_category.get('caption', 'Missing')
        toc_info_dict[caption] = {}
        for chapter in content_type_category.get('chapters', []):
            file_path = chapter.get('file', '')
            if not isinstance(file_path, str) or len(file_path.strip()) == 0:
                continue
            name = os.path.splitext(file_path.split('/')[-1])[0]
            chapt_tail = os.path.splitext(file_path)[0]
            toc_info_dict[caption][name] = chapt_tail
    return toc_info_dict

def build_filename_map(toc_structure, logging=False):
    file_map = {}
    parts = toc_structure.get("parts", []) if isinstance(toc_structure, dict) else []
    for content_type_category in parts:
        if not isinstance(content_type_category, dict):
            continue
        chapters = content_type_category.get("chapters", [])
        if not isinstance(chapters, list):
            continue
        for chapter in chapters:
            if not isinstance(chapter, dict):
                continue
            file_path = chapter.get("file")
            if not isinstance(file_path, str):
                continue
            file_path = file_path.strip()
            if not file_path:
                continue

            path_stem = os.path.splitext(file_path)[0]
            base_name = path_stem.split("/")[-1]
            base_name_with_ext = file_path.split("/")[-1]

            file_map[file_path] = path_stem
            file_map[path_stem] = path_stem
            file_map[base_name] = path_stem
            file_map[base_name_with_ext] = path_stem

    if logging is True:
        print('file_d', file_map)

    return file_map

def pull_gallery_info(config_loc):
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

    return gallery_info_dict, status1

def normalize_chapter_dict(_chapter, file_map, content_type_tag, _repo_dict, gallery_info_url, cookbook_loc, published=False, logging=False):
    if logging is True:
        print('normalize_chapter_dict chapter', type(_chapter))
    file_name = _chapter['filename']
    url_tail = file_map.get(file_name, file_name)
    shortname = _repo_dict['shortname']#

    chapter_thumbnail = _chapter.get('thumbnail', '')  # if 'thumbnail' in chapter else ''
    chapter_thumbnail = chapter_thumbnail if '.' in chapter_thumbnail else chapter_thumbnail + '.png' if len(
        chapter_thumbnail) > 0 else chapter_thumbnail
    _chapter['tags']['formats'] = ['notebook']

    if content_type_tag is not None:
        _chapter['content_type_tag'] = content_type_tag
        _chapter['tags']['formats'] += [content_type_tag]
    _chapter['tags']['book'] = [shortname]

    language = _chapter.get('language', 'python')
    # if 'language' in chapter.keys():
    #     language = chapter['language']
    # else:
    #     language = 'python'
    if isinstance(language, str) == True:
        language = [language]
    _chapter['tags']['language'] = language
    _chapter['tags']['published'] = ['published'] if published is True else []
    # chapter['tags']['formats'] = ['notebook', content_type_tag]
    # chapter['url'] = f'{cookbook_loc}/{url_tail}'
    _chapter['url'] = f'{cookbook_loc}/{url_tail}'  # if file_name in file_d.keys() else f'{cookbook_loc}/{url_tail}'

    _chapter['thumbnail_url'] = f'{gallery_info_url}/thumbnails/{chapter_thumbnail}'

    _chapter['tags'] = {
        k: v for k, v in _chapter["tags"].items() if (v is not None and len(v) > 0 and v[0] is not None)
    }

    return _chapter


def generate_repo_dicts(all_items):
    repo_dicts = []
    chapter_dicts = []
    logging = False

    for item in all_items:

        repo_dict = {}
        host = item['host'].strip()
        user = item['user'].strip()
        # repo = item['repo_name'].strip()  # item.strip()
        repo_dict.update({'repo': item['repo_name'].strip(), 'github_url':item['repo_url'].strip(),
                          'published':item['published'].strip().lower() in ['true', '1', 'yes', 'True']})
        # published =
        print('repo: ', repo_dict['repo'],'user', user, 'host', host, 'published', repo_dict['published'])
        landingpage = item['landingpage'].strip()
        landingpage_url = item['landingpage_url'].strip()
        # print(repo_dict)
        # github_url = item['repo_url'].strip()  # f"https://github.com/ProjectPythia/{repo}"
        branch = item['branch'].strip()
        if len(item['branch']) == 0:
            branch = 'main'

        config_url = item['config_url'].strip()
        config_url, config_loc = _normalize_config_and_loc(
            config_url, repo_dict['github_url'], user, repo_dict['repo'], branch
        )

        cookbook_loc = item['cookbook_loc'].strip().lstrip('/')
        if len(item['cookbook_loc']) == 0:
            cookbook_loc = f"{host}/{repo_dict['repo']}".strip().lstrip('/')
        repo_dict['cookbook_url'] = landingpage_url if len(landingpage_url)>0 else  f"{cookbook_loc}/{landingpage}.html".strip()
        print('cookbook_loc', cookbook_loc, repo_dict['cookbook_url'])
        master_tags = {key: [] for key in ['formats', 'language', 'book', 'published', 'domains']}
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

        # Get tags and thumbnail for repo
        status = ''
        # try:
            # assume config and gallery_info_url are the same...
        gallery_info_url = config_loc
        print('gallery_info_url', gallery_info_url)

        try:
            gallery_info_dict, status1 = pull_gallery_info(gallery_info_url)
        except:
            print('failed to pull gallery info for', repo_dict['repo'], 'with url', gallery_info_url)
            continue

        status += status1+'; '

        toc_info_dict__raw = fetch_toc_structure(gallery_info_url)
        status += 'toc parsed from myst.yml/_toc.yml; '
        if logging is True:
            print('toc_info_dict__raw', toc_info_dict__raw)

        if logging is True:
            print('gallery_info_dict', gallery_info_dict)

        # can phase out config_dict fallback
        repo_dict['cookbook_title'] = gallery_info_dict.get('title', config_dict.get('title', gallery_info_dict.get('shortname', '')))  # if 'author' in gallery_info_dict.keys() else ''
        repo_dict['authors'] = gallery_info_dict.get('author', config_dict.get('author', ''))  # if 'author' in gallery_info_dict.keys() else ''
        repo_dict['description'] = gallery_info_dict.get('description', config_dict.get('description', ''))  # if 'author' in gallery_info_dict.keys() else ''

        content_type = gallery_info_dict.get('type', 'PaleoBook')
        if 'standalone' in content_type: content_type = 'standalone'

        toc_info_dict = build_toc_info_dict(toc_info_dict__raw)

        repo_dict['shortname'] = gallery_info_dict['shortname']
        thumbnail, thumbnail_url = fetch_thumbnail(gallery_info_dict, gallery_info_url, fallback = 'thumbnail.png', host=host)
        repo_dict.update({'thumbnail': thumbnail, 'thumbnail_url': thumbnail_url})

        print(repo_dict['shortname'], 'thumbnail', thumbnail, 'in', gallery_info_url)

        file_d = build_filename_map(toc_info_dict__raw, logging=logging)

        chapters = []
        content_types, gallery_info_dict = sort_content_types(gallery_info_dict)

        if logging is True:
            print('content_types', content_types)
        for content_type_category in content_types:
            content_type_tag = content_type_category.get('caption', None)

            for chapter in content_type_category['chapters']:
                chapter = normalize_chapter_dict(chapter, file_d, content_type_tag, repo_dict, gallery_info_url, cookbook_loc, logging=logging)
                for tag_cat in chapter['tags'].keys():
                    if tag_cat not in master_tags:
                        master_tags[tag_cat] = []
                    master_tags[tag_cat] += chapter['tags'][tag_cat]

                chapters.append(chapter)

        if logging is True:
            print('reached end of try')

        if logging is True:
            print('repo status', status)

        if logging is True:
            print('reached master tags', len(master_tags))
        for tag_cat in master_tags.keys():
            master_tags[tag_cat] = list(set(master_tags[tag_cat]))

        repo_tags = {
            k: v for k, v in master_tags.items() if (v is not None and len(v)>0 and v[0] is not None)
        }
        if 'formats' in repo_tags: repo_tags['formats'].remove('notebook')
        repo_dict["tags"] = repo_tags

        if content_type != 'standalone':
            repo_dicts.append(repo_dict)

        chapter_dicts += chapters
        del(repo_dict)
        del(chapters)

    if logging is True:
        print('\n\n\n\nchapter dicts', len(chapter_dicts))

    print('leaving repo dicts', len(repo_dicts))
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

    options = "".join(
        f'<li><label class="dropdown-item checkbox {tag_key}">'
        f'<input type="checkbox" rel={tag.replace(" ", "-").lower()} onchange="change();">&nbsp;{tag}'
        f'</label></li>'
        for tag in tag_list
    )

    return f"""
<div class="dropdown">
  <button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle"
          type="button"
          id="{tag_key}Dropdown"
          data-toggle="dropdown"
          aria-haspopup="true"
          aria-expanded="false">
    {tag_key.title()}
  </button>
  <ul class="dropdown-menu dropdown-menu-scroll" aria-labelledby="{tag_key}Dropdown">
    {options}
  </ul>
</div>\n
"""


def generate_menu(repo_dicts, submit_btn_txt=None, submit_btn_link=None):
    key_list = _generate_sorted_tag_keys(repo_dicts)
    print('key_list', key_list)

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
    print('generated menu html')
    # print('\t', menu_html)
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
    for repo_dict in repo_dicts['repos']:
        # print('build from repos', repo_dict['cookbook_url'], repo_dict.keys())
        if repo_dict.get('cookbook_title', '') == '':
            print('skipping repo with missing title', repo_dict['cookbook_url'])
            continue
        authors = repo_dict["authors"]
        authors_str = f"<strong>Author:</strong> {authors}"
        cookbook_title = repo_dict["cookbook_title"]
        panel, modal_str = make_repo_panel(repo_dict, tag_types, max_descr_len=max_descr_len)

        panels_repos.append(panel)

    panels_chapters = []
    for repo_dict in repo_dicts['chapters']:
        print('build from chapter', repo_dict['url'], repo_dict.keys())
        panel, modal_str = make_chapter_panel(repo_dict, tag_types, max_descr_len=300, authors_str=authors_str)

        panels_chapters.append(panel)
        print('built chapter panel', cookbook_title, len(panels_chapters), len(repo_dicts['chapters']))

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

.. grid:: 1 2 3 3

{panels_repos}

+++++++++++++++
Chapters
+++++++++++++++

.. grid:: 1 2 3 3

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
