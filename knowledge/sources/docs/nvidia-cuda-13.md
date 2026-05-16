---
id: doc-cuda-13
title: "NVIDIA CUDA Toolkit 13.x for Blackwell"
url: https://developer.nvidia.com/blog/whats-new-and-important-in-cuda-toolkit-13-0/
source_category: official-doc
architectures: [sm100, sm100a]
tags: [tcgen05, tmem, clc, tma, pdl, gdc, nvfp4, fp8, fp4, fp6, block-scale]
retrieved_at: 2026-04-16
---

# NVIDIA CUDA Toolkit 13.x for Blackwell

## Overview

CUDA 13.0 and 13.1 introduce full Blackwell (SM100) support, including new compiler intrinsics, PTX instructions, and runtime features for tcgen05, TMEM, CLC, and sub-byte data types.

## CUDA 13.0 Key Features

### SM100 Compiler Support

- New target architectures: `sm_100`, `sm_100a`
- NVCC supports `-arch=sm_100` and `-arch=sm_100a`
- `sm_100a` includes architecture-accelerated features (required for B200-specific instructions)
- PTX ISA 8.7+ for SM100 instructions

### tcgen05 Intrinsics

```cpp
// tcgen05.mma via PTX inline assembly
asm volatile(
    "tcgen05.mma.cta_group::1.kind::f16 "
    "[%0], [%1], [%2];"
    : : "l"(tmem_addr), "l"(smem_desc_a), "l"(smem_desc_b)
);

// CUDA C++ wrappers via CUTLASS/CuTe
// (No direct CUDA runtime intrinsics -- PTX or CuTe abstraction required)
```

### TMEM Access

```cpp
// TMEM allocation and access (via PTX)
asm volatile("tcgen05.alloc.cta_group::1 [%0], %1;"
    : : "l"(tmem_addr), "r"(num_rows));

// TMEM to register readback
asm volatile("tcgen05.ld.16x256b [%0], [%1];"
    : : "l"(reg_addr), "l"(tmem_addr));

// TMEM release
asm volatile("tcgen05.dealloc.cta_group::1 [%0], %1;"
    : : "l"(tmem_addr), "r"(num_rows));
```

### CLC APIs

```cpp
// CLC dynamic tile scheduling
asm volatile("clc.arrive.group::1;"  ::);
asm volatile("clc.wait.group::1;"    ::);

// CLC replaces manual tile queue management
// Hardware schedules tiles to available SMs
```

### Sub-Byte Type Support

```cpp
// FP4 type (E2M1)
#include <cuda_fp4.h>
__nv_fp4_e2m1 val;

// FP6 type
#include <cuda_fp6.h>

// Block-scale types
#include <cuda_fp8.h>
__nv_fp8_e4m3 scale;

// Conversion intrinsics
__half2 result = __cvt_fp4x2_to_halfx2(packed_fp4);
```

### PDL Default Enabled

Programmatic Dependent Launch is on by default in CUDA 13.0:
- Overlapping dependent kernel executions
- Grid Dependency Control (GDC) for explicit dependency management
- Near-zero gap between dependent kernel launches

## CUDA 13.1 Additions

### cuTile (NVIDIA)

New tile-level programming model:
- Higher-level abstraction than raw PTX
- Automatic TMA and MMA scheduling
- Targets SM100, SM103, SM110, SM120, SM121

### Performance Improvements

- Improved NVRTC (Runtime Compilation) for JIT kernels
- Better NVCC code generation for SM100 instruction scheduling
- Enhanced profiling support in Nsight Compute for TMEM and CLC

## PTX ISA SM100 Highlights

Key new PTX instructions for SM100:

| Instruction | Purpose |
|---|---|
| `tcgen05.mma.*` | Tensor core MMA (7 variants) |
| `tcgen05.alloc` | Allocate TMEM rows |
| `tcgen05.dealloc` | Release TMEM rows |
| `tcgen05.ld` | Load from TMEM to registers |
| `tcgen05.st` | Store from registers to TMEM |
| `clc.arrive` | CLC tile arrival |
| `clc.wait` | CLC tile wait |
| `cvt.rn.f16x2.e2m1x2` | FP4 to FP16 conversion |
| `cvt.rn.e2m1x2.f16x2` | FP16 to FP4 conversion |

## Compiler Flags for SM100

```bash
# Basic SM100 compilation
nvcc -arch=sm_100 kernel.cu

# SM100a (architecture-accelerated, required for B200)
nvcc -arch=sm_100a kernel.cu

# Register budget control (critical for memory-bound kernels)
nvcc -arch=sm_100a -maxrregcount=32 kernel.cu

# Generate PTX + SASS
nvcc -arch=sm_100a --ptx kernel.cu
nvcc -arch=sm_100a --cubin kernel.cu
```

## Sources

- [CUDA 13.0 Blog](https://developer.nvidia.com/blog/whats-new-and-important-in-cuda-toolkit-13-0/)
- [CUDA 13.1 Blog](https://developer.nvidia.com/blog/nvidia-cuda-13-1-powers-next-gen-gpu-programming-with-nvidia-cuda-tile-and-performance-gains/)
- [CUDA 13.0 Release Notes](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/)
- [PTX ISA 8.7 Reference](https://docs.nvidia.com/cuda/parallel-thread-execution/)
