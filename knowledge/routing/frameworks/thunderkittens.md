# ThunderKittens

Repository: <https://github.com/HazyResearch/ThunderKittens>

Deep reference: `knowledge/references/source-guides/thunderkittens.md`

ThunderKittens is HazyResearch's tile-primitive library for SM80 / SM90.
It exposes `kittens::tile`, `kittens::vec`, and warpgroup-aware operators that
target attention, matmul, and state-space-model kernels.

## Where the kernels live

| Path | What you find there |
| --- | --- |
| `include/kittens.cuh` | Main entry header. |
| `examples/` | Attention, matmul, gating, and SSM kernels. |

## Optimization patterns documented here

- **Tile primitives**: `rt`, `st` register/shared tile types with built-in
  load/store helpers and matmul.
- **Warpgroup-aware GEMM**: cleaner Hopper warpgroup matmul than raw inline
  PTX, useful as a study target for warpgroup specialization.
- **Attention forward / backward**: reference for an alternative tile vocabulary
  vs FlashAttention.

## When to read this framework

- You want a second design opinion (besides FA / FlashInfer / CUTLASS) for
  Hopper attention.
- You want a tile-primitive vocabulary to reason about shared-memory layout.

## Reuse / Copy Rules

- ThunderKittens code may seed a candidate only when the user or baseline calls
  for that implementation family and license / attribution are handled.
- Record source path or URL, commit, copied files, and delta in the source
  ledger before mutating copied or adapted code.
