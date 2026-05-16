---
id: doc-cutile-python-dsl
title: "cuTile Python DSL Reference"
url: https://docs.nvidia.com/cuda/cutile-python/
source_category: official-doc
architectures: [sm100, sm100a]
tags: [cutile, python, gemm, tcgen05, tmem, tma, swizzling]
retrieved_at: 2026-04-17
---

# cuTile Python DSL Reference

## Overview

cuTile (CUDA Tile) is a new Python domain-specific language introduced in CUDA 13.1 for writing tile-based GPU kernels. Described by NVIDIA as "one of the most fundamental additions to GPU programming since CUDA was invented," cuTile operates at a tile-level abstraction where developers specify operations on tile-sized data chunks while the compiler and runtime automatically handle thread partitioning, memory movement, and hardware feature utilization (tensor cores, TMA, shared memory). cuTile supports compute capability 8.x, 10.x (Blackwell), 11.x, and 12.x.

## Architecture

### CUDA Tile IR
cuTile Python builds on CUDA Tile IR, a new virtual instruction set for NVIDIA GPUs that enables high-performance tile-based code generation at a higher level of abstraction than PTX. The compilation pipeline:

1. **Python kernel** (cuTile DSL) -> CUDA Tile IR
2. **CUDA Tile IR** -> optimized GPU code via NVCC
3. Automatic selection of hardware features based on target architecture

### Relationship to Other Frameworks
- **vs CUTLASS/CuTe DSL**: cuTile is higher-level; CuTe DSL provides explicit tensor layout and memory control
- **vs Triton**: Similar tile-level abstraction but cuTile is NVIDIA-native with deeper hardware integration
- **vs JAX Pallas**: Different ecosystem; Pallas targets JAX's functional paradigm

## Core Abstractions

### Arrays
Arrays reside in global memory with physical, strided layouts. They support a limited set of operations, primarily loading and storing data to/from tiles:
- Represent tensors in GPU global memory (HBM)
- Physical layout with explicit strides
- Source/destination for tile load/store operations

### Tiles
Tiles are immutable compile-time values restricted to power-of-two dimensions. They support a comprehensive set of operations:
- Elementwise arithmetic (add, multiply, etc.)
- Matrix multiplication (matmul)
- Reduction (sum, max, etc.)
- Scan operations
- Shape manipulation
- Atomic operations

Key constraint: tile dimensions must be powers of two, enabling efficient hardware mapping.

## Kernel Programming Model

### Kernel Definition
Kernels are marked with the `@ct.kernel` decorator and execute on a logical grid of blocks:

```python
@ct.kernel
def vector_add(a, b, c, tile_size: ct.Constant[int]):
    pid = ct.bid(0)  # Block ID in dimension 0
    a_tile = ct.load(a, index=(pid,), shape=(tile_size,))
    b_tile = ct.load(b, index=(pid,), shape=(tile_size,))
    result = a_tile + b_tile
    ct.store(c, index=(pid,), tile=result)
```

### Key Functions
- `ct.bid(dim)`: Get block identifier in specified dimension
- `ct.load(array, index, shape)`: Load a tile from global memory
- `ct.store(array, index, tile)`: Store a tile to global memory
- Standard arithmetic operators work on tiles

### Execution Model
The runtime automatically determines:
- Thread block size (based on tile dimensions and hardware)
- Memory movement strategy (direct load, TMA, shared memory staging)
- Hardware feature utilization (tensor cores for matmul tiles)

## Hardware Feature Automation

cuTile automatically leverages architecture-specific features without explicit programmer intervention:

### For Blackwell (SM100)
- **Tensor Cores**: Matrix multiplication operations on tiles automatically use tcgen05 instructions
- **TMA (Tensor Memory Accelerator)**: Bulk data movement operations use TMA when beneficial
- **Shared Memory**: Intermediate data staging uses shared memory with automatic swizzling
- **Tensor Memory (TMEM)**: Accumulator storage may use TMEM for tcgen05 operations

### Cross-Architecture Portability
The same cuTile kernel can target multiple architectures:
- Compute capability 8.x (Ampere): Uses Ampere tensor cores and async copy
- Compute capability 10.x (Blackwell): Uses tcgen05, TMA, TMEM
- Compute capability 12.x: Future architecture support

## Profiling and Debugging

NVIDIA Nsight Compute provides cuTile-specific profiling:
- **Tile Statistics**: Reports tile block counts and compiler-selected block sizes
- **Source-Level Metrics**: Performance data correlated to cuTile source lines
- Requires R590 driver or newer for tile-specific profiling features

## System Requirements

- **CUDA Toolkit**: 13.1 or later
- **Driver**: R580 minimum (R590 for tile profiling)
- **Supported GPUs**: Compute capability 8.x, 10.x, 11.x, 12.x
- **Python**: Python interface with JIT compilation

## Resources

- **Official documentation**: https://docs.nvidia.com/cuda/cutile-python/
- **GitHub**: https://github.com/NVIDIA/cutile-python
- **CUDA 13.1 quickstart**: https://docs.nvidia.com/cuda/archive/13.1.0/cutile-python/quickstart.html
- **Blog post**: https://developer.nvidia.com/blog/simplify-gpu-programming-with-nvidia-cuda-tile-in-python/
- **CUDA 13.1 overview**: https://developer.nvidia.com/blog/nvidia-cuda-13-1-powers-next-gen-gpu-programming-with-nvidia-cuda-tile-and-performance-gains/
