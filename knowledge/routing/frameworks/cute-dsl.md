# CuTe DSL

Repository: <https://github.com/NVIDIA/cutlass>

Deep reference: `knowledge/references/source-guides/cute-dsl.md`

CuTe DSL is the Python-facing DSL in CUTLASS for writing layout-rich GPU
kernels. It is especially relevant for Hopper / Blackwell GEMM, attention,
normalization, and memory-bound kernels that benefit from CuTe layout algebra
without writing full C++ template stacks.

## Where the kernels live

| Directory | What you find there |
| --- | --- |
| `python/` | CuTe DSL frontend, examples, and package code. |
| `include/cute/` | C++ CuTe layout and tensor algebra backing the DSL concepts. |
| `examples/` | Hopper / Blackwell examples using CuTe concepts. |
| `test/unit/` | Layout, copy, MMA, and epilogue coverage. |

## When to read this framework

- The user asks for a CuTe DSL candidate.
- The baseline is a CuTe DSL or QuACK kernel.
- You need layout algebra, tiled copy, TMA/WGMMA, or epilogue vocabulary before
  choosing an optimization direction.

## Reuse / Copy Rules

- CuTe DSL code can seed standalone candidates when license / attribution is
  handled.
- Record exact source path, commit, copied files, selected tile/layout config,
  and delta in the source ledger and lineage.
