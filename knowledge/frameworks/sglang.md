# SGLang

Repository: <https://github.com/sgl-project/sglang>

SGLang is a serving framework for LLMs and VLMs. For kernel work it is the
canonical place to look at **production attention scheduling**, **fused MoE on
Triton + CUDA**, **FP8 paths**, **RadixAttention / HiCache**, **speculative /
EAGLE / tree decode**, and **sampling kernels** tuned for both Hopper and
Blackwell.

## Where the kernels live

| Directory | What you find there |
| --- | --- |
| `sgl-kernel/csrc/` | C++/CUDA AOT kernel binaries (attention, gemm, moe, fused norm, sampling, spec-decode, communication). |
| `sgl-kernel/csrc/attention/` | FMHA wrappers, paged KV gather, masked variants, kv-cache layout helpers. |
| `sgl-kernel/csrc/gemm/` | FP8/INT8 GEMM wrappers, cuBLAS / CUTLASS shim, FP4 paths. |
| `sgl-kernel/csrc/moe/` | `moe_align_block_size`, `topk`, fused `moe_silu_and_mul`, permute / unpermute, grouped GEMM glue. |
| `sgl-kernel/csrc/elementwise/` | Fused RMSNorm + add, RoPE variants, silu_and_mul, dequant. |
| `sgl-kernel/csrc/spec_decode/` | Tree-decode bookkeeping, EAGLE draft-token kernels. |
| `python/sglang/srt/layers/attention/` | Backend selection logic (FlashInfer / FA / FA3 / Triton / TRTLLM-MLA / cuDNN). |
| `python/sglang/srt/layers/moe/` | Python-side fused-MoE Triton kernels and quant-aware variants. |
| `python/sglang/srt/layers/quantization/` | FP8 / FP4 / W8A8 weight prep and runtime dequant paths. |
| `python/sglang/srt/layers/sampler.py` | Top-k / top-p logits processing. |

## Optimization patterns documented here

- **Backend-routing layer**: kernel selection is data-driven (head dim, dtype,
  page size, masking style). Mimic this when designing new attention variants
  instead of hard-coding one kernel.
- **MoE pipeline**: `topk` → `moe_align_block_size` → permute → grouped GEMM →
  fused activation → unpermute. Read `csrc/moe/moe_align_block_size.cu` to see
  how block alignment is converted into a sorted token map without a global
  sort.
- **FP8 epilogue fusion**: per-channel / per-tensor scales fused into the
  CUTLASS epilogue; observe how `cutlass_extensions` are layered.
- **Speculative decode (EAGLE/tree)**: gather/scatter into per-request branch
  tables, often the actual bottleneck instead of the GEMM itself.
- **HiCache / RadixCache**: layered host+device prefix cache, look at the page
  table bookkeeping for ideas on KV layout when adding new attention variants.

## Common pitfalls

- The Triton MoE kernels in `python/sglang/srt/layers/moe/` are not the C++
  variants in `sgl-kernel/csrc/moe/`. Read the wrapper in `sgl-kernel/python/`
  to confirm which path is active for the chosen GPU and dtype.
- `moe_align_block_size` is more subtle than it looks; misreading the cumulative
  sums silently corrupts expert routing under tail batches.
- Some kernels have **separate Hopper and Blackwell** entry points selected at
  load time. Always check the SM-arch guard before claiming a regression.

## When to read this framework

- The target operator is attention, MoE, RMSNorm/RoPE fusion, sampling, or
  speculative decoding for an LLM serving workload.
- You need a *real-world* end-to-end harness that already wires kernel into
  scheduler, KV manager, and benchmarks (`python/sglang/bench_one_batch.py`,
  `python/sglang/bench_serving.py`).

## When NOT to copy

- Tuned kernel bodies (anything under `sgl-kernel/csrc/*`) must not be
  pattern-matched into a candidate. Use the surrounding integration code as
  oracle / correctness reference.

## Recommended ncu metrics for SGLang kernels

- Attention: `sm__pipe_alu_cycles_active`, `smsp__inst_executed_pipe_tensor`,
  `l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum.per_second`.
- MoE align/permute: `smsp__warp_issue_stalled_*`, `l1tex__data_bank_conflicts_pipe_lsu.sum`.
- Fused norm / elementwise: `dram__throughput`, `smsp__inst_executed`.
