---
id: contest-gpumode-p2
title: 'GPU Mode NVFP4 Hackathon - Problem 2: NVFP4 GEMM'
source_category: contest-report
architectures:
- sm100
- sm100a
tags:
- nvfp4
- gemm
- fp4
- block-scale
- tcgen05
- tmem
- tma
techniques:
- warp-specialization
- pipeline-stages
- swizzling
- register-reuse
hardware_features:
- nvfp4
- fp4
- block-scale
- tcgen05
- tmem
- tma
kernel_types:
- gemm
languages:
- cuda-cpp
- ptx
- cute-dsl
url: https://github.com/gpu-mode/reference-kernels
submissions:
- rank: 1
  participant: Simon (veitner)
  score: 10.807us geomean
  technique: CUTLASS SM100 warp-specialized NVFP4 GEMM with tcgen05.mma, optimized
    TMA pipeline depth and tile scheduling
  submission_truth: unavailable
  code_unavailable_reason: Simon's NVFP4 GEMM winning submission posted in the GPU
    Mode Discord problem-2 thread; author has not republished the GEMM variant on
    a public platform
- rank: 2
  participant: yue
  score: 10.914us geomean
  technique: CUTLASS-based warp specialization with tuned pipeline stages, TMA async
    bulk loads, TMEM accumulator management
  submission_truth: unavailable
  code_unavailable_reason: Yue's NVFP4 GEMM submission posted in the GPU Mode Discord
    problem-2 thread; the public hackathon blog covers GEMV (problem 1), not problem-2
    GEMM
- rank: 3
  participant: currybab
  score: 10.931us geomean
  technique: CUTLASS KernelPtrArrayTmaWarpSpecialized1SmNvf4Sm100 schedule with custom
    tile size and cluster shape tuning
  submission_truth: unavailable
  code_unavailable_reason: currybab's submission posted in the GPU Mode Discord problem-2
    thread; no public author republish at collection time
---

# Problem 2: NVFP4 GEMM

## Problem Description

Standard NVFP4 block-scaled general matrix multiplication on B200 GPUs. Unlike Problem 1 (GEMV), this is compute-bound and targets tensor core utilization.

**Operation**: C = A * B where A and B are NVFP4 (E2M1) with per-16-element FP8 E4M3 block scaling.

**Nature**: Compute-bound -- high arithmetic intensity enables tensor core saturation.

## Timeline

November 29 -- December 19, 2025. Second problem, weighted 20% for grand prize.

## Top Performer Results

Geometric mean across benchmark configurations:
| Rank | Participant | Geometric Mean |
|------|-----------|----------------|
| 1 | Simon | 10.807us |
| 2 | yue | 10.914us |
| 3 | currybab | 10.931us |

Extremely tight competition -- top 3 within 1.1% of each other.

## Optimization Techniques

### Tensor Core Utilization

Unlike Problem 1 (memory-bound GEMV), GEMM fully leverages Blackwell tensor cores:

```
// tcgen05.mma operates directly on shared memory
// No ldmatrix needed -- operands read from SMEM, results written to TMEM
tcgen05.mma.cta_group::1.kind::f16
    [tmem_addr],        // accumulator in TMEM
    [smem_desc_a],      // operand A descriptor (shared memory)
    [smem_desc_b];      // operand B descriptor (shared memory)
```

Key Blackwell advantage: tcgen05.mma reads operands directly from shared memory and writes results to tensor memory (TMEM), eliminating the register-based ldmatrix/stmatrix pipeline required on Hopper.

### Warp Specialization

Dedicated warp roles for overlapping data movement and computation:

- **TMA warps**: Issue async bulk loads from global to shared memory via TMA descriptors
- **Tensor core warps**: Execute tcgen05.mma on data already in shared memory
- **Epilogue warps**: Handle accumulator readback from TMEM and output conversion

```
// CUTLASS schedule used by top performers:
// KernelPtrArrayTmaWarpSpecialized1SmNvf4Sm100
```

### TMA for Async Bulk Loads

Tensor Memory Accelerator handles data movement without consuming SM resources:

- 128-byte alignment requirement for TMA descriptors
- Async pipeline from HBM -> SMEM via TMA, overlapped with tensor core compute
- Shared memory acts as staging buffer for NVFP4 data + scale factors

### TMEM for MMA Results

Tensor Memory holds accumulator state:

- 128 x 512 matrix of 32-bit elements per SM
- MMA results written directly to TMEM (not registers)
- Eliminates register pressure from large accumulator tiles
- Readback to registers only during epilogue

### NVFP4 Block Scale Handling

Scale factors must be applied during or after the MMA:

```
// Two-level dequantization in epilogue:
// 1. Apply per-block E4M3 scale factors
// 2. Apply per-tensor FP32 global scale
// 3. Convert accumulator to FP16 output
result[i] = fp16(global_scale * block_scale_a[i/16] * block_scale_b[j/16] * acc[i][j]);
```

## Key Code Pattern: CUTLASS SM100 NVFP4 GEMM

Top performers leveraged CUTLASS 4.x infrastructure:

```cpp
// CUTLASS collective MMA for NVFP4 on SM100
using CollectiveMainloop = typename cutlass::gemm::collective::CollectiveBuilder<
    cutlass::arch::Sm100,
    cutlass::arch::OpClassTensorOp,
    cutlass::float_e2m1_t,        // Element A: NVFP4
    LayoutA,
    AlignmentA,
    cutlass::float_e2m1_t,        // Element B: NVFP4
    LayoutB,
    AlignmentB,
    float,                         // Accumulator: FP32
    TileShape,
    ClusterShape,
    cutlass::gemm::collective::StageCountAutoCarveout<>,
    cutlass::gemm::KernelPtrArrayTmaWarpSpecialized1SmNvf4Sm100
>::CollectiveOp;
```

## Performance Context

On B200 (142 SMs, peak FP4 tensor TFLOPS):
- Top performers achieved near-cuBLAS performance for NVFP4 GEMM
- The ~10.8us geometric mean represents excellent tensor core utilization
- Key differentiator from Problem 1: this is compute-bound, so tensor core scheduling and pipeline depth matter more than memory access patterns

## B200 Hardware Used

- sm_100a, 142 SMs
- TMEM: 256KB per SM (128 rows x 512 cols x 32-bit)
- tcgen05.mma with native NVFP4 support
- TMA with 128-byte alignment
- 8 TB/s HBM3e bandwidth (less relevant for compute-bound GEMM)

## Sources

- [gpu-mode/reference-kernels](https://github.com/gpu-mode/reference-kernels) (`/problems/nvidia/nvfp4_gemm/`)
- [NVIDIA Forums Announcement](https://forums.developer.nvidia.com/t/join-us-for-the-blackwell-nvfp4-kernel-hackathon-with-nvidia-and-gpu-mode/350092)
- [TFLOPS Gap Blog](https://huggingface.co/blog/apsys/blackwell-nvfp4-comparison)
