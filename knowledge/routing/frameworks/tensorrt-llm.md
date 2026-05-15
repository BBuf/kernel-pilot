# TensorRT-LLM

Repository: <https://github.com/NVIDIA/TensorRT-LLM>

Deep reference: `knowledge/references/source-guides/tensorrt-llm.md`

TensorRT-LLM ships NVIDIA's reference LLM kernels and is the closest public
implementation of the techniques in NVIDIA's blogs (FP8, FP4, TMA + WGMMA
attention, MoE on Hopper / Blackwell, NVLS userbuffers, multi-block decoder
attention).

## Where the kernels live

| Directory | What you find there |
| --- | --- |
| `cpp/tensorrt_llm/kernels/` | The main kernels tree (CUDA C++). |
| `cpp/tensorrt_llm/kernels/decoderMaskedMultiheadAttention/` | Decoder MMHA family (single-token decode, multi-block decode). |
| `cpp/tensorrt_llm/kernels/contextFusedMultiHeadAttention/` | Context FMHA (prefill), TMA/WGMMA variants per arch. |
| `cpp/tensorrt_llm/kernels/mixtureOfExperts/` | MoE GEMM, expert permute, fused activations. |
| `cpp/tensorrt_llm/kernels/quantization/` | FP8, FP4, INT8, AWQ; per-tensor, per-channel, block-scaled. |
| `cpp/tensorrt_llm/kernels/cutlass_kernels/` | CUTLASS-based GEMM kernels, fused epilogues. |
| `cpp/tensorrt_llm/kernels/internal_cutlass_kernels/` | Internal CUTLASS variants used by FP8 / FP4 paths. |
| `cpp/tensorrt_llm/kernels/userbuffers/` | NVLS / userbuffers / all-reduce-overlap helpers for multi-GPU. |
| `cpp/tensorrt_llm/kernels/preQuantScaleKernel/` | Pre-GEMM activation quant + scale fusion. |
| `cpp/tensorrt_llm/kernels/rmsnormKernels.cu` | Fused RMSNorm + residual + (optional) quant. |
| `cpp/tensorrt_llm/kernels/topkSampling*.cu` | Top-k sampling kernels. |

## Optimization patterns documented here

- **Decoder MMHA**: single-token decode pattern with multi-block split,
  including the post-process `multi_block_finalize_kernel`. The cleanest
  reference for split-K decode attention.
- **Context FMHA per arch**: separate paths for SM75 / SM80 / SM89 / SM90 /
  SM100, often using different smem layouts. Always confirm the dispatch path
  before benchmarking.
- **MoE expert mapping**: cumulative-sum-based permute used in MoE GEMM; very
  similar pattern to SGLang's `moe_align_block_size`. Compare both before
  designing a new permute.
- **Block-scaled FP8 / FP4**: NVIDIA's recommended layout (`SF` blocks, 32x32
  tiles), the canonical reference for `block_scaled_gemm` design.
- **Userbuffers / NVLS**: registered host buffers + `multimem` PTX for
  cluster-wide reductions; reference for any comm-overlap work.

## Common pitfalls

- Many MMHA kernels are templated and only one specialization is selected at
  runtime; a benchmark "regression" can really be a different specialization
  being chosen.
- FP4 paths assume `SF` (scale factor) tensors next to the data; missing this
  layout gives silently wrong outputs.
- The `internal_cutlass_kernels` directory shadows `cutlass_kernels`; the
  internal path is the one TensorRT-LLM actually links by default on Hopper /
  Blackwell.

## When to read this framework

- You are designing FMHA / decoder attention, MoE GEMM, FP8/FP4 GEMM, or
  comm-overlap kernels for an LLM serving workload on Hopper or Blackwell.
- You want NVIDIA's "official" answer for shape / dtype / arch routing.

## Reuse / Copy Rules

- TensorRT-LLM code may seed a candidate only when the user or baseline calls
  for that implementation family and license / attribution are handled.
- Record source path or URL, commit, copied files, and delta in the source
  ledger before mutating copied or adapted code.
- Otherwise use it as the best reference for **what to measure** and **which
  tile shapes are expected** to win.

## Recommended ncu metrics for TensorRT-LLM kernels

- Context FMHA: `sm__inst_executed_pipe_tensor.avg.pct_of_peak_sustained_elapsed`,
  `lts__t_bytes`, `dram__throughput`.
- Decoder MMHA: `smsp__average_warp_latency_per_inst_executed`,
  `l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum.per_second`.
- MoE permute / GEMM: `smsp__inst_executed`, `l1tex__data_bank_conflicts_pipe_lsu.sum`.
- Userbuffers all-reduce: `dram__throughput`, `lts__t_bytes`,
  `smsp__cycles_active`.
