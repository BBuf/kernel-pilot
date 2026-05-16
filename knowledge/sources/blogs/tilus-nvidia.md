---
id: blog-tilus-nvidia
title: "Tilus: A Tile-Level GPGPU Programming Language for Low-Precision Computation"
author: NVIDIA
url: https://github.com/NVIDIA/tilus
source_category: community-note
architectures: [sm100, sm100a]
tags: [nvfp4, fp4, fp6, fp8, gemm, swizzling, pipeline-stages, cute-dsl, ptx]
retrieved_at: 2026-04-17
---

# Tilus: A Tile-Level GPGPU Programming Language for Low-Precision Computation

## Overview

Tilus is NVIDIA's open-source domain-specific language (DSL) for GPU programming that operates at thread-block-level granularity with tensors as the primary data type. Unlike Triton, Tilus provides explicit control over shared memory and register tensor layouts while supporting low-precision data types with arbitrary bit-widths (1 to 8 bits). Published at ASPLOS 2026 and available on GitHub, Tilus targets Blackwell's advanced features including TMA loads, tensor memory, warp specialization, and cluster-level synchronization.

## Programming Model

### Thread-Block Level Abstraction
Tilus abstracts GPU program execution into thread-block-level instructions, operating at a coarser computational grain than CUDA C++ while being more explicit than Triton:
- Thread-block-level granularity (not warp or thread level)
- Tensors as the fundamental data structure
- Explicit control over shared memory and tensor layouts (unlike Triton's implicit management)

### Memory Hierarchy Control
Users directly manage four levels of the memory hierarchy:
- **Register tensors**: Per-thread storage for computation
- **Shared memory tensors**: Thread-block collaboration and data reuse
- **Global memory tensors**: Inter-block data communication
- **Tensor Memory (TMemory)**: Blackwell-specific on-chip storage for tcgen05 operands

### Key Differentiator from Triton
While Triton abstracts away memory management, Tilus deliberately exposes it. Developers can specify tensor layouts in shared memory and registers, enabling fine-grained optimization of data movement patterns including swizzling and bank conflict avoidance.

## Low-Precision Data Type Support

Tilus's defining feature is support for arbitrary low-precision types with bit-widths from 1 to 8 bits:
- 1-bit: Binary neural networks
- 2-bit: Aggressive quantization
- 3-bit: Custom formats
- 4-bit: FP4 (E2M1), INT4, NVFP4
- 6-bit: FP6 (E3M2, E2M3)
- 8-bit: FP8 (E4M3, E5M2), INT8

This is critical for Blackwell, which introduces native hardware support for FP4 and FP6 in its 5th generation tensor cores.

## Advanced Features

### Automatic Layout Inference
Tilus includes a comprehensive algebraic layout system that can automatically infer optimal data layouts for tensors, reducing the manual effort required for layout optimization.

### Autotuning
Built-in autotuning capabilities allow parameter optimization (tile sizes, pipeline depths, thread counts) without manual sweep scripts.

### Compilation Pipeline
Tilus programs are compiled into highly efficient GPU programs through:
- Automatic vectorization for memory access
- Instruction selection targeting specific hardware features
- Caching mechanisms to reduce recompilation overhead

### Pythonic Interface
Despite compiling to low-level GPU code, Tilus provides a Python-based interface for kernel authoring, lowering the barrier to entry for GPU programming.

## Architecture-Specific Support

### Blackwell (SM100) Features
- TMA (Tensor Memory Accelerator) loads for asynchronous data movement
- Warp specialization for producer/consumer patterns
- Cluster-level synchronization primitives
- Tensor Memory (TMEM) as a first-class storage level
- Native FP4/FP6 tensor core instruction emission

### Multi-Architecture Support
Tutorials cover both Ampere and Blackwell architectures, demonstrating the portability of the programming model across GPU generations.

## Paper Reference

Published as "Tilus: A Tile-Level GPGPU Programming Language for Low-Precision Computation" at ASPLOS 2026 (arXiv:2504.12984). The paper describes Tilus as a virtual machine for arbitrary low-precision GPGPU computation, with a focus on LLM serving workloads.

## Resources

- **GitHub**: https://github.com/NVIDIA/tilus
- **Documentation**: https://nvidia.github.io/tilus/
- **Paper**: https://arxiv.org/abs/2504.12984
- **ACM**: https://dl.acm.org/doi/10.1145/3760250.3762219
