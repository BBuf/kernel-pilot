---
id: blog-yue-nvfp4
title: Blackwell NVFP4 Kernel Hackathon Journey
author: Yue Zhang
url: https://yue-zhang-2025.github.io/2025/12/02/blackwell-nvfp4-kernel-hackathon-journey.html
source_category: community-note
architectures:
- sm100
- sm100a
tags:
- nvfp4
- gemv
- fp4
- block-scale
- batched-gemv
techniques:
- vectorized-loads
- cache-policy
- register-reuse
- loop-unrolling
hardware_features:
- nvfp4
- fp4
- block-scale
kernel_types:
- batched-gemv
- gemv
languages:
- cuda-cpp
- ptx
- cute-dsl
retrieved_at: 2026-04-16
artifact_dir: evidence/blog-capsules/yue-nvfp4-hackathon/code
---

# Blackwell NVFP4 Kernel Hackathon Journey (Yue Zhang)

## Overview

Yue Zhang's detailed account of optimizing Problem 1 (NVFP4 Batched GEMV) in the GPU Mode hackathon. Documents the full optimization journey from a naive CuTe DSL implementation (~100us) to a highly optimized CUDA/PTX kernel (22.392us) -- a 4.5x improvement through systematic optimization.

## Performance Progression

| Stage | Approach | Latency | Improvement |
|-------|----------|---------|-------------|
| 1 | CuTe DSL baseline | ~100us | -- |
| 2 | Naive CUDA (coalesced access) | ~443us | (worse than CuTe initially) |
| 3 | Hardware intrinsics | ~39us | 11.4x from stage 2 |
| 4 | PTX assembly | ~27us | 1.44x from stage 3 |
| 5 | ILP optimization | ~22.9us | 1.18x from stage 4 |
| 6 | Final tuned | 22.392us | 4.5x from stage 1 |

Key observation: The initial naive CUDA attempt was slower than CuTe DSL, demonstrating that manual optimization requires deep understanding of the hardware to outperform a well-designed DSL.

## Key Optimization Steps

### Step 1: CuTe DSL Baseline (~100us)

```cpp
// CuTe DSL approach:
// - Automatic partition/copy for NVFP4 data
// - Handles packing/unpacking of FP4 values
// - Reasonable but not optimal memory access patterns
// Result: ~100us -- decent starting point
```

CuTe DSL provided a functional baseline without requiring deep hardware knowledge, but left significant performance on the table for this memory-bound kernel.

### Step 2: Coalesced Memory Access (~443us, then improved)

Initial hand-written CUDA was actually slower because the memory access pattern was not properly coalesced:

```cpp
// Bad: each thread reads non-contiguous FP4 elements
// Good: threads in a warp read contiguous 128-byte chunks
// The FP4 packing (2 elements per byte) requires careful indexing
// to maintain coalesced access at the byte level
```

After fixing coalescing, performance improved dramatically but still required hardware-specific optimizations.

### Step 3: Hardware Intrinsics (~39us)

Replaced generic type conversions with NVIDIA FP4 hardware intrinsics:

```cpp
// Generic: manual bit manipulation for FP4 -> FP16 conversion
// float val = decode_fp4_manual(packed_byte >> 4);  // slow

// Hardware intrinsic: single instruction for FP4 -> FP16x2
// __half2 result = __cvt_fp4x2_to_halfx2(packed_fp4);  // fast
```

The hardware intrinsic path is 11.4x faster than the manual approach, demonstrating the importance of using ISA-specific instructions for sub-byte data types.

### Step 4: PTX Assembly (~27us)

Dropped to raw PTX for fine-grained control:

```asm
// Key PTX optimizations:
// 1. cvt.rn.f16x2.e2m1x2 for FP4 conversion (vs C intrinsic)
cvt.rn.f16x2.e2m1x2 %result, %fp4_packed;

// 2. Byte unpacking via mov.b32 (vs bitwise shift/mask)
mov.b32 {b0, b1, b2, b3}, %packed_word;
// Splits 32-bit word into 4 bytes without arithmetic

// 3. Cache-qualified loads
ld.global.L1::no_allocate.v4.u64 {a0,a1,a2,a3}, [addr_a];  // stream A
ld.global.L1::evict_last.v4.u64 {b0,b1,b2,b3}, [addr_b];   // keep B hot
```

The PTX byte unpacking (`mov.b32 {a,b,c,d}`) is a critical optimization: it replaces 3-4 shift/mask instructions with a single register move, and the savings compound across the entire K dimension.

### Step 5: ILP Optimization (~22.9us)

Increased instruction-level parallelism by unrolling and interleaving independent operations:

```cpp
// Before: sequential FP4 decode + accumulate
for (int k = 0; k < K; k += 16) {
    decode_fp4(a[k:k+16]);
    accumulate(partial_sum);
}

// After: unrolled with interleaved decode + accumulate
// Decode batch[i+1] while accumulating batch[i]
// Multiple independent accumulator registers
```

### Final Result: 22.392us

The final kernel combined all optimizations. Key factors in the 4.5x total improvement:
1. Hardware FP4 conversion intrinsics (biggest single win)
2. PTX byte unpacking (avoids bitwise overhead)
3. Cache policy differentiation (A: no-allocate, B: evict-last)
4. ILP through unrolling and register interleaving
5. Proper memory coalescing for FP4 packed data

## Key Lessons Shared

1. **CuTe DSL is a good starting point**: Even for memory-bound kernels, CuTe provides a reasonable baseline. But for the last 4x of performance, manual optimization is required.

2. **Hardware intrinsics are essential for sub-byte types**: Generic FP4 decoding is an order of magnitude slower than hardware-specific paths.

3. **PTX gives control that C++ cannot**: Cache policies, byte unpacking, and instruction scheduling are only accessible at the PTX level.

4. **Memory-bound kernels need different optimization strategies**: Unlike compute-bound GEMM (where tensor core utilization is key), GEMV optimization is about maximizing memory bandwidth utilization.

## Sources

- [Yue's Hackathon Journey](https://yue-zhang-2025.github.io/2025/12/02/blackwell-nvfp4-kernel-hackathon-journey.html)
- [gpu-mode/reference-kernels](https://github.com/gpu-mode/reference-kernels)
