import pytest

import gallery_generator_v2 as gallery


@pytest.mark.parametrize(
    ("filename", "expected"),
    [
        ("1_intro", "intro"),
        ("01_chapter_one", "chapter-one"),
        ("2025_results", "2025-results"),
        ("a_name_with_spaces", "a-name-with-spaces"),
        ("fish&chips", "fish-and-chips"),
    ],
)
def test_create_myst_slug_matches_expected_filename_rules(filename, expected):
    assert gallery.create_myst_slug(filename) == expected


def test_myst_slug_map_preserves_folders_and_maps_the_index_to_root():
    toc = {
        "parts": [
            {
                "caption": "Missing",
                "chapters": [
                    {"file": "intro.md"},
                    {"file": "notebooks/0_Data/1_chapter_one.ipynb"},
                    {"file": "notebooks/Methods/overview.md"},
                ],
            }
        ]
    }

    result = gallery.build_myst_slug_map(toc, folders_enabled=True)

    assert result["intro.md"] == ""
    assert result["notebooks/0_Data/1_chapter_one"] == "notebooks/data/chapter-one"
    assert result["notebooks/Methods/overview"] == "notebooks/methods/overview"


def test_flat_myst_slug_map_disambiguates_duplicate_basenames():
    toc = {
        "parts": [
            {
                "caption": "Missing",
                "chapters": [
                    {"file": "intro.md"},
                    {"file": "data/overview.md"},
                    {"file": "methods/overview.md"},
                ],
            }
        ]
    }

    result = gallery.build_myst_slug_map(toc, folders_enabled=False)

    assert result["data/overview"] == "overview"
    assert result["methods/overview"] == "overview-1"


def test_legacy_filename_map_keeps_source_paths():
    toc = {
        "parts": [
            {
                "caption": "Science",
                "chapters": [{"file": "notebooks/example"}],
            }
        ]
    }

    result = gallery.build_filename_map(toc)

    assert result["notebooks/example"] == "notebooks/example"
    assert result["example"] == "notebooks/example"

