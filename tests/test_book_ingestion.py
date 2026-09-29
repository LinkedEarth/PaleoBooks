import gallery_generator_v2 as gallery


def _chapter(shortname, filename, thumbnail="chapter.png"):
    return {
        "shortname": shortname,
        "filename": filename,
        "thumbnail": thumbnail,
        "tags": {"domains": ["testing"], "packages": ["pytest"]},
    }


def _metadata(*chapters, title="Gallery title"):
    return {
        "title": title,
        "author": "Gallery Author",
        "description": "Metadata supplied by chapter_meta.yml",
        "shortname": "Stub",
        "type": "Paleobook",
        "thumbnail": "book.png",
        "parts": [{"caption": "Examples", "chapters": list(chapters)}],
    }


def test_jupyter_book_1_uses_legacy_toc_and_chapter_metadata(
    make_stub_book, use_stub_requests
):
    book, client = make_stub_book(
        config_name="_config.yml",
        config={
            "title": "Legacy config title",
            "author": "Legacy Author",
            "description": "Legacy description",
        },
        toc={
            "format": "jb-book",
            "root": "intro",
            "parts": [
                {
                    "caption": "Examples",
                    "chapters": [{"file": "notebooks/example"}],
                }
            ],
        },
        chapter_meta=_metadata(_chapter("Example", "notebooks/example")),
    )
    use_stub_requests(client)

    result = gallery.BookRepo(book.item)

    assert result.title == "Gallery title"
    assert result.authors == "Gallery Author"
    assert result.description == "Metadata supplied by chapter_meta.yml"
    assert result.chapters[0]["url"] == (
        "https://books.example.test/stub-book/notebooks/example"
    )
    assert any(url.endswith("/_toc.yml") for url in client.requested_urls)


def test_pure_jupyter_book_2_uses_myst_toc_without_config_or_legacy_toc(
    make_stub_book, use_stub_requests
):
    myst = {
        "version": 1,
        "project": {
            "title": "MyST project title",
            "toc": [
                {"file": "intro.md"},
                {
                    "title": "Data",
                    "children": [
                        {"file": "notebooks/0_Data/1_chapter_one.ipynb"}
                    ],
                },
            ],
        },
        "site": {"template": "book-theme", "options": {"folders": True}},
    }
    book, client = make_stub_book(
        config_name="myst.yml",
        config=myst,
        chapter_meta=_metadata(
            _chapter("Chapter one", "notebooks/0_Data/1_chapter_one")
        ),
    )
    use_stub_requests(client)

    result = gallery.BookRepo(book.item)

    assert result.title == "Gallery title"
    assert result.chapters[0]["url"] == (
        "https://books.example.test/stub-book/notebooks/data/chapter-one"
    )
    assert not any(url.endswith("/_toc.yml") for url in client.requested_urls)
    assert not any(url.endswith("/_config.yml") for url in client.requested_urls)


def test_jupyter_book_2_prefers_myst_when_legacy_toc_is_also_present(
    make_stub_book, use_stub_requests
):
    myst = {
        "version": 1,
        "project": {
            "toc": [
                {"file": "intro.md"},
                {"file": "notebooks/new_chapter.ipynb"},
            ]
        },
        "site": {"template": "book-theme"},
    }
    book, client = make_stub_book(
        config_name="myst.yml",
        config=myst,
        toc={"format": "jb-book", "root": "intro", "chapters": []},
        chapter_meta=_metadata(
            _chapter("New chapter", "notebooks/new_chapter")
        ),
    )
    use_stub_requests(client)

    result = gallery.BookRepo(book.item)

    assert result.chapters[0]["url"].endswith("/new-chapter")
    assert not any(url.endswith("/_toc.yml") for url in client.requested_urls)


def test_jupyter_book_2_full_paths_disambiguate_duplicate_flat_slugs(
    make_stub_book, use_stub_requests
):
    myst = {
        "version": 1,
        "project": {
            "toc": [
                {"file": "intro.md"},
                {"file": "data/overview.md"},
                {"file": "methods/overview.md"},
            ]
        },
        "site": {"template": "book-theme", "options": {"folders": False}},
    }
    book, client = make_stub_book(
        config_name="myst.yml",
        config=myst,
        chapter_meta=_metadata(
            _chapter("Data overview", "data/overview", "data.png"),
            _chapter("Methods overview", "methods/overview", "methods.png"),
        ),
    )
    use_stub_requests(client)

    result = gallery.BookRepo(book.item)

    assert [chapter["url"] for chapter in result.chapters] == [
        "https://books.example.test/stub-book/overview",
        "https://books.example.test/stub-book/overview-1",
    ]


def test_config_metadata_remains_a_fallback_for_legacy_books(
    make_stub_book, use_stub_requests
):
    metadata = _metadata(_chapter("Example", "notebooks/example"))
    metadata.pop("title")
    metadata.pop("author")
    metadata.pop("description")
    book, client = make_stub_book(
        config_name="_config.yml",
        config={
            "title": "Fallback title",
            "author": "Fallback author",
            "description": "Fallback description",
        },
        toc={
            "format": "jb-book",
            "root": "intro",
            "chapters": [{"file": "notebooks/example"}],
        },
        chapter_meta=metadata,
    )
    use_stub_requests(client)

    result = gallery.BookRepo(book.item)

    assert result.title == "Fallback title"
    assert result.authors == "Fallback author"
    assert result.description == "Fallback description"


def test_unknown_chapter_filename_exposes_the_current_fallback_behavior(
    make_stub_book, use_stub_requests
):
    myst = {
        "version": 1,
        "project": {"toc": [{"file": "intro.md"}, {"file": "known.ipynb"}]},
        "site": {"template": "book-theme"},
    }
    book, client = make_stub_book(
        config_name="myst.yml",
        config=myst,
        chapter_meta=_metadata(_chapter("Missing", "notebooks/not_in_toc")),
    )
    use_stub_requests(client)

    result = gallery.BookRepo(book.item)

    # This captures current behavior so a future validation change is explicit.
    assert result.chapters[0]["url"].endswith("/notebooks/not_in_toc")

