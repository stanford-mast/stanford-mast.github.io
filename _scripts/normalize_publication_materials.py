#!/usr/bin/env python3
"""Normalize publication material labels, publisher links, and display order."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


PUBLISHERS = (
    "ACM DL",
    "CACM",
    "EPFL",
    "TRANSACT",
    "Hot Chips",
    "HiPEAC",
    "Stanford Library",
    "Berkeley Library",
    "IEEE Xplore",
    "IEEE Computer",
    "USENIX",
    "Springer",
    "PMLR",
    "SysML",
    "OpenReview",
    "VLDB",
    "ACM SIGOPS",
    "arXiv",
    "Elsevier",
    "DOI",
)
PUBLISHER_ORDER = {name: index for index, name in enumerate(PUBLISHERS)}


def scalar(front_matter: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:[ \t]*(.*)$", front_matter)
    return match.group(1).strip().strip("'\"") if match else ""


def publisher_for_url(url: str) -> str:
    domain = urlparse(url).netloc.lower()
    path = urlparse(url).path.lower()
    if "dl.acm.org" in domain:
        return "ACM DL"
    if "cacm.acm.org" in domain:
        return "CACM"
    if "infoscience.epfl.ch" in domain:
        return "EPFL"
    if "transact2013.cse.lehigh.edu" in domain:
        return "TRANSACT"
    if domain == "hotchips.org" or domain.endswith(".hotchips.org"):
        return "Hot Chips"
    if domain == "hipeac.net" or domain.endswith(".hipeac.net"):
        return "HiPEAC"
    if domain == "purl.stanford.edu" or domain == "searchworks.stanford.edu":
        return "Stanford Library"
    if domain in {"digicoll.lib.berkeley.edu", "search.library.berkeley.edu"}:
        return "Berkeley Library"
    if "ieeexplore.ieee.org" in domain:
        return "IEEE Xplore"
    if "computer.org" in domain:
        return "IEEE Computer"
    if "usenix.org" in domain:
        return "USENIX"
    if "link.springer.com" in domain:
        return "Springer"
    if "proceedings.mlr.press" in domain:
        return "PMLR"
    if "mlsys.org" in domain and "/2018/" in path:
        return "SysML"
    if "openreview.net" in domain:
        return "OpenReview"
    if "vldb.org" in domain:
        return "VLDB"
    if "sigops.org" in domain:
        return "ACM SIGOPS"
    if "arxiv.org" in domain:
        return "arXiv"
    if "doi.org" in domain:
        return "DOI"
    return ""


def publisher_for_doi(doi: str) -> str:
    lowered = doi.lower()
    if lowered.startswith(("10.1145/", "10.5555/")):
        return "ACM DL"
    if lowered.startswith("10.1109/"):
        return "IEEE Xplore"
    if lowered.startswith("10.1007/"):
        return "Springer"
    if lowered.startswith("10.14778/"):
        return "VLDB"
    if lowered.startswith("10.48550/"):
        return "arXiv"
    if lowered.startswith("10.1016/"):
        return "Elsevier"
    return "DOI"


def publisher_url(doi: str, publisher: str) -> str:
    if publisher == "ACM DL":
        return f"https://dl.acm.org/doi/{doi}"
    return f"https://doi.org/{doi}"


def parse_materials(block: str) -> list[dict[str, str]]:
    materials: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for line in block.splitlines():
        stripped = line.strip()
        if stripped.startswith("- name:"):
            current = {"name": stripped.split(":", 1)[1].strip().strip("'\"")}
            materials.append(current)
        elif current is not None and stripped.startswith("url:"):
            current["url"] = stripped.split(":", 1)[1].strip().strip("'\"")
        elif current is not None and stripped.startswith("type:"):
            current["type"] = stripped.split(":", 1)[1].strip().strip("'\"")
    return materials


def normalize_materials(materials: list[dict[str, str]], doi: str) -> list[dict[str, str]]:
    normalized: list[dict[str, str]] = []
    for material in materials:
        item = dict(material)
        name = item.get("name", "")
        url = item.get("url", "")
        detected_publisher = publisher_for_url(url)

        if name == "DOI" and doi:
            item["name"] = publisher_for_doi(doi)
        elif name == "Slides":
            item["name"] = "talk"
        elif name in {"PDF", "Paper", "USENIX PDF", "Article", "SIGOPS"}:
            item["name"] = detected_publisher or "paper"
        elif name == "paper" and url.startswith("http") and detected_publisher:
            item["name"] = detected_publisher
        elif name == "PMLR copy" and not any(
            other.get("name") == "PMLR" for other in materials
        ):
            item["name"] = "PMLR"
        normalized.append(item)

    # When a publisher landing page and its direct PDF are both present, keep
    # the landing page as the publisher link and label the direct file `paper`.
    for publisher in PUBLISHERS:
        matches = [item for item in normalized if item.get("name") == publisher]
        if len(matches) < 2:
            continue
        direct_files = [
            item for item in matches
            if item.get("type") == "file-pdf"
            or re.search(r"(?:/pdf\?|\.pdf(?:$|\?))", item.get("url", ""), re.I)
        ]
        landing_pages = [item for item in matches if item not in direct_files]
        if landing_pages:
            for item in direct_files:
                item["name"] = "paper"

    # A direct publisher/platform URL is preferable to a DOI alias when both
    # identify the same destination (for example, arxiv.org plus doi.org).
    for publisher in PUBLISHERS:
        matches = [item for item in normalized if item.get("name") == publisher]
        if len(matches) < 2:
            continue
        preferred = min(
            matches,
            key=lambda item: (
                publisher_for_url(item.get("url", "")) != publisher,
                "doi.org" in item.get("url", ""),
            ),
        )
        normalized = [
            item for item in normalized
            if item.get("name") != publisher or item is preferred
        ]

    if doi and not any(item.get("name") in PUBLISHERS for item in normalized):
        publisher = publisher_for_doi(doi)
        normalized.append({
            "name": publisher,
            "url": publisher_url(doi, publisher),
            "type": "file-alt",
        })

    unique: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for item in normalized:
        key = (item.get("name", ""), item.get("url", ""))
        if key not in seen:
            seen.add(key)
            unique.append(item)

    def order(item: dict[str, str]) -> tuple[int, int, str, str]:
        name = item.get("name", "")
        if name in {"paper", "thesis"}:
            return (0, 0, name, item.get("url", ""))
        if name in {"talk", "defense"}:
            return (1, 0, name, item.get("url", ""))
        if name == "tutorial":
            return (1, 0, name, item.get("url", ""))
        if name in {"extended", "poster"}:
            return (2, 0, name, item.get("url", ""))
        if name in PUBLISHER_ORDER:
            return (3, PUBLISHER_ORDER[name], name, item.get("url", ""))
        return (4, 0, name.lower(), item.get("url", ""))

    return sorted(unique, key=order)


def render_materials(materials: list[dict[str, str]]) -> str:
    return "".join(
        f"  - name: {item['name']}\n"
        f"    url: {item['url']}\n"
        f"    type: {item.get('type', 'file-alt')}\n"
        for item in materials
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    repo = args.repo.resolve()
    changed = 0
    publisher_counts: Counter[str] = Counter()
    missing: list[tuple[Path, str, str]] = []

    for path in sorted((repo / "_pubs").glob("*/*.md")):
        text = path.read_text(encoding="utf-8")
        front_matter = text.split("---", 2)[1]
        block_match = re.search(
            r"(?ms)^materials:[ \t]*\n(.*?)(?=^[A-Za-z_][A-Za-z0-9_-]*:|\Z)",
            front_matter,
        )
        if not block_match:
            raise ValueError(f"No materials block in {path}")

        materials = parse_materials(block_match.group(1))
        normalized = normalize_materials(materials, scalar(front_matter, "doi"))
        for item in normalized:
            if item.get("name") in PUBLISHERS:
                publisher_counts[item["name"]] += 1
        if not any(item.get("name") in PUBLISHERS for item in normalized):
            missing.append((path.relative_to(repo), scalar(front_matter, "venue"), scalar(front_matter, "title")))

        replacement = "materials:\n" + render_materials(normalized)
        old = "materials:\n" + block_match.group(1)
        if replacement != old:
            changed += 1
            if args.write:
                path.write_text(text.replace(old, replacement, 1), encoding="utf-8")

    print(f"Publication records requiring normalization: {changed}")
    print(f"Publisher coverage after normalization: {sum(publisher_counts.values())}")
    for name in PUBLISHERS:
        print(f"  {name}: {publisher_counts[name]}")
    print(f"Records without a trustworthy publisher link: {len(missing)}")
    for path, venue, title in missing:
        print(f"  {path} | {venue} | {title}")


if __name__ == "__main__":
    main()
