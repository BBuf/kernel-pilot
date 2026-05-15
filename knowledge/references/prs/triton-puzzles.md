# Triton Puzzles PR Knowledge Notes

Repository: <https://github.com/gpu-mode/Triton-Puzzles>

This page is the production-PR layer for kernel-knowledge. It favors merged PRs that changed kernels, dispatch, JIT/runtime integration, tuning policy, tests, benchmarks, or profiling evidence. Release, CI-only, formatting, pure version-bump, and non-target-backend PRs are filtered out.

## Repository Source Scan

## Coverage Summary

| Category | CUDA-kernel PRs |
| --- | ---: |
| Attention / KV / Decode | 1 |
| Compiler / Runtime | 6 |

## Pull Request Case Notes

### Attention / KV / Decode

Use this section for: Preserve page/KV/layout and plan-run contracts; profile memory traffic separately from math utilization.
NCU first look: Long scoreboard, L2/DRAM traffic, global-load sectors, tensor pipe %, and shared-memory bank conflicts.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#37](https://github.com/gpu-mode/Triton-Puzzles/pull/37) Fix the Puzzle 9 flash attention test block size | 2026-04-01 | attention_kv, benchmark_test, compiler_runtime | Fixes 27. The notebook currently tests puzzle 9 with `B0=200`, but the puzzle pattern typically relies on `tl.arange(0, B0)`, which expects a power-of-two block size. This changes the example test to use `B0=64` while keeping `N0=T=200`. | other: `Triton-Puzzles.ipynb` | Preserve page/KV/layout and plan-run contracts; profile memory traffic separately from math utilization. |

### Compiler / Runtime

Use this section for: Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests.
NCU first look: Generated kernel shape, launch overhead, occupancy, register pressure, and compile-time-selected schedule.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#19](https://github.com/gpu-mode/Triton-Puzzles/pull/19) Fix Triton-viz breaking changes by using v1.1 version. | 2024-09-09 | compiler_runtime | Solves issue 18. | other: `Triton-Puzzles.ipynb` | Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests. |
| [#2](https://github.com/gpu-mode/Triton-Puzzles/pull/2) Fix link to triton-viz | 2024-03-19 | compiler_runtime | Fix link to triton-viz | docs: `README.md` | Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests. |
| [#6](https://github.com/gpu-mode/Triton-Puzzles/pull/6) Correct the shape description in Triton-Puzzles.ipynb | 2024-04-03 | compiler_runtime | Correct the shape description in Triton-Puzzles.ipynb | other: `Triton-Puzzles.ipynb` | Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests. |
| [#25](https://github.com/gpu-mode/Triton-Puzzles/pull/25) Update triton to 3.1.0 and triton-viz to 1.1.1 | 2024-11-18 | compiler_runtime | Update triton to 3.1.0 and triton-viz to 1.1.1 | other: `Triton-Puzzles.ipynb` | Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests. |
| [#34](https://github.com/gpu-mode/Triton-Puzzles/pull/34) Use == instead of - to set triton version in pip and upgrade to 3.2.0 | 2026-03-16 | compiler_runtime | Should fix the issue seen in 32 where the Colab notebook doesn't install the older version of `triton` (`3.1.0`) and instead uses the version that comes pre-installed on Colab (`3.4.0` at the time of me writing this), causing the error. It seems the `triton` install command was broken (at least on C... | other: `Triton-Puzzles.ipynb` | Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests. |
| [#35](https://github.com/gpu-mode/Triton-Puzzles/pull/35) New triton viz | 2026-03-18 | compiler_runtime | - update the README.md picture to show the current version of the triton-viz UI - fix notebook to use the new version of triton-viz @Jokeren | docs: `README.md`<br>other: `Triton-Puzzles.ipynb` | Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests. |

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
