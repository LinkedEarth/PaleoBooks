#!/usr/bin/env python3
import csv
import json
import os
import re
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
    "landingpage",
    "landingpage_url",
    "config_url",
    "cookbook_loc",
    "branch",
]
KEY_VALUE_RE = re.compile(r"^(\w+):\s*(.*)$")
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
    data = {}
    for line in body.splitlines():
        match = KEY_VALUE_RE.match(line)
        if not match:
            continue
        key, value = match.groups()
        if key not in COLUMNS:
            continue
        data[key] = value.strip()

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

    if "submission" not in labels:
        print("Issue does not have 'submission' label. Skipping.")
        return

    body = issue.get("body") or ""
    fields = parse_issue_fields(body)

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
