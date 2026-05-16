---
id: blog-deepgemm
title: DeepGEMM — FP8 GEMM Library
author: DeepSeek AI
url: https://github.com/deepseek-ai/DeepGEMM
source_category: benchmark-blog
architectures:
- sm100
- sm90
tags:
- gemm
- fp8
- fine-grained-quantization
- block-scale
- jit-compilation
- tcgen05
- wgmma
retrieved_at: 2026-04-16
artifact_dir: evidence/blog-capsules/deepgemm/code
---

## Summary

DeepSeek's high-performance FP8 GEMM library with fine-grained scaling, supporting both Hopper and Blackwell.

## Key Techniques
- Fine-grained quantization: tile-wise 1×128 activations, block-wise 128×128 weights
- SM90: WGMMA with Nc=128 CUDA core promotion (FP22→FP32)
- SM100: tcgen05.mma with TMEM, packed UE8M0 scale format, all memory layouts
- MoE grouped GEMMs: M-axis grouping, contiguous/masked/K-grouped layouts
- JIT compilation via NVRTC
- ~300 lines core kernel code
- Up to 1550 TFLOPS on H800

## Key Code

### Nc=128 CUDA-core promotion (Hopper SM90)

```cpp
// On Hopper, the TC accumulator is only ~FP22-precise. DeepGEMM promotes
// the partial sum to an FP32 CUDA-core accumulator every Nc=128 columns
// (4 consecutive WGMMAs of n=32 each) to avoid precision drift.
constexpr int Nc = 128;
constexpr int WGMMA_N = 32;

float cuda_core_acc[TILE_M][TILE_N] = {0};

for (int k = 0; k < K; k += Nc) {
    __half2 tc_acc[TILE_M][WGMMA_N];
    memset(tc_acc, 0, sizeof(tc_acc));
    for (int sub_k = 0; sub_k < Nc; sub_k += WGMMA_K) {
        wgmma_mma_async(tc_acc, A_smem + sub_k, B_smem + sub_k);
    }
    wgmma_wait();
    for (int m = 0; m < TILE_M; m++)
        for (int n = 0; n < TILE_N; n++)
            cuda_core_acc[m][n] += (float)tc_acc[m][n] * scale_a[m] * scale_b[n];
}
```

### SM100 path — tcgen05.mma with UE8M0 block scaling

```cpp
// On Blackwell, tcgen05.mma consumes UE8M0 scale factors directly.
// 4 UE8M0 values pack into a single uint32; TMEM accumulates in full FP32
// precision so no CUDA-core promotion is needed.
uint32_t packed_scales = pack_ue8m0(sf[0], sf[1], sf[2], sf[3]);
asm volatile(
    "tcgen05.mma.cta_group::1.kind::f8f6f4.block_scale "
    "[%0], %1, %2, [%3], %4, 1;\n"
    :: "r"(tmem_acc), "l"(desc_a), "l"(desc_b),
       "r"(sf_tmem_addr), "r"(0));
```

### MoE grouped-GEMM launch

```cpp
// Grouped-GEMM packs a variable list of per-expert GEMMs into one kernel
// launch via a prefix-sum offset array; layouts are contiguous (M-axis),
// masked (variable-K), or K-grouped depending on router output.
struct GroupedGemmArgs {
    int num_groups;
    int* m_prefix;                    // [num_groups+1]
    const __nv_fp8_e4m3* A;
    const __nv_fp8_e4m3* B;
    const float* scales_a;
    const float* scales_b;
    __half* C;
    int N, K;
};

__global__ void grouped_gemm_launch(GroupedGemmArgs args) {
    int group = blockIdx.y;
    int m_start = args.m_prefix[group];
    int m_end   = args.m_prefix[group + 1];
    // Dispatch a standard tile-level GEMM for [m_start, m_end) × N × K.
}
```
