---
id: contest-gpumode-p3
title: 'GPU Mode NVFP4 Hackathon - Problem 3: Gated Dual GEMM'
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
- kernel-fusion
- epilogue-fusion
- pipeline-stages
hardware_features:
- nvfp4
- fp4
- block-scale
- tcgen05
- tmem
- tma
kernel_types:
- gated-dual-gemm
- gemm
- fused-kernel
languages:
- cuda-cpp
- ptx
- cute-dsl
url: https://github.com/gpu-mode/reference-kernels
submissions:
- rank: 1
  participant: Simon (veitner)
  score: ~19us geomean
  technique: Fused dual GEMM with shared A tile, epilogue SiLU fusion, dual TMEM accumulator
    layout, CUTLASS SM100 schedule
  submission_truth: unavailable
  code_unavailable_reason: Simon's gated-dual-GEMM winning submission posted in the
    GPU Mode Discord problem-3 thread; not republished publicly
- rank: 2
  participant: yue
  score: ~19.5us geomean
  technique: CUTLASS warp-specialized dual GEMM with TMA pipeline overlap for W_gate
    and W_up streams
  submission_truth: unavailable
  code_unavailable_reason: Yue's gated-dual-GEMM submission posted in the GPU Mode
    Discord problem-3 thread; blog covers problem-1 progression, not this problem
- rank: 3
  participant: currybab
  score: ~20us geomean
  technique: Epilogue-fused SiLU + element-wise multiply, shared input tiling across
    both GEMMs
  submission_truth: unavailable
  code_unavailable_reason: currybab's gated-dual-GEMM submission posted in the GPU
    Mode Discord problem-3 thread; no public republish at collection time
---

# Problem 3: NVFP4 Gated Dual GEMM

## Problem Description

Fused gated dual GEMM implementing the standard MLP gate-up pattern found in modern LLMs (e.g., LLaMA, DeepSeek, Qwen):

```
gate = A @ W_gate    // First GEMM
up   = A @ W_up      // Second GEMM
out  = SiLU(gate) * up  // Activation + element-wise multiply
```

Both GEMMs use NVFP4 (E2M1) block-scaled inputs on B200 GPUs. The challenge is fusing the two GEMMs with the SiLU activation and element-wise multiply into a single kernel launch.

**Nature**: Compute-bound (two full GEMMs), with fusion opportunity in the epilogue.

## Timeline

December 20, 2025 -- January 16, 2026. Third problem, weighted 30% for grand prize.

## Optimization Techniques

### Kernel Fusion Strategy

The naive approach requires 3 kernel launches:
1. GEMM for gate projection
2. GEMM for up projection
3. Element-wise SiLU(gate) * up

The fused approach combines all three into a single kernel:

```
// Fused approach: single kernel, shared input tiles
// 1. Load A tile from SMEM (shared between both GEMMs)
// 2. Load W_gate tile -> compute partial gate accumulator
// 3. Load W_up tile -> compute partial up accumulator
// 4. In epilogue: apply SiLU to gate, multiply with up, write output
```

Key benefit: Input matrix A is loaded once from HBM and reused for both GEMMs, cutting global memory traffic for A in half.

### Epilogue Fusion

The SiLU activation and element-wise multiply are fused into the GEMM epilogue:

```cpp
// SiLU(x) = x * sigmoid(x) = x / (1 + exp(-x))
// Applied to gate GEMM output, then multiplied with up GEMM output

// In CUTLASS epilogue visitor:
struct SiLUGateFusion {
    template <typename AccumTile>
    __device__ auto operator()(AccumTile const& gate_acc, AccumTile const& up_acc) {
        auto gate_f32 = convert<float>(gate_acc);
        auto up_f32 = convert<float>(up_acc);
        // SiLU + element-wise multiply
        return gate_f32 * sigmoid(gate_f32) * up_f32;
    }
};
```

### Dual Accumulator Management in TMEM

Both GEMM accumulators must fit in TMEM simultaneously:

- TMEM capacity: 128 rows x 512 columns x 32-bit per SM
- Gate accumulator: occupies one region of TMEM
- Up accumulator: occupies adjacent region
- Careful tile sizing to fit both without spilling

```
// TMEM layout for dual GEMM:
// [0, 255]   columns: gate accumulator
// [256, 511] columns: up accumulator
// Both share the same 128 rows
```

### Warp Specialization for Dual GEMM

Extended warp specialization with separate pipelines for each GEMM's weight loads:

- **TMA warp group 1**: Loads A tiles + W_gate tiles
- **TMA warp group 2**: Loads W_up tiles (A tiles shared)
- **Compute warps**: Execute tcgen05.mma for both GEMMs
- **Epilogue warps**: Fused SiLU + multiply + FP16 output

### Pipeline Scheduling

Multi-stage software pipeline handles both weight streams:

```
// Stage N:   TMA loads A[n], W_gate[n], W_up[n]
// Stage N-1: tcgen05.mma on A[n-1] * W_gate[n-1], A[n-1] * W_up[n-1]
// Stage N-2: Epilogue fusion on completed tiles
```

The shared A tile across both GEMMs means only 3 TMA streams (A, W_gate, W_up) instead of 4 (A_gate, W_gate, A_up, W_up).

## Relevance to LLM Inference

This pattern appears in every transformer MLP block using gated activations:
- **LLaMA/LLaMA-2/LLaMA-3**: SwiGLU MLP (gate + up projections)
- **DeepSeek-V3**: Same gated MLP structure in each expert
- **Qwen-3**: SwiGLU in both dense and MoE variants
- **Mistral/Mixtral**: Gated MLP in every layer

Fusing the dual GEMM reduces kernel launch overhead and halves the A matrix memory traffic, making it essential for inference latency optimization.

## CUTLASS Schedule

Top performers used CUTLASS 4.x with the SM100 NVFP4 schedule:

```cpp
using KernelSchedule = cutlass::gemm::KernelPtrArrayTmaWarpSpecialized1SmNvf4Sm100;

// The dual GEMM is composed as two CUTLASS GEMMs with shared input
// and a fused epilogue visitor
```

## Sources

- [gpu-mode/reference-kernels](https://github.com/gpu-mode/reference-kernels) (`/problems/nvidia/nvfp4_dual_gemm/`, `/problems/nvidia/modal_nvfp4_dual_gemm/`)
- [GPU MODE Hackathon (Luma)](https://luma.com/9n27uem4)
- [NVIDIA Forums Announcement](https://forums.developer.nvidia.com/t/join-us-for-the-blackwell-nvfp4-kernel-hackathon-with-nvidia-and-gpu-mode/350092)
