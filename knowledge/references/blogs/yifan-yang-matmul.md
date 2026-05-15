# Yifan Yang CUDA Matmul

Article: <https://yang-yifan.github.io/blogs/reg_tile/reg_tile.html>

Use this source for reasoning about why register tiling and throughput modeling
matter in hand-written CUDA matmul.

## Read For

| Kernel question | What to extract |
| --- | --- |
| Why shared-memory tiling alone is insufficient | arithmetic intensity and memory bandwidth argument |
| How to choose register tile size | per-thread work, register reuse, and occupancy tradeoff |
| How to reason with roofline | target bandwidth/throughput and where the kernel falls short |
| When to stop optimizing naive CUDA GEMM | compare against tensor-core/CUTLASS path and expected ceiling |

## Companion Code

No canonical repository is bundled here. Use this as a reasoning reference, then
implement or compare against:

- `siboehm/SGEMM_CUDA` for the full code ladder.
- `leimao/CUDA-GEMM-Optimization` for staged CUDA C++ variants.
- `NVIDIA/cutlass` or `ColfaxResearch/cfx-article-src` when the target should
  move to tensor cores, TMA, or WGMMA.

## Optimization Signals

- Look at achieved FLOP/s relative to bytes moved.
- If DRAM traffic is already low but tensor/FP32 pipe is weak, inspect register
  reuse, instruction mix, and occupancy.
- If register tile size increases speed but occupancy collapses, compare
  achieved active cycles and eligible warps.
