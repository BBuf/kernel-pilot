---
id: blog-simon-nvfp4-gemv
title: NVFP4 GEMV and Improved NVFP4 GEMV
author: Simon Veitner
url: https://veitner.bearblog.dev/nvfp4-gemv/
source_category: community-note
architectures:
- sm100
tags:
- nvfp4
- gemv
- fp4
- block-scale
- cute-dsl
- vectorized-loads
- register-reuse
- batched-gemv
retrieved_at: 2026-04-17
artifact_dir: evidence/blog-capsules/simon-nvfp4-gemv/code
---

# NVFP4 GEMV and Improved NVFP4 GEMV (Simon Veitner)

## Overview

Simon Veitner's two-part blog series on implementing NVFP4 GEMV kernels using CuTe DSL for Blackwell GPUs. Part 1 presents a reference CuTe implementation with hierarchical tensor layouts for FP4 block-scaled GEMV. Part 2 ("Improved") introduces three optimization strategies that parallelize the K-dimension reduction, achieving up to 6.4x speedup over the reference.

## Part 1: Reference CuTe DSL Implementation

### Configuration

- Tile dimensions: (128, 1, 64) for M, N, K
- Data types: FP4 (E2M1) for weight matrix, FP8 (E4M3) for scale factors, FP16 output
- Scale factor block size: 16 elements per FP8 scale value
- Thread block size: 128 threads per CTA

### NVFP4 Format Handling

NVFP4 is composed of two tensors: one in FP4 precision and another in FP8 precision. The scale factor applies to every block of 16 values to minimize quantization error while reducing memory footprint.

### Memory Access Patterns

The kernel uses hierarchical CuTe tensor indexing:
- Matrix A: shape (128, 64, 1, 4, 1) representing one M-tile with four K-tiles
- Scale factors: hierarchical layout ((32,4), (16,4)) enabling broadcast optimization
- Vector B: single N-tile with K-dimension iteration

### Core Computation

The computation loop applies two-level scaling:
```
res += tArA[i] * tArSFA[i] * tBrB[i] * tBrSFB[i]
```
FP4 values are multiplied by their corresponding FP8 scale factors before accumulation. Values convert from FP4/FP8 to FP32 registers for computation, then convert to FP16 for storage.

## Part 2: Improved NVFP4 GEMV

### Three Optimization Strategies

**Strategy 1: Extra Blocks (K-Parallel Grid)**
- Launches grid blocks corresponding to K-tiles, eliminating the K-tile loop
- Uses atomic operations on global memory (F32 accumulation buffer)
- Performance: ~36,864 ops (benchmark 0), ~55,399 ops (benchmark 1)
- Achieves 6.4x improvement on benchmark 0 versus reference

**Strategy 2: Thread-Level with Atomic Add**
- Distributes work across thread dimensions (threads_per_m=32, threads_per_k=32)
- Uses shared memory atomics for collaborative result calculation
- Avoids separate F32 tensor allocation overhead
- Performance: ~38,911 ops (benchmark 0), ~67,258 ops (benchmark 1)

**Strategy 3: Thread-Level with Reduction (No Atomics)**
- Allocates 2D shared memory tensor (K-major stride)
- Each thread pair stores intermediate results, then performs synchronous reduction
- Performance: ~38,911 ops (benchmark 0), ~65,599 ops (benchmark 1)

### Key Technical Changes

- Serial K-dimension loop replaced with parallel K-reduction
- Intermediate products converted to FP16 for storage efficiency
- FP32 maintained for scale factor operations
- Synchronization barriers inserted between computation and reduction phases
- K-major memory layouts optimize the reduction step access patterns

### Performance Summary

Reference baseline: ~234,495 ops. Best improvement (extra blocks) delivers 6.4x speedup on larger K dimensions, though smaller K problems show more modest gains.

## Key Insights

- CuTe DSL's hierarchical tensor layouts naturally express NVFP4's two-level scaling structure
- K-dimension parallelism is critical for GEMV performance on Blackwell
- Atomic-free reductions in shared memory match or approach atomic-based approaches
- The choice between strategies depends on K-dimension size and available SM resources

## Key Code

### Reference core computation (Part 1)

```cpp
// NVFP4 GEMV: FP4 values are decoded to FP32 via their per-block FP8 scale,
// then multiplied against a decoded B element + its FP8 scale. Accumulation
// stays in FP32. Simon's reference kernel does this in a CuTe register tile:
for (int i = 0; i < TILES_K; i++) {
    float a = decode_nvfp4(tArA[i]) * decode_fp8(tArSFA[i]);
    float b = decode_nvfp4(tBrB[i]) * decode_fp8(tBrSFB[i]);
    res += a * b;                // FP32 accumulation
}
```

### Strategy 1 — K-parallel grid with atomic accumulation

```cpp
// Launch one CTA per (M-tile, K-tile); accumulate partial products into a
// global FP32 buffer via atomicAdd, then cast to FP16 in a second pass.
__global__ void nvfp4_gemv_k_parallel(
    const __nv_fp4_e2m1* A, const __nv_fp8_e4m3* SFA,
    const __nv_fp4_e2m1* B, const __nv_fp8_e4m3* SFB,
    float* accum_f32, int K_TILES)
{
    int m_tile = blockIdx.x;
    int k_tile = blockIdx.y;
    float partial = nvfp4_dot_product(A, SFA, B, SFB, m_tile, k_tile);
    atomicAdd(&accum_f32[m_tile], partial);
}
```

### Strategy 3 — Atomic-free shared-memory reduction

```cpp
// Each thread pair stores an intermediate product; after __syncthreads()
// the CTA reduces along K-major in shared memory without atomics.
__shared__ float smem[THREADS_PER_M][THREADS_PER_K];
smem[tid_m][tid_k] = thread_partial;
__syncthreads();

// Warp-wide parallel reduction along the K axis
for (int s = THREADS_PER_K / 2; s > 0; s >>= 1) {
    if (tid_k < s) smem[tid_m][tid_k] += smem[tid_m][tid_k + s];
    __syncthreads();
}
if (tid_k == 0) C[m_base + tid_m] = __float2half(smem[tid_m][0]);
```
