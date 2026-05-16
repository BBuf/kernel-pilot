#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from _kb import as_list, iter_pages
from _wiki_root import wiki_root


INDEXES = {
    "by-problem.md": ("symptoms", "Problem / Symptom"),
    "by-technique.md": ("techniques", "Technique"),
    "by-hardware-feature.md": ("hardware_features", "Hardware Feature"),
    "by-repo.md": ("repo", "Repository"),
    "by-kernel-type.md": ("kernel_types", "Kernel Type"),
    "by-language.md": ("languages", "Language"),
}


def values_for(page, field: str) -> list[str]:
    value = page.meta.get(field)
    if field == "repo" and value:
        return [str(value)]
    return as_list(value)


def main() -> int:
    root = wiki_root()
    query_dir = root / "queries"
    query_dir.mkdir(exist_ok=True)
    pages = iter_pages()
    for filename, (field, title) in INDEXES.items():
        groups: dict[str, list] = defaultdict(list)
        for page in pages:
            for value in values_for(page, field):
                groups[value].append(page)
        lines = [f"# {title} Index\n"]
        for value in sorted(groups):
            lines.append(f'<a id="{value.lower().replace("/", "").replace(" ", "-")}"></a>')
            lines.append(f"## {value}\n")
            lines.append(f"{len(groups[value])} pages\n")
            lines.append("| ID | Type | Path | Title |")
            lines.append("| --- | --- | --- | --- |")
            for page in sorted(groups[value], key=lambda item: item.relpath):
                lines.append(f"| `{page.id or '-'}` | {page.kind} | [`{page.relpath}`](../{page.relpath}) | {page.title} |")
            lines.append("")
        (query_dir / filename).write_text("\n".join(lines), encoding="utf-8")
    print(f"generated {len(INDEXES)} query indices")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
