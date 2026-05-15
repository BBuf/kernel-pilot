# QuACK

Repository: <https://github.com/Dao-AILab/quack>

Deep reference: `knowledge/references/source-guides/quack.md`

QuACK is Dao-AILab's "Quirky Assortment of CuTe Kernels": a modern CuTe DSL
kernel collection with memory-bound kernels, Hopper / Blackwell GEMM, epilogues,
and benchmarks.

## Where the kernels live

| Directory | What you find there |
| --- | --- |
| `quack/` | CuTe DSL kernels and Python package surface. |
| `benchmarks/` | Kernel timing harnesses. |
| `microbenchmarks/` | Focused kernel experiments. |
| `examples/` | Runnable usage examples. |
| `tests/` | Correctness and regression coverage. |
| `docs/` | Kernel notes and memory-bound CuTe DSL discussion. |

## When to read this framework

- The user asks for CuTe DSL or Tri Dao / QuACK style kernels.
- You need a Python-first CuTe DSL baseline for norm, softmax, cross entropy,
  GEMM, or fused epilogue work.
- You want a reference for H100/B200/B300 CuTe DSL packaging and benchmarks.

## Reuse / Copy Rules

- QuACK is a valid candidate starting point when the user chooses CuTe DSL or
  QuACK-style work and license / attribution are handled.
- Record exact source path, commit, license/notice, copied files, and delta.
