---
id: reference-legacy-import-notes
title: Legacy Reference Import Notes
type: reference
source_category: local-policy
architectures:
- sm100
- sm90
tags:
- pr-diff
- provenance
- corpus-refresh
confidence: verified
---
# Legacy Reference Import Notes

The old `knowledge/index.json` and `knowledge/references/prs/pr-index.json` are used as PR-selection inputs, not as the knowledge body.

Imported into the current PR-diff corpus:

- Repo catalog and kernel-path routing: `data/repo-catalog.yaml`
- Curated merged PR seeds: `data/legacy-pr-seeds.yaml`
- Open PR watchlist, kept out of merged evidence: `data/open-pr-watchlist.yaml`
- Refresh window: `2024-01-01` through `2026-05-16`
- Distilled architecture/profiling/blog-code notes from the old `references/ako4all` and `references/blogs` trees, rewritten into `sources/docs`, `sources/blogs`, `wiki/hardware`, and `wiki/techniques`

Deliberately not restored as primary evidence:

- Vendored CUDA documentation trees
- Source-guide prose as standalone authority
- Repo source snapshots that are not anchored to a merged PR

The old AKO4ALL/blog material is now background knowledge only: compact source
pages and wiki synthesis, plus small provenance-carrying blog code capsules for
representative CUDA/CuTe examples. It must not override PR-diff evidence when
the two disagree.

The current evidence contract is: candidate ledger row -> `sources/prs/<repo-id>/PR-<number>.md` -> `evidence/pull-bundles/<repo-id>/gh-<number>/review.diff` plus `upstream.json`, `ORIGIN.yaml`, and `source-snapshot/`.

After materialization, `scripts/audit-pr-diff-relevance.py --apply` must inspect each `review.diff` and remove PRs whose actual changed files are docs/config/CI/test-only, non-CUDA accelerator, or host-only changes. Dropped PRs are deleted from source pages, evidence bundles, and candidate ledgers; `data/pr-diff-relevance-audit.yaml` keeps only aggregate counts, not per-PR dropped details.
