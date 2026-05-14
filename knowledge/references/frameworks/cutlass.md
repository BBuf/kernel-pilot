# CUTLASS / CuTe Kernel Reference

Repository: <https://github.com/NVIDIA/cutlass>

Use CUTLASS and CuTe as prior art for GEMM, tensor-core tiling, TMA/WGMMA,
epilogue fusion, and profiler-driven shape exploration. Candidate kernels still
must be naive hand-written CUDA C++ unless the user explicitly changes that
rule.

## Required Companion References

Read these before using CUTLASS as prior art:

- `../ako4all/cutlass-cpp-kernel-reference.md`
- `../ako4all/cutlass-cpp/cutlass-cpp-overview.md`
- `../ako4all/nvidia-architecture-reference.md`
- `../ako4all/architectures/sm90-optimization-guide.md` for H100
- `../ako4all/profiling-debugging-reference.md`

## Code Map

| Area | Paths to inspect |
| --- | --- |
| CUTLASS templates | `include/cutlass/` |
| CuTe C++ | `include/cute/` |
| Hopper examples | `examples/48_hopper_*` |
| Blackwell examples | `examples/50_blackwell_*`, `examples/60_*` |
| Profiler | `tools/profiler/` |
| Docs | `media/docs/` |
| Tests | `test/unit/` |
| CuTe DSL | `python/` |

## Search Patterns

```bash
rg -n "CollectiveBuilder|Mainloop|Epilogue|TileShape|ClusterShape|KernelSchedule|EpilogueSchedule|Tma|Wgmma|StreamK" include examples test tools
rg -n "block_scaled|fp8|fp4|int8|scale|visitor|EVT|epilogue" include examples test
rg -n "sm90|hopper|warp_specialized|persistent|stream_k|grouped" include examples test
```

## Baseline Extraction

- Use `tools/profiler/` to understand which tile/schedule family wins before
  designing a standalone CUDA candidate.
- Record tile shape, cluster shape, stage count, schedule, epilogue schedule,
  math instruction, scale layout, and alignment guard.
- Check unit tests for the shape and dtype combinations that catch partial-tile
  bugs.

## Candidate Translation

Translate:

- tile-size intuition into a simpler CUDA tiling experiment
- epilogue fusion opportunity into a naive CUDA epilogue
- scale layout and shape coverage into tests
- profiler result into candidate hypotheses

Do not copy CUTLASS collectives, CuTe layout code, or generated kernels into the
candidate.

## NCU Focus

| Kernel family | First metrics |
| --- | --- |
| Hopper GEMM | tensor pipe %, active cycles, occupancy, register pressure, L2/DRAM traffic |
| Stream-K / split-K | workload imbalance, active cycles, long scoreboard, inter-block overhead |
| Fused epilogue | tensor pipe %, ALU pipe %, store traffic, register pressure |
| Block-scaled GEMM | scale-load traffic, epilogue ALU, tensor pipe %, L2 bytes |

## Useful Cross-Framework Priors

- TensorRT-LLM for NVIDIA-serving shape routing.
- SGLang and vLLM for concrete serving hot shapes.
- PyTorch for correctness and tolerance.

