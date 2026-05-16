#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import yaml

from _kb import id_map, parse_markdown
from _wiki_root import wiki_root


def render_page(path: Path, *, frontmatter_only: bool, body_only: bool) -> str:
    page = parse_markdown(path)
    if frontmatter_only:
        return yaml.safe_dump(page.meta, sort_keys=False, allow_unicode=True)
    if body_only:
        return page.body
    return path.read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch a KernelPilot knowledge page by id or path")
    parser.add_argument("page")
    parser.add_argument("--follow-sources", action="store_true")
    parser.add_argument("--frontmatter-only", action="store_true")
    parser.add_argument("--body-only", action="store_true")
    args = parser.parse_args()

    root = wiki_root()
    pages = id_map()
    page = pages.get(args.page)
    path = page.path if page else root / args.page
    if not path.exists():
        raise SystemExit(f"page not found: {args.page}")
    print(render_page(path, frontmatter_only=args.frontmatter_only, body_only=args.body_only), end="")
    if args.follow_sources and not args.frontmatter_only:
        current = parse_markdown(path)
        sources = current.meta.get("sources") or []
        if sources:
            print("\n\n---\n\n# Followed Sources\n")
        for source_id in sources:
            source = pages.get(str(source_id))
            if not source:
                print(f"\n## Missing source `{source_id}`\n")
                continue
            print(f"\n## {source.id} — {source.relpath}\n")
            print(source.path.read_text(encoding="utf-8"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
