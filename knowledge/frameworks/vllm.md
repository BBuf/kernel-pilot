# vLLM

Repository: <https://github.com/vllm-project/vllm>

Deep reference: `knowledge/references/frameworks/vllm.md`

vLLM is one of the largest production LLM-serving codebases. Its kernels are
written either by the vLLM team or upstreamed from FlashInfer / FlashAttention /
xFormers, then wrapped with paged-attention bookkeeping.

## Where the kernels live

| Directory | What you find there |
| --- | --- |
| `csrc/attention/` | Paged-attention v1/v2 kernels, prefix-cache aware variants. |
| `csrc/moe/` | Top-k softmax, fused MoE GEMM glue, marlin variants. |
| `csrc/quantization/` | AWQ, GPTQ, marlin, fp8, machete, smoothquant kernels. |
| `csrc/cutlass_extensions/` | CUTLASS epilogue and tile selection helpers. |
| `csrc/cache_kernels.cu` | KV-cache reshape, copy, swap kernels (PagedKV layout). |
| `vllm/attention/` | Backend-selection layer for FlashAttention, FlashInfer, xFormers, Triton. |
| `vllm/model_executor/layers/` | Python-side fused norms, activations, embedding. |

## Optimization patterns documented here

- **PagedAttention v2**: split-K over the sequence axis with on-the-fly online
  softmax reduction. The two-pass design is the reference for any new paged
  attention kernel.
- **AWQ / GPTQ kernels**: per-group dequant fused inside the GEMM epilogue;
  read the `marlin` and `machete` variants for two different design choices
  on small-batch decode.
- **PagedKV layout**: `csrc/cache_kernels.cu` contains the canonical block-table
  + offset scheme used by most LLM-serving frameworks.
- **Pluggable backend dispatcher**: `vllm/attention/backends/` is the cleanest
  example of how to dispatch by hardware, dtype, and head-dim. Reuse the
  pattern when adding a new attention kernel.

## Common pitfalls

- Older `paged_attention_v1` kernels remain in the tree for low-batch decode
  even though `v2` is preferred for prefill; always check which variant the
  caller actually selects.
- vLLM has multiple **redundant** AWQ kernels (`marlin`, `marlin_24`, `awq`).
  Confirm which one is the active baseline before benchmarking.
- FP8 paths are split across `csrc/quantization/fp8/` and CUTLASS epilogues;
  they assume per-tensor scaling unless explicitly per-channel.

## When to read this framework

- You are designing a paged-attention variant, an AWQ/GPTQ kernel, or
  a backend-selection layer for a new attention kernel.
- You need a reference for the **block-table** layout used by KV-cache.

## When NOT to copy

- Quant kernel bodies (`marlin`, `machete`, etc.) and paged-attention kernels
  are out-of-bounds for direct copy. They are excellent for hypothesis-building
  and for comparing tile shapes / epilogue layouts.

## Recommended ncu metrics for vLLM kernels

- Paged attention: `l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum.per_second`,
  `smsp__inst_executed_pipe_tensor`, `sm__warps_active`.
- AWQ/GPTQ decode: `smsp__warp_issue_stalled_lg_throttle`, `dram__throughput`,
  `lts__t_bytes`.
