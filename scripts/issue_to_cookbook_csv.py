#!/usr/bin/env python3
import csv
import json
import os
import re
from urllib.parse import urlparse
from pathlib import Path

CSV_PATH = Path("doc/cookbook_gallery.csv")
COLUMNS = [
    "repo_name",
    "repo_url",
    "host",
    "user",
    "landingpage",
    "landingpage_url",
    "config_url",
    "cookbook_loc",
    "branch",
    "published",
]
REQUIRED_FIELDS = [
    "repo_name",
    "repo_url",
    "host",
    "user",
    "landingpage_url",
    "branch",
]
KEY_VALUE_RE = re.compile(r"^\s*(?:\d+\.\s*)?([^:]+):\s*(.*)$")
TRUE_VALUES = {"true", "yes", "1"}
FALSE_VALUES = {"false", "no", "0"}


def fail(message: str) -> None:
    print(message.strip())
    raise SystemExit(1)


def load_event(path: str) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        fail(f"GITHUB_EVENT_PATH not found: {path}")
    except json.JSONDecodeError as exc:
        fail(f"Failed to parse GITHUB_EVENT_PATH JSON: {exc}")


def parse_issue_fields(body: str) -> dict:
    """
    Parse submission issues in two formats:
    - Exact CSV column keys (repo_name, repo_url, etc.)
    - Gallery submission template labels (human-friendly text)

    Human-error corrections applied later in main():
    - Always rewrite host to the landing page base (scheme + domain).
    - Always rewrite user to the GitHub repo owner from repo_url (when github.com).
    - If landingpage ends with .html, strip the suffix.
    """
    template_key_map = {
        "name of the repository": "repo_name",
        "repo url": "repo_url",
        "branch": "branch",
        "url of .config.yml": "config_url",
        "host for the jupyterbook": "host",
        "user": "user",
        "landing suffix (name of the page you want users to land on)": "landingpage",
        "landing page url": "landingpage_url",
    }

    data = {}
    for line in body.splitlines():
        match = KEY_VALUE_RE.match(line)
        if not match:
            continue
        key, value = match.groups()
        normalized_key = key.strip()
        if normalized_key in COLUMNS:
            target_key = normalized_key
        else:
            target_key = template_key_map.get(normalized_key.lower())
        if not target_key:
            continue
        data[target_key] = value.strip()

    if "published" in data:
        raw = data["published"].strip().lower()
        if raw in TRUE_VALUES:
            data["published"] = "True"
        elif raw in FALSE_VALUES:
            data["published"] = "False"
        else:
            fail(
                "Invalid published value. Allowed: true/false/yes/no/1/0 (case-insensitive)."
            )
    else:
        data["published"] = "False"

    return data


def derive_host_from_landingpage(landingpage_url: str) -> str:
    """Return scheme+netloc if possible; otherwise the first path segment."""
    parsed = urlparse(landingpage_url)
    if parsed.scheme and parsed.netloc:
        return f"{parsed.scheme}://{parsed.netloc}"
    return landingpage_url.split("/", 1)[0].strip()


def derive_landingpage_from_url(landingpage_url: str) -> str:
    """Return the URL tail without extension, if present."""
    parsed = urlparse(landingpage_url)
    path = (parsed.path or "").rstrip("/")
    if not path:
        return ""
    tail = path.rsplit("/", 1)[-1].strip()
    if not tail:
        return ""
    return os.path.splitext(tail)[0].strip()


def derive_github_owner(repo_url: str) -> str | None:
    """Extract GitHub owner from repo_url if it points at github.com."""
    parsed = urlparse(repo_url)
    netloc = parsed.netloc.lower() if parsed.netloc else ""
    if netloc and netloc != "github.com":
        return None
    path = parsed.path.lstrip("/")
    if not path:
        return None
    owner = path.split("/", 1)[0].strip()
    return owner or None


def validate_fields(data: dict) -> list:
    return [key for key in REQUIRED_FIELDS if not data.get(key, "").strip()]
        


def main() -> None:
    event_path = os.getenv("GITHUB_EVENT_PATH")
    if not event_path:
        fail("GITHUB_EVENT_PATH is not set.")

    event = load_event(event_path)
    issue = event.get("issue") or {}
    issue_number = issue.get("number")
    issue_url = issue.get("html_url") or ""
    labels = [label.get("name") for label in issue.get("labels", []) if label.get("name")]

    if "gallery submission" not in labels:
        print("Issue does not have 'gallery submission' label. Skipping.")
        return

    body = issue.get("body") or ""
    fields = parse_issue_fields(body)

    landingpage_url = fields.get("landingpage_url", "").strip()
    if landingpage_url:
        fields["host"] = derive_host_from_landingpage(landingpage_url)

    repo_url = fields.get("repo_url", "").strip()
    repo_owner = derive_github_owner(repo_url) if repo_url else None
    if repo_owner:
        fields["user"] = repo_owner

    landingpage = fields.get("landingpage", "").strip()
    if landingpage.endswith(".html"):
        fields["landingpage"] = landingpage[: -len(".html")]
    elif not landingpage and landingpage_url:
        fields["landingpage"] = derive_landingpage_from_url(landingpage_url)

    missing = validate_fields(fields)
    if missing:
        missing_list = ", ".join(missing)
        required_block = "\n".join(f"{key}:" for key in REQUIRED_FIELDS)
        message = (
            "Missing or empty required fields: "
            + missing_list
            + "\n\nPlease include the required keys in the issue body:\n```"
            + required_block
            + "\n```"
        )
        fail(message)

    if not CSV_PATH.exists():
        fail(f"CSV file not found: {CSV_PATH}")

    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        header = reader.fieldnames or []
        rows = list(reader)

    if header != COLUMNS:
        fail(
            "CSV header does not match expected columns. "
            f"Expected: {COLUMNS}. Found: {header}"
        )

    config_key = fields.get("config_url", "").strip()
    repo_key = fields.get("repo_url", "").strip()

    if not config_key and not repo_key:
        fail("Both config_url and repo_url are empty; cannot deduplicate.")

    match_index = None
    dedup_key = None

    if config_key:
        for idx, row in enumerate(rows):
            if row.get("config_url", "").strip() == config_key:
                match_index = idx
                dedup_key = "config_url"
                break

    if match_index is None and repo_key:
        for idx, row in enumerate(rows):
            if row.get("repo_url", "").strip() == repo_key:
                match_index = idx
                dedup_key = "repo_url"
                break

    if match_index is not None:
        rows[match_index] = {col: fields.get(col, "").strip() for col in COLUMNS}
        action = "update"
    else:
        rows.append({col: fields.get(col, "").strip() for col in COLUMNS})
        action = "append"
        dedup_key = dedup_key or "none"

    with CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    print(
        f"Issue #{issue_number} ({issue_url}): {action} row using {dedup_key} match."
    )


if __name__ == "__main__":
    main()
