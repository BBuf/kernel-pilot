---
name: humanize-kernel-agent-loop
description: "Run an end-to-end Humanize Kernel Agent Loop for GPU kernel optimization: plan, refine, create a clean standalone repo, use kernel-knowledge, benchmark, profile with Nsight Compute, maintain lineage/ledgers, and drive RLCR autonomously."
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

The loop is autonomous. Do not ask the user to run separate `gen-plan`,
`refine-plan`, or `humanize-rlcr` steps.

Given a one-sentence kernel request, you must:

1. Build the kernel-specific plan yourself.
2. Refine it yourself.
3. Create or enter a clean standalone optimization repo.
4. Start Humanize RLCR on the refined plan.
5. Execute the current round until the Stop hook takes over.

Ask the user only if the target kernel, target GPU, or baseline framework is
missing and cannot be inferred.

## Hard Rules

- Candidate implementations must be naive, hand-written CUDA C++ in `.cu` or
  `.cuh`.
- Do not use Triton, CuTe DSL, CUTLASS, ThunderKittens, torch.compile, library
  dispatch, generated kernels, or framework DSLs as candidate implementations.
  They are allowed only as baselines, behavior references, or prior art.
- Keep the source framework repository read-only unless the user explicitly asks
  for an in-place patch.
- Run optimization work in a fresh standalone git repo with its own PyTorch
  binding, correctness tests, benchmark harness, ledgers, lineage, and profile
  artifacts.
- Every correct candidate attempt gets an attempt-ledger row. Only correct
  candidates that improve performance get an optimization-ledger row.
- Nsight Compute evidence is a first-class feedback source. Do not declare the
  loop complete while relevant NCU/profile acceptance criteria are unmet.

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
2. Read `{{KERNELPILOT_ROOT}}/knowledge/topics/index.md`.
3. Read `{{KERNELPILOT_ROOT}}/knowledge/references/index.md`.
4. Read relevant topic pages, usually one or more of:
   - `knowledge/topics/matmul-gemm.md`
   - `knowledge/topics/attention.md`
   - `knowledge/topics/normalization.md`
   - `knowledge/topics/activation-fusion.md`
   - `knowledge/topics/quantization-fp8.md`
5. Read relevant framework pages, usually:
   - `knowledge/frameworks/sglang.md`
   - plus `cutlass.md`, `deepgemm.md`, `vllm.md`, `flashinfer.md`,
     `flash-attention.md`, `triton.md`, or `pytorch.md` as appropriate.
6. Read the matching deep framework reference under
   `knowledge/references/frameworks/`.
7. Read `{{KERNELPILOT_ROOT}}/references/kernel-source-catalog.md`.

Prefer source code, tests, benchmarks, and open PRs/issues before blogs or
articles. External kernels are prior art only.

## Plan Requirements

Write `.humanize/kernel-agent/refined-plan.md` in the standalone repo. It must
use the Humanize gen-plan schema and include these acceptance criteria:

- Clean standalone repo exists and is committed before RLCR starts.
- Baseline framework is read-only and measured as baseline/prior art.
- Candidate kernels obey the naive hand-written CUDA C++ rule.
- Correctness tests cover representative shapes, dtypes, edge cases, and
  baseline parity.
- Benchmark harness records per-shape timing, geomean, best/worst cases, and
  environment metadata.
- Nsight Compute profiles are captured for representative bottleneck cases and
  converted into Profile Evidence Digests before profile-driven edits.
- Attempt ledger records every version, including failed correctness,
  regressions, plateaus, and abandoned ideas.
- Optimization ledger records only correct versions with measured improvement.
- Lineage records parent version, mutation/motivation, source idea keys, result,
  and selected/rejected status.
- After two consecutive weak rounds with less than 1% geomean improvement over
  the prior best, perform research expansion before editing again: read at
  least 50 new code-first sources before prose sources, log source provenance,
  and avoid re-reading by checking `artifacts/source-idea-ledger.md`.
- Stop only when all ACs are met, or when NCU evidence shows the kernel is
  already beyond 85% of the relevant peak and no low-effort CUDA edit remains.

## Profile Evidence

Invoke profile-evidence rules whenever any of these hold:

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
