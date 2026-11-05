#!/usr/bin/env python3
"""Check distribution documentation, public release metadata and download links."""

import argparse
import json
import os
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]


def fetch_metadata(url):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "distribution-check"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urlopen(Request(url, headers=headers), timeout=30) as response:
        return json.load(response)


def check_local_links():
    files = list(ROOT.glob("*.md"))
    files.extend((ROOT / "docs").rglob("*.md"))
    errors = []
    for document in files:
        text = document.read_text(encoding="utf-8")
        for target in re.findall(r"!?\[[^\]]*\]\(([^)\s]+)\)", text):
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            destination = (document.parent / unquote(parts.path)).resolve()
            if not destination.is_relative_to(ROOT) or not destination.exists():
                errors.append(f"{document.relative_to(ROOT)}: missing local link {target}")
    return errors


def check_releases(configuration, downloads):
    repository = configuration["repository"]
    if re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository) is None:
        raise ValueError("Invalid repository name")
    api = f"https://api.github.com/repos/{repository}"
    metadata = fetch_metadata(api)
    if metadata["private"]:
        raise ValueError("The application distribution repository must be public")
    for expected in configuration["releases"]:
        release = fetch_metadata(f"{api}/releases/tags/{expected['tag']}")
        if release["draft"] or release["prerelease"] != expected["prerelease"]:
            raise ValueError(f"Unexpected release status: {expected['tag']}")
        assets = {asset["name"]: asset for asset in release["assets"]}
        for name in expected["assets"]:
            asset = assets.get(name)
            if asset is None or asset["size"] <= 0:
                raise ValueError(f"Missing or empty asset: {name}")
            if downloads:
                # Download links are public; never forward the API token to a CDN.
                request = Request(asset["browser_download_url"], method="HEAD")
                with urlopen(request, timeout=30) as response:
                    length = response.headers.get("Content-Length")
                    if length is not None and int(length) != asset["size"]:
                        raise ValueError(f"Download length differs from API metadata: {name}")
                    if "text/html" in response.headers.get("Content-Type", ""):
                        raise ValueError(f"An HTML page was returned instead of {name}")
            print(f"OK {expected['tag']} {name} ({asset['size']} bytes)")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--downloads", action="store_true", help="Also check public HTTP download links.")
    args = parser.parse_args()
    configuration = json.loads((ROOT / "distribution.json").read_text(encoding="utf-8"))
    errors = check_local_links()
    for folder in configuration.get("excluded_application_directories", []):
        if (ROOT / folder).exists():
            errors.append(f"Application sources or data do not belong in this distribution: {folder}")
    if errors:
        raise SystemExit("\n".join(errors))
    check_releases(configuration, args.downloads)


if __name__ == "__main__":
    main()
