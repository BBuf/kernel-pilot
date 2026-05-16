---
id: blog-gated-delta-net
title: Gated Delta Networks
author: NVlabs
url: https://github.com/NVlabs/GatedDeltaNet
source_category: benchmark-blog
architectures:
- sm90
- sm100
tags:
- gated-delta-net
- linear-attention
- attention
- triton
- chunk-parallelism
retrieved_at: 2026-04-16
artifact_dir: evidence/blog-capsules/gated-delta-net/code
---

## Summary

Linear attention mechanism with delta rule for intelligent memory management (ICLR 2025). Used in Qwen3-Next (3:1 hybrid ratio).

## Architecture
- Delta rule: targeted state updates (keep/forget)
- Exponential gating: adaptive memory decay
- Causal Conv1D for local context
- Fixed-size 128×128 state matrix (independent of sequence length)
- O(n) complexity vs O(n²) for standard attention

## Implementations
- NVlabs reference: Triton kernels
- FLA optimized: recommended, significantly faster, varlen support
- Chunk-based parallelism for prefill, streaming for decode

## Adoption
- Qwen3-Next-80B (3:1 GDN:attention ratio, 512 experts)
- Qwen3.5 (262K context, 10x+ throughput over Qwen3-32B at 32K+)

## Key Code

### Chunk-parallel prefill reference (PyTorch)

```python
import torch

def gated_delta_net_prefill(q, k, v, gate, initial_state, CHUNK_SIZE=64):
    """
    Chunk-parallel prefill. Each chunk's state matrix is reused across its
    query window, so we pay the O(Dk*Dv) state update once per chunk, not
    per token.
    q, k: [B, L, Dk]    v: [B, L, Dv]    gate: [B, L]
    """
    B, L, Dk = q.shape
    Dv = v.shape[-1]
    out = torch.empty(B, L, Dv, device=q.device, dtype=q.dtype)
    state = initial_state.clone()                  # [B, Dk, Dv]
    for ci in range(0, L, CHUNK_SIZE):
        ce = min(ci + CHUNK_SIZE, L)
        k_chunk = k[:, ci:ce]
        v_chunk = v[:, ci:ce]
        g_chunk = gate[:, ci:ce]
        decay = torch.cumprod(g_chunk, dim=1)       # adaptive memory decay
        for t in range(ce - ci):
            state = state * decay[:, t:t+1, None]
            state = state + k_chunk[:, t, :, None] * v_chunk[:, t, None, :]
            out[:, ci + t] = (q[:, ci + t, :, None] * state).sum(dim=1)
    return out, state
```

### Triton decode-step kernel (streaming)

```python
import triton
import triton.language as tl

@triton.jit
def gdn_decode_step_kernel(
    Q, K, V, GATE, STATE, OUT,
    stride_qb, stride_kb, stride_vb,
    Dk: tl.constexpr, Dv: tl.constexpr):
    """
    One-token delta-rule update for decode. STATE is a [Dk, Dv] matrix kept
    per sample; we fold in the new (k,v) pair after applying the decay gate.
    """
    b = tl.program_id(0)
    dk = tl.arange(0, Dk)
    dv = tl.arange(0, Dv)

    q = tl.load(Q + b * stride_qb + dk)                          # [Dk]
    k = tl.load(K + b * stride_kb + dk)                          # [Dk]
    v = tl.load(V + b * stride_vb + dv)                          # [Dv]
    g = tl.load(GATE + b)                                        # scalar decay

    state = tl.load(STATE + b * Dk * Dv + dk[:, None] * Dv + dv[None, :])
    state = state * g                                             # apply decay
    state = state + k[:, None] * v[None, :]                       # delta update
    tl.store(STATE + b * Dk * Dv + dk[:, None] * Dv + dv[None, :], state)

    out = tl.sum(q[:, None] * state, axis=0)                      # [Dv]
    tl.store(OUT + b * Dv + dv, out)
```
