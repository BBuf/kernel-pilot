---
id: blog-amandeep-nvfp4
title: "Twelve Attempts at NVFP4 Batched GEMV"
author: Amandeep Singh
url: https://amandeepsp.github.io/blog/nvfp4-blackwell-gemv/
source_category: community-note
architectures: [sm100, sm100a]
tags: [nvfp4, gemv, fp4, block-scale, batched-gemv]
techniques: [vectorized-loads, cache-policy, register-budgeting, per-k-specialization, data-reuse]
hardware_features: [nvfp4, fp4, block-scale]
kernel_types: [batched-gemv, gemv]
languages: [cuda-cpp, ptx]
retrieved_at: 2026-04-16
---

# Twelve Attempts at NVFP4 Batched GEMV (Amandeep Singh)

## Overview

Amandeep Singh's detailed blog documenting 12 different approaches to solving Problem 1 (NVFP4 Batched GEMV) in the GPU Mode hackathon. Final performance: ~26.7us (3.1x off speed-of-light). The blog is valuable for its honest documentation of failed approaches and the debugging methodology using Nsight Compute.

## Final Performance

~26.7us geometric mean across benchmark configurations. Approximately 3.1x off the theoretical speed-of-light (~8.6us), which is limited by B200's 8 TB/s memory bandwidth.

## The 12 Attempts

### Attempts 1-3: Getting the Basics Right

```
Attempt 1: Naive CUDA kernel
- One thread per output element
- Result: very slow (>1000us)
- Problem: no coalescing, no vectorization

Attempt 2: Coalesced memory access
- Threads in warp read contiguous bytes
- Result: ~500us
- Problem: still using generic FP4 decode

Attempt 3: Vectorized loads (uint4)
- 128-bit loads for better bandwidth utilization
- Result: ~200us
- Problem: FP4 decode still manual bitwise ops
```

### Attempts 4-6: FP4 Decode Optimization

```
Attempt 4: Hardware FP4 intrinsics
- __cvt_fp4x2_to_halfx2 for type conversion
- Result: ~80us
- Big improvement from hardware-accelerated decode

Attempt 5: PTX byte unpacking
- mov.b32 {a,b,c,d} instead of shift/mask
- Result: ~50us
- Eliminates bitwise extraction overhead

Attempt 6: Combined PTX for load + decode
- Inline PTX for entire load-decode pipeline
- Result: ~40us
```

### Attempts 7-9: Memory System Optimization

```
Attempt 7: Cache policy differentiation
- L1::no_allocate for matrix A (streamed)
- L1::evict_last for vector B (reused)
- Result: ~35us
- B vector stays hot in L1 across rows

Attempt 8: Wider loads (v4.u64 = 256-bit)
- Maximum vector width for global loads
- Result: ~30us
- Better memory transaction efficiency

Attempt 9: Register budgeting (-maxrregcount)
- Tested 32, 40, 48, 56 max registers
- Result: ~28us with -maxrregcount=40
- More warps per SM -> better latency hiding
```

### Attempts 10-12: Fine-Tuning

```
Attempt 10: Block size tuning
- Tested BLOCK_M = 1, 2, 4, 8
- Result: ~27.5us with BLOCK_M=4
- B vector amortized across more rows

Attempt 11: K-dimension unrolling
- #pragma unroll for inner K loop
- Result: ~27us
- Marginal improvement from reduced loop overhead

Attempt 12: Per-K specialization
- Separate kernels for different K values
- Result: ~26.7us (final)
- Each K variant fully unrolled
```

## Key Debugging Methodology

### Nsight Compute Analysis

The blog emphasizes using Nsight Compute to confirm the kernel is memory-bound:

```
// Nsight Compute key metrics to check:
// 1. Memory throughput: how close to 8 TB/s?
// 2. Compute throughput: should be low for memory-bound
// 3. Achieved occupancy: higher is better for memory-bound
// 4. L1 hit rate: should be high for B vector (evict_last)
// 5. L2 hit rate: confirms data reuse patterns

// Key insight from Amandeep:
// "Run Nsight Compute to confirm memory-bound behavior"
// Many optimizations are counterproductive if you misidentify
// the bottleneck (e.g., compute optimizations on memory-bound kernel)
```

### Performance Model

```
// Speed-of-light calculation:
// Total data to read:
//   A: M * K * 0.5 bytes (FP4)
//   B: 1 * K * 0.5 bytes (FP4)
//   sfa: M * (K/16) bytes (FP8)
//   sfb: 1 * (K/16) bytes (FP8)
//   Total ≈ M * K * 0.5625 bytes
//
// For M=7168, K=16384, L=1:
//   Total = 7168 * 16384 * 0.5625 = 66 MB
//   At 8 TB/s: 66 MB / 8 TB/s = 8.25us
//
// Actual: 26.7us = 3.2x off SOL
// The gap comes from: FP4 decode overhead, scale factor application,
// partial sum reduction, and less-than-perfect vectorization
```

## Failed Approaches (Instructive)

1. **Shared memory for A matrix**: No benefit because A is streamed (each element read once). Shared memory only helps when data is reused.

2. **Tensor cores for GEMV**: tcgen05.mma requires MxNxK tiles with M >= 128. GEMV has M=1 (or small M for batched), so tensor cores cannot be efficiently utilized. This is fundamentally a CUDA-core memory-bandwidth problem.

3. **Warp shuffle reduction**: Expected to help for the K-dimension reduction, but the overhead of shuffle instructions exceeded the benefit over simple register accumulation at these K sizes.

## Key Lessons

1. **Profile first, optimize second**: Nsight Compute should be the first tool, not the last. Knowing whether a kernel is memory-bound or compute-bound determines the entire optimization strategy.

2. **FP4 decode is the hidden bottleneck**: The sub-byte format introduces decode overhead that doesn't exist for standard FP16/FP32 kernels. Hardware intrinsics and PTX byte unpacking are essential.

3. **Tensor cores don't help for GEMV**: GEMV is fundamentally memory-bandwidth-limited and the arithmetic intensity is too low for tensor cores. CUDA cores + wide vectorized loads are the right approach.

4. **3x off SOL is realistic for FP4 GEMV**: The FP4 decode overhead, scale factor application, and reduction operations add unavoidable computation that a pure bandwidth model doesn't account for.

5. **Systematic exploration beats intuition**: Documenting 12 attempts with measurements at each step is more productive than guessing at the optimal configuration.

## Sources

- [Twelve Attempts at NVFP4 Batched GEMV](https://amandeepsp.github.io/blog/nvfp4-blackwell-gemv/)
- [gpu-mode/reference-kernels](https://github.com/gpu-mode/reference-kernels)
