---
id: blog-blackwell-microbenchmarking
title: "Microbenchmarking NVIDIA's Blackwell Architecture"
author: Aaron Jarmusch et al.
url: https://arxiv.org/abs/2512.02189
source_category: benchmark-blog
architectures: [sm100, sm100a]
tags: [tcgen05, tmem, fp4, fp8, fp6, gemm, wgmma, cluster, 2sm-cooperative]
retrieved_at: 2026-04-17
---

# Microbenchmarking NVIDIA's Blackwell Architecture

## Overview

Two complementary papers systematically microbenchmark the NVIDIA Blackwell architecture. The primary paper (arXiv 2512.02189, Jarmusch et al.) provides an in-depth B200 datacenter GPU analysis including memory subsystem, tensor core pipeline, decompression engine, and real-world workload benchmarks versus H200. A companion paper (arXiv 2507.10789, Jarmusch, Graddon, Chandrasekaran) focuses on the consumer RTX 5080 vs H100 PCIe, emphasizing FP4/FP6 tensor core behavior. Together they form the most comprehensive public architectural characterization of Blackwell.

## B200 Architecture Specifications

- **Die configuration**: Dual-die, 208 billion transistors
- **SM count**: 148 Streaming Multiprocessors across 8 GPCs
- **L2 cache**: Four partitions (doubled from Hopper's two)
- **Memory**: Unified 192 GB HBM3e across eight stacks
- **Interconnect**: NVIDIA High-Bandwidth Interface (NV-HBI) connecting dies

## Tensor Memory (TMEM)

- **Capacity**: 256 KB on-chip memory per SM
- **Structure**: 2D array of 512 columns by 128 lanes of 32-bit cells
- **Bandwidth**: ~16 TB/s read performance
- **Optimal tile size**: 64x64 elements (4 KB for FP8)

## Memory Subsystem

### L2 Cache Hit Rates
- FP16 workloads: 68% hit rate
- FP4 workloads: 84% hit rate (lower data volume benefits caching)

### Memory Bandwidth (STREAM Triad)
- B200 theoretical peak: 8 TB/s
- Measured sustainable: ~4.14 TB/s at 4-16 GB working sets (51.8% utilization)

## 5th Generation Tensor Core Performance (tcgen05)

### Instruction Latency Comparison
| Instruction | Latency (cycles) |
|---|---|
| wgmma (Hopper m64n64k16) | 32.0 |
| tcgen05.mma (B200 m64n64k16) | 11.0 |
| tcgen05.mma (B200 m128n128k16) | 11.3 |
| tcgen05.mma (B200 m256n256k16) | 11.4 |

The tcgen05 instruction achieves ~3x lower latency than Hopper's wgmma at the same tile size, with minimal latency increase for larger tiles.

### Throughput by Precision

| Precision | TFLOPS/TOPS | % Peak |
|-----------|-------------|--------|
| FP64 | 44.8 | 99.6% |
| FP32 | 482.0 | 96.4% |
| BF16 | 1,926.4 | 96.3% |
| FP16 | 1,929.6 | 96.5% |
| FP8 | 3,850.6 | 96.3% |
| FP6 | 5,134.4 | 96.0% |
| FP4 | 7,700.2 | 96.2% |
| INT8 | 3,928.5 | 98.2% |

All precisions achieve >96% of theoretical peak throughput in microbenchmarks.

### Architecture Changes from Hopper
- **Execution model**: Shifted from warp-group (128-thread wgmma) to warp-level (32-thread tcgen05.mma) synchronization
- **CTA pair scheduling**: Adjacent Cooperative Thread Arrays share operands via dedicated intra-TPC communication
- **New precisions**: FP4 (E2M1) and FP6 (E3M2/E2M3) with 1 sign bit
- **Limitation**: tcgen05.mma does not support FP64; FP64 uses separate doubled DMMA units

## Decompression Engine (DE)

Blackwell introduces a hardware decompression engine. Format-specific throughput on 100 MB datasets with 64 KB chunks:

| Format | Throughput (GB/s) | Latency (ms) |
|--------|-------------------|---------------|
| ANS | 539.21 | 0.194 |
| Bitcomp | 462.37 | 0.227 |
| Cascaded | 213.42 | 0.491 |
| LZ4 | 172.55 | 0.608 |
| Zstandard | 154.94 | 0.677 |
| Snappy | 117.24 | 0.894 |
| GZIP | 83.83 | 1.251 |

## B200 vs H200 Performance Comparison

### GEMM Speedups
- FP16: 1.27x
- FP8: 1.27x
- FP64: 1.32x
- INT8: 1.27x

### Real-World Workloads
- Mistral-7B inference (FP16): 1.97x
- Mistral-7B inference (FP8): 1.16x
- Mixtral-8x7B inference (FP8): 1.58x
- ResNet-50 training: 1.85x
- GPT-1.3B mixed-precision training: 1.55x
- Energy efficiency improvement: 32% better than H200

## Companion Paper (2507.10789): RTX 5080 Analysis

The companion paper by Jarmusch, Graddon, and Chandrasekaran focuses on the consumer GeForce RTX 5080 (SM120) vs H100 PCIe, examining:
- Memory hierarchy (latency, cache sizes, bandwidth)
- SM execution pipelines
- SM sub-core units and 5th generation tensor cores
- FP4 and FP6 precision behavior and performance
- Scheduling details revealing subtle tuning metrics

## Key Insights for Kernel Developers

1. **tcgen05 latency advantage**: 3x lower instruction latency enables better pipelining
2. **TMEM is critical**: 256 KB per SM at 16 TB/s bandwidth makes it essential for high-performance kernels
3. **FP4 cache efficiency**: 84% L2 hit rate vs 68% for FP16 means FP4 kernels benefit more from caching
4. **Memory bandwidth gap**: Only 51.8% of theoretical bandwidth is sustainable, making compute-bound kernels more important
5. **All precisions near peak**: >96% utilization means the bottleneck is data movement, not compute
