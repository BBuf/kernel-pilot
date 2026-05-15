# PyTorch PR Knowledge Notes

Repository: <https://github.com/pytorch/pytorch>

This page is the production-PR layer for kernel-knowledge. It keeps merged PRs with CUDA/NVIDIA target evidence, real kernel/source changes, and an optimization/performance mechanism such as tuning, fusion, tensor-core paths, memory movement, scheduling, profiling, or benchmark-backed speed work. Release, CI-only, formatting, dependency-only, correctness-only, and non-target-backend PRs are filtered out.

## Repository Source Scan

Read these source regions before opening individual PR diffs:

- `aten/src/ATen/native/cuda`
- `aten/src/ATen/native/transformers/cuda`
- `aten/src/ATen/native/cudnn`
- `torch/_inductor`
- `torch/csrc/distributed`

## Coverage Summary

| Category | CUDA optimization PRs |
| --- | ---: |
| Scheduler / Autotune | 1 |

## Pull Request Case Notes

### Scheduler / Autotune

Use this section for: Treat scheduler/autotune configs as shape-specific evidence; replay benchmark shapes before generalizing.
NCU first look: SM occupancy, waves/SM, active cycles, tail effects, and load imbalance.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#161816](https://github.com/pytorch/pytorch/pull/161816) [Reland][Inductor] Prune configs that require more shared memory than the hardware limit | 2025-08-30 | scheduler_autotune, compiler_runtime | Stack from ghstack (oldest at bottom): * __->__ 161816 Summary: This is a re-land of PR161040, which had previously caused test failures on AMD GPUs. The tests are now configured to target only NVIDIA GPUs. This diff removes configurations that exceed the hardware shared memory limit, which causes t... | kernel: `torch/_inductor/template_heuristics/triton.py`<br>test: `test/inductor/test_max_autotune.py`, `test/inductor/test_triton_heuristics.py`<br>wrapper: `torch/_inductor/config.py`, `torch/_inductor/select_algorithm.py` | Treat scheduler/autotune configs as shape-specific evidence; replay benchmark shapes before generalizing. |

## Per-PR Ledger Fields

When using an idea from this page, add one row to `artifacts/source-idea-ledger.md` with:

| Field | Value to record |
| --- | --- |
| Source key | `<repo>#<pr-number>` |
| Code evidence | Kernel, wrapper, benchmark, and test paths opened from the PR diff |
| Hypothesis | The concrete optimization idea derived from the PR |
| First experiment | Candidate version and benchmark shape set |
| Result | Correctness, geomean, best/worst cases, and NCU digest path |
| Do-not-reread key | Same as source key unless a single PR yields multiple independent ideas |

## How To Use This Page

- During the initial knowledge pass, read the category matching the target kernel and copy PR URL, changed paths, and hypothesis into the source idea ledger.
- During plateau expansion, choose PRs not already present in ledger do-not-reread keys; inspect the diff, linked issue, changed tests, and benchmark files before using the idea.
- Treat PR code as baseline/prior art unless the task and license allow copying or adapting it. When copied, record exact PR, commit, files, notice, and first delta.
