#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re

from _kb import iter_pages


def main() -> int:
    parser = argparse.ArgumentParser(description="Regex search across wiki and PR source pages")
    parser.add_argument("patterns", nargs="+")
    parser.add_argument("--only", choices=["wiki", "sources", "prs"], default=None)
    parser.add_argument("--any", action="store_true", help="match any pattern instead of all")
    parser.add_argument("--ignore-case", action="store_true")
    parser.add_argument("--context", type=int, default=0, help="print N context lines around each matching line")
    parser.add_argument("--files-only", action="store_true", help="print each matching page path once")
    args = parser.parse_args()

    flags = re.I if args.ignore_case else 0
    patterns = [re.compile(pattern, flags) for pattern in args.patterns]
    for page in iter_pages():
        if args.only == "wiki" and not page.relpath.startswith("wiki/"):
            continue
        if args.only == "sources" and not page.relpath.startswith("sources/"):
            continue
        if args.only == "prs" and not page.relpath.startswith("sources/prs/"):
            continue
        text = page.path.read_text(encoding="utf-8")
        whole_match = any(p.search(text) for p in patterns) if args.any else all(p.search(text) for p in patterns)
        if not whole_match:
            continue
        if args.files_only:
            print(page.relpath)
            continue
        lines = text.splitlines()
        printed: set[int] = set()
        for index, line in enumerate(lines):
            line_match = any(p.search(line) for p in patterns)
            if not line_match:
                continue
            start = max(0, index - args.context)
            end = min(len(lines), index + args.context + 1)
            for ctx_index in range(start, end):
                if ctx_index in printed:
                    continue
                printed.add(ctx_index)
                print(f"{page.relpath}:{ctx_index + 1}:{lines[ctx_index]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
