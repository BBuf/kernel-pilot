# KernelPilot Knowledge — Blackwell & Hopper Kernel Optimization Evidence Base

> **Knowledge cutoff: 2026-05-16.** Merged PR evidence is collected from **2024-01-01** through this date (recorded in [`data/refresh-cutoff.yaml`](data/refresh-cutoff.yaml)). Triton claims pin to release **3.6.0** (released 2026-01-21); CUTLASS claims pin to **4.5.0** (released 2026-03-27); see [`data/tool-versions.yaml`](data/tool-versions.yaml) for all tracked tools. To advance the cutoff, run `scripts/expand-pr-corpus.py`, regenerate PR pages, materialize evidence bundles, and rerun validation.

A structured knowledge base of NVIDIA Blackwell (SM100, B200) and Hopper (SM90, H100) GPU kernel optimization, packaged as a KernelPilot-local Claude Code skill. This `knowledge/` directory is the skill root.

## Install as a Claude Code Skill

```bash
cd /path/to/kernel-pilot/knowledge
pip install -r requirements.txt
```

The query scripts auto-resolve the wiki root to this directory, so no environment variable is required.

Smoke test:

```bash
python3 scripts/query.py --tag nvfp4 --type kernel --compact
python3 scripts/get_page.py kernel-flash-attention-4 --frontmatter-only
```

Optional override for relocating the scripts:

```bash
export KERNEL_KNOWLEDGE_ROOT=/path/to/kernel-pilot/knowledge
```

## What's Here

- **3,660 PR references** from NVIDIA/cutlass (64), sgl-project/sglang (777), vllm-project/vllm (1,069), flashinfer-ai/flashinfer (779), pytorch/pytorch (75), deepseek-ai/DeepGEMM (27), NVIDIA/TensorRT-LLM (180), Dao-AILab/flash-attention (146), NVIDIA/cccl (228), tile-ai/tilelang (195), triton-lang/triton (57), Dao-AILab/quack (49), HazyResearch/ThunderKittens (13), deepseek-ai/TileKernels (1) — Jan 2024 – May 16 2026
- **52 synthesized wiki pages** — hardware features, techniques, kernel case studies, problem patterns, DSL guides, migration guides
- **26 blog/community summaries**, **17 doc/reference summaries**, **7 competition pages** (GPU Mode NVFP4 hackathon, FlashInfer MLSys 2026)
- **3,660 PR evidence bundles** under `evidence/pull-bundles/`, plus supporting blog, contest, and kernel-case capsules under `evidence/` — pinned to upstream SHAs via `ORIGIN.yaml`
- **6 auto-generated cross-reference indices** — by problem / technique / hardware feature / repo / kernel type / language
- **14 candidate ledgers** tracking 3,656 active merged PR candidates with include/defer decisions only; dropped PRs are not retained as rows
- **Actual-diff relevance audit** — [`data/pr-diff-relevance-audit.yaml`](data/pr-diff-relevance-audit.yaml) keeps only aggregate counts for the 2026-05-16 diff audit; per-PR dropped details are intentionally not recorded.
- **PR-driven legacy import records** — [`data/repo-catalog.yaml`](data/repo-catalog.yaml), [`data/legacy-pr-seeds.yaml`](data/legacy-pr-seeds.yaml), [`data/open-pr-watchlist.yaml`](data/open-pr-watchlist.yaml), and [`references/legacy-import-notes.md`](references/legacy-import-notes.md)
- **Hybrid version-claim registry** ([`data/version-claims.yaml`](data/version-claims.yaml)) — per-page `version_sensitive: <id>` pointers + central registry, validated for bidirectional consistency

## Query Tools

All tools run from the skill root, no env var needed.

| Tool | Purpose |
|---|---|
| `scripts/query.py` | Unified search across 3,762 indexed IDs (keywords + filters + alias-aware) |
| `scripts/get_page.py` | Fetch any page by `id` or path; `--follow-sources` expands cited sources |
| `scripts/grep_wiki.py` | Regex text search across wiki bodies and PR pages |
| `scripts/fetch-pr-evidence.py` | Materialize PR `review.diff`, metadata, provenance, and key changed files from candidate ledgers |
| `scripts/materialize-source-prs.py` | Ensure every `sources/prs/**/PR-*.md` page has a matching PR evidence bundle |

Examples:

```bash
python3 scripts/query.py "ping-pong attention" --limit 5
python3 scripts/query.py --tag UMMA --type hardware --compact          # alias → tcgen05
python3 scripts/query.py --architecture B200 --type kernel             # alias → sm100
python3 scripts/get_page.py kernel-flash-attention-4 --follow-sources
python3 scripts/grep_wiki.py "tcgen05\\.fence" --only wiki
```

## Companion Docs

- [`SKILL.md`](SKILL.md) — Skill entry point: when to engage, 5 navigation paths, output contract.
- [`references/primer.md`](references/primer.md) — Topic map: hardware features, techniques, kernels, symptoms → canonical page IDs.
- [`references/schema.md`](references/schema.md) — Frontmatter schema, confidence rules, reproducibility ladder, controlled vocabulary, canonical aliases.
- [`references/examples.md`](references/examples.md) — 10 worked query patterns (user question → command sequence → synthesis).
- [`references/legacy-import-notes.md`](references/legacy-import-notes.md) — What was imported from the old references and what remains outside the PR-diff corpus.
- [`CLAUDE.md`](CLAUDE.md) — Extended schema + navigation reference for Claude Code.
- [`index.md`](index.md) — Human-facing curated top-level index.

## Architecture

Three layers:

1. **`sources/`** — Raw data. Immutable summaries of PRs, blogs, docs, contests.
2. **`wiki/`** — Synthesized knowledge pages. Cross-referenced by `id`. All have YAML frontmatter.
3. **`queries/`** — Auto-generated cross-reference indices. Do not edit manually; regenerate via `scripts/generate-indices.py`.

Supporting files:
- `data/schemas.yaml` — Required/optional fields per page type
- `data/tags.yaml` — Controlled vocabulary (80+ tags)
- `data/aliases.yaml` — Canonical → synonym mappings
- `data/version-claims.yaml` — Central registry for version-sensitive claims (DEC-1 hybrid)
- `data/tool-versions.yaml` — Snapshot of tracked tool releases (Triton, CUTLASS, CUDA, PTX, …)
- `data/refresh-cutoff.yaml` — Single source of truth for the knowledge cutoff date
- `data/repo-catalog.yaml` — PR-driven repo catalog imported from the old index, with kernel paths and scan modes
- `data/legacy-pr-seeds.yaml` — Curated merged PR seeds imported from old PR notes
- `data/open-pr-watchlist.yaml` — Open PRs kept as watchlist only, not materialized evidence
- `candidates/` — Reviewed PR candidate ledgers (per repo)
- `evidence/` — Verbatim / extracted / derived evidence bundles, each with `ORIGIN.yaml`

## Maintenance Tooling

| Script | Purpose |
|---|---|
| `scripts/validate.py` | Validate YAML frontmatter, enforce schema, check link and evidence-bundle integrity |
| `scripts/generate-indices.py` | Regenerate `queries/*.md` from frontmatter |
| `scripts/generate-pr-pages.py` | Batch-generate source PR pages from candidate ledgers |
| `scripts/expand-pr-corpus.py` | Import old PR seeds and run GitHub merged-PR search over the repo catalog |
| `scripts/sync-pr-evidence-metadata.py` | Backfill source-page metadata from `upstream.json` and prune out-of-window PRs |

```bash
pip install -r requirements.txt
python3 scripts/validate.py            # reports 3762 ids / 3660 PR bundles / 14 ledgers, 0 errors
python3 scripts/generate-indices.py    # regenerate query indices
```

## Quality Gates (knowledge cutoff: 2026-05-16)

- 3,768 markdown/index pages, 3,762 IDs, 0 validation errors
- 3,660 PR evidence bundles validated, with 3,660 complete source-page-matched bundles
- 14 candidate ledgers normalized
- 0 broken links across all internal references
- All `verified` wiki pages have official-doc + upstream-code evidence (enforced by `evidence_basis` field)
- All technique/kernel/language pages have compilable code snippets (`reproducibility >= snippet`)
- All Hopper-inclusive pages explain their `blackwell_relevance`
- Version-sensitive claims (Triton 3.6, CUTLASS 4.5, etc.) carry `version_sensitive: <id>` pointers resolving to the central registry

## Scope Rules

- **Blackwell-first** — SM100 content is primary. SM90 requires explicit `blackwell_relevance` field.
- **PR-diff first** — Merged upstream PR diff + source snapshot is the primary evidence shape. Old source guides and vendored docs can seed repo selection, but they are not primary knowledge.
- **Kernel-only** — No distributed-system topics unless a merged PR directly changes CUDA/Triton/CuTe/CUTLASS kernel code or kernel benchmarks.
- **English canonical** — All content in English.
- **First-class DSLs** — CuTe DSL, CUDA C++, PTX, Triton. TileLang / cuTile / JAX-Pallas mentioned but no dedicated guides.

## Repository Layout

```
kernel-pilot/knowledge/
├── SKILL.md                           # Skill entry point
├── README.md                          # This file
├── CLAUDE.md                          # Extended navigation + schema reference
├── index.md                           # Curated top-level index
├── requirements.txt                   # PyYAML
│
├── scripts/                           # Query tools + maintenance tooling
│   ├── query.py                       # Unified search
│   ├── get_page.py                    # Page fetcher
│   ├── grep_wiki.py                   # Regex search
│   ├── _wiki_root.py                  # Shared root resolver
│   ├── validate.py                    # Schema validator
│   ├── generate-indices.py            # Query-index generator
│   ├── generate-pr-pages.py           # Batch PR page generator
│   ├── expand-pr-corpus.py            # Repo catalog + PR search expansion
│   └── sync-pr-evidence-metadata.py   # Source-page metadata backfill
│
├── references/                        # Skill knowledge layer
│   ├── primer.md                      # Topic map
│   ├── schema.md                      # Condensed schema reference
│   ├── examples.md                    # 10 worked query patterns
│   └── legacy-import-notes.md         # Old-reference import policy
│
├── data/                              # Schema + vocabulary
│   ├── schemas.yaml
│   ├── tags.yaml
│   ├── aliases.yaml
│   ├── repo-catalog.yaml
│   ├── legacy-pr-seeds.yaml
│   └── open-pr-watchlist.yaml
│
├── candidates/                        # Reviewed PR ledgers (ingestion source of truth)
│   ├── cutlass.yaml
│   ├── sglang.yaml
│   ├── vllm.yaml
│   ├── flashinfer.yaml
│   ├── pytorch.yaml
│   ├── deepgemm.yaml
│   ├── tensorrt-llm.yaml
│   ├── flash-attention.yaml
│   ├── cccl-cub.yaml
│   ├── tilelang.yaml
│   ├── triton.yaml
│   ├── quack.yaml
│   ├── thunderkittens.yaml
│   └── tilekernels.yaml
│
├── sources/                           # Layer 1: raw data
│   ├── prs/{repo}/PR-{N}.md
│   ├── contests/{contest}/
│   ├── docs/
│   └── blogs/
│
├── wiki/                              # Layer 2: synthesized knowledge
│   ├── hardware/
│   ├── techniques/
│   ├── kernels/
│   ├── patterns/
│   ├── languages/
│   └── migration/
│
└── queries/                           # Layer 3: auto-generated indices
    ├── by-problem.md
    ├── by-technique.md
    ├── by-hardware-feature.md
    ├── by-repo.md
    ├── by-kernel-type.md
    └── by-language.md
```

## License

Summaries and wiki syntheses in this repository are derivative works citing upstream PRs, blogs, and docs. The tooling (`scripts/`, `references/`, `data/`) is MIT-style; see individual files for any exceptions.
