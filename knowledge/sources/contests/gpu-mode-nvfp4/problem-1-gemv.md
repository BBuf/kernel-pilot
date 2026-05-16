---
id: contest-gpumode-p1
title: 'GPU Mode NVFP4 Hackathon - Problem 1: Batched GEMV'
source_category: contest-report
architectures:
- sm100
- sm100a
tags:
- nvfp4
- gemv
- fp4
- block-scale
techniques:
- vectorized-loads
- cache-policy
- register-reuse
- per-k-specialization
- data-reuse
- register-budgeting
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
url: https://github.com/gpu-mode/reference-kernels
submissions:
- rank: 1
  participant: Simon (veitner)
  score: ~22.4us geomean
  technique: Full PTX assembly with cache policy differentiation, byte unpacking,
    and aggressive register budgeting (maxrregcount=32)
  submission_truth: reconstructed-from-blog
  code_path: evidence/challenge-capsules/gpu-mode-nvfp4/problem-1-gemv/submissions/rank-1-simon-veitner/03-strategy-3-atomic-free-shared-memory-reduction.cpp
- rank: 2
  participant: yue
  score: ~23.0us geomean
  technique: Shared B vector reads across BLOCK_M rows, PTX load/decode path, ILP
    optimization
  submission_truth: reconstructed-from-blog
  code_path: evidence/challenge-capsules/gpu-mode-nvfp4/problem-1-gemv/submissions/rank-2-yue/05-step-5-ilp-optimization-22-9us.cpp
- rank: 3
  participant: Amandeep
  score: ~24.0us geomean
  technique: PTX assembly with per-K specialization, vectorized 256-bit loads, cache
    bypass for streamed matrix A
  submission_truth: unavailable
  code_unavailable_reason: Amandeep's PTX-level per-K specialization kernel was shared
    in the GPU Mode Discord problem-1 thread; author has not republished to a public
    platform at collection time
artifact_dir: evidence/challenge-capsules/gpu-mode-nvfp4/problem-1-gemv
---

# Problem 1: NVFP4 Batched GEMV

## Problem Description

Batched matrix-vector multiply with NVFP4 (E2M1) block-scaled inputs on B200 GPUs.

**Inputs**:
- Matrix `a`: shape (M x K x L), NVFP4 format
- Vector `b`: shape (1 x K x L), NVFP4 format
- Scale factors `sfa`: shape (M x K/16 x L), FP8 E4M3 (one scale per 16 FP4 elements)
- Scale factors `sfb`: shape (1 x K/16 x L), FP8 E4M3

**Output**: `c`: shape (M x 1 x L), FP16

**Nature**: Memory-bound (low arithmetic intensity -- each FP4 element is only used once in the dot product).

**Benchmark configurations**:
| Config | M | K | L |
|--------|------|-------|---|
| 1 | 7168 | 16384 | 1 |
| 2 | 4096 | 7168 | 8 |
| 3 | 7168 | 2048 | 4 |

**Speed of light**: ~8.6us for the largest configuration (theoretical bound from B200 8 TB/s memory bandwidth).

## Timeline

November 10 -- November 28, 2025. First of four problems in the hackathon series.

Prizes: 1st place DGX Spark + GTC pass, 2nd RTX 5090 + GTC, 3rd RTX 5080.

## NVFP4 Data Format

- 4-bit floating-point E2M1: 1 sign bit, 2 exponent bits, 1 mantissa bit
- Representable values: 0, 0.5, 1, 1.5, 2, 3, 4, 6 (positive and negative)
- Block scaling: every 16 FP4 elements share one FP8 E4M3 scale factor
- Two-level scaling: per-block E4M3 scale + per-tensor FP32 global scale
- Dequantization formula: `x_hat_i = s_global * s_block * deq_FP4(q_i)`
- Key difference from MXFP4: E4M3 block scale (non-power-of-two), smaller block size (16 vs 32)

## Top Performer Results

Geometric mean across all three benchmark configurations:
- Rank 1: ~22.4us (using full PTX assembly with per-K specialization)
- Rank 2: ~23.0us (shared B vector reads across BLOCK_M rows)
- Rank 3: ~24.0us

Speed-of-light gap: top performers achieved roughly 2.6x of SOL (~8.6us), reflecting the overhead of FP4 decoding and scale application.

## Optimization Techniques from Top Performers

### PTX-Level Control

Raw PTX instructions instead of C intrinsics for critical paths:

```asm
// FP4 to FP16 conversion via PTX
cvt.rn.f16x2.e2m1x2 %result, %fp4_packed;

// Byte unpacking: avoid bitwise extraction overhead
mov.b32 {tmp0, tmp1, tmp2, tmp3}, %packed_word;
```

Key insight: PTX byte unpacking (`mov.b32 {a, b, c, d}`) is significantly faster than manual bitwise extraction (`>> 4 & 0xF`) for splitting packed FP4 values.

### Cache Policy Differentiation

Different cache strategies for different access patterns:

```asm
// Matrix A (streamed once, never reused): bypass L1 to avoid pollution
ld.global.L1::no_allocate.v4.u64 {a0,a1,a2,a3}, [addr_a];

// Vector B (reused across M rows): keep hot in L1
ld.global.L1::evict_last.v4.u64 {b0,b1,b2,b3}, [addr_b];
```

Rank 1 solution used different `ld.global` qualifiers depending on which K-dimension variant was being compiled.

### Register Budgeting

Lower register counts force higher occupancy, which is critical for memory-bound kernels:

```
// Rank 1: aggressive register limit
nvcc -maxrregcount=32 ...

// Rank 3: slightly relaxed
nvcc -maxrregcount=45 ...
```

Fewer registers per thread -> more warps per SM -> better memory latency hiding.

### Wider Vectorized Loads

128-bit and 256-bit vector loads to maximize memory bandwidth utilization:

```asm
// 128-bit load (2x uint64)
ld.global.v2.u64 {r0, r1}, [addr];

// 256-bit load (4x uint64)
ld.global.v4.u64 {r0, r1, r2, r3}, [addr];
```

Only effective when combined with PTX byte unpacking to avoid bitwise overhead in the unpack stage.

### Per-K Specialization

Separate kernel compilations per K-dimension, each with full loop unrolling:

```cpp
// Each K variant compiled separately with optimal config
template <int K_SIZE>
__global__ void nvfp4_gemv_specialized();

// K=1024: fewer iterations, aggressive unrolling
// K=3584: moderate unrolling, different block dims
// K=8192: deepest loop, different register budget
```

Different K values have different optimal block dimensions, register limits, and unroll factors. Compiling separate kernels avoids runtime branching.

### Data Reuse (Rank 2 approach)

Share the B vector reads across all BLOCK_M rows within a thread block:

```
// Each thread block handles BLOCK_M rows
// Vector B is loaded once into shared memory
// All threads in the block reuse the same B data
__shared__ half b_shared[K_TILE];
```

Since B is shape (1 x K x L), every row of A multiplies against the same B vector. Sharing B reads across BLOCK_M rows reduces global memory traffic proportionally.

## Performance Progression (from Yue's blog)

| Stage | Technique | Latency |
|-------|-----------|---------|
| CuTe DSL baseline | Basic CuTe partition/copy | ~100us |
| Coalesced access | Fix memory access patterns | ~443us -> 39us |
| Hardware intrinsics | Use cvt.rn.f16x2.e2m1x2 | ~39us |
| PTX assembly | Full PTX with byte unpacking | ~27us |
| ILP optimization | Instruction-level parallelism | ~22.9us |
| Final submission | All combined | 22.392us |

## Key Lessons

1. **Memory-bound kernels need bandwidth-first thinking**: Arithmetic optimizations have minimal impact; focus on memory access patterns, cache policies, and vectorized loads.
2. **PTX gives real control on Blackwell**: The gap between C intrinsics and hand-written PTX was substantial (443us -> 27us in one participant's journey).
3. **Nsight Compute confirms memory-bound behavior**: "Run Nsight Compute to confirm memory-bound behavior" (Amandeep's key lesson after 12 attempts).
4. **Register budgeting matters**: On memory-bound kernels, lower register count -> higher occupancy -> better memory latency hiding. The difference between 32 and 45 max registers was measurable.

## B200 Context

- Architecture: sm_100a, 142 SMs
- Memory bandwidth: 8 TB/s HBM3e
- Native FP4 (E2M1) tensor core instructions
- TMA for async bulk loads
- TMEM: 128 x 512 x 32-bit per SM (not used for GEMV -- memory-bound, not compute-bound)

## Sources

- [gpu-mode/reference-kernels](https://github.com/gpu-mode/reference-kernels) (`/problems/nvidia/nvfp4_gemv/`)
- [Yue's Hackathon Journey](https://yue-zhang-2025.github.io/2025/12/02/blackwell-nvfp4-kernel-hackathon-journey.html)
- [Twelve Attempts (Amandeep)](https://amandeepsp.github.io/blog/nvfp4-blackwell-gemv/)
- [Simon's NVFP4 GEMV Blog](https://veitner.bearblog.dev/nvfp4-gemv/)
- [NVFP4 Format Details](https://haroldbenoit.com/notes/ml/engineering/precision/nvfp4-format)
