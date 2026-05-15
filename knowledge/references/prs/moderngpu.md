# ModernGPU PR Knowledge Notes

Repository: <https://github.com/moderngpu/moderngpu>

This page is the production-PR layer for kernel-knowledge. It favors merged PRs that changed kernels, dispatch, JIT/runtime integration, tuning policy, tests, benchmarks, or profiling evidence. Release, CI-only, formatting, pure version-bump, and non-target-backend PRs are filtered out.

## Repository Source Scan

## Coverage Summary

| Category | CUDA-kernel PRs |
| --- | ---: |
| Memory / Primitives | 5 |
| Other Kernel Cases | 2 |

## Pull Request Case Notes

### Memory / Primitives

Use this section for: Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract.
NCU first look: DRAM throughput, L2 hit rate, memory sectors, shared-memory conflicts, and synchronization overhead.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#36](https://github.com/moderngpu/moderngpu/pull/36) Fix potential deadlock after switching to shfl.sync. | 2020-01-27 | memory_primitives, benchmark_test | 1 Use __activemask() to avoid potential deadlock. 2 Remove sm_20 related settings in Makefile. Micro-benchmark on V100 and P40 show no performance regression after this. I did not do a thorough regression test though. @seanbaxter Would you please take a look? Thanks! | other: `Makefile`, `src/moderngpu/cta_segscan.hxx`, `src/moderngpu/intrinsics.hxx` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |
| [#35](https://github.com/moderngpu/moderngpu/pull/35) Add support for .shfl.sync and __ballot_sync() primitives... | 2019-12-24 | memory_primitives | ...Also fix a bug that returns boolean for a unique_ptr type object. The purpose is to make moderngpu 2.0 usable with CUDA 9+. | other: `demo/graph.cxx`, `src/moderngpu/cta_scan.hxx`, `src/moderngpu/cta_segscan.hxx`, `src/moderngpu/intrinsics.hxx` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |
| [#33](https://github.com/moderngpu/moderngpu/pull/33) Applying ballot_sync() fix for CUDA 9+ support. | 2019-05-28 | memory_primitives | Missed the ballot (vote) support, oops. Same thing as 32 @seanbaxter | other: `include/device/ctascan.cuh`, `include/device/ctasegscan.cuh`, `include/device/intrinsics.cuh` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |
| [#42](https://github.com/moderngpu/moderngpu/pull/42) Fix lockup in ctasegscan.cuh | 2021-11-22 | memory_primitives | Fix lockup in ctasegscan.cuh | other: `include/device/ctasegscan.cuh` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |
| [#58](https://github.com/moderngpu/moderngpu/pull/58) Fix operator argument ordering in cta_segscan.hxx | 2026-01-17 | memory_primitives | The scan operator arguments in `cta_segscan_t::segscan()` were reversed, causing incorrect results for non-commutative operators. Changes - **Line 84**: Swapped operator arguments from `op(x, storage.values[first + tid - offset])` to `op(storage.values[first + tid - offset], x)` This aligns with the... | other: `src/moderngpu/cta_segscan.hxx` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |

### Other Kernel Cases

Use this section for: Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea.
NCU first look: Choose metrics based on the changed kernel family after opening the diff.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#32](https://github.com/moderngpu/moderngpu/pull/32) Adding support for shfl primitives after CUDA 9. | 2019-04-29 | kernel_other | Support 31 fix as well. These commits will help run morderngpu `v1.1` beyond CUDA 9. | other: `include/device/intrinsics.cuh` | Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea. |
| [#57](https://github.com/moderngpu/moderngpu/pull/57) Fix CUDA 13.0 compatibility: use cudaDeviceGetAttribute for clock rates | 2026-01-17 | kernel_other | CUDA 13.0 removes `memoryClockRate` and `clockRate` fields from `cudaDeviceProp`. The `device_prop_string()` function accessed these fields directly, causing compilation failures. Changes - Replace `prop.memoryClockRate` and `prop.clockRate` with `cudaDeviceGetAttribute()` API calls using `cudaDevAt... | other: `.gitignore`, `src/moderngpu/context.hxx` | Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea. |

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
