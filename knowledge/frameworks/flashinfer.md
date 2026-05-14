# FlashInfer

Repository: <https://github.com/flashinfer-ai/flashinfer>

Deep reference: `knowledge/references/frameworks/flashinfer.md`

FlashInfer is the kernel library most LLM-serving stacks (SGLang, vLLM, MLC)
adopt for **paged attention**, **prefix-cache aware attention**, **MLA**, and
**sampling**. Its codebase is the cleanest open reference for paged KV with
flexible block sizes and head groupings.

## Where the kernels live

| Directory | What you find there |
| --- | --- |
| `include/flashinfer/` | Header-only kernels (paged attention, prefix attention, sampling, MLA, FMHA). |
| `csrc/` | PyTorch C++ extensions that bind the headers. |
| `csrc/fmha_v2/fmha/` | FMHA v2 kernels. |
| `csrc/fmha_v2/fmha/hopper/` | Hopper-specific FMHA (TMA + WGMMA). |
| `csrc/fmha_v2/fmha/warpspec/` | Warp-specialized FMHA variants. |
| `benchmarks/bench_blackwell_attention.py` | Blackwell-specific attention benchmark. |
| `python/flashinfer/` | Python wrappers, `BatchPrefillWithPagedKVCacheWrapper`, sampling APIs. |

## Optimization patterns documented here

- **Paged KV with variable block sizes**: flexible page table that supports
  arbitrary block lengths per request. Reference for any new paged-attention
  design.
- **Prefix-cache aware kernels**: separate "shared prefix" and "unique
  suffix" KV passes; reduces redundant loads when many requests share a
  system prompt.
- **MLA (DeepSeek)**: explicit latent-attention path with KV-projection
  fusion; clean reference for low-rank-K attention.
- **Sampling primitives**: top-k / top-p / min-p / temperature sampling
  kernels including tree-decode-aware variants; reference for any new
  sampling kernel.
- **Hopper warp-spec FMHA**: distinct producer / consumer warp groups,
  reference for any Hopper FMHA design.

## Common pitfalls

- FlashInfer's `BatchPrefill*Wrapper` allocates internal workspaces; benchmark
  numbers without warmup are dominated by the workspace allocation, not the
  kernel.
- The "paged" path supports both `block_table` and `kv_indices` formats; the
  Python wrapper picks one silently. Confirm which format the kernel actually
  consumes.
- Some FlashInfer kernels assume `page_size` is a power of two; mismatch
  causes silent correctness drift on the last block.

## When to read this framework

- You are designing a paged-attention kernel, a prefix-cache-aware kernel, an
  MLA variant, or a sampling kernel.
- You want a reference for how to expose a kernel to a Python serving stack
  (`Wrapper` pattern + plan / run split).

## When NOT to copy

- FMHA / paged / MLA kernel bodies are out-of-bounds for direct copy. The
  page-table and prefix-cache *interfaces* are good design references.

## Recommended ncu metrics for FlashInfer

- Paged attention: `l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum.per_second`,
  `smsp__inst_executed_pipe_tensor`, `dram__throughput`.
- MLA: `smsp__inst_executed_pipe_tensor`, `lts__t_bytes`.
- Sampling: `smsp__warp_issue_stalled_*`, `l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum`.
