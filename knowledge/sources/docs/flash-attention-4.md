---
id: doc-flash-attention-4
title: "FlashAttention-4: Hardware-Friendly Attention on Blackwell"
url: https://arxiv.org/abs/2603.05451
source_category: paper
architectures: [sm100]
tags: [attention, flash-attention, tcgen05, tmem, 2sm-cooperative, software-exp, ping-pong-scheduling]
retrieved_at: 2026-04-16
---

## Summary

FlashAttention-4 paper — algorithm-kernel co-design for Blackwell's asymmetric hardware scaling (tensor core throughput doubles but SFU count unchanged).

## Key Contributions

### Forward Pass
- Ping-pong scheduling with two 128-token query tiles per CTA
- Dedicated softmax warpgroups handle S=QK^T accumulator in TMEM
- Software-emulated exponential via Cody-Waite range reduction + Horner polynomial
- Conditional softmax rescaling (only when max jump is large)

### Backward Pass
- 2-CTA backward spanning paired CTAs in a cluster, sharing TMEM
- Halves shared memory traffic and global atomic reductions for dQ

### Implementation
- Written in CuTe-DSL (Python), 20-30x faster compilation than C++ templates

## Performance
- Up to 1605 TFLOPS on B200 BF16 (71% utilization)
- 1.1-1.3x over cuDNN 9.13
- 2.1-2.7x over Triton
