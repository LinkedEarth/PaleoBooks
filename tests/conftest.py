from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

import pytest
import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXTENSIONS_DIR = PROJECT_ROOT / "_extensions"
sys.path.insert(0, str(EXTENSIONS_DIR))

import gallery_generator_v2 as gallery  # noqa: E402


@dataclass
class StubBook:
    """A tiny local book presented to the gallery as a remote repository."""

    root: Path
    base_url: str
    config_name: str

    @property
    def item(self) -> dict[str, str]:
        return {
            "repo_name": self.root.name,
            "repo_url": "https://github.com/example/stub-book",
            "host": "https://books.example.test",
            "user": "example",
            "landingpage": "intro",
            "landingpage_url": "https://books.example.test/stub-book/",
            "config_url": f"{self.base_url}/{self.config_name}",
            "cookbook_loc": "https://books.example.test/stub-book",
            "branch": "main",
            "published": "False",
        }


class StubResponse:
    def __init__(self, content: bytes = b"", status_code: int = 200):
        self.content = content
        self.status_code = status_code


class StubRequests:
    """Resolve raw-GitHub-style requests from one local stub-book directory."""

    def __init__(self, book: StubBook):
        self.book = book
        self.requested_urls: list[str] = []

    def get(self, url: str) -> StubResponse:
        self.requested_urls.append(url)
        prefix = self.book.base_url.rstrip("/") + "/"
        if not url.startswith(prefix):
            return StubResponse(status_code=404)

        relative_path = url[len(prefix) :]
        candidate = self.book.root / relative_path
        if not candidate.is_file():
            return StubResponse(status_code=404)
        return StubResponse(candidate.read_bytes(), status_code=200)


def _write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


@pytest.fixture
def make_stub_book(tmp_path):
    """Build a stub book and return it with its mocked requests client."""

    counter = 0

    def make(
        *,
        config_name: str,
        config: dict,
        chapter_meta: dict,
        toc: dict | None = None,
        myst: dict | None = None,
    ) -> tuple[StubBook, StubRequests]:
        nonlocal counter
        counter += 1
        root = tmp_path / f"stub_book_{counter}"
        root.mkdir()
        base_url = f"https://raw.githubusercontent.test/example/stub-book-{counter}/main"
        book = StubBook(root=root, base_url=base_url, config_name=config_name)

        _write_yaml(root / config_name, config)
        _write_yaml(root / "meta_data" / "chapter_meta.yml", chapter_meta)
        if toc is not None:
            _write_yaml(root / "_toc.yml", toc)
        if myst is not None and config_name != "myst.yml":
            _write_yaml(root / "myst.yml", myst)

        thumbnails = root / "thumbnails"
        thumbnails.mkdir()
        (thumbnails / "book.png").write_bytes(b"stub image")
        for part in chapter_meta.get("parts", []):
            for chapter in part.get("chapters", []):
                thumbnail = chapter.get("thumbnail")
                if thumbnail:
                    (thumbnails / thumbnail).write_bytes(b"stub image")

        return book, StubRequests(book)

    return make


@pytest.fixture
def use_stub_requests(monkeypatch):
    """Patch the active gallery module to fetch from a generated stub book."""

    def use(client: StubRequests) -> StubRequests:
        monkeypatch.setattr(gallery.requests, "get", client.get)
        return client

    return use

