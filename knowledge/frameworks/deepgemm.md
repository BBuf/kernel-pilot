# DeepGEMM

Repository: <https://github.com/deepseek-ai/DeepGEMM>

DeepGEMM is DeepSeek's high-performance FP8 / block-scaled GEMM library, the
de-facto reference for **FP8 grouped GEMM** in MoE workloads and for
block-scaled GEMM on Hopper and Blackwell.

## Where the kernels live

| Directory | What you find there |
| --- | --- |
| `csrc/apis/` | Public C API surface (`gemm_fp8_fp8_*`, `m_grouped_gemm_fp8_*`). |
| `csrc/jit/` | JIT compilation pipeline (NVRTC-based). |
| `csrc/jit_kernels/heuristics/` | Tile / cluster / schedule heuristics. |
| `csrc/jit_kernels/impls/` | Actual kernel templates (Hopper, Blackwell). |
| `deep_gemm/include/deep_gemm/` | Header-only kernel templates. |
| `deep_gemm/testing/` | Correctness oracles and reference implementations. |
| `tests/` | Numerical and performance tests. |

## Optimization patterns documented here

- **FP8 block-scaled GEMM**: 128x128 weight scale, 1x128 activation scale on
  Hopper; reference layout for any FP8 MoE GEMM.
- **Grouped GEMM for MoE**: `m_grouped_gemm_*` operates on a concatenated M
  dimension with a `group_offsets` array; mirror this layout when permuting
  tokens.
- **Heuristic dispatch**: tile / cluster / schedule are chosen at JIT time
  from a small heuristic table; cleaner than a giant `template<>` switch.
- **JIT compilation**: NVRTC plus per-shape caching; reference for any
  JIT-friendly kernel.

## Common pitfalls

- The "block-scaled" layout requires a specific scale tensor stride; mis-
  alignment silently degrades numerics rather than throwing.
- FP8 fast paths assume sufficient M / N alignment; small-batch decode can
  silently fall back to a slower path.
- Hopper and Blackwell kernels live side by side; the JIT picks one per arch.
  Always confirm SM-arch dispatch before benchmarking.

## When to read this framework

- You are designing FP8 / FP4 GEMM (especially grouped GEMM for MoE).
- You need a reference for block-scaled scale tensor layouts.
- You are designing a JIT-compiled kernel and want a small heuristic table
  pattern.

## When NOT to copy

- Kernel bodies are out-of-bounds for direct copy. Use as a reference for
  scale layouts, tile shapes, and heuristic structure.

## Recommended ncu metrics for DeepGEMM

- Block-scaled GEMM: `sm__inst_executed_pipe_tensor.avg.pct_of_peak_sustained_elapsed`,
  `lts__t_bytes`, `dram__throughput`.
- Grouped GEMM tail batches: `smsp__cycles_active`,
  `smsp__warp_issue_stalled_*`.
