---
id: blog-tflops-gap-fp4-moe
title: 'TFLOPS Gap: Why FP4 MoE Kernel Engineering Matters on Blackwell'
author: apsys (HuggingFace)
url: https://huggingface.co/blog/apsys/blackwell-nvfp4-comparison
source_category: benchmark-blog
architectures:
- sm100
- sm100a
tags:
- nvfp4
- fp4
- moe
- warp-specialization
- tma
- kernel-fusion
- tile-scheduling
- persistent-kernel
- block-scale
- gemm
- grouped-gemm
- fine-grained-quantization
retrieved_at: 2026-04-17
artifact_dir: evidence/blog-capsules/tflops-gap-fp4-moe/code
---

# TFLOPS Gap: Why FP4 MoE Kernel Engineering Matters on Blackwell

## Overview

A comprehensive benchmark comparing three MoE inference backends (vLLM, SGLang, FlashInfer) running Mixture of Experts models with NVFP4 quantization on NVIDIA Blackwell B200. The analysis reveals a 145 TFLOPS gap between best and worst performers at peak throughput, attributable entirely to kernel engineering differences rather than hardware limitations. Three specific optimization techniques (kernel fusion, Blackwell-specific CUTLASS schedules, adaptive grid sizing) account for the performance delta.

## Benchmark Configuration

- **GPU**: NVIDIA Blackwell B200 (sm_100a), 8 TB/s memory bandwidth
- **Model**: GPT-OSS-20B with 32 experts, top-4 routing, hidden=2880, intermediate=7680
- **Quantization**: NVFP4 (E2M1 format, 4-bit floating point with E4M3 block scales)
- **Benchmark code**: https://github.com/advpropsys/fp4-blackwell-bench

## Performance Results

### Peak Throughput (Batch Size 4096)

| Backend | TFLOPS | vs BF16 |
|---------|--------|---------|
| SGLang FP4 | 1262 | 3.54x |
| FlashInfer FP4 | 1225 | 3.43x |
| vLLM FP4 | 1117 | 3.24x |
| **Gap** | **145 TFLOPS** | **13% advantage** |

### Interactive Inference (Batch Size 1)

| Backend | Latency |
|---------|---------|
| SGLang FP4 | 206.9 us/layer (1.78x faster than vLLM) |
| vLLM FP4 | 369.5 us/layer |
| FlashInfer FP4 | 481.9 us/layer |

### Decode Sweet Spot (Batch Size 128)

SGLang FP4 achieves 0.433 ms/layer (157.1 TFLOPS) vs vLLM FP4 at 0.604 ms/layer (112.6 TFLOPS), a 28.3% speedup translating to 171 seconds saved per 1000 tokens over 24 layers.

## Three Key Optimization Techniques

### 1. Kernel Fusion (21.9% Memory Traffic Reduction)

vLLM uses a sequential 7-kernel pipeline: token reorder, FP4 quantize, gate_up GEMM, SiLU activation, intermediate quantize, down GEMM, output reorder. This incurs 7 kernel launches (5-10 us overhead each), 7 global memory roundtrips, and 6 synchronization points.

SGLang fuses to 5 kernels using a combined shuffle+multiply+sum kernel with 128-bit vectorized loads (8 bfloat16 elements per load), performing token reordering, weight multiplication, and topK reduction in a single global memory pass. Memory traffic drops from 26.5 MB to 20.7 MB at batch size 128.

### 2. Blackwell-Specific CUTLASS Schedules and TMA

SGLang uses the Blackwell-optimized CUTLASS schedule:
```
KernelSchedule = cutlass::gemm::KernelPtrArrayTmaWarpSpecialized1SmNvf4Sm100
ThreadBlockShape = Shape<_128, _128, _128>
```

Key features:
- **Warp Specialization for FP4**: Dedicated warp roles for loading FP4 data, dequantizing to FP16/BF16, and accumulating in FP32
- **TMA Integration**: Asynchronous bulk tensor loads bypassing L1 cache, feeding directly into shared memory with strict 128-byte alignment
- **1 SM Grouping**: Multiple experts processed per SM rather than one-expert-per-SM, better for variable expert sizes
- **Native NvFP4 Support**: Hardware FP4 instructions instead of software emulation

TMA alignment is enforced by padding blockscale offsets to 128-byte boundaries:
```cuda
blockscale_offsets[expert_id + 1] = (expert_offsets[expert_id + 1] + 127) / 128 * 128;
```

### 3. Adaptive Grid Sizing for Small Batches

At batch size 1, B200's 142 SMs are 99.3% underutilized with fixed block sizing. SGLang dynamically halves block size and doubles grid size until SM occupancy is maximized:
```
Initial:     grid=128, block=360
Iteration 1: grid=256, block=180
Iteration 2: grid=256, block=180 (stop, block > 64)
```

## DeepSeek-V3 Variant (256 Experts)

With 256 experts and topK=8 at batch size 4096, FlashInfer leads (1132 TFLOPS) due to its expert-first layout advantages with many experts. The gap between backends shrinks because more experts provide inherent parallelism.

At small batches (BS=1), SGLang maintains advantage (1.47x vs BF16) while vLLM FP4 is actually slower than BF16 (0.86x) due to overhead.

## Backend Comparison Summary

| Metric | SGLang | FlashInfer | vLLM |
|--------|--------|-----------|------|
| Peak TFLOPS (BS=4096) | 1262 | 1225 | 1117 |
| BS=1 Latency | 206.9 us | 481.9 us | 369.5 us |
| Memory Fusion | Yes (5 kernels) | Partial | No (7 kernels) |
| TMA Optimized | Yes | Partial | No |
| Adaptive Grid | Yes | No | No |
| Strength | Small batches | Large expert count | Modularity |

## Key Takeaway

FP4 hardware support is necessary but insufficient. Frameworks achieving 3.54x speedup over BF16 and 1.32x over competitors employ systematic kernel engineering targeting Blackwell-specific features: TMA with strict alignment, warp specialization for FP4 decode, kernel fusion to reduce memory traffic, and adaptive launch heuristics for small batch sizes.
