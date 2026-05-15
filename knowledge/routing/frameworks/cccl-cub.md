# CCCL (CUB / Thrust / libcu++)

Repository: <https://github.com/NVIDIA/cccl>

CCCL is the canonical reference for **device-wide and block-level primitives**:
reductions, scans, sorts, segmented reductions, warp shuffles, cooperative
groups.

## Where the kernels live

| Directory | What you find there |
| --- | --- |
| `cub/` | Device, block, and warp primitives (`BlockReduce`, `WarpScan`, `DeviceRadixSort`, etc.). |
| `thrust/` | High-level algorithms built on CUB. |
| `libcudacxx/` | C++ standard library types (`atomic`, `barrier`, `pipeline`). |

## Optimization patterns documented here

- **BlockReduce / BlockScan**: the reference for any fused-norm or fused-MoE
  reduction. Use the actual CUB template when permitted; otherwise mirror the
  algorithm.
- **Cooperative-thread radix sort**: reference for top-k / sort kernels.
- **`cuda::pipeline` + `cp.async`**: the reference for software-pipelined
  shared-memory loads with split barriers.
- **`cuda::atomic_ref`**: the modern way to write lock-free reductions and
  histograms.

## Common pitfalls

- CUB's `BlockReduce<int>` and `BlockReduce<float>` choose different
  algorithms internally; do not assume `T` is invariant.
- `cuda::pipeline` requires SM80+; older fallbacks must be guarded.
- `DeviceRadixSort` is faster than handwritten sorts only above a size
  threshold; below it, a warp-level sort is usually better.

## When to read this framework

- You need a block / warp reduction, scan, sort, or histogram.
- You need a `cp.async` + pipeline reference for software pipelining.
- You are designing a fused-norm or fused-MoE kernel that needs a
  numerically-stable reduction.

## Reuse / Copy Rules

- CCCL templates can be linked directly when license / attribution is
  handled. Lineage notes must still record which CUB primitive is used.

## Recommended ncu metrics

- Reductions: `smsp__warps_eligible.avg.per_cycle_active`,
  `l1tex__data_bank_conflicts_pipe_lsu.sum`.
- Sorts: `dram__throughput`, `lts__t_bytes`,
  `smsp__inst_executed_op_global_atom.sum`.
