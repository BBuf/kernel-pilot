# Colfax Article Source PR Knowledge Notes

Repository: <https://github.com/ColfaxResearch/cfx-article-src>

This page is the production-PR layer for kernel-knowledge. It keeps merged PRs with CUDA/NVIDIA target evidence, real kernel/source changes, and an optimization/performance mechanism such as tuning, fusion, tensor-core paths, memory movement, scheduling, profiling, or benchmark-backed speed work. Release, CI-only, formatting, dependency-only, correctness-only, and non-target-backend PRs are filtered out.

## Repository Source Scan

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
| [#9](https://github.com/ColfaxResearch/cfx-article-src/pull/9) Add code for Stream-K post | 2024-12-20 | scheduler_autotune, arch_pipeline, benchmark_test, gemm_quant, norm_elementwise | Add code for Stream-K post | kernel: `streamk/epilogue_sm90_tma_ws.hpp`, `streamk/hopper_gemm_kernel.h`, `streamk/hopper_gemm_kernel_launch.h`, `streamk/kernel_traits.h`<br>benchmark: `streamk/cutlass_streamk/benchmark.cu`, `streamk/cutlass_streamk/profile.sh`<br>wrapper: `streamk/cli_options.h`, `streamk/convert_util.h`<br>docs: `streamk/README.md`<br>other: `streamk/Makefile`, `streamk/cutlass_streamk/Makefile`, `streamk/streamk.cu` | Treat scheduler/autotune configs as shape-specific evidence; replay benchmark shapes before generalizing. |

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
