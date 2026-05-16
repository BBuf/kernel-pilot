---
id: blog-nvidia-cuda-kernel-patterns
title: "NVIDIA CUDA Developer Blog Kernel Patterns"
author: NVIDIA Developer Blog
url: https://developer.nvidia.com/blog/tag/cuda/
source_category: community-note
architectures: [sm90, sm100, sm120]
tags: [coalescing, vectorized-loads, shared-memory-optimization, cuda-graphs, profiling, ldmatrix, wgmma]
languages: [cuda-cpp, ptx]
kernel_types: [gemm, fused-kernel]
retrieved_at: 2026-05-16
description: "Official blog/code-sample map for CUDA reductions, tensor cores, NVTX, profiling, unified memory, and CUDA samples."
---

# NVIDIA CUDA Developer Blog Kernel Patterns

Use this as an official blog/code-sample index for small CUDA kernels and
profiling patterns.

## Companion Repos

- `NVIDIA-developer-blog/code-samples`
- `NVIDIA/cuda-samples`

## Code Families

| Family | Example paths |
|---|---|
| Warp/block reductions | `posts/parallel_reduction_with_shfl/` |
| Tensor cores | `posts/tensor-cores/simpleTensorCoreGEMM.cu` |
| Mixed precision | `posts/mixed-precision/` |
| NVTX/profiling | `posts/nvtx/` |
| CUDA primitives | `cuda-samples/Samples/2_Concepts_and_Techniques/` |
| CUDA features | `cuda-samples/Samples/3_CUDA_Features/` |

## Search Patterns

```bash
grep -R -E -n "shfl|warp_reduce|block_reduce|wmma|mma|tensor core|shared|bank|coales|atomic|nvtx|cudaEvent" posts Samples
```
