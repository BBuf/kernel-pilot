---
id: blog-flashmla
title: FlashMLA — Multi-head Latent Attention
author: DeepSeek AI
url: https://github.com/deepseek-ai/FlashMLA
source_category: benchmark-blog
architectures:
- sm100
- sm90
tags:
- mla
- attention
- decode
- prefill
- fp8
- sparse-attention
- tcgen05
- tmem
retrieved_at: 2026-04-27
artifact_dir: evidence/blog-capsules/flashmla/code
---

## Summary

DeepSeek's efficient MLA kernels for V3/V3.2 with massive KV cache compression (70KB/token).

## Variants
- Dense MLA decoding (SM90): BF16, paged KV (block 64), 3000 GB/s, 660 TFLOPS on H800
- Sparse MLA decoding (SM90/SM100): FP8 KV, token-level sparsity, 410 TFLOPS H800, 350 TFLOPS B200
- Dense prefill (SM100): 1460 TFLOPS fwd, 1000 TFLOPS bwd on B200
- Sparse prefill (SM90/SM100): 640 TFLOPS H800, 1450 TFLOPS B200

## Token Format
656 bytes/token: 512B FP8 data + 16B FP32 scales + 128B BF16 RoPE embeddings

## Key Code

### MLA decode inner loop

```cuda
// MLA collapses K and V into a shared latent matrix of head-dim Dc=128.
// On decode (one query vector against N KV tokens) we alternate TMA load,
// wgmma/tcgen05 into the q@K^T accumulator, online softmax, and the second
// accumulator against V.
constexpr int Dc = 128;              // latent head dim
constexpr int BLOCK_N = 64;          // paged KV block size
float acc[Dc] = {0};
float max_val = -INFINITY;
float l = 0.f;
for (int n0 = 0; n0 < seqlen; n0 += BLOCK_N) {
    tma_load(smem_kv, KV_pages + n0);
    cp_async_wait();
    float scores[BLOCK_N];
    wgmma_or_tcgen05_mma(scores, q, smem_kv);       // q @ K^T
    float new_max = warp_reduce_max(scores, BLOCK_N);
    float scale = expf(max_val - new_max);
    for (int j = 0; j < Dc; j++) acc[j] *= scale;
    l *= scale;
    for (int j = 0; j < BLOCK_N; j++) {
        float p = expf(scores[j] - new_max);
        l += p;
        for (int d = 0; d < Dc; d++) acc[d] += p * smem_kv[j * Dc + d];
    }
    max_val = new_max;
}
for (int d = 0; d < Dc; d++) O[d] = acc[d] / l;
```

### Sparse-MLA KV-retrieval kernel (V3.2)

```cuda
// Sparse MLA selects top-k KV positions per query before running the dense
// MLA kernel on just those positions. Retrieval uses FP8 dot products with
// per-token scale factors.
__global__ void sparse_mla_topk(
    const __nv_fp8_e4m3* Q, const __nv_fp8_e4m3* K,
    const float* Q_scale, const float* K_scale,
    int* topk_idx, float* topk_score,
    int N, int K_DIM, int TOPK)
{
    int q_tile = blockIdx.x;
    float scores[N];
    for (int n = 0; n < N; n++) {
        float s = 0.f;
        for (int k = 0; k < K_DIM; k++) {
            s += decode_fp8(Q[q_tile * K_DIM + k]) * Q_scale[q_tile]
               * decode_fp8(K[n * K_DIM + k]) * K_scale[n];
        }
        scores[n] = s;
    }
    warp_topk_select(scores, N, topk_idx + q_tile * TOPK,
                     topk_score + q_tile * TOPK, TOPK);
}
```
