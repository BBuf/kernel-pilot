# Topic: Mixture of Experts (MoE)

## What it covers

MoE kernels: top-k routing, `moe_align_block_size`, permute / unpermute,
grouped GEMM, fused activation, expert-parallel comm.

## Per-framework references

| Framework | Where to look | What it teaches |
| --- | --- | --- |
| `sglang` | `sgl-kernel/csrc/moe/`, `python/sglang/srt/layers/moe/` | `moe_align_block_size`, FP8-aware grouped GEMM, fused silu_and_mul, FP4 paths. |
| `tensorrt-llm` | `cpp/tensorrt_llm/kernels/mixtureOfExperts/` | NVIDIA's permute + grouped GEMM + activation reference. |
| `vllm` | `csrc/moe/`, `vllm/model_executor/layers/fused_moe/` | Triton fused-MoE with Marlin / AWQ variants. |
| `deepgemm` | `csrc/apis/m_grouped_gemm_*` | FP8 grouped GEMM reference for MoE. |
| `triton` | `python/tutorials/` + community kernels | Triton block-pointer fused-MoE templates. |

## Common optimization patterns

- **`moe_align_block_size`**: sort tokens by expert and pad each expert's
  block to a fixed BLOCK_SIZE so the grouped GEMM has aligned tiles. Compute
  the permutation map without a global sort by using a cumulative-sum trick.
- **Grouped GEMM**: concatenate per-expert GEMMs along M with a
  `group_offsets` array; the kernel iterates per group.
- **Fused activation in epilogue**: silu / swiglu / gelu fused into the
  grouped GEMM epilogue.
- **Expert-parallel routing**: combine `top-k` routing with all-to-all
  bookkeeping; overlap comm with intermediate GEMM.

## Common bottlenecks

- Permute / unpermute are gather-heavy and often hit shared-memory bank
  conflicts.
- Tail batches: when one expert receives many more tokens than the others,
  SMs become idle.
- Top-k softmax on the routing logits can be a surprising bottleneck for
  large expert counts.

## Recommended ncu metrics

- `l1tex__data_bank_conflicts_pipe_lsu.sum`
- `smsp__average_warp_latency_per_inst_executed`
- `sm__warps_eligible.avg.per_cycle_active`
- `dram__throughput.avg.pct_of_peak_sustained_elapsed`
- `sm__inst_executed_pipe_tensor.avg.pct_of_peak_sustained_elapsed` (grouped GEMM)
