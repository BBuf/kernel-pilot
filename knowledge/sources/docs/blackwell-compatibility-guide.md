---
id: doc-blackwell-compatibility-guide
title: "NVIDIA Blackwell Compatibility Guide"
url: https://docs.nvidia.com/cuda/blackwell-compatibility-guide/
source_category: official-doc
architectures: [sm100, sm100a]
tags: [ptx, cuda-cpp]
retrieved_at: 2026-04-17
---

# NVIDIA Blackwell Compatibility Guide

## Overview

The official NVIDIA Blackwell Compatibility Guide (Release 13.2) documents the rules governing binary and PTX compatibility for the Blackwell GPU architecture (compute capability 10.0). It covers CUDA toolkit version requirements, the distinction between SM100 (datacenter) and SM120 (consumer), PTX forward compatibility, sm_100a architecture-accelerated features, and migration guidance for existing CUDA applications.

## Compute Capability: SM100

Blackwell datacenter GPUs use compute capability 10.0:
- **sm_100**: NVIDIA B100 (GB100), B200, B40
- **sm_100a**: Architecture-accelerated variant (required for B200-specific features like certain tcgen05 modes)

**Important**: SM120 (consumer Blackwell, e.g., RTX 5090) is a separate compilation target. SM100 datacenter cubins are NOT compatible with SM120 consumer GPUs, and vice versa. These are distinct architectures despite both being marketed as "Blackwell."

## CUDA Toolkit Version Requirements

### Forward Compatibility via PTX

Applications built with CUDA Toolkit versions 2.1 through 12.8 are compatible with Blackwell as long as they include PTX versions of their kernels. PTX is forward-compatible: code generated for compute capability 9.x runs on 9.x or higher architectures including Blackwell.

### Native Blackwell Support

CUDA Toolkit 12.8 is the first version supporting native Blackwell cubin generation. The recommended compilation flags:
```
-gencode=arch=compute_100,code=sm_100
-gencode=arch=compute_100,code=compute_100
```

Including both native cubin AND PTX provides optimal performance (native cubin) plus future compatibility (PTX).

## Binary Compatibility Rules

### Cubin (Native Binary)
- Cubin binaries are NOT forward-compatible
- A cubin compiled for compute capability 8.6 cannot run on 8.0
- A cubin compiled for sm_100 runs only on sm_100 GPUs
- sm_100 cubins do NOT run on sm_120 GPUs

### PTX (Virtual ISA)
- PTX IS forward-compatible across architectures
- PTX compiled for compute_90 can JIT-compile and run on Blackwell
- JIT compilation occurs at first launch (with driver caching)

## Architecture-Accelerated Features (sm_100a)

Applications using `sm_100a` or `compute_100a` compilation targets:
- Are NOT forward or backward compatible
- Can only run on sm_100a-capable hardware (e.g., B200)
- PTX compiled for compute_90a (Hopper) will NOT function on Blackwell
- Required for certain architecture-specific instructions and optimizations

The "a" suffix denotes architecture-accelerated features that are hardware-specific and do not carry forward to next-generation architectures.

## Compatibility Verification

To verify if an existing CUDA application is Blackwell compatible:

1. Download and install the latest NVIDIA driver
2. Set environment variable: `CUDA_FORCE_PTX_JIT=1`
3. Launch the application
4. If the application works correctly, it is Blackwell compatible via PTX JIT

This forces all kernels to go through the PTX JIT path, simulating what happens when running on a new architecture without native cubins.

## Migration Guidance

### For New Applications Targeting Blackwell
```bash
# Compile with both native cubin and PTX fallback
nvcc -gencode=arch=compute_100,code=sm_100 \
     -gencode=arch=compute_100,code=compute_100 \
     my_kernel.cu
```

### For Existing Applications (Pre-12.8 Toolkit)
- Ensure PTX is included in the binary (default for most builds)
- Test with CUDA_FORCE_PTX_JIT=1 to verify compatibility
- For best performance, recompile with CUDA 12.8+ to get native cubins

### Multi-Architecture Binaries
```bash
# Target Hopper, Blackwell datacenter, and Blackwell consumer
nvcc -gencode=arch=compute_90,code=sm_90 \
     -gencode=arch=compute_100,code=sm_100 \
     -gencode=arch=compute_120,code=sm_120 \
     -gencode=arch=compute_120,code=compute_120 \
     my_kernel.cu
```

The final `compute_120` entry provides PTX fallback for future architectures.

## Key Compatibility Matrix

| Source | Target sm_90 | Target sm_100 | Target sm_120 |
|---|---|---|---|
| sm_90 cubin | Yes | No | No |
| sm_100 cubin | No | Yes | No |
| sm_120 cubin | No | No | Yes |
| compute_90 PTX | Yes (native) | Yes (JIT) | Yes (JIT) |
| compute_100 PTX | No | Yes (native) | No* |
| compute_90a PTX | Yes | No | No |
| compute_100a PTX | No | Yes (sm_100a only) | No |

*compute_100 PTX cannot JIT to sm_120; these are separate architecture families.
