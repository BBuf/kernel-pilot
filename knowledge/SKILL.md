---
name: kernel-knowledge
description: Use when the user asks about optimizing NVIDIA Blackwell (SM100, B200) or Hopper (SM90, H100) GPU kernels — tcgen05/TMEM/CLC/NVFP4/2-SM cooperative, warp specialization, FlashAttention-4, DeepGEMM, FlashMLA, MoE, grouped GEMM, CuTe-DSL/PTX/Triton on Blackwell, or wants concrete PR references from CUTLASS/SGLang/vLLM/FlashInfer/PyTorch/TensorRT-LLM/FlashAttention/CCCL/TileLang/Triton/QuACK/ThunderKittens/TileKernels.
argument-hint: "[natural-language-question] | [--tag foo --type kernel] | [page-id]"
allowed-tools: "Bash Read Grep Glob"
---

# KernelPilot Kernel Knowledge

> **Knowledge cutoff: 2026-05-16.** Merged PR evidence is collected from **2024-01-01** through this date (per `data/refresh-cutoff.yaml`). Re-run the refresh tooling to advance the cutoff.

Query a structured, cross-referenced knowledge base of GPU kernel optimization for NVIDIA Blackwell (SM100) and Hopper (SM90) — 3,660 actual-diff-audited merged PR evidence pages, 52 wiki synthesis pages, 7 competitions, 26 blogs/community notes, 17 doc/reference summaries.

## When To Use This Skill

Trigger this skill when the user asks about:

- **Blackwell/SM100 kernel programming** — tcgen05.mma, TMEM, CLC, 2-SM cooperative, NVFP4, FP8/FP4 block scaling, PDL/GDC
- **Kernel implementations** — FlashAttention-4, DeepGEMM, FlashMLA, NSA, GatedDeltaNet, NVFP4 GEMM/GEMV, fused MoE, gated dual GEMM
- **Performance patterns** — low SM utilization, memory-bound, register pressure, compute-bound, tail effects, pipeline stalls
- **DSLs for Blackwell** — CuTe DSL, CUDA C++ with PTX inline, Triton on Blackwell
- **Hopper → Blackwell migration** — wgmma → tcgen05, register → TMEM accumulators
- **PR references** — "how did vLLM/SGLang/FlashInfer/CUTLASS/PyTorch/TensorRT-LLM/FlashAttention/CCCL/Triton/TileLang implement X for SM100?"
- **Competition solutions** — GPU Mode NVFP4 hackathon, FlashInfer MLSys 2026 submissions

## How To Query

All commands below run from the skill directory (the clone root — the directory this `SKILL.md` lives in). The scripts auto-resolve the wiki root; **no environment variable required**.

### Path 1: Unified search (preferred for natural language)

```bash
python3 scripts/query.py "how to fuse gate-up dual GEMM on Blackwell"
python3 scripts/query.py --tag nvfp4 --type kernel
python3 scripts/query.py --repo NVIDIA/cutlass --limit 20
python3 scripts/query.py --symptom tail-effect --compact
```

Filters: `--type`, `--tag`, `--repo`, `--language`, `--architecture`,
`--symptom`, `--confidence`, `--limit`, `--compact`, `--paths-only`. `--tag`
and `--architecture` accept aliases — `--tag UMMA` matches `tcgen05`,
`--architecture B200` matches `sm100`, etc.

### Path 2: Fetch a specific page by id or path

```bash
python3 scripts/get_page.py kernel-flash-attention-4
python3 scripts/get_page.py pr-cutlass-2472
python3 scripts/get_page.py kernel-flash-attention-4 --follow-sources
python3 scripts/get_page.py kernel-flash-attention-4 --body-only
```

### Path 3: Regex text search across wiki bodies and PR pages

```bash
python3 scripts/grep_wiki.py "tcgen05\\.fence"
python3 scripts/grep_wiki.py "2-CTA backward" --only wiki
python3 scripts/grep_wiki.py "nvfp4" "block_scale" --any
```

### Path 4: Pre-built cross-reference indices

Auto-generated under `queries/`:

- `queries/by-problem.md` — symptom → pattern page → candidate techniques
- `queries/by-technique.md` — 17 techniques with architectures, confidence, reproducibility, source count
- `queries/by-hardware-feature.md` — tcgen05/tmem/clc/tma/nvfp4/etc. → related wiki + PR pages
- `queries/by-kernel-type.md` — gemm/attention/moe/mla/gated-delta-net → pages
- `queries/by-language.md` — cute-dsl/cuda-cpp/ptx/triton → guide page + related kernels/sources
- `queries/by-repo.md` — all 3,660 materialized PR pages across 14 repo ledgers

### Path 5: Primer, schema, examples

Companion docs under `references/`:

- `references/primer.md` — topic map: hardware features, techniques, symptoms, canonical page IDs. Read this first when the question is broad.
- `references/schema.md` — condensed frontmatter schema, confidence rules, reproducibility ladder, controlled vocabulary, canonical aliases.
- `references/examples.md` — 10 worked query patterns mapping user questions → command sequences → synthesis.

## Output Pattern

When answering from this KB:

1. **Cite specific pages** with paths (e.g., `wiki/kernels/flash-attention-4.md`) and IDs (`kernel-flash-attention-4`).
2. **Follow `sources:` fields** to trace claims back to PRs/blogs/docs.
3. **Respect confidence levels** — `verified` > `source-reported` > `inferred` > `experimental`. Call out when a claim is `experimental` or `inferred`.
4. **Include code snippets** from wiki pages when they exist — technique/kernel/language pages are guaranteed `snippet`-reproducibility (validator-enforced).
5. **Report performance claims with all six fields** — `gpu`, `dtype`, `shape`, `metric`, `value`, `source_id`.

## Knowledge Base Contents (knowledge cutoff: 2026-05-16)

- **3,768 total markdown/indexed pages** — 3,660 PR references + 52 wiki synthesis + 26 blogs/community notes + 17 docs/reference notes + 7 contests + references/queries
- **14 candidate ledgers** in `candidates/` — 3,656 active merged PR candidates classified as include/defer from 2024-01-01 through 2026-05-16; dropped PRs are not retained as rows
- **3,660 PR evidence bundles** in `evidence/pull-bundles/`, plus blog, contest, and kernel-case capsules under `evidence/` — pinned to upstream SHAs via `ORIGIN.yaml`
- **Actual-diff relevance audit** in `data/pr-diff-relevance-audit.yaml` — aggregate-only diff audit after inspecting materialized `review.diff` paths and changed code; per-PR dropped details are intentionally not recorded
- **6 auto-generated query indices** in `queries/`
- **Controlled vocabulary** (80+ tags) in `data/tags.yaml`, alias map in `data/aliases.yaml`
- **Hybrid version-claim registry** — per-page `version_sensitive: <id>` pointers + `data/version-claims.yaml` central registry, validated for bidirectional consistency
- **PR corpus tooling** — `scripts/expand-pr-corpus.py`, `scripts/generate-pr-pages.py`, `scripts/materialize-source-prs.py`, `scripts/sync-pr-evidence-metadata.py`
- **Validator** `scripts/validate.py` — 3762 IDs / 3660 PR bundles / 14 ledgers / 0 errors
- **Blackwell-first** — SM90 pages only appear when they carry explicit `blackwell_relevance`

The knowledge cutoff date is the last day on which upstream PRs / blog snapshots were refreshed. To advance it: run `scripts/expand-pr-corpus.py`, regenerate PR pages, materialize missing bundles, sync metadata, then validate.

## Quality Guarantees

- Every `verified` page has official-doc + upstream-code evidence
- Every technique/kernel/language page has a compilable snippet
- Every PR page has `inclusion_reason` and `status: merged`
- All Hopper-inclusive pages have explicit `blackwell_relevance`
