# DeepSeek TileKernels PR Knowledge Notes

Repository: <https://github.com/deepseek-ai/TileKernels>

This page is the production-PR layer for kernel-knowledge. It favors merged PRs that changed kernels, dispatch, JIT/runtime integration, tuning policy, tests, benchmarks, or profiling evidence. Release, CI-only, formatting, pure version-bump, and non-target-backend PRs are filtered out.

Note: this repository has little public PR history. Use the source guide and direct code scan as the main knowledge pass, and treat this page as provenance when PRs exist.

## Repository Source Scan

Read these source regions before opening individual PR diffs:

- `tile_kernels`
- `tests`
- `README.md`

## Coverage Summary

| Category | CUDA-kernel PRs |
| --- | ---: |
| Other Kernel Cases | 1 |

## Pull Request Case Notes

### Other Kernel Cases

Use this section for: Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea.
NCU first look: Choose metrics based on the changed kernel family after opening the diff.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#1](https://github.com/deepseek-ai/TileKernels/pull/1) Revise Engram Kernel Comments | 2026-04-23 | kernel_other | Revise Engram Kernel Comments | kernel: `tile_kernels/engram/engram_gate_kernel.py` | Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea. |

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
