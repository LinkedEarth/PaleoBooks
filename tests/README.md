# Gallery ingestion tests

These tests exercise the active ingestion path in
`_extensions/gallery_generator_v2.py` without building the full Sphinx site or
contacting GitHub.

Run the complete suite from the repository root:

```console
python -m pytest
```

Run one scenario while diagnosing a book:

```console
python -m pytest tests/test_book_ingestion.py -k jupyter_book_2 -vv
```

`make_stub_book` in `tests/conftest.py` creates a miniature book under pytest's
temporary directory. The mocked request client presents those local files to
the production ingestion code as raw GitHub URLs. Add a new test with only the
trait that caused trouble—for example, a duplicate filename, unusual nesting,
or missing metadata—and assert the expected card fields and published URLs.

The unit tests cover TOC normalization and URL-slug rules. The integration
tests cover complete Jupyter Book 1 and 2 ingestion, including metadata
precedence and TOC selection.

