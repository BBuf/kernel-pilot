# provenance: derived from pr-sglang-21339, pr-vllm-23696, blog-deepgemm; not upstream code
# origin: wiki/kernels/fused-moe.md Phase 3 variant

# Fused MoE skeleton: router logits -> top-k expert selection -> grouped
# GEMM dispatch with contiguous M-axis packing.

import torch

def fused_moe_forward(hidden, router_weights, expert_weights_gate,
                      expert_weights_up, expert_weights_down, top_k=2):
    """Reference PyTorch implementation of the dispatch + fused-dual-GEMM path.
    Production kernels (vllm+sglang+DeepGEMM) fuse all three stages."""
    B, L, D = hidden.shape
    logits = hidden @ router_weights.T            # [B, L, E]
    top_vals, top_idx = logits.topk(top_k, dim=-1)
    weights = torch.softmax(top_vals, dim=-1)     # renormalize
    # Scatter tokens to their selected experts (grouped M-axis)
    E = expert_weights_gate.shape[0]
    out = torch.zeros_like(hidden)
    for e in range(E):
        mask = (top_idx == e).any(dim=-1)          # [B, L]
        if not mask.any():
            continue
        x_e = hidden[mask]                          # [Ne, D]
        gate = x_e @ expert_weights_gate[e].T
        up   = x_e @ expert_weights_up[e].T
        y_e  = (torch.nn.functional.silu(gate) * up) @ expert_weights_down[e].T
        # Scatter back, weighted by the routing weight for this expert
        w_e = weights[mask * (top_idx == e).any(dim=-1)[..., None]].sum(dim=-1)
        out[mask] = out[mask] + w_e[:, None] * y_e
    return out
