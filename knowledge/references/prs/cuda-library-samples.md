# CUDA Library Samples PR Knowledge Notes

Repository: <https://github.com/NVIDIA/CUDALibrarySamples>

This page is the production-PR layer for kernel-knowledge. It favors merged PRs that changed kernels, dispatch, JIT/runtime integration, tuning policy, tests, benchmarks, or profiling evidence. Release, CI-only, formatting, pure version-bump, and non-target-backend PRs are filtered out.

## Repository Source Scan

## Coverage Summary

| Category | CUDA-kernel PRs |
| --- | ---: |
| Compiler / Runtime | 1 |
| Other Kernel Cases | 1 |

## Pull Request Case Notes

### Compiler / Runtime

Use this section for: Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests.
NCU first look: Generated kernel shape, launch overhead, occupancy, register pressure, and compile-time-selected schedule.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#49](https://github.com/NVIDIA/CUDALibrarySamples/pull/49) [cuTENSOR] Fix a license resolve error. | 2021-12-07 | compiler_runtime | Problem description When installing cuTENSOR with python extension (the Step 3 in Installation section) , the `pip install .` command returned error and cannot successfully install the package. Environment NGC containers: nvcr.io/nvidia/pytorch:21.10-py3 it contains setuptools 58.2.0. Manually upgra... | kernel: `cuTENSOR/python/cutensor/package_info.py` | Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests. |

### Other Kernel Cases

Use this section for: Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea.
NCU first look: Choose metrics based on the changed kernel family after opening the diff.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#2](https://github.com/NVIDIA/CUDALibrarySamples/pull/2) Update spmm_csr_example.c | 2020-08-17 | kernel_other | There is a small mistake on the file. The function to check cudaMalloc should be CHECK_CUDA, not CHECK_SPARSE | other: `cuSPARSE/spmm_csr/spmm_csr_example.c` | Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea. |

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
