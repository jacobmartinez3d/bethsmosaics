#!/usr/bin/env python3
"""Validate the published static artifact using only the Python standard library."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1] / "src"
EXPECTED_PAGES = {
    "index.html", "bio/index.html", "contact/index.html", "classes-and-shows/index.html",
    "portfolio/mexican-tile-sun-table/index.html",
    "portfolio/dancing-women-table/index.html",
    "portfolio/talavera-tile-night-stand/index.html",
    "portfolio/deer-in-the-trees-wall-hanging/index.html",
    "portfolio/potted-plant-holder/index.html",
    "portfolio/wooden-birds-wall-hanging/index.html",
    "portfolio/mountain-scene-wall-hanging/index.html",
    "portfolio/black-bear-wall-hanging/index.html",
    "portfolio/tree-of-life-table/index.html",
}

CONTENT_PAGES = {"index.html", "bio/index.html", "contact/index.html", "classes-and-shows/index.html"}
LEGACY_PAGES = EXPECTED_PAGES - CONTENT_PAGES


class Document(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.ids = []
        self.references = []
        self.images = []
        self.h1_count = 0
        self.redirect = None
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            delay, separator, target = attrs.get("content", "").partition(";")
            self.redirect = target.strip()[4:] if delay == "0" and separator and target.strip().lower().startswith("url=") else ""
            self.references.append(self.redirect)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "h1":
            self.h1_count += 1
        if tag == "img":
            self.images.append(attrs)
        if tag in {"a", "link"} and "href" in attrs:
            self.references.append(attrs["href"])
        if tag in {"img", "script", "source"} and "src" in attrs:
            self.references.append(attrs["src"])
        if "srcset" in attrs:
            self.references.extend(part.strip().split()[0] for part in attrs["srcset"].split(","))


def main():
    failures = []
    documents = {path.resolve(): Document(path) for path in ROOT.rglob("*.html")}
    actual = {str(path.relative_to(ROOT)) for path in ROOT.rglob("*.html")}
    for missing in sorted(EXPECTED_PAGES - actual):
        failures.append(f"Missing approved page: {missing}")
    for unexpected in sorted(actual - EXPECTED_PAGES):
        failures.append(f"Unexpected unapproved page: {unexpected}")
    for document in documents.values():
        name = document.path.relative_to(ROOT)
        if document.h1_count != 1:
            failures.append(f"{name}: expected one main heading")
        if "main" not in document.ids:
            failures.append(f"{name}: missing skip-link destination")
        if len(document.ids) != len(set(document.ids)):
            failures.append(f"{name}: duplicate IDs")
        contacts = {"mailto:bethemeyerson@gmail.com", "tel:+17079723040"}
        if name.as_posix() in LEGACY_PAGES:
            if document.redirect != "../../index.html#portfolio":
                failures.append(f"{name}: legacy artwork URL must return to the gallery")
        elif not contacts.issubset(document.references):
            failures.append(f"{name}: missing working email/phone destinations")
        for image in document.images:
            if not image.get("alt", "").strip():
                failures.append(f"{name}: artwork image missing descriptive alt text")
            if not all(image.get(key, "").isdigit() and int(image[key]) > 0 for key in ("width", "height")):
                failures.append(f"{name}: image missing intrinsic dimensions")
        for reference in document.references:
            url = urlsplit(reference)
            if url.scheme or url.netloc:
                if url.netloc.endswith("wixstatic.com") or url.netloc.endswith("bethsmosaics.com"):
                    failures.append(f"{name}: migrated content still depends on Wix: {reference}")
                continue
            if reference.startswith("/"):
                failures.append(f"{name}: root-relative URL breaks repository hosting: {reference}")
                continue
            target = (document.path.parent / unquote(url.path)).resolve() if url.path else document.path.resolve()
            if target.is_dir():
                target = target / "index.html"
            if not target.is_relative_to(ROOT):
                failures.append(f"{name}: URL escapes published artifact: {reference}")
            elif not target.is_file():
                failures.append(f"{name}: missing destination: {reference}")
            elif url.fragment and target in documents and unquote(url.fragment) not in documents[target].ids:
                failures.append(f"{name}: missing fragment: {reference}")
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".py", ".yml", ".yaml"}:
            failures.append(f"Nonpublishable file in src/: {path.relative_to(ROOT)}")
    if failures:
        print("\n".join(f"FAIL: {failure}" for failure in failures))
        raise SystemExit(1)
    print(f"PASS: {len(documents)} pages; all local links, fragments, images, legacy redirects, and contact destinations resolve.")


if __name__ == "__main__":
    main()
