# KernelPilot Knowledge Phase 3 — Data Depth: Local Code Artifacts

## Goal Description

Transform KernelPilot Knowledge from an "index-card" knowledge base (545 markdown summaries that link out to real code) into a self-contained code library in which LLM agents can answer concrete kernel questions — "how do I write an NVFP4 batched GEMV?", "how is warp specialization structured on Blackwell?", "how does DeepGEMM do Nc=128 CUDA-core promotion?" — by reading files inside the repository, without following external links.

The transformation pulls three classes of code into the repo:

1. **Cleaned PR diffs** from the 5 tracked repositories (CUTLASS, SGLang, vLLM, FlashInfer, PyTorch), restricted to kernel-relevant source files at the merged commit SHA.
2. **Contest kernel sources** (GPU Mode NVFP4 hackathon submissions and FlashInfer MLSys 2026 track entries) where authors have published them.
3. **Blog code blocks** lifted out of the 20 captured community/technical blogs into standalone source files, with back-references to the originating blog section.

A dedicated set of **deep wiki kernel pages** (12 chosen pages across `wiki/kernels/` and `wiki/techniques/`) ship with full, compilable or pseudocode-complete kernels plus a labeled progression of variants (naive → pipelined → warp-specialized → CLC-persistent) demonstrating each optimization step.

Phase 3 deliberately preserves the existing `sources/ → wiki/ → queries/` mental model. All pulled code lives in a new top-level `evidence/` tree and is referenced from source/wiki pages by pointer (`artifact_dir:` field), never embedded inside `wiki/` itself. Every code asset carries explicit provenance: origin URL, upstream commit SHA, license, retrieval date, and an `asset_mode` field distinguishing **verbatim** (copied unchanged from upstream), **extracted** (lifted out of a mixed-format source such as a blog markdown file), and **derived** (written by us based on publicly-documented behaviour). Derived assets are isolated from verbatim upstream code so consumers never mistake tutorialized reconstruction for authoritative source.

The plan explicitly expands Blackwell-DSL coverage: **CuTe DSL** becomes a first-class code lane (the user-directive `多调研一些语言` is interpreted as "bring in more CuTe DSL and Triton real code"), and **Triton** is handled with a narrower policy scoped to memory-bound / backend-fallback exemplars, because `wiki/languages/triton-blackwell.md` already documents that Triton has no direct tcgen05/TMEM path on SM100.

## Acceptance Criteria

Following TDD philosophy, each criterion includes positive and negative tests for deterministic verification.

- AC-1: The "core PR" set covered by Phase 3 is deterministic, automation-derived, and reproducible
  - Positive Tests (expected to PASS):
    - Running `python3 scripts/compute_core_prs.py` twice on an unchanged corpus prints the same ordered list of PR IDs; the list is stored as `data/core-prs.yaml` and diff-equal on re-run
    - Every PR ID appearing in any `wiki/**.md` frontmatter `sources:` list is present in the core set (graph-derivation completeness)
    - Every CuTe DSL tutorial PR (PRs tagged `cute-dsl` whose `changed_paths` touch CUTLASS example/tutorial directories) is present in the core set
    - Every contest-referenced PR (PRs appearing in any `sources/contests/**/*.md` body) is present in the core set
  - Negative Tests (expected to FAIL):
    - Manually editing `data/core-prs.yaml` without a corresponding `wiki/` or `data/core-prs-allowlist.yaml` change is rejected by `scripts/validate.py`
    - A core PR whose upstream state has `status: reverted` or whose `merge_sha` no longer resolves is flagged by `scripts/verify_core_prs.py` (does not auto-remove, but fails a `--strict` mode)

- AC-2: Every captured code asset carries full provenance metadata with per-file manifest granularity, and the validator enforces it
  - **Provenance unit definition**: an "evidence bundle" is a directory under `evidence/` that directly contains source or patch files (`.cu`, `.cuh`, `.ptx`, `.py`, `.cpp`, `.h`, `.hpp`, `.patch`). Every evidence bundle root has exactly one `ORIGIN.yaml` that describes the bundle at two layers:
    1. **Bundle-level defaults**: `origin_url`, `upstream_repo`, `upstream_sha`, `license`, `retrieved_at`, bundle-default `asset_mode` (one of `verbatim`, `extracted`, `derived`), and `derived_from: [source_id, ...]` when the bundle default is `derived`.
    2. **Per-file manifest** (`files:` list): each file inside the bundle (including files in sub-directories such as `source-snapshot/include/...`) gets an entry `{local_path, role, mode, upstream_path?, sha256, heading_path?}`. `role` is one of {`pr-diff`, `upstream-file`, `extracted-block`, `derived-source`, `approach-notes`, `bench-record`}. `mode` is per-file and overrides the bundle default when set (most bundles are mode-homogeneous, but `evidence/pull-bundles/*/` bundles are naturally mixed: the `review.diff` has `role: pr-diff, mode: upstream-patch`, while each `source-snapshot/...` entry has `role: upstream-file, mode: verbatim, upstream_path: <upstream-path>`).
    - **Extracted-mode semantics** (blog code): `role: extracted-block, mode: extracted`, `heading_path` records the originating blog section (e.g., `"## Mainloop > ### TMA descriptor setup"`), `sha256` is the SHA-256 of the extracted file bytes. `upstream_path` is either a path within a blog source repo (when the blog ships its own markdown on GitHub) or the string `"inline-in-blog-markdown"` (when only the captured `sources/blogs/<slug>.md` exists).
  - **Bundle roots in the standard layout**: `evidence/pull-bundles/<repo>/gh-<N>/`, `evidence/challenge-capsules/<contest>/<problem>/submissions/<rank-N-author>/`, `evidence/blog-capsules/<slug>/code/`, `evidence/kernel-cases/<slug>/full/`, `evidence/kernel-cases/<slug>/variants/`.
  - Positive Tests (expected to PASS):
    - Every evidence bundle root contains exactly one `ORIGIN.yaml` with the bundle-level defaults and a `files:` list that enumerates every source-or-patch file in the bundle (recursively)
    - Every `files[*]` entry specifies a concrete `mode` and a `sha256` that matches the current bytes of `local_path`
    - For `mode: verbatim` entries, `upstream_path` is required and `scripts/verify_verbatim.py --strict` (owned by task15) byte-matches `local_path` against `gh api` content at `upstream_repo@upstream_sha:upstream_path`
    - For `mode: upstream-patch` entries (whole-PR diffs), `scripts/verify_verbatim.py --strict` byte-matches the file against `gh pr diff` output at `upstream_sha`
    - For `mode: extracted` entries, `heading_path` is set and (when the blog ships markdown on GitHub) `upstream_path` + `upstream_sha` are set
    - For `mode: derived` entries (only allowed under `evidence/kernel-cases/<slug>/variants/`), bundle `derived_from:` references at least one existing page ID resolvable by `scripts/get_page.py`
  - Negative Tests (expected to FAIL):
    - Adding a `.cu` file to `evidence/pull-bundles/cutlass/gh-3106/source-snapshot/include/...` without updating `ORIGIN.yaml`'s `files:` list fails validation (drift between filesystem and manifest)
    - Placing two `ORIGIN.yaml` files in the same bundle (root + a sub-directory) fails validation — nested provenance declarations are disallowed to keep ownership flat
    - A `files[*]` entry with `mode: verbatim` whose `local_path` bytes differ from the upstream at `upstream_sha:upstream_path` is flagged by `scripts/verify_verbatim.py --strict`
    - A `files[*]` entry whose `sha256` does not match the current on-disk file bytes fails validation (hand-edit detection)
    - A bundle with `asset_mode: derived` but no `derived_from:` list fails validation

- AC-3: Contest submissions distinguish official source from reconstruction via an explicit truth model
  - Positive Tests (expected to PASS):
    - Every `source-contest` frontmatter `submissions[*]` entry carries a `submission_truth:` field with one of: `official-submission`, `author-published-posthoc`, `reconstructed-from-blog`, `unavailable`
    - When `submission_truth != unavailable`, a `code_path:` pointing to an existing file under `evidence/challenge-capsules/<contest>/<problem>/submissions/<rank-N-author>/` is required
    - When `submission_truth == unavailable`, a human-readable `code_unavailable_reason:` string explains why (e.g., `"Discord-only posting; author did not re-publish"`)
  - Negative Tests (expected to FAIL):
    - A submission page that claims "rank 1 kernel" without any of the four truth-model tags is rejected by validation
    - A submission with `submission_truth: official-submission` but no accompanying `code_path` fails validation

- AC-4: Blog code extraction is section-preserving, manifest-traceable, and drift-detectable
  - Positive Tests (expected to PASS):
    - Every blog page whose markdown contains fenced code blocks with language hints in {`cuda`, `cpp`, `python`, `ptx`, `cute`, `triton`} has a corresponding `evidence/blog-capsules/<slug>/code/` directory
    - `evidence/blog-capsules/<slug>/MANIFEST.yaml` maps each extracted file to (a) its originating heading path in the blog markdown (e.g., `"## Mainloop > ### TMA descriptor setup" → 03-tma-descriptor-setup.cuh`) and (b) a SHA-256 content checksum of the extracted file
    - Running `scripts/extract_blog_code.py --check <blog-slug>` on an unmodified blog exits 0 (idempotent): the extractor re-parses the markdown AST, recomputes the expected file set, and verifies each file's checksum matches `MANIFEST.yaml`
    - A blog with no fenced code has a `MANIFEST.yaml` noting `code_present: false` (so downstream tooling distinguishes "no code yet extracted" from "this blog has no code")
  - Negative Tests (expected to FAIL):
    - A blog page gains a new code fence in markdown but the extractor is not re-run → `scripts/extract_blog_code.py --check` exits non-zero (markdown-vs-manifest drift)
    - An extracted file is hand-edited (its SHA-256 no longer matches `MANIFEST.yaml`) → `scripts/extract_blog_code.py --check` exits non-zero
    - `MANIFEST.yaml` missing the checksum field fails validation

- AC-5: `scripts/validate.py` enforces nested-schema rules and referenced-asset existence within the declared single-field frontmatter contract
  - **Validation scope** (aligned with AC-11 to avoid contract confusion):
    - Page frontmatter validates `artifact_dir:` — must resolve to an existing directory; no sibling page-level field acts as an alternate code pointer (the validator's disallow-list is declared in `data/schemas.yaml` under the `source-pr` / `source-blog` / `wiki-kernel` / `wiki-technique` schemas)
    - Nested `submissions[*].code_path` — must resolve to a file under the implicit submission bundle path (`evidence/challenge-capsules/<contest>/<problem>/submissions/<rank-N-author>/`)
    - Bundle `ORIGIN.yaml` `files[*].local_path` — must resolve to an existing file inside the bundle and the `sha256` must match the file bytes
  - Positive Tests (expected to PASS):
    - Missing required nested fields inside `submissions[*]` (e.g., `submission_truth`) trigger validation errors (the current validator skips nested validation)
    - `artifact_dir:` resolves to an existing directory for every page that declares it
    - `scripts/validate.py` post-run summary reports: total files, total evidence bundles, total provenance records, total verbatim/extracted/derived breakdown, broken-reference count (required 0)
  - Negative Tests (expected to FAIL):
    - Introducing `artifact_dir: evidence/nonexistent/` in any page fails validation
    - Placing any disallow-listed alternate code-pointer field as a peer of `artifact_dir:` at the page frontmatter level fails validation (the disallow-list is codified in `data/schemas.yaml`; enforces AC-11's single-field contract)
    - Adding a `submissions[]` entry without `submission_truth` fails validation even if the outer page fields are correct
    - A `submissions[*].code_path` that points outside the implicit submission bundle path (e.g., references a blog bundle) fails validation

- AC-6: Query and fetch tools become code-aware
  - Positive Tests (expected to PASS):
    - `python3 scripts/query.py --has-code --type kernel` returns only pages whose associated `artifact_dir` contains at least one source file
    - `python3 scripts/get_page.py kernel-nvfp4-gemv --include-code` prints the page body plus the full text of every file under its `artifact_dir`, clearly delimited
    - `python3 scripts/grep_wiki.py "tcgen05\\.mma" --ext cu,cuh,ptx` searches inside `.cu/.cuh/.ptx` files under `evidence/`, not only markdown
  - Negative Tests (expected to FAIL):
    - A page that exists as markdown but has no local code assets is **not** returned by `--has-code` filters
    - `grep_wiki.py` without the `--ext` flag continues to match only markdown (backward compatible)

- AC-7: The "Definition of Done" questions from the draft are mechanically checkable via a fixture
  - **Mechanism**: `data/phase3-dod-fixtures.yaml` is a checked-in fixture file (authored in task11) listing one entry per question. Each entry declares `question:`, `required_assets:` (list of glob patterns that MUST match at least one existing file), `required_min_lines:` (per-asset line-count floor, defaults 100), `required_provenance_modes:` (allowed set, e.g. `[verbatim, extracted]` to disallow a `derived`-only answer), and optional `required_content_patterns:` (regex that must occur across the matched files, e.g. `mbarrier|tma_load|tcgen05\.mma` for the warp-specialization question). `scripts/check_dod_fixtures.py` (owned by task15) iterates the fixture and returns pass/fail per question.
  - Positive Tests (expected to PASS):
    - `scripts/check_dod_fixtures.py` exits 0 on a correctly-populated repo with all fixture entries satisfied
    - For the "NVFP4 batched GEMV" question, `required_assets` includes `evidence/challenge-capsules/gpu-mode-nvfp4/problem-1/submissions/rank-*/kernel.{cu,ptx}` OR `evidence/kernel-cases/nvfp4-gemv/full/*.cu`; at least one match must be ≥200 lines
    - For the "warp specialization" question, the fixture requires at least one file matching `evidence/kernel-cases/warp-specialization/full/*.cu` OR `evidence/pull-bundles/cutlass/PR-*/source-snapshot/**/*.{cu,cuh,hpp}` whose content matches the content-pattern regex
    - For the "CUTLASS PersistentScheduler+CLC" question, the fixture requires `evidence/pull-bundles/cutlass/gh-2161/review.diff` to exist AND `evidence/pull-bundles/cutlass/gh-2161/source-snapshot/**` to be non-empty
    - For the "DeepGEMM Nc=128 CUDA-core promotion" question, the fixture requires at least one asset with `asset_mode: verbatim` (via companion `ORIGIN.yaml`)
    - For the "FA4 software exp" question, the fixture requires `evidence/blog-capsules/flash-attention-4/code/*` files whose aggregate matches the regex for exp|rescale patterns
  - Negative Tests (expected to FAIL):
    - A fixture entry whose `required_assets` glob matches nothing fails (e.g., the DeepGEMM Nc=128 file is missing)
    - A fixture entry whose only matching asset has `asset_mode: derived` when `required_provenance_modes: [verbatim, extracted]` fails
    - A matched file is shorter than `required_min_lines` fails
    - `required_content_patterns` regex fails to match across the matched files

- AC-8: CuTe DSL and Triton inclusion follow **separate, documented policies**
  - Positive Tests (expected to PASS):
    - `data/inclusion-policy.yaml` defines two distinct policies: `cute-dsl` (primary code lane, all tutorial+kernel PRs captured) and `triton` (scoped lane, only memory-bound / SM100-integration / backend-fallback PRs captured)
    - `scripts/compute_core_prs.py` applies the policies and reports a classification of the 22 CuTe DSL PRs and 42 Triton PRs into `captured` / `skipped-with-reason`
    - At least one `wiki/languages/cute-dsl.md` section `### Full Examples` enumerates verbatim CuTe DSL source files under `evidence/pull-bundles/cutlass/PR-*/source-snapshot/` or `evidence/kernel-cases/<slug>/full/`
    - `wiki/languages/triton-blackwell.md` gains a `### Blackwell Triton Examples` section that only cites Triton PRs where the scope matches the policy
  - Negative Tests (expected to FAIL):
    - A Triton PR for a pure Hopper-era kernel (no SM100 relevance) gets captured into `evidence/pull-bundles/` → fails policy check
    - The two policies are collapsed into a single `languages` allowlist → fails validation

- AC-9: Derived assets are labeled and quarantined from verbatim upstream code
  - Positive Tests (expected to PASS):
    - Files under `evidence/kernel-cases/<slug>/variants/` are allowed to have `asset_mode: derived` if they carry a file-header comment `// provenance: derived from <source-id-list>; not upstream code`
    - Files under `evidence/pull-bundles/**` and `evidence/challenge-capsules/**/submissions/**` always carry `asset_mode ∈ {verbatim, extracted}`, never `derived`
    - `scripts/validate.py` enforces the directory-to-mode mapping
  - Negative Tests (expected to FAIL):
    - A `derived` file placed under `evidence/pull-bundles/...` fails validation
    - A `verbatim` file under `evidence/kernel-cases/<slug>/variants/` without `upstream_sha` fails validation

- AC-10: Repo size and file-count stay within evidence-based bounds
  - **Baseline (measured)**: working tree excluding `.git/.humanize/.codex` is 7.0 MiB pre-Phase-3. Empty-`changed_paths` PRs (65/460) need path-reconciliation before any size estimate is believable.
  - **Size budget is evidence-based, not spreadsheet-fiction**: task5 runs a pilot fetch of 20 representative PRs (spanning CUTLASS, SGLang, vLLM, FlashInfer, PyTorch, with both small and large `changed_paths`). The pilot's aggregate `review.diff + source-snapshot/` size is extrapolated linearly (`pilot_size * target_pr_count / 20`) and published in `data/phase3-size-budget.yaml`. The real ceiling is set from that number plus 25% margin, not from the draft's guess.
  - **Scope → ceiling mapping**:
    - Lower bound (~80 core PRs + 12 hackathon kernels + 8 blog extractions + 4 deep wiki kernels): ceiling = `lower_bound_extrapolation * 1.25`, not to exceed 25 MiB working-tree (18 MiB headroom from baseline).
    - Upper bound (460 PRs + 21 submissions + 20 blog extractions + 12 deep wiki kernels): ceiling = `upper_bound_extrapolation * 1.25`, not to exceed 60 MiB working-tree. If the pilot extrapolation exceeds 60 MiB, the plan automatically falls back to the core set (AC-1) and documents which extra PRs were dropped with reason.
  - **Per-file and bundle size caps**: every single file in `evidence/` ≤ 1 MiB; every bundle aggregate ≤ 5 MiB. `size_cap_truncated` is a documented marker at two levels:
    - **File-level** `files[*].size_cap_truncated: true` — that specific entry's captured bytes are a truncated stub because the upstream file exceeded 1 MiB; the stub's first lines explain the truncation and cite the upstream URL.
    - **Bundle-level** `size_cap_truncated: true` (in the bundle-default block of `ORIGIN.yaml`) — the whole bundle was downgraded, e.g., `review.diff` was omitted because the aggregate exceeded 5 MiB.
    Both levels are independently validated; their absence when the caps are breached is a validation error.
  - **File-count budget**: ≤ 6000 files under `evidence/` (derived from the upper-bound estimate: 460 PRs × ~8 files/PR + 21 submissions × ~5 + 20 blogs × ~10 + 12 deep wiki × ~8 ≈ 4100, with 50% headroom). Overrun requires shrinking scope or bumping the ceiling with a recorded justification.
  - Positive Tests (expected to PASS):
    - `scripts/repo_size_check.py` (owned by task15) reports working-tree size within the active ceiling (lower-bound ceiling if operating lower-bound, upper-bound ceiling otherwise), and file count under budget
    - `data/phase3-size-budget.yaml` exists and records the pilot measurement + extrapolation + chosen ceiling
  - Negative Tests (expected to FAIL):
    - A commit that would push working-tree size above the active ceiling is rejected by `scripts/repo_size_check.py` (run via a git pre-commit hook installed by task15)
    - A single `review.diff` or `source-snapshot/...` > 1 MiB without a `files[*].size_cap_truncated: true` marker (file-level) or bundle-level `size_cap_truncated: true` (when the whole bundle was downgraded) in `ORIGIN.yaml` fails validation
    - The upper-bound scope is pursued without a pilot-based budget file in place → task14's final audit fails

- AC-11: Frontmatter contract for pointing from a source/wiki page to its evidence bundle is consistent and validator-enforced
  - **Single-field contract**: a page points at its bundle via `artifact_dir: <path-relative-to-repo-root>`. Per-file pointers exist only as `files[*].local_path` inside a bundle's `ORIGIN.yaml`, or as `submissions[*].code_path` inside a `source-contest` page's nested submission list. No alternate page-level code-pointer sibling of `artifact_dir:` is allowed; the disallow-list is enforced via `data/schemas.yaml`.
  - Positive Tests (expected to PASS):
    - Every `sources/prs/<repo>/PR-<N>.md` with an associated bundle carries `artifact_dir: evidence/pull-bundles/<repo>/gh-<N>` and no sibling page-level code-pointer field alongside it
    - Every `sources/contests/**/*.md` submission entry uses `code_path:` inside its `submissions[*]` object, which must resolve relative to the page's implicit bundle at `evidence/challenge-capsules/<contest>/<problem>/submissions/<rank-N-author>/`
    - Every deep wiki kernel page carries `artifact_dir: evidence/kernel-cases/<slug>` at the frontmatter level; the bundle contains `full/` and optionally `variants/`
  - Negative Tests (expected to FAIL):
    - A page frontmatter carrying `artifact_dir:` and any disallow-listed alternate code-pointer field at the top level fails validation (the two-contract confusion Codex flagged during convergence)
    - An `artifact_dir` that does not exist on disk fails validation

## Path Boundaries

### Upper Bound (Maximum Acceptable Scope)

The repository contains cleaned bundles (`review.diff` + `source-snapshot/`) for all **460** PRs currently tagged `included` **iff the pilot-based size extrapolation demonstrates feasibility within the 60 MiB upper-bound ceiling defined in AC-10**; otherwise, the plan automatically falls back to a core-plus subset documented in `data/phase3-size-budget.yaml`. Upper-bound also delivers: full code of the **21** hackathon + MLSys26 top-3 submissions where authors have public releases, extracted code blocks for all **20** blogs with code fences, and **12 deepened wiki kernel/technique pages** each with a `full/` verbatim-or-extracted canonical kernel plus 3–5 labeled `variants/` showing the naive→optimized progression. `wiki/languages/cute-dsl.md` and `wiki/languages/triton-blackwell.md` each gain their own `### Full Examples` / `### Blackwell Triton Examples` section citing verbatim local files from `evidence/pull-bundles/**`. Query, fetch, grep, and validator tools are all code-aware. `data/inclusion-policy.yaml` documents explicit CuTe DSL and Triton policies. A git pre-commit hook enforces the active size ceiling.

### Lower Bound (Minimum Acceptable Scope)

The repository contains cleaned bundles for the automation-derived "core PR" set (~60–80 PRs, the graph closure of `wiki/**.sources` plus the CuTe DSL / contest-referenced allowlists), **12 hackathon kernels** where authors have public releases (the FlashInfer MLSys 2026 9 track entries may be `unavailable` if the leaderboard is not yet public), extracted code blocks for every blog whose markdown contains fenced code (empirically ≥ 8 blogs: FA4, Colfax CUTLASS, tcgen05-tutorial, hackathon participant blogs, DeepGEMM, etc.) with the remaining code-less blogs still receiving a `MANIFEST.yaml` carrying `code_present: false` (so the full 20-blog corpus has uniform downstream treatment), and **4 deepened wiki kernel pages** (nvfp4-gemv, warp-specialization, flash-attention-4, deepgemm — one per four of the five Definition-of-Done questions; the fifth answer comes from the PR-2161 cleaned bundle which is required regardless). The CuTe DSL and Triton capture-and-classify step (task2b) runs even at lower bound, so `wiki/languages/cute-dsl.md` gains at least one `### Full Examples` entry pointing to a real local file. Query tooling supports `--has-code` and `--include-code`; validator enforces provenance, nested schema, frontmatter-contract uniqueness, and the lower-bound size ceiling (25 MiB working-tree).

### Allowed Choices

- **Can use**: `gh api` for per-file retrieval at a pinned `merge_sha`, and `gh pr diff` for whole-patch capture; whichever produces the smaller cleaned bundle per PR is preferred; symlinks within `evidence/` to avoid duplication; file-header license preservation (Apache-2.0 / MIT inherited); derived kernels under `evidence/kernel-cases/<slug>/variants/` with explicit labeling.
- **Can use**: `git submodule` for a pinned upstream mirror — **only when** (a) the upstream repo's kernel universe exceeds 10 captured PRs, AND (b) the pinned snapshot is < 2 MiB, AND (c) a `ORIGIN.yaml` at the submodule root records the pin. Default is no submodules; the single-clone install promise wins unless these three conditions all hold.
- **Cannot use**: embedding code files inside `wiki/` (must live under `evidence/`); uploading PR diffs or blog code without a bundle-root `ORIGIN.yaml`; synthesizing "full kernels" presented as upstream truth (all synthesized files must be `asset_mode: derived` and segregated under `evidence/kernel-cases/<slug>/variants/`); scraping Discord-only content without the author's public republish; Git LFS (adds install friction, blocks the one-shot clone); placing any alternate code-pointer sibling of `artifact_dir:` at the page frontmatter level (see AC-11).

## Feasibility Hints and Suggestions

### Conceptual Approach

```
1. Schema + tooling upgrade (task1, task3, task4, task15)
   - Extend data/schemas.yaml with artifact_dir, asset_mode, submission_truth,
     upstream_sha, nested submissions[*] validation
   - Author data/inclusion-policy.yaml (CuTe DSL primary lane; Triton scoped)
   - Author data/core-prs-allowlist.yaml (human-justified additions / exclusions)
   - Write scripts/compute_core_prs.py (deterministic graph-closure, checksumed
     output) and its companion scripts/verify_core_prs.py
   - Extend scripts/validate.py for nested schema, provenance presence,
     frontmatter-contract uniqueness, derived-vs-verbatim placement
   - Extend scripts/query.py, get_page.py, grep_wiki.py for code-awareness
   - Build scripts/verify_verbatim.py, scripts/repo_size_check.py,
     scripts/check_dod_fixtures.py; install git pre-commit hook

2. Universe freeze + pilot (task2a, task2b, task5 pilot phase)
   - Run scripts/compute_core_prs.py → data/core-prs.yaml,
     data/cute-dsl-universe.yaml, data/triton-universe.yaml (all checksumed)
   - Run scripts/fetch_pr_diff.py in 20-PR pilot mode → data/phase3-size-budget.yaml
   - Pick active ceiling (lower-bound or upper-bound) from the budget; document
     the choice

3. Core PR bundle capture (task6)
   - scripts/fetch_pr_diff.py full-run over data/core-prs.yaml
   - Per PR: gh api /repos/{owner}/{repo}/pulls/{N}/files at merge_sha,
     filter by kernel allowlist, write review.diff + source-snapshot/ + ORIGIN.yaml
   - Kernel allowlist: *.cu, *.cuh, *.cpp, *.hpp, *.h under kernel dirs;
     *.py/*.pyx only when path contains kernel/triton/cute/ops; CuTe DSL
     tutorial *.py included unconditionally
   - Reconcile the 65 empty-changed_paths PRs using the fetched file-list
   - Update sources/prs/<repo>/PR-<N>.md with artifact_dir:

4. Contest + blog code landing (task7-10)
   - scripts/collect_contest_code.py: iterate contest submissions, fetch
     author-public code, set submission_truth per entry
   - scripts/extract_blog_code.py: markdown-AST-driven extraction with
     SHA-256 manifest checksums; idempotent --check mode
   - Reconcile the 18.5µs/22.4µs problem-1 inconsistency

5. Deep wiki kernels + DoD fixture (task11, task12)
   - For each of 4 anchor pages: evidence/kernel-cases/<slug>/full/<kernel>.cu
     (verbatim-or-extracted, sourced from evidence/pull-bundles/** or evidence/blog-capsules/**)
     + evidence/kernel-cases/<slug>/variants/<N>-<tag>.cu (derived, labeled)
   - Author data/phase3-dod-fixtures.yaml encoding the 5 DoD questions with
     required_assets + min_lines + provenance_modes + content_patterns
   - Extend to 8 more pages if the budget allows

6. CuTe DSL + Triton language integration (task13)
   - wiki/languages/cute-dsl.md ### Full Examples: ≥ 3 verbatim local files
   - wiki/languages/triton-blackwell.md ### Blackwell Triton Examples:
     ≥ 3 entries, all from captured:true PRs in data/triton-universe.yaml

7. Final audit (task14)
   - scripts/validate.py: 0 errors
   - scripts/check_dod_fixtures.py: all fixture entries pass
   - scripts/repo_size_check.py: within active ceiling
   - Empirical skill-load test (DEC-5 verification)
   - Structured Codex audit per-AC until STATUS: complete
```

### Relevant References

- `data/schemas.yaml` — Phase 3 extends the `source-pr`, `source-contest`, `source-blog`, `wiki-kernel`, `wiki-technique` schemas with new optional fields listed in §3.
- `data/tags.yaml`, `data/aliases.yaml` — controlled vocabulary, extended if new kernel-class tags surface during CuTe DSL / Triton reclassification.
- `scripts/validate.py` — current validator, extended for nested `submissions[*]` validation and `evidence/**` reference checking.
- `scripts/query.py`, `scripts/get_page.py`, `scripts/grep_wiki.py` — existing tools extended with code-awareness.
- `sources/prs/cutlass/PR-2161.md` — canonical example of a PR page whose associated `evidence/pull-bundles/cutlass/gh-2161/` directory will ship a cleaned diff for the "CUTLASS PersistentScheduler+CLC" Definition-of-Done question.
- `wiki/languages/cute-dsl.md`, `wiki/languages/triton-blackwell.md` — both pages gain `### Full Examples` / `### Blackwell Triton Examples` sections citing verbatim local files.
- Upstream candidate repos for verbatim capture: `NVIDIA/cutlass` (CuTe DSL tutorial tree), `deepseek-ai/DeepGEMM`, `Dao-AILab/flash-attention` (if FA4 branch is public), `flashinfer-ai/flashinfer` (kernels tree), `sgl-project/sgl-kernel`.
- `data/aliases.yaml` §Architecture — the existing `sm100` alias set resolves `B200/Blackwell` queries; CuTe DSL alias extension is probably needed for `cutlass.cute.*` namespace.

## Dependencies and Sequence

### Milestones

1. Milestone 1 — Infrastructure + ownership (task1, task3, task4, task15)
   - Phase A: Extend `data/schemas.yaml` with artifact-aware fields; author `data/inclusion-policy.yaml` and `data/core-prs-allowlist.yaml`
   - Phase B: Extend `scripts/validate.py` (nested schema, provenance presence, frontmatter-contract uniqueness, placement rule, per-file cap)
   - Phase C: Extend `scripts/query.py`, `scripts/get_page.py`, `scripts/grep_wiki.py` for code-awareness
   - Phase D: Build `scripts/verify_verbatim.py`, `scripts/repo_size_check.py`, `scripts/check_dod_fixtures.py`; install git pre-commit hook

2. Milestone 2 — Universe freeze + pilot (task2a, task2b, task5 pilot)
   - Step 1: Run `scripts/compute_core_prs.py` → `data/core-prs.yaml`, `data/cute-dsl-universe.yaml`, `data/triton-universe.yaml` (all checksumed, deterministic)
   - Step 2: Run `scripts/verify_core_prs.py --strict` (reproducibility check)
   - Step 3: Run `scripts/fetch_pr_diff.py` 20-PR pilot → `data/phase3-size-budget.yaml`
   - Step 4: Pick active ceiling (lower-bound 25 MiB vs upper-bound 60 MiB) based on the budget; record the choice

3. Milestone 3 — Core PR bundle capture (task6)
   - Step 1: `scripts/fetch_pr_diff.py` full-run over `data/core-prs.yaml`; commit batches of ≤ 20 PRs
   - Step 2: Reconcile the 65 empty-`changed_paths` PRs using authoritative file-lists from the fetch; drop those whose kernel-filter yields zero files with a `skipped_reason:`
   - Step 3: Update each `sources/prs/<repo>/PR-<N>.md` with `artifact_dir:`
   - Step 4 (optional upper bound): extend beyond core set toward the 460 PRs, bounded by the active ceiling

4. Milestone 4 — Contest + blog code (task7, task8, task9, task10)
   - Step 1: Implement `scripts/extract_blog_code.py`; run across 20 blogs with `--check` idempotency verification
   - Step 2: Implement `scripts/collect_contest_code.py`; run across GPU Mode NVFP4 hackathon; record `submission_truth`
   - Step 3: FlashInfer MLSys 2026 tracks: `unavailable` entries with `code_unavailable_reason` pointing at the leaderboard URL if public code is not yet released
   - Step 4: Reconcile `sources/contests/gpu-mode-nvfp4/problem-1-gemv.md` frontmatter (18.5µs → 22.4µs per body evidence)

5. Milestone 5 — Deep wiki kernel pages + DoD fixture (task11, task12, task13)
   - Step 1: Select anchor pages (nvfp4-gemv, warp-specialization, flash-attention-4, deepgemm); populate `full/` verbatim + `variants/` derived for each
   - Step 2: Author `data/phase3-dod-fixtures.yaml` (5 questions, mechanically checkable)
   - Step 3: Extend `wiki/languages/cute-dsl.md` `### Full Examples` and `wiki/languages/triton-blackwell.md` `### Blackwell Triton Examples` with ≥3 verbatim local files each
   - Step 4 (optional upper bound): 8 more deep wiki pages

6. Milestone 6 — Final validation + Codex audit (task14)
   - Step 1: `scripts/validate.py` → 0 errors
   - Step 2: `scripts/check_dod_fixtures.py` → all 5 entries pass
   - Step 3: `scripts/repo_size_check.py` → within active ceiling
   - Step 4: Empirical skill-load test (DEC-5 verification via measurement); record in `data/phase3-skill-load.md`
   - Step 5: Structured Codex audit per-AC; iterate until `STATUS: complete` on all 11 ACs

### Relative Dependencies

- Milestone 1 gates everything: no code capture before schema + validator + size-check + DoD-fixture-checker exist
- Milestone 2's `data/phase3-size-budget.yaml` gates Milestone 3's scope decision (lower vs upper bound)
- Milestone 3 must deliver `evidence/pull-bundles/cutlass/gh-2161/` before Milestone 5 can cite it for the CUTLASS PersistentScheduler DoD answer
- Milestone 4's extracted blog code (especially FA4) gates Milestone 5's `flash-attention-4` anchor page
- Milestone 5's anchor pages gate `scripts/check_dod_fixtures.py` returning green, which is a Milestone 6 prerequisite
- `data/inclusion-policy.yaml` (Milestone 1 Phase A) gates Milestone 2's CuTe DSL / Triton classification

## Task Breakdown

| Task ID | Description | Target AC | Tag | Depends On |
|---------|-------------|-----------|-----|------------|
| task1 | Extend `data/schemas.yaml` with `artifact_dir`, `asset_mode`, `submission_truth`, `upstream_sha`, `code_unavailable_reason`, and **nested** `submissions[*]` schema (the current validator skips nested validation). Document `size_cap_truncated` at two levels (bundle-level inside `ORIGIN.yaml` defaults = the whole bundle was downgraded; file-level inside `files[*]` entries = that specific file's content was truncated to a stub). Author `data/inclusion-policy.yaml` (CuTe DSL primary lane; Triton scoped lane with explicit criteria: memory-bound / SM100-integration / backend-fallback) and `data/core-prs-allowlist.yaml`. Document the single-field frontmatter contract: the only page-level pointer is `artifact_dir:`; per-file pointers exist only as `files[*].local_path` inside bundle `ORIGIN.yaml` or as `submissions[*].code_path` inside `source-contest` nested lists. | AC-2, AC-3, AC-5, AC-8, AC-10, AC-11 | coding | — |
| task2a | Implement `scripts/compute_core_prs.py`: graph-closure over `wiki/**.sources`, union contest-referenced PRs (BFS through `sources/contests/**` bodies), apply `data/inclusion-policy.yaml` filter, produce deterministic ordered output to `data/core-prs.yaml` with a content checksum at the top of the file. Also write `data/cute-dsl-universe.yaml` and `data/triton-universe.yaml` — the full classified candidate universes (CuTe DSL: 22 PRs; Triton: 42 PRs as measured) with per-entry `captured: true|false` and `skipped_reason:` for the `false` cases. | AC-1, AC-8 | coding | task1 |
| task2b | Implement `scripts/verify_core_prs.py`: re-runs task2a's derivation and asserts the output is byte-equal to `data/core-prs.yaml` (deterministic-regeneration check); also resolves each PR's `merge_sha` via `gh api` and flags entries whose upstream state is `reverted` or `unknown`. `--strict` mode fails on any flag; default mode warns. | AC-1 | coding | task2a |
| task3 | Extend `scripts/validate.py`: (a) full nested validation of `submissions[*]` including `submission_truth` presence and `code_path` existence; (b) `ORIGIN.yaml` presence at every asset-bundle root (one and only one per bundle, no nested declarations); (c) `artifact_dir:` existence check (page level) and `files[*].local_path` existence + SHA-256 match (bundle level) and `submissions[*].code_path` existence (nested level); (d) derived vs verbatim directory-placement rule (AC-9); (e) per-file ≤ 1 MiB cap with `files[*].size_cap_truncated: true` escape hatch, bundle ≤ 5 MiB cap with bundle-level `size_cap_truncated: true` escape hatch; (f) frontmatter-contract uniqueness (AC-11 negative test: no alternate code-pointer field at page-level top; disallow-list codified in `data/schemas.yaml`). | AC-2, AC-3, AC-5, AC-9, AC-10, AC-11 | coding | task1 |
| task4 | Extend `scripts/query.py` with `--has-code` (filters to pages whose `artifact_dir` contains ≥ 1 source file) and `--include-code` flag on `scripts/get_page.py` (prints bundle files after the page body); extend `scripts/grep_wiki.py` with `--ext cu,cuh,ptx,py,cpp,h,hpp` to search inside `evidence/**` source files. Keep backward compatibility: unflagged behavior is unchanged. | AC-6 | coding | task1 |
| task5 | Implement `scripts/fetch_pr_diff.py`: given a list of PR IDs, for each PR use `gh api /repos/{owner}/{repo}/pulls/{N}/files` to get the file list at `merge_sha`, apply the kernel-file allowlist (`*.cu`, `*.cuh`, `*.cpp`, `*.hpp`, `*.h` under kernel directories; `.py` and `.pyx` only when the path contains `kernel/triton/cute/ops`; blog tutorial `.py` for CuTe DSL), preserve file-header license comments, and emit `review.diff` + `source-snapshot/<upstream-path-mirror>/*` + `ORIGIN.yaml` per bundle. **Size-cap enforcement (aligned with AC-10)**: (a) per-file cap — any `source-snapshot/...` entry > 1 MiB is either split across multiple smaller files or its `files[*]` entry is flagged with `size_cap_truncated: true` and the oversized content is replaced with a summary stub; (b) bundle-total cap — any bundle whose aggregate exceeds 5 MiB is downgraded to `source-snapshot/`-only (no `review.diff`) and the bundle's `ORIGIN.yaml` sets `size_cap_truncated: true` at the bundle level. **First invocation runs a 20-PR pilot** spanning all 5 repos; pilot output is written to `data/phase3-size-budget.yaml` and used to set AC-10's active ceiling before full-scale runs begin. | AC-1, AC-2, AC-10 | coding | task1, task3 |
| task6 | Run `scripts/fetch_pr_diff.py` across the frozen `data/core-prs.yaml` set (lower-bound path first, extend toward `data/cute-dsl-universe.yaml` + `data/triton-universe.yaml` captured set afterward). Commit in batches of ≤ 20 PRs to keep review tractable. Update each `sources/prs/<repo>/PR-<N>.md` with an `artifact_dir:` pointer. Reconcile the 65 PRs with empty `changed_paths` by re-deriving from the fetched file-list (task5 produces authoritative paths) and writing them back; PRs whose reconciliation yields zero kernel-relevant files are dropped from the captured set with a `skipped_reason:` recorded in `data/core-prs.yaml`. | AC-1, AC-2, AC-7, AC-10 | coding | task5 |
| task7 | Implement `scripts/extract_blog_code.py`: markdown AST parser (prefer `mistune` or `markdown-it-py`) → `evidence/blog-capsules/<slug>/code/NN-<heading-slug>.<ext>` + `MANIFEST.yaml` with per-file heading-path **and** SHA-256 content checksum (AC-4). `--check <blog-slug>` mode is idempotent: re-parses markdown, re-extracts in-memory, compares to on-disk files + manifest checksums, exits 0 only if all match. | AC-4 | coding | task1, task3 |
| task8 | Run blog code extraction across the 20 blogs; for blogs with substantive code (FA4, Colfax CUTLASS, tcgen05-tutorial, Simon/yue/Amandeep hackathon blogs, DeepGEMM blog, etc.) verify each extracted file against its originating markdown section; for blogs without code fences write a `MANIFEST.yaml` noting `code_present: false`. | AC-4 | coding | task7 |
| task9 | Implement `scripts/collect_contest_code.py`: iterates `sources/contests/**`, looks up author-published-posthoc code via each `submissions[*]`'s existing URL hints (participant GitHub/personal blog/Discord-pointed-GitHub), fetches code into `evidence/challenge-capsules/<contest>/<problem>/submissions/<rank-N-author>/{kernel.<ext>, approach.md}`, and records `submission_truth` (`official-submission` / `author-published-posthoc` / `reconstructed-from-blog` / `unavailable`). For `unavailable`, populate `code_unavailable_reason`. | AC-3 | coding | task1, task3 |
| task10 | Run contest collection across the GPU Mode NVFP4 hackathon (12 slots across 4 problems) and FlashInfer MLSys 2026 (3 tracks × top-3, where public). Reconcile the `~18.5µs` frontmatter vs `~22.4µs` body inconsistency in `sources/contests/gpu-mode-nvfp4/problem-1-gemv.md` by editing the frontmatter to match body evidence (22.4µs) and noting the reconciliation in a commit message referencing this AC. | AC-3, AC-7 | coding | task9 |
| task11 | Deep wiki kernel pages (lower-bound anchor set of 4): populate `evidence/kernel-cases/nvfp4-gemv/`, `evidence/kernel-cases/warp-specialization/`, `evidence/kernel-cases/flash-attention-4/`, `evidence/kernel-cases/deepgemm/` with a `full/` canonical kernel (verbatim-or-extracted, not derived) and `variants/` for naive→optimized progression. Every `variants/*` file carries a `// provenance: derived from <source-ids>; not upstream code` header. Edit the corresponding `wiki/**.md` pages to add a `## Full Reference Implementation` section linking to `artifact_dir`. **Author `data/phase3-dod-fixtures.yaml`** (AC-7 mechanism): encode the five Definition-of-Done questions with `required_assets`, `required_min_lines`, `required_provenance_modes`, and `required_content_patterns` so `scripts/check_dod_fixtures.py` can verify pass/fail mechanically. | AC-7, AC-9 | coding | task6, task8, task10 |
| task12 | Upper-bound path: expand deep wiki kernel coverage to 8 more pages: `nvfp4-gemm`, `flashmla`, `gated-delta-net`, `gated-dual-gemm`, `fused-moe`, `epilogue-fusion`, `persistent-kernels`, `ping-pong-scheduling`. Each gets `full/` + at least one `variants/` file. Executed only if the pilot-based size budget (AC-10) allows headroom. | AC-7, AC-9 | coding | task11 |
| task13 | CuTe DSL and Triton deep integration: add `### Full Examples` to `wiki/languages/cute-dsl.md` citing verbatim CuTe DSL files from `evidence/pull-bundles/cutlass/PR-*/source-snapshot/**/*.py`; add `### Blackwell Triton Examples` to `wiki/languages/triton-blackwell.md` citing only Triton PRs whose `data/triton-universe.yaml` entry has `captured: true`. Validation target: for each DSL, at least 3 linked entries point to local files whose `ORIGIN.yaml` is `asset_mode: verbatim`. | AC-8 | coding | task6 |
| task14 | Full `scripts/validate.py` run → 0 errors. `scripts/check_dod_fixtures.py` → all 5 Definition-of-Done entries pass. `scripts/repo_size_check.py` → within active ceiling (from `data/phase3-size-budget.yaml`). **Empirical skill-load test** (resolves DEC-5): clone the repo to a temp path, measure Claude Code's skill-directory scan latency and context footprint on boot; record the measurement in `data/phase3-skill-load.md`; if the observed behaviour requires an exclude mechanism, document what the actual Claude Code feature is (or open an upstream issue) — do not invent `.claude-skill-ignore`. Codex audit iterates per-AC until `STATUS: complete`. | AC-1 – AC-11 | analyze | task2a, task2b, task3, task4, task6, task8, task10, task11, task13, task15 |
| task15 | Implement the ownership scripts + git hook that several ACs reference: `scripts/verify_verbatim.py --strict` (byte-matches every `files[*]` entry whose `mode` is `verbatim` or `upstream-patch` against `gh api` / `gh pr diff` content at pinned `upstream_sha`); `scripts/repo_size_check.py` (reports working-tree size excluding `.git/.humanize/.codex`, file count under `evidence/`, max file size, compares against `data/phase3-size-budget.yaml` when present); `scripts/check_dod_fixtures.py` (runs `data/phase3-dod-fixtures.yaml` entries when the file exists, exits non-zero only on failure of existing entries). Install a **conditional git pre-commit hook**: always runs `scripts/validate.py`; runs `scripts/repo_size_check.py` only if `data/phase3-size-budget.yaml` exists (so intermediate Milestone-1/2 commits don't fail due to missing budget file); runs `scripts/check_dod_fixtures.py` only if `data/phase3-dod-fixtures.yaml` exists (authored in task11). This keeps intermediate commits tractable while still gating the final repo state. | AC-1, AC-2, AC-7, AC-10 | coding | task1, task3 |

## Claude-Codex Deliberation

### Agreements (pre-convergence round)

- The Phase 2 corpus is "index cards": 545 markdown files with ~10–80 lines of real code each, insufficient for LLM-only kernel authoring.
- PR diffs, contest kernel sources, and blog code are the three natural axes of code ingestion.
- Provenance metadata is mandatory per asset; `verbatim` / `extracted` / `derived` is the right three-way split (Codex-proposed, Claude-accepted).
- Contest submissions need a four-valued truth-model (`official-submission` / `author-published-posthoc` / `reconstructed-from-blog` / `unavailable`) (Codex-proposed, Claude-accepted).
- Code assets live in a separate `evidence/` tree; do NOT embed inside `wiki/` (Codex-proposed, Claude-accepted — supersedes the draft's proposed `wiki/kernels/<slug>/full/` layout).
- "Core PR" set must be deterministic and reproducible from automation, not a hand-curated "TBD ~60" (Codex-proposed, Claude-accepted).
- CuTe DSL and Triton require separate inclusion policies because Triton on SM100 has no direct tcgen05/TMEM access per `wiki/languages/triton-blackwell.md`.
- The existing `sources/contests/gpu-mode-nvfp4/problem-1-gemv.md` has a self-inconsistent `~18.5µs` frontmatter vs `~22.4µs` body; this must be reconciled during Phase 3 (Codex-spotted).
- 65/460 PRs have empty `changed_paths` — the task6 path-reconciliation step addresses this gap rather than ignoring it.
- The current draft's "~5MB" repo estimate is wrong; actual working tree is ~7 MiB. AC-10's active ceiling (25 MiB lower-bound / 60 MiB upper-bound, pilot-derived) is sized accordingly with headroom.

### Resolved Disagreements

- *"Code goes under `wiki/kernels/<slug>/full/`" (draft) vs "Code goes under a separate `evidence/` tree" (Codex first-pass)*: Resolved in favour of `evidence/`. Rationale: keeps `sources → wiki → queries` intact; simplifies directory-to-asset-mode enforcement (AC-9); makes code indexing a first-class concern.
- *"~60 core PRs, TBD" (draft) vs "deterministic graph-derived core set" (Codex first-pass)*: Resolved via automation. `scripts/compute_core_prs.py` produces `data/core-prs.yaml`; allowlist deltas go through `data/core-prs-allowlist.yaml` with human-written justifications.
- *"Synthesize variants freely" (draft) vs "Derived content must be quarantined and labeled" (Codex first-pass)*: Resolved — derived assets are allowed only under `evidence/kernel-cases/<slug>/variants/`, carry file-header `provenance: derived from ...` comments, and never appear under `evidence/pull-bundles/**` or `evidence/challenge-capsules/**`.
- *"Provenance unit = each `evidence/**` directory" (candidate v1) vs "Provenance unit = evidence bundle root" (Codex convergence round 1)*: Resolved in favour of "evidence bundle root" with a flat ownership graph; AC-2 rewritten; nested `ORIGIN.yaml` declarations are explicitly disallowed.
- *"AC-7 qualitative answerability" (candidate v1) vs "AC-7 needs a scripted fixture" (Codex convergence round 1)*: Resolved — AC-7 now encodes its check in `data/phase3-dod-fixtures.yaml` and `scripts/check_dod_fixtures.py`.
- *"Single fixed ceiling" (candidate v1) vs "Ceiling must be pilot-based evidence" (Codex convergence round 1)*: Resolved — AC-10 rewritten to derive active ceiling from a 20-PR pilot recorded in `data/phase3-size-budget.yaml`; 25 MiB (lower-bound) and 60 MiB (upper-bound) brackets replace the candidate v1 fixed figure.
- *"Multiple peer-level code-pointer fields at page frontmatter" (candidate v1) vs "Single-field contract: `artifact_dir` at page level, per-file pointers only inside bundle metadata or nested submission lists" (Codex convergence round 1)*: Resolved — AC-11 added; frontmatter-contract uniqueness is validator-enforced.
- *"Several named scripts (verify_core_prs, verify_verbatim, repo_size_check, pre-commit gate) have no owner" (Codex convergence round 1)*: Resolved — task2b and task15 added as explicit owners.
- *"Bloated pending-decision list (6 items)" (Codex convergence round 1)*: Resolved — the five non-licensing decisions collapsed into default resolutions; only the licensing policy required a standing user call, and was subsequently resolved to the conservative default (see below).
- *"Bundle `ORIGIN.yaml` too weak for multi-file PR evidence bundles (one scalar `upstream_path` cannot describe a `review.diff` plus many `source-snapshot/**`)" (Codex convergence round 2)*: Resolved — schema now has a per-file `files[*]` manifest with `{local_path, role, mode, upstream_path?, sha256, heading_path?}`; extracted-mode semantics explicitly specified (`heading_path` required, `upstream_path` points to blog-source-repo path or the sentinel `"inline-in-blog-markdown"`); AC-2 rewritten accordingly.
- *"AC-5 carried an obsolete page-level peer-pointer existence rule conflicting with AC-11's single-field contract" (Codex convergence round 2)*: Resolved — AC-5 rewritten to scope validation to `artifact_dir:` at the page level, `submissions[*].code_path` in nested entries, and `files[*].local_path` inside bundle `ORIGIN.yaml`.
- *"Pre-commit hook sequenced too early (Milestone 1 installs a hook whose required inputs aren't created until Milestones 2 and 5)" (Codex convergence round 2)*: Resolved — task15's hook is now **conditional**: always runs `scripts/validate.py`, runs `scripts/repo_size_check.py` only if `data/phase3-size-budget.yaml` exists, runs `scripts/check_dod_fixtures.py` only if `data/phase3-dod-fixtures.yaml` exists. Intermediate commits are not blocked; final repo state is still gated.

### Convergence Status
- Final Status: `converged` (two convergence rounds executed; all Codex required changes from both rounds applied; the licensing policy was resolved to the conservative default per the repo owner's explicit request to skip human review; no outstanding decisions remain.)

## Decision Status

> All initial disagreements have been resolved into plan-level defaults. No decisions are open. The contest-licensing policy (previously considered as DEC-1) has been set to the conservative default described below and is documented under "Default Resolutions" for potential user override.

*(All decisions resolved; none outstanding.)*

### Default Resolutions (previously considered for user input; may be overridden)

- ~~DEC-1: Contest submission licensing~~ → **Default (conservative)**: only store submissions whose author has republished on a public platform (personal GitHub, personal blog, project repository) with an implicit redistribution posture. For Discord-only content, set `submission_truth: unavailable` and populate `code_unavailable_reason` with the Discord message URL plus the reason string `"Discord-only posting; no author republish on a public platform"`. This protects against copyright complications; expected cost is 3–6 of the 12 hackathon slots dropping to `unavailable`. Both Claude and Codex agreed on this default; the repo owner explicitly elected to skip human review and adopt the conservative posture.

- ~~DEC-2: PR capture scope~~ → **Default**: core set first (from `data/core-prs.yaml`), then extend toward captured CuTe DSL + Triton universe set, then toward 460 PRs only if pilot-based size budget (AC-10) demonstrates feasibility. Task6 Step 4 is explicitly optional.
- ~~DEC-3: Upstream-repo mirroring~~ → **Default**: no `git submodule` by default. A submodule is allowed only when (a) >10 PRs from that upstream are captured, (b) pinned snapshot < 2 MiB, (c) `ORIGIN.yaml` records the pin. See "Allowed Choices" path boundary.
- ~~DEC-4: Verification bar~~ → **Default**: file existence + `ORIGIN.yaml` schema completeness + `scripts/verify_verbatim.py --strict` byte-match for `asset_mode: verbatim` assets. No `nvcc` syntax check (toolchain not portable). Documented in AC-2.
- ~~DEC-5: Skill-load mechanism~~ → **Resolved technical**: task14 empirically measures Claude Code's skill-dir scan behaviour on a clean clone. Writes the measurement to `data/phase3-skill-load.md`. The plan does not invent `.claude-skill-ignore` — if the measurement shows scan pressure, the corrective action is documented based on the real Claude Code runtime behaviour, not an assumed feature.
- ~~DEC-6: Repo split~~ → **Default**: single `KernelPilot Knowledge` repo. The 25 MiB lower-bound / 60 MiB upper-bound ceilings keep the single-clone promise tractable; split is revisited only if the upper-bound ceiling is breached during task6 extension, in which case an explicit follow-up proposal is written before any split happens.

## Implementation Notes

### Code Style Requirements

- Implementation code and comments must NOT contain plan-specific terminology such as "AC-", "Milestone", "Step", "Phase", or similar workflow markers
- Use descriptive, domain-appropriate naming: e.g., `compute_core_prs.py`, not `AC1_core_pr_deriver.py`; comments describe WHY the code behaves as it does, not which acceptance criterion they satisfy
- `ORIGIN.yaml` field names and `asset_mode` vocabulary are content-layer concepts (shared with Phase 3's data), not plan-layer markers, so they are fine to use in code.

### Content-Layer Conventions

- Every bundle-root `ORIGIN.yaml` follows this schema (enforced by `scripts/validate.py`):

  ```yaml
  # Bundle-level defaults
  origin_url: <URL of the originating PR/blog/contest-problem/wiki-page>
  upstream_repo: <owner/name>             # or URL for non-GitHub sources
  upstream_sha: <40-char SHA>             # the merge commit for PR evidence bundles; the
                                          # blog-repo commit if the blog ships
                                          # its markdown on GitHub; omitted (with
                                          # explicit "upstream_sha: none") when
                                          # only inline-markdown source exists
  license: <SPDX id or "unknown" or "multiple (see files)">
  retrieved_at: <YYYY-MM-DD>
  asset_mode: verbatim | extracted | derived   # bundle-default mode
  derived_from: [<source_id>, ...]             # required when asset_mode=derived
  size_cap_truncated: false                     # bundle-level: true if whole
                                                 # bundle was downgraded (e.g.
                                                 # review.diff omitted because
                                                 # aggregate > 5 MiB)
  license_notice: <optional-path-to-NOTICE>

  # Per-file manifest
  files:
    - local_path: review.diff
      role: pr-diff
      mode: upstream-patch
      sha256: <64-char hex>
      size_cap_truncated: false                  # file-level: true if this
                                                  # entry's content is a stub
                                                  # because upstream > 1 MiB
    - local_path: source-snapshot/include/cutlass/detail/collective/mixed_input_utils.hpp
      role: upstream-file
      mode: verbatim
      upstream_path: include/cutlass/detail/collective/mixed_input_utils.hpp
      sha256: <64-char hex>
    - local_path: 01-mainloop.cu                # blog-extracted example
      role: extracted-block
      mode: extracted
      heading_path: "## Mainloop"
      sha256: <64-char hex>
    - local_path: variants/01-naive.cu          # derived variant example
      role: derived-source
      mode: derived
      sha256: <64-char hex>
    - local_path: approach.md                   # contest-submission note
      role: approach-notes
      mode: extracted
      sha256: <64-char hex>
  ```

- `mode` values and their verification semantics:
  - `verbatim` — `scripts/verify_verbatim.py --strict` byte-matches `local_path` bytes against `gh api contents/<upstream_path>?ref=<upstream_sha>` from `upstream_repo`
  - `upstream-patch` — byte-matches `local_path` bytes against `gh pr diff <N>` at `upstream_sha` for the declared PR
  - `extracted` — no byte-equality check against upstream; `sha256` detects hand-edits; `heading_path` is required
  - `derived` — only allowed under `evidence/kernel-cases/<slug>/variants/`; bundle-level `derived_from:` must cite existing page IDs

- Code file-header comment for `mode: derived` files:
  ```c
  // provenance: derived from <comma-separated source-ids>; not upstream code
  // origin: wiki/<slug> Phase 3 variants; see ORIGIN.yaml in this directory
  ```
