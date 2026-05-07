import itertools, json, yaml, pathlib, subprocess, requests
import copy
import os
from abc import ABC, abstractmethod
from textwrap import dedent, indent
from truncatehtml import truncate
from urllib.parse import urlparse


# ── Utility functions (verbatim from gallery_generator.py) ────────────────────

def extract_files(data, result=None):
    if result is None:
        result = {}
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "file":
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


def fetch_thumbnail(_gallery_info_dict, gallery_info_url, fallback='thumbnail.png', host='https://projectpythia.org'):
    thumbnail = _gallery_info_dict.get("thumbnail", fallback)

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
    gallery_info_url = config_loc
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
    shortname = _repo_dict['shortname']

    chapter_thumbnail = _chapter.get('thumbnail', '')
    chapter_thumbnail = chapter_thumbnail if '.' in chapter_thumbnail else chapter_thumbnail + '.png' if len(
        chapter_thumbnail) > 0 else chapter_thumbnail
    _chapter['tags']['formats'] = ['notebook']

    if content_type_tag is not None:
        _chapter['content_type_tag'] = content_type_tag
        _chapter['tags']['formats'] += [content_type_tag]
    _chapter['tags']['book'] = [shortname]

    language = _chapter.get('language', 'python')
    if isinstance(language, str) == True:
        language = [language]
    _chapter['tags']['language'] = language
    _chapter['tags']['published'] = ['published'] if published is True else []
    _chapter['url'] = f'{cookbook_loc}/{url_tail}'
    _chapter['thumbnail_url'] = f'{gallery_info_url}/thumbnails/{chapter_thumbnail}'

    _chapter['tags'] = {
        k: v for k, v in _chapter["tags"].items() if (v is not None and len(v) > 0 and v[0] is not None)
    }

    return _chapter


# ── BookRepo ──────────────────────────────────────────────────────────────────

class BookRepo:
    """Owns all remote fetching and chapter normalization for one CSV row."""

    def __init__(self, item, logging=False):
        host = item['host'].strip()
        user = item['user'].strip()

        self.repo = item['repo_name'].strip()
        self.github_url = item['repo_url'].strip()
        self.published = item['published'].strip().lower() in ['true', '1', 'yes', 'True']

        print('repo: ', self.repo, 'user', user, 'host', host, 'published', self.published)

        landingpage = item['landingpage'].strip()
        landingpage_url = item['landingpage_url'].strip()
        branch = item['branch'].strip() or 'main'

        config_url, config_loc = _normalize_config_and_loc(
            item['config_url'].strip(), self.github_url, user, self.repo, branch
        )

        cookbook_loc = item['cookbook_loc'].strip().lstrip('/')
        if len(item['cookbook_loc']) == 0:
            cookbook_loc = f"{host}/{self.repo}".strip().lstrip('/')
        self.cookbook_loc = cookbook_loc
        self.cookbook_url = landingpage_url if len(landingpage_url) > 0 else f"{cookbook_loc}/{landingpage}.html".strip()
        print('cookbook_loc', cookbook_loc, self.cookbook_url)

        try:
            config = requests.get(config_url).content
            config_dict = yaml.safe_load(config)
        except:
            config_dict = {}

        self.gallery_info_url = config_loc
        print('gallery_info_url', self.gallery_info_url)

        # Raises on failure — caller catches and skips this repo
        gallery_info_dict, status1 = pull_gallery_info(self.gallery_info_url)
        status = status1 + '; '

        toc_info_dict__raw = fetch_toc_structure(self.gallery_info_url)
        status += 'toc parsed from myst.yml/_toc.yml; '

        if logging:
            print('toc_info_dict__raw', toc_info_dict__raw)
            print('gallery_info_dict', gallery_info_dict)

        self.title = gallery_info_dict.get('title', config_dict.get('title', gallery_info_dict.get('shortname', '')))
        self.authors = gallery_info_dict.get('author', config_dict.get('author', ''))
        self.description = gallery_info_dict.get('description', config_dict.get('description', ''))

        content_type = gallery_info_dict.get('type', 'PaleoBook')
        # Preserve substring check (Contract B)
        self.is_standalone = 'standalone' in content_type

        self.shortname = gallery_info_dict['shortname']
        self.thumbnail, self.thumbnail_url = fetch_thumbnail(
            gallery_info_dict, self.gallery_info_url, fallback='thumbnail.png', host=host
        )
        print(self.shortname, 'thumbnail', self.thumbnail, 'in', self.gallery_info_url)

        file_d = build_filename_map(toc_info_dict__raw, logging=logging)
        self._file_map = file_d

        # Proxy repo_dict for normalize_chapter_dict (needs 'shortname')
        _repo_proxy = {'shortname': self.shortname}

        content_types, gallery_info_dict = sort_content_types(gallery_info_dict)
        if logging:
            print('content_types', content_types)

        master_tags = {key: [] for key in ['formats', 'language', 'book', 'published', 'domains']}
        chapters = []
        for content_type_category in content_types:
            content_type_tag = content_type_category.get('caption', None)
            for chapter in content_type_category['chapters']:
                chapter = normalize_chapter_dict(
                    chapter, file_d, content_type_tag, _repo_proxy,
                    self.gallery_info_url, cookbook_loc, logging=logging
                )
                for tag_cat in chapter['tags'].keys():
                    if tag_cat not in master_tags:
                        master_tags[tag_cat] = []
                    master_tags[tag_cat] += chapter['tags'][tag_cat]
                chapters.append(chapter)

        self.chapters = chapters

        if logging:
            print('reached master tags', len(master_tags))

        for tag_cat in master_tags.keys():
            master_tags[tag_cat] = list(set(master_tags[tag_cat]))

        repo_tags = {
            k: v for k, v in master_tags.items() if (v is not None and len(v) > 0 and v[0] is not None)
        }
        # published excluded from tags (Contract A) — but still remove 'notebook' from formats
        if 'formats' in repo_tags:
            repo_tags['formats'] = [f for f in repo_tags['formats'] if f != 'notebook']
            if not repo_tags['formats']:
                del repo_tags['formats']
        repo_tags.pop('published', None)
        self.tags = repo_tags

        if logging:
            print('repo status', status)


# ── GalleryCard base class ────────────────────────────────────────────────────

class GalleryCard(ABC):
    """Abstract base providing shared static helpers for badge building and truncation."""

    _LANGUAGE_COLORS = {'R': 'mauve', 'python': 'teal', 'missing': 'gray'}

    @staticmethod
    def _compute_tag_class_str(tag_dict):
        tag_list = sorted(itertools.chain(*tag_dict.values()))
        return " ".join(t.replace(" ", "-") for t in tag_list).lower()

    @staticmethod
    def _truncate_description(description, max_len):
        ellipsis_str = '<a class="modal-btn"> ... more</a>'
        short = truncate(description, max_len, ellipsis=ellipsis_str)
        return short, ellipsis_str in short

    @abstractmethod
    def render(self, tag_types, max_descr_len=200):
        """Return (panel_rst, modal_html)."""


# ── RepoCard ──────────────────────────────────────────────────────────────────

class RepoCard(GalleryCard):

    def __init__(self, github_url, cookbook_url, title, authors, thumbnail,
                 thumbnail_url, description, tags, published):
        self.github_url = github_url
        self.cookbook_url = cookbook_url
        self.title = title
        self.authors = authors
        self.thumbnail = thumbnail
        self.thumbnail_url = thumbnail_url
        self.description = description
        self.tags = tags
        self.published = published

    @classmethod
    def from_book_repo(cls, book_repo):
        return cls(
            github_url=book_repo.github_url,
            cookbook_url=book_repo.cookbook_url,
            title=book_repo.title,
            authors=book_repo.authors,
            thumbnail=book_repo.thumbnail,
            thumbnail_url=book_repo.thumbnail_url,
            description=book_repo.description,
            tags=book_repo.tags,
            published=book_repo.published,
        )

    def render(self, tag_types, max_descr_len=200):
        cookbook_title = self.title
        cookbook_url = self.cookbook_url
        thumbnail = self.thumbnail
        thumbnail_url = self.thumbnail_url
        authors_str = f"<strong>Author:</strong> {self.authors}"

        print('repo', cookbook_title, cookbook_url)

        # Build a working copy that includes published for tag_class_str (Contract A)
        tag_dict = copy.deepcopy(self.tags)
        tag_dict['published'] = ['published'] if self.published else []

        tag_list = sorted(itertools.chain(*tag_dict.values()))
        tag_list_f = [tag.replace(" ", "-") for tag in tag_list]
        tag_class_str = " ".join(tag_list_f).lower()

        # Book badges
        hold_outs = []
        tags_book = ', '.join(f':bdg-danger:`{tag}`' for tag in tag_dict['book'])
        hold_outs += [f":`{t}`" for t in tag_dict['book']]
        tag_dict.pop('book')

        # Language badges
        tag_language_dict = self._LANGUAGE_COLORS
        if len(tag_dict['language']) == 1:
            language_color = tag_language_dict[tag_dict['language'][0]] if tag_dict['language'][0] in tag_language_dict else 'warning'
        else:
            language_color = 'light'
        tags_language = ', '.join(f':bdg-{language_color}:`{lang}`' for lang in tag_dict['language'])
        hold_outs += [f":`{lang}`" for lang in tag_dict['language']]
        tag_dict.pop('language')

        # Published badge (from bool, not from tags — Contract A)
        tags_published = ':bdg-warning:`published`' if self.published else ''
        tag_dict.pop('published')

        # Remaining cycling tags (with hold_outs, matching repo behavior)
        tags_parts = []
        for ip, tag_key in enumerate(tag_dict.keys()):
            tag_type = tag_types[ip]
            _tags = ' '.join(
                f':bdg-{tag_type}:`{tag}`' for tag in tag_dict[tag_key]
                if f':`{tag}`' not in hold_outs
            )
            tags_parts.append(_tags)
        tags = ', '.join(tags_parts)

        description = self.description
        short_description, was_truncated = self._truncate_description(description, max_descr_len)

        if was_truncated:
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


# ── ChapterCard ───────────────────────────────────────────────────────────────

class ChapterCard(GalleryCard):

    def __init__(self, filename, url, shortname, thumbnail, thumbnail_url, description, tags):
        self.filename = filename
        self.url = url
        self.shortname = shortname
        self.thumbnail = thumbnail
        self.thumbnail_url = thumbnail_url
        self.description = description
        self.tags = tags

    @classmethod
    def from_book_repo(cls, book_repo, chapter_dict):
        return cls(
            filename=chapter_dict['filename'],
            url=chapter_dict['url'],
            shortname=chapter_dict.get('shortname', book_repo.shortname),
            thumbnail=chapter_dict.get('thumbnail', ''),
            thumbnail_url=chapter_dict.get('thumbnail_url', ''),
            description=chapter_dict.get('description', ''),
            tags=chapter_dict.get('tags', {'language': ['python'], 'formats': ['notebook']}),
        )

    def render(self, tag_types, max_descr_len=200):
        cookbook_title = self.shortname
        cookbook_url = self.url
        thumbnail = self.thumbnail
        thumbnail_url = self.thumbnail_url

        print('chapter', cookbook_title, cookbook_url, self.tags.keys())

        _tag_dict = copy.deepcopy(self.tags)
        if 'language' not in _tag_dict:
            _tag_dict['language'] = ['python']

        # tag_class_str computed BEFORE removing 'notebook' (matching original line 122–123, 155)
        tag_list = sorted(itertools.chain(*_tag_dict.values()))
        tag_list_f = [tag.replace(" ", "-") for tag in tag_list]
        tag_class_str = " ".join(tag_list_f).lower()

        # Language badges — per-language color lookup (chapter behavior)
        tag_language_dict = self._LANGUAGE_COLORS
        language = _tag_dict.get('language', ['python'])
        if isinstance(language, list) and len(language) == 1:
            language_color = tag_language_dict.get(language[0], 'warning')
        else:
            language_color = 'light'

        tags_language = ', '.join(
            f':bdg-{tag_language_dict.get(lang, "warning")}:`{lang}`' for lang in _tag_dict['language']
        )
        print('made it past language for chapter, hold_outs', _tag_dict.keys())
        _tag_dict.pop('language')

        # Book badges
        tags_book = ', '.join(f':bdg-danger:`{tag}`' for tag in _tag_dict['book'])
        _tag_dict.pop('book')

        # Remove 'notebook' from formats ONLY for badge display (tag_class_str already computed above)
        if 'formats' in _tag_dict and 'notebook' in _tag_dict['formats']:
            _tag_dict['formats'].remove('notebook')

        # Remaining cycling tags (no hold_outs — chapter behavior)
        tags_parts = []
        for ip, tag_key in enumerate(_tag_dict.keys()):
            tag_type = tag_types[ip]
            _tags = ' '.join(f':bdg-{tag_type}:`{tag}`' for tag in _tag_dict[tag_key])
            tags_parts.append(_tags)
        tags = ', '.join(tags_parts)

        description = self.description if self.description else ''
        short_description, was_truncated = self._truncate_description(description, max_descr_len)

        if was_truncated:
            modal_str = f"""
                            <div class="modal">
                            <div class="content">
                            <img src="{thumbnail_url}" class="modal-img" />
                            <h3 class="display-3">{cookbook_title}</h3>
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
        return panel, modal_str


# ── Orchestration ─────────────────────────────────────────────────────────────

def generate_repo_dicts(all_items):
    repos = []
    chapters = []

    for item in all_items:
        try:
            br = BookRepo(item)
        except Exception:
            print('failed to pull gallery info for', item.get('repo_name', '?'))
            continue

        # Contract C: skip repos with missing title before creating a card
        if br.title == '':
            print('skipping repo with missing title', br.cookbook_url)
            continue

        if not br.is_standalone:
            repos.append(RepoCard.from_book_repo(br))

        chapters.extend(ChapterCard.from_book_repo(br, ch) for ch in br.chapters)

    print('leaving repo dicts', len(repos))
    return {'repos': repos, 'chapters': chapters}


def _generate_sorted_tag_keys(cards):
    key_set = set(itertools.chain(*[card.tags.keys() for card in cards]))
    return sorted(key_set)


def _generate_tag_set(cards, tag_key=None):
    tag_set = set()
    for card in cards:
        for k, e in card.tags.items():
            if tag_key and k != tag_key:
                continue
            for t in e:
                tag_set.add(t)
    return tag_set


def _generate_tag_menu(cards, tag_key):
    tag_set = _generate_tag_set(cards, tag_key)
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


def generate_menu(cards, submit_btn_txt=None, submit_btn_link=None):
    key_list = _generate_sorted_tag_keys(cards)
    print('key_list', key_list)

    menu_html = '<div class="d-sm-flex mt-3 mb-4">\n'
    menu_html += '<div class="d-flex gallery-menu">\n'
    if submit_btn_txt:
        menu_html += f'<div><a role="button" class="btn btn-primary btn-sm mx-1" href={submit_btn_link}>{submit_btn_txt}</a></div>\n'
    menu_html += "</div>\n"
    menu_html += '<div class="ml-auto d-flex">\n'
    menu_html += '<div><button class="btn btn-link btn-sm mx-1" onclick="clearCbs()">Clear all filters</button></div>\n'
    for tag_key in key_list:
        menu_html += _generate_tag_menu(cards, tag_key) + "\n"
    menu_html += "</div>\n"
    menu_html += "</div>\n"
    menu_html += '<script>$(document).on("click",function(){$(".collapse").collapse("hide");}); </script>\n'
    print('generated menu html')
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

    panels_repos = []
    for card in repo_dicts['repos']:
        panel, _ = card.render(tag_types, max_descr_len=max_descr_len)
        panels_repos.append(panel)

    panels_chapters = []
    authors_str = ''
    for card in repo_dicts['chapters']:
        print('build from chapter', card.url, card.tags.keys())
        panel, _ = card.render(tag_types, max_descr_len=300)
        panels_chapters.append(panel)
        print('built chapter panel', card.shortname, len(panels_chapters), len(repo_dicts['chapters']))

    panels_repos = "\n".join(panels_repos)
    panels_chapters = "\n".join(panels_chapters)

    stitle = f"{subtitle}" if subtitle else ""
    stext = subtext if subtext else ""

    # Contract D: modal_html is discarded; only the static backdrop is written
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
