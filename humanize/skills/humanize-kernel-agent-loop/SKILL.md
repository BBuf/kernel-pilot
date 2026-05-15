---
name: humanize-kernel-agent-loop
description: "Run an end-to-end Humanize Kernel Agent Loop for GPU kernel optimization: plan, refine, create a clean standalone repo, use kernel-knowledge, benchmark, profile with Nsight Compute, maintain lineage/ledgers, and start RLCR."
type: flow
---

# Humanize Kernel Agent Loop

Use this flow when the user wants a CUDA kernel optimization loop, not a
general software feature loop. This is a kernel-specialized wrapper around
Humanize RLCR.

The installer hydrates these paths:

```text
Humanize runtime: {{HUMANIZE_RUNTIME_ROOT}}
KernelPilot root: {{KERNELPILOT_ROOT}}
```

If `{{KERNELPILOT_ROOT}}` was not hydrated, locate a repository containing
`knowledge/index.json` and `references/kernel-source-catalog.md`.

## Contract

Run the Humanize steps inside this skill. Do not ask the user to run separate
`gen-plan`, `refine-plan`, or `humanize-rlcr` commands.

Given a one-sentence kernel request, you must:

1. Build the kernel-specific plan yourself.
2. Refine it yourself.
3. Create or enter a clean standalone optimization repo.
4. Start Humanize RLCR on the refined plan.
5. Execute the current round until the Stop hook takes over.

Ask the user only if the target kernel, target GPU, or baseline framework is
missing and cannot be inferred.

## Hard Rules

- Candidate implementation language is user-directed. If the user specifies
  CUDA C++/PTX, Triton, CuTe DSL, TileLang, CUTLASS/CuTe, ThunderKittens,
  torch.compile/Inductor, or another kernel stack, use that stack.
- If the user does not specify a language, start from the active baseline
  kernel's implementation system unless there is a measured reason to choose a
  different one.
- The baseline kernel can be the starting point. You may copy or adapt baseline
  code into the standalone repo when license and attribution allow.
  Record the exact source path/URL, commit, license/notice, and delta in the
  source ledger and lineage.
- If the user explicitly asks for a from-scratch kernel or says not to use the
  baseline implementation, do not copy, adapt, or pattern-match the baseline
  kernel code. Use that baseline only for correctness, benchmark, profiler, and
  API comparison.
- Keep the source framework checkout itself read-only for standalone work unless
  the user explicitly asks for an in-place framework patch. The standalone repo
  may contain the copied/adapted baseline candidate and subsequent mutations.
- Run optimization work in a fresh standalone git repo with its own PyTorch
  binding, correctness tests, benchmark harness, ledgers, lineage, and profile
  artifacts.
- Every correct candidate attempt gets an attempt-ledger row. Only correct
  candidates that improve performance get an optimization-ledger row.
- Collect one baseline Nsight Compute digest for a representative case after
  baseline correctness/benchmark succeeds. Skip it only when NCU cannot run, and
  record the reason.
- Use NCU again for regressions, plateaus, surprising wins, or profile-driven
  edits. Do not run full NCU for every tiny iteration unless the benchmark
  result is hard to explain.
- Do not declare the loop complete while relevant NCU/profile acceptance
  criteria are unmet.

## Required Files In The Standalone Repo

Create these before starting RLCR, then keep them updated during the loop:

```text
.gitignore
.humanize/kernel-agent/refined-plan.md
README.md
src/<task_name>/
tests/
benchmarks/
artifacts/attempt-ledger.md
artifacts/optimization-ledger.md
artifacts/source-idea-ledger.md
artifacts/lineage.jsonl
artifacts/profile-digests/README.md
```

The plan file may stay gitignored under `.humanize/` so RLCR can start without
tracking local loop state.

## Knowledge Pass

Before writing the plan or choosing any optimization direction:

1. Read `{{KERNELPILOT_ROOT}}/knowledge/README.md`.
2. Read `{{KERNELPILOT_ROOT}}/knowledge/routing/topics/index.md`.
3. Read `{{KERNELPILOT_ROOT}}/knowledge/references/index.md`.
4. Read relevant topic pages, usually one or more of:
   - `knowledge/routing/topics/matmul-gemm.md`
   - `knowledge/routing/topics/attention.md`
   - `knowledge/routing/topics/normalization.md`
   - `knowledge/routing/topics/activation-fusion.md`
   - `knowledge/routing/topics/quantization-fp8.md`
5. Read relevant framework pages, usually:
   - `knowledge/routing/frameworks/sglang.md`
   - plus `cutlass.md`, `deepgemm.md`, `vllm.md`, `flashinfer.md`,
     `flash-attention.md`, `triton.md`, `tilelang.md`, `cute-dsl.md`,
     `quack.md`, `tilekernels.md`, `thunderkittens.md`,
     `veitner-blog.md`, `colfax-research.md`, `cuda-blog-kernels.md`, or
     `pytorch.md` as appropriate.
6. Read the matching deep source guide under
   `knowledge/references/source-guides/`.
7. For PR-driven production repositories, read the matching PR guide under
   `knowledge/references/prs/` in the same knowledge pass. Treat PR diffs,
   changed kernel files, linked tests, benchmark files, review-linked issues,
   source guide paths, and direct source scans as the paired kernel-knowledge
   evidence layer. Do not query PRs for source-only repositories such as
   PyTorch, DeepSeek TileKernels, CUDA sample repos, blog/code companion repos,
   puzzle repos, source catalogs, and repositories with fewer than 10 selected
   CUDA optimization PRs; inspect their source guide and current code directly
   instead.
8. PR pages keep filtered CUDA optimization PRs rather than a small curated
   top-N. Each entry must have CUDA/NVIDIA target evidence, a real kernel/source
   change, and an optimization/performance mechanism. Search both the PR page,
   when applicable, and source guide for kernel family, dtype, architecture,
   backend, and bottleneck terms before choosing an edit.
9. If the bottleneck is known but the best source repository is unclear, read
   `knowledge/references/prs/by-topic/index.md` and the matching topic page.
10. Read `knowledge/references/prs/open-watchlist.md` only for volatile current
   ideas, and re-check linked GitHub PRs before using code or benchmark claims.
11. Read `{{KERNELPILOT_ROOT}}/references/kernel-source-catalog.md`.
12. For plateau research or blog-driven source ideas, read
   `knowledge/references/blogs/index.md` and the matching blog page before
   opening companion code.

Keep the first pass scoped: one topic page, one framework page, one source
guide, and one PR page when the repository is PR-driven. Do not scan the whole
knowledge tree up front.

Pair production PRs with current source code, tests, and benchmarks before blogs
or articles when the repository is PR-driven. For source-only repositories such
as PyTorch, blog/code companion repos, and repositories with fewer than 10
selected CUDA optimization PRs, skip PR lookup and use source guides plus direct
source scans. During plateau expansion, use merged repository PR pages plus
matching source guides for PR-driven repos, then cross-repository by-topic PR
pages plus relevant source guides, then the open PR watchlist plus current
source scan, then blog/code references. External kernels may be used as
baselines, starting candidates, or prior art when their license/attribution
allows it.

## Plan Requirements

Write `.humanize/kernel-agent/refined-plan.md` in the standalone repo. It must
use the Humanize gen-plan schema and include these acceptance criteria:

- Clean standalone repo exists and is committed before RLCR starts.
- Baseline framework checkout is protected from accidental edits unless the
  user asks for an in-place patch.
- Candidate implementation language is documented and follows the user request
  or the active baseline's kernel stack.
- If baseline code seeds the first candidate, provenance, license/notice,
  copied files, and the first optimization delta are recorded before further
  mutation.
- If the user requested a from-scratch kernel, the plan states that baseline
  kernel code is comparison-only and cannot seed candidates.
- Correctness tests cover representative shapes, dtypes, edge cases, and
  baseline parity.
- Benchmark harness records per-shape timing, geomean, best/worst cases, and
  environment metadata.
- A baseline Nsight Compute profile is captured for one representative
  bottleneck case after baseline benchmark succeeds and before the first
  profile-driven edit.
- Later Nsight Compute profiles are captured for regressions, plateaus,
  surprising wins, or reviewer-requested evidence, then converted into Profile
  Evidence Digests.
- Attempt ledger records every version, including failed correctness,
  regressions, plateaus, and abandoned ideas.
- Optimization ledger records only correct versions with measured improvement.
- Lineage records parent version, mutation/motivation, source idea keys, result,
  and selected/rejected status.
- Source idea ledger records both PR provenance, when available, and source-code
  provenance: repo, path, symbol/function, opened tests or benchmarks,
  hypothesis, result, and do-not-reread key.
- After two consecutive weak rounds with less than 1% geomean improvement over
  the prior best, perform research expansion before editing again: read at
  least 50 new code-first sources before prose sources, prioritize unread PR
  diffs, current source files, symbols, and changed kernel/test/benchmark
  files, log paired source provenance, and avoid re-reading by checking
  `artifacts/source-idea-ledger.md`.
- Stop only when all ACs are met, or when profile evidence shows the kernel is
  already beyond 85% of the relevant peak and no low-effort implementation edit
  remains.

## Profile Evidence

Invoke profile-evidence rules whenever any of these hold:

- Baseline benchmark has passed and no baseline Profile Evidence Digest exists.
- A correct candidate is within +/-2% of baseline across configured cases.
- A correct candidate regresses on one or more configured cases.
- Two consecutive iterations show less than 1% geomean improvement over the
  prior best.
- A candidate is much faster than expected and needs explanation.
- A reviewer asks for a Profile Evidence Digest.

Persist both `.ncu-rep` and CSV export paths in the digest. Each digest must end
with one concrete next edit.

## RLCR Startup

After writing and committing the standalone repo scaffolding, start the loop
from inside the standalone repo:

```bash
"{{HUMANIZE_RUNTIME_ROOT}}/scripts/setup-rlcr-loop.sh" .humanize/kernel-agent/refined-plan.md --yolo
```

If setup exits non-zero, stop and report the error. Do not bypass the gate.

After setup succeeds:

1. Read `.humanize/rlcr/<timestamp>/round-0-prompt.md`.
2. Execute the current round.
3. Commit changes.
4. Write the required round summary.
5. Stop normally so the native Humanize Stop hook can review.

If the hook blocks exit, follow the generated next-round prompt exactly.
