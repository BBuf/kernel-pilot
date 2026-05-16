---
id: blog-flash-attention-4
title: FlashAttention-4 Blog
author: Tri Dao
url: https://tridao.me/blog/2026/flash4/
source_category: benchmark-blog
architectures:
- sm100
tags:
- attention
- flash-attention
- tcgen05
- tmem
- 2sm-cooperative
- software-exp
- ping-pong-scheduling
- conditional-rescaling
- cute-dsl
retrieved_at: 2026-04-27
artifact_dir: evidence/blog-capsules/flash-attention-4/code
---

## Summary

Tri Dao's blog post on FlashAttention-4 design for Blackwell's asymmetric hardware scaling.

## Key Techniques
- Asymmetric problem: tensor core throughput doubles but SFU count and SMEM bandwidth unchanged
- Ping-pong scheduling: two 128-token query tiles per CTA
- Software 2^x: Cody-Waite range reduction + Horner polynomial (Sollya-optimized coefficients)
- Multiplies exponential throughput without additional SFU hardware
- Conditional softmax rescaling: only when max jump is large
- 2-CTA backward: paired CTAs share TMEM, halves SMEM traffic
- CuTe-DSL implementation: 20-30x faster compilation than C++ templates

## Performance
- 1605 TFLOPS on B200 BF16 (71% utilization)
- 1.1-1.3x over cuDNN 9.13, 2.1-2.7x over Triton

## Key Code

### Software exp (Cody-Waite + Horner)

```cuda
// Software-emulated exp2(x) using Cody-Waite range reduction and a
// Horner-scheme polynomial, Sollya-optimized coefficients. Lets FA-4
// overlap the exp path with tcgen05.mma because it stays off the SFU.
__device__ __forceinline__ float sw_exp2(float x) {
    // Range reduction: x = n + r, with n = round(x), r in [-0.5, 0.5]
    int n = __float2int_rn(x);
    float r = x - (float)n;
    // Horner-scheme polynomial for 2^r, r in [-0.5, 0.5]
    float p = 0x1.62e430p-1f;                // ~ ln(2)
    p = fmaf(p, r, 0x1.ebfc1ep-3f);
    p = fmaf(p, r, 0x1.c6af98p-5f);
    p = fmaf(p, r, 0x1.3b2c9cp-7f);
    p = fmaf(p, r, 0x1.62e43ap-10f);
    float y = fmaf(r, p, 1.0f);
    // Scale by 2^n via direct FP32 bit manipulation
    int bits = __float_as_int(y) + (n << 23);
    return __int_as_float(bits);
}
```

### Ping-pong scheduling

<!-- extract-skip: synthesized pseudo-code illustrating the scheduling concept (issue_mma, wait_mma, softmax_and_rescale are placeholders, not upstream functions). Not safe to publish under evidence/blog-capsules/** as mode=extracted. -->
```cuda
// Ping-pong two 128-token query tiles per CTA. While one tile is in the
// softmax/rescale stage, the other issues tcgen05.mma — the 2x tensor-core
// throughput on B200 gets fed while the SFU-bound softmax stays out of the
// critical path.
for (int tile = 0; tile < Q_tiles; tile += 2) {
    issue_mma(query_a, key_block);
    wait_mma();
    softmax_and_rescale(query_a);           // SFU + MUFU path
    issue_mma(query_b, key_block);
    wait_mma();
    softmax_and_rescale(query_b);
}
```

### 2-CTA cooperative backward

```cuda
// 2-CTA cooperative backward: paired CTAs in a cluster share a single TMEM
// accumulator half, halving SMEM traffic for dK/dV accumulation.
asm volatile(
    "tcgen05.mma.cta_group::2.kind::f16 [%0], %1, %2, %3, 1;"
    : : "r"(tmem_acc_shared), "l"(desc_a), "l"(desc_b), "r"(0));
```
