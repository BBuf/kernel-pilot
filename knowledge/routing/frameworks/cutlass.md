# CUTLASS / CuTe

Repository: <https://github.com/NVIDIA/cutlass>

Deep reference: `knowledge/references/source-guides/cutlass.md`

CUTLASS is NVIDIA's primary template library for GEMM, GEMV, convolution, and
fused-epilogue kernels. CuTe (`include/cute/`) is the tensor-algebra layer
used internally; the CuTe DSL exposes the same semantics in Python.

## Where the kernels live

| Directory | What you find there |
| --- | --- |
| `include/cutlass/` | Kernel templates (`gemm/kernel`, `gemm/collective`, `gemm/threadblock`, `gemm/warp`, `epilogue`). |
| `include/cute/` | CuTe tensor algebra: `Layout`, `Tensor`, `Shape`, `Stride`, partitioning, swizzles. |
| `examples/` | Architecture-specific examples (`48_hopper_*`, `50_blackwell_*`, `60_*`). |
| `python/` | CuTe DSL bindings. |
| `tools/profiler/` | CUTLASS profiler harness; reference for benchmarking design. |
| `media/docs/` | Official CUTLASS docs (collectives, epilogues, profiler, block-scaled). |
| `test/unit/` | Unit tests, the canonical reference for tile-shape coverage. |

## Optimization patterns documented here

- **Hopper warp-specialized collective**: producer (TMA) + consumer (WGMMA) +
  epilogue warpgroups with smem barriers; the reference architecture for any
  Hopper GEMM.
- **Block-scaled GEMM (FP8 / FP4)**: explicit scale tensors next to the data,
  fused into the epilogue.
- **Stream-K**: split-K variant for low-batch or skinny-K GEMMs; reference for
  small-batch decode GEMM.
- **Epilogue fusion (EVT)**: visitor-based fusion of bias / activation /
  scaling / dequant; canonical reference for fused-epilogue work.
- **CuTe layout algebra**: `composition`, `complement`, `tiled_divide`,
  `make_tiled_copy`; the vocabulary used by every modern CUTLASS kernel.

## Common pitfalls

- CUTLASS configuration is *huge*; small changes to `TileShape`, `ClusterShape`,
  or `Schedule` can change which collective is selected and which SASS is
  emitted. Always pin all three.
- The `cutlass-2.x` vocabulary (`epilogue::thread::*`) differs from the
  `cutlass-3.x` Hopper / Blackwell vocabulary (`epilogue::collective::*`).
  Mixing them is a common confusion source.
- `tools/profiler/` lets you sweep configs without writing code; use it before
  proposing a new tile shape.

## When to read this framework

- You are designing any GEMM / GEMV / matmul kernel, fused-epilogue kernel,
  or block-scaled FP8/FP4 kernel.
- You need a Hopper warpgroup-specialized reference.
- You need CuTe vocabulary to describe a tile layout in lineage notes.

## Reuse / Copy Rules

- CUTLASS templates are usable as candidate code or library calls when license /
  attribution is handled.
- A tuned third-party kernel that builds on top of CUTLASS may be used as a
  starting point only when its license permits it and the exact source, commit,
  copied files, and delta are recorded.

## Recommended ncu metrics for CUTLASS kernels

- Hopper GEMM: `sm__inst_executed_pipe_tensor.avg.pct_of_peak_sustained_elapsed`,
  `lts__t_bytes`, `dram__throughput`, `sm__cycles_active`.
- Stream-K: same as above plus `smsp__cycles_active`,
  `smsp__warp_issue_stalled_*` to see workload imbalance.
- Block-scaled FP8: `sm__inst_executed_pipe_tensor`,
  `lts__t_sectors_pipe_lsu_mem_global_op_ld.sum.per_second`.
