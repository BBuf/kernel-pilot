---
id: doc-cutlass-blackwell
title: "NVIDIA CUTLASS 4.x Blackwell Support"
url: https://docs.nvidia.com/cutlass/latest/CHANGELOG.html
source_category: official-doc
architectures: [sm100, sm100a]
tags: [tcgen05, tmem, tma, clc, 2sm-cooperative, nvfp4, fp8, fp4, fp6, block-scale, cute-dsl]
retrieved_at: 2026-04-16
---

# NVIDIA CUTLASS 4.x Blackwell Support

## Overview

CUTLASS 4.x introduces comprehensive SM100 (Blackwell) support, including new MMA atoms for tcgen05, TMEM management, CLC-based tile scheduling, and sub-byte data type support (FP4, FP6, FP8 with block scaling).

## Key Components

### UMMA (Unified Matrix Multiply-Accumulate)

CUTLASS abstraction replacing WGMMA for Blackwell:

- **Register-free operation**: Operands in SMEM, accumulators in TMEM
- **Single-thread launch**: One thread issues the MMA (vs warpgroup of 128 on Hopper)
- **Built-in block scaling**: Native support for FP4/FP6/FP8 with per-block scale factors
- **Two-level abstraction**:
  - `MMA_Atom`: Direct PTX wrapper for tcgen05.mma variants
  - `MMA_Traits`: CuTe layout definitions for data arrangement

### SM100 GEMM Schedules

CUTLASS provides several optimized kernel schedules for SM100:

```cpp
// Standard 1-SM warp-specialized GEMM
cutlass::gemm::KernelTmaWarpSpecialized1Sm

// 2-SM cooperative GEMM (doubled M tile)
cutlass::gemm::KernelTmaWarpSpecialized2Sm

// NVFP4 specialized (block-scale aware)
cutlass::gemm::KernelPtrArrayTmaWarpSpecialized1SmNvf4Sm100

// Persistent kernel with CLC scheduling
cutlass::gemm::KernelTmaWarpSpecializedPersistent1Sm
```

### CuTe SM100 Atoms

New CuTe atoms for Blackwell hardware:

```cpp
// tcgen05 MMA atom
using MMA = decltype(make_tiled_mma(
    SM100_MMA_SS_128x256x16_BF16_RS{},  // MMA atom: SMEM x SMEM -> TMEM
    Layout<Shape<_1,_1,_1>>{}            // Atom layout
));

// TMA copy atom
using CopyA = SM100_TMA_LOAD;
using CopyB = SM100_TMA_LOAD;
```

### SM100 Attention Kernels

CUTLASS 4.x adds SM100 attention kernels with Blackwell-specific features:

- **Fused reduction for MLA**: Weight-absorbed MLA decoding kernel, similar to FlashMLA
- **MLA K-splitting**: Supports splitting K dimension across multiple SMs for large head dimensions
- **16-warp kernels**: Distinct warp specialization roles (TMA, compute, softmax, epilogue)
- **Ping-pong scheduling**: Two query tiles per CTA with dedicated softmax warpgroups handling TMEM

### Sub-Byte Data Type Support

CUTLASS handles the complexity of sub-byte data types:

```cpp
// FP4 element type
using ElementA = cutlass::float_e2m1_t;
using ElementB = cutlass::float_e2m1_t;

// Block scale type
using ElementScale = cutlass::float_e4m3_t;

// Layout with interleaved scales
// Every 16 FP4 elements -> 1 FP8 scale factor
// CUTLASS handles packing/unpacking automatically
```

### Epilogue Support

SM100 epilogue visitors for fused operations:

```cpp
// Standard epilogue: scale + bias + activation
using EpilogueOp = cutlass::epilogue::fusion::LinCombEltAct<
    cutlass::epilogue::thread::SiLU,  // Activation function
    float,                             // Compute type
    float,                             // Scale type
    cutlass::half_t                   // Output type
>;

// Custom visitor for dual GEMM fusion (gate-up pattern)
using EpilogueVisitor = cutlass::epilogue::fusion::DualGemmSiLU<...>;
```

## CUTLASS Collective Builder Pattern

The builder pattern simplifies kernel configuration:

```cpp
using CollectiveMainloop = typename cutlass::gemm::collective::CollectiveBuilder<
    cutlass::arch::Sm100,                     // Architecture
    cutlass::arch::OpClassTensorOp,           // Op class
    ElementA, LayoutA, AlignmentA,            // Operand A
    ElementB, LayoutB, AlignmentB,            // Operand B
    ElementAccumulator,                       // Accumulator
    TileShape_MxNxK,                          // Tile shape
    ClusterShape,                             // Cluster shape
    cutlass::gemm::collective::StageCountAutoCarveout<>,  // Pipeline stages
    KernelSchedule                            // Kernel schedule
>::CollectiveOp;
```

## Performance Data

CUTLASS SM100 kernels achieve near-cuBLAS performance:
- BF16 GEMM: 98% of cuBLAS with persistent kernel + CLC
- FP8 GEMM: Competitive with DeepGEMM on standard shapes
- NVFP4 GEMM: Used as baseline in GPU Mode Hackathon
- MLA attention: Comparable to FlashMLA for decode workloads

## Key Files in CUTLASS Repository

| Path | Description |
|---|---|
| `include/cute/arch/mma_sm100*.hpp` | SM100 MMA atom definitions |
| `include/cute/atom/copy_sm100*.hpp` | SM100 TMA copy atoms |
| `include/cutlass/gemm/kernel/sm100_*.hpp` | SM100 kernel schedules |
| `include/cutlass/gemm/collective/sm100_*.hpp` | SM100 collective operations |
| `include/cutlass/epilogue/fusion/*.hpp` | Epilogue visitors |
| `examples/cute/blackwell/` | Blackwell GEMM examples |

## Sources

- [CUTLASS Changelog](https://docs.nvidia.com/cutlass/latest/CHANGELOG.html)
- [CUTLASS GitHub](https://github.com/NVIDIA/cutlass)
- [Colfax CUTLASS Blackwell GEMM Tutorial](https://research.colfax-intl.com/cutlass-tutorial-writing-gemm-kernels-using-tmem-for-nvidia-blackwell-gpus/)
- [Colfax Sub-Byte GEMM Tutorial](https://research.colfax-intl.com/cutlass-tutorial-sub-byte-gemm-on-nvidia-blackwell-gpus/)
