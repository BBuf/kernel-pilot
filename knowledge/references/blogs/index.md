# Blog Kernel References

This folder is the prose-to-code map for kernel optimization sources. Use it
after `routing/` selects a topic and before opening large repositories. Prefer
the linked companion code when an article has code; record both the article URL
and code path in the source ledger.

| Source | Read when |
| --- | --- |
| `veitner.md` | CuTe DSL, QuACK, TMA/WGMMA, swizzling, transpose, RMSNorm, block-scaled GEMM, NVFP4, GDN |
| `colfax.md` | CUTLASS/CuTe Hopper/Blackwell GEMM, TMA, WGMMA, Stream-K, FlashAttention, FlexAttention |
| `nvidia-cuda.md` | Classic CUDA reductions, tensor cores, unified memory, NVTX/profiling, official companion kernels |
| `simon-boehm-sgemm.md` | Stepwise SGEMM optimization ladder with code kernels v1-v12 |
| `lei-mao-cuda.md` | CUDA GEMM, transpose, reductions, bank conflicts, benchmarking notes |
| `yifan-yang-matmul.md` | Register tiling, roofline reasoning, throughput model for CUDA matmul |

## Use Rules

- Read code-first when companion code exists.
- Use prose to understand the invariant and failure mode, not as a substitute
  for testing.
- Log source URL, companion repo/path, hypothesis, result, and do-not-reread
  key during plateau research.
