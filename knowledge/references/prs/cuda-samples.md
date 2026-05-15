# CUDA Samples PR Knowledge Notes

Repository: <https://github.com/NVIDIA/cuda-samples>

This page is the production-PR layer for kernel-knowledge. It keeps merged PRs with CUDA/NVIDIA target evidence, real kernel/source changes, and an optimization/performance mechanism such as tuning, fusion, tensor-core paths, memory movement, scheduling, profiling, or benchmark-backed speed work. Release, CI-only, formatting, dependency-only, correctness-only, and non-target-backend PRs are filtered out.

## Repository Source Scan

## Coverage Summary

| Category | CUDA optimization PRs |
| --- | ---: |
| Memory / Primitives | 1 |

## Pull Request Case Notes

### Memory / Primitives

Use this section for: Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract.
NCU first look: DRAM throughput, L2 hit rate, memory sectors, shared-memory conflicts, and synchronization overhead.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#363](https://github.com/NVIDIA/cuda-samples/pull/363) fix bug in 6_Performance/transpose: copy sharedmem kernel | 2025-05-05 | memory_primitives, benchmark_test | I believe there is a bug in the copy sharedmem kernel that was hidden by the fact that in the host calling loop, the device output data was not reset before each loop iteration | kernel: `Samples/6_Performance/transpose/transpose.cu` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |

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
