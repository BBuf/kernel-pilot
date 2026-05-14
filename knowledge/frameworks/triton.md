# Triton

Repository: <https://github.com/triton-lang/triton>

Triton is the dominant DSL for **portable, autotuned LLM kernels**. SGLang,
vLLM, and PyTorch Inductor all use Triton for fused MoE, fused norms,
attention variants, and elementwise fusion.

## Where the kernels live

| Directory | What you find there |
| --- | --- |
| `python/tutorials/` | Canonical Triton tutorials (matmul, softmax, attention, layer-norm). |
| `python/triton/language/` | Triton language primitives (`tl.dot`, `tl.load`, `tl.store`, `tl.atomic`, block pointers, TMA). |
| `python/triton/runtime/` | Autotuner, JIT cache, `do_bench`. |
| `lib/Conversion/` | MLIR conversion passes (informative for "why is my kernel slow on this arch"). |
| `test/TritonGPU/` | IR-level tests; reference for what the compiler optimizes. |

## Optimization patterns documented here

- **Block pointers + TMA**: the modern way to load tiles on Hopper / Blackwell
  Triton kernels.
- **Autotune configs**: `triton.Config({...}, num_warps=, num_stages=)`. The
  default Inductor configs are a strong starting point.
- **Software pipelining via `num_stages`**: increasing stages overlaps loads
  with compute, but increases smem pressure.
- **Persistent kernels**: a small grid that loops over tiles, used for
  Stream-K-like GEMMs and tail-aware MoE.
- **`tl.atomic_*` collectives**: the standard way to write fused-add
  outputs and reductions across program ids.

## Common pitfalls

- The same source produces different SASS on different GPU arches; always
  recompile and re-tune when changing arch.
- `tl.load(mask=)` with out-of-bounds addresses is cheap on H100 but
  *expensive* on A100; choose the mask strategy per arch.
- The autotuner caches by `key=` arguments only; missing a runtime-varying
  argument from `key=` causes the autotuner to pick a stale config.
- `num_stages` higher than 2 often regresses on smem-bound kernels.

## When to read this framework

- You are designing any Triton kernel.
- You are reading SGLang / vLLM / Inductor Triton kernels and want to
  understand the underlying primitives.

## When NOT to copy

- Triton kernel bodies in this repo are tutorials, freely usable as
  inspiration; downstream Triton kernels (in SGLang / vLLM) follow each
  task's candidate-source rules.

## Recommended ncu metrics for Triton

- Triton kernels still emit CUDA SASS; use the standard CUDA metrics.
- Matmul: `sm__inst_executed_pipe_tensor`, `lts__t_bytes`.
- Softmax / norm: `dram__throughput`, `smsp__inst_executed`.
- Attention: `smsp__inst_executed_pipe_tensor`,
  `l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum.per_second`.
