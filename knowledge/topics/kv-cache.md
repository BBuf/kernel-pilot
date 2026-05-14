# Topic: KV-Cache / Paged Memory

## What it covers

Paged KV layouts (block tables, page tables), HiCache / RadixAttention
prefix sharing, KV swap / copy / reshape kernels, append-attention bookkeeping.

## Per-framework references

| Framework | Where to look | What it teaches |
| --- | --- | --- |
| `vllm` | `csrc/cache_kernels.cu`, `vllm/worker/cache_engine.py` | Canonical block-table layout and KV swap / reshape kernels. |
| `flashinfer` | `include/flashinfer/page.cuh`, `python/flashinfer/*` (BatchPrefill/BatchDecode wrappers) | Flexible page table with variable block sizes. |
| `sglang` | `python/sglang/srt/mem_cache/`, `sgl-kernel/csrc/attention/` | RadixAttention + HiCache + production block tables. |
| `tensorrt-llm` | `cpp/tensorrt_llm/kernels/kvCacheUtils/` | NVIDIA's KV utility kernels. |

## Common optimization patterns

- Page-aligned KV blocks with a per-request block-index tensor.
- Prefix-cache aware attention: split shared prefix from unique suffix to
  avoid redundant KV loads.
- KV reshape / swap: avoid Python-side reshapes; the kernel writes directly
  into the paged layout.
- HiCache: host-resident eviction tier with async H2D for warm prefixes.

## Common bottlenecks

- Indirect KV loads through block tables stress L2 and HBM; check
  `lts__t_bytes` and `l1tex__t_sectors`.
- KV append on extend-attention can become a host-overhead bottleneck if
  Python wrappers re-allocate.

## Recommended ncu metrics

- `l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum.per_second`
- `dram__throughput.avg.pct_of_peak_sustained_elapsed`
- `lts__t_bytes.avg.pct_of_peak_sustained_elapsed`
- `smsp__inst_executed.avg.per_cycle_active`
