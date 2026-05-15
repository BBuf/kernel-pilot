# CCCL / CUB Kernel Reference

Repository: <https://github.com/NVIDIA/cccl>

PR case notes: `../prs/cccl-cub.md`

Use CCCL/CUB when the target kernel needs production-grade CUDA primitives:
block/warp reductions, scans, radix sort, segmented operations, cooperative
groups, or benchmark methodology for memory-movement kernels.

## Read Order

1. The CUB device or block primitive matching the target operation.
2. The agent and dispatch policy headers used by that primitive.
3. Benchmarks under `cub/benchmarks/bench/`.
4. Tests that cover partial tiles, custom operators, non-power-of-two sizes,
   and architecture-specific dispatch.
5. Recent PRs that changed tuning policy, dispatch layering, or benchmark
   methodology.

## Code Map

| Area | Paths to inspect |
| --- | --- |
| Device primitives | `cub/cub/device/` |
| Block and warp primitives | `cub/cub/block/`, `cub/cub/warp/` |
| Dispatch and agents | `cub/cub/device/dispatch/`, `cub/cub/agent/` |
| Benchmarks | `cub/benchmarks/bench/` |
| Tests | `cub/test/`, `c2h/` |
| libcu++ helpers | `libcudacxx/include/cuda/` |
| cudax experimental copy/compute | `cudax/include/cuda/experimental/` |

## Search Patterns

```bash
rg -n "sm_90|sm_100|policy|tuning|scan|reduce|sort|radix|segmented|mdspan|shared" cub cudax libcudacxx
rg -n "bench|nvbench|CUDAX_REQUIRE|CCCLRT_REQUIRE|catch2" cub/benchmarks cub/test c2h
```

## PR-Driven Lessons

- Dispatch refactors are performance-sensitive even when intended to be
  behavior-preserving; read benchmark notes and SASS/perf claims in the PR.
- Segmented scan/reduce changes usually carry edge-case knowledge for partial
  tiles, arbitrary operators, and policy selection.
- `cudax` copy and mdspan PRs are useful for transpose and tensor movement
  candidates even when the final candidate is not written with CCCL.

## NCU Focus

| Primitive family | First metrics |
| --- | --- |
| Scan / reduction | occupancy, shared-bank conflicts, issue stalls, L2/DRAM bytes |
| Sort / radix | global memory transactions, long scoreboard, active cycles |
| Tensor copy / transpose | coalescing, shared-memory replay, DRAM throughput |

