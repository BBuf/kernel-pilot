# QuACK Deep Reference

Repository: <https://github.com/Dao-AILab/quack>

PR case notes: `../prs/quack.md`

QuACK is a CuTe DSL kernel collection from Dao-AILab. Use it for CuTe DSL
memory-bound kernels, normalization, softmax, cross entropy, Hopper GEMM, and
Blackwell GEMM/epilogue baselines.

## Read Order

1. README and docs for supported GPU/CUDA version and package constraints.
2. Kernel implementation under `quack/`.
3. Matching benchmark under `benchmarks/` or `microbenchmarks/`.
4. Tests for correctness and dtype/shape coverage.
5. Any linked blog post for the optimization rationale.

## Code Map By Kernel Type

| Kernel type | Paths to inspect | What to extract |
| --- | --- |
| GEMM core | `quack/{gemm.py,gemm_base.py,gemm_config.py,gemm_interface.py,gemm_sm80.py,gemm_sm90.py,gemm_sm100.py,gemm_sm120.py}`, `tests/test_gemm_*`, `benchmarks/benchmark_gemm*.py` | architecture split, tile config, autotune, launch API |
| GEMM epilogues | `quack/{gemm_default_epi.py,gemm_act.py,gemm_dact.py,gemm_norm_act.py,gemm_sq_reduce.py,epi_*.py}`, `benchmarks/benchmark_gemm_epilogues.py` | activation/norm/reduction epilogue fusion |
| Block-scaled / low precision | `quack/{gemm_blockscaled_interface.py,blockscaled_gemm_utils.py,mx_utils.py,rounding.py}`, `tests/test_gemm_sm100_blockscaled.py`, `AI/varlen_blockscaled_sf_layout.md` | scale-factor layout, MX/NVFP style utility code |
| Norms | `quack/{rmsnorm.py,rmsnorm_config.py,rms_final_reduce.py,reduce.py,reduction_base.py}`, `benchmarks/benchmark_rmsnorm.py`, `tests/test_rmsnorm.py`, `tests/test_layernorm.py` | two-pass/final-reduce structure and memory-bound benchmark |
| Softmax / top-k / sort | `quack/{softmax.py,topk.py,sort/*}`, `benchmarks/benchmark_softmax.py`, `benchmark_topk.py`, tests | reduction, sorting networks, top-k selection |
| Cross entropy / linear | `quack/{cross_entropy.py,linear.py,linear_cross_entropy.py,mlp.py}`, benchmarks/tests | fused linear + loss and MLP composition |
| Rotary / Hadamard | `quack/{rotary.py,hadamard.py}`, matching benchmarks/tests | memory-bound elementwise transforms |
| Runtime/autotune/compile | `quack/{autotuner.py,compile_utils.py,cache_utils.py,cute_dsl_*.py,tensormap_manager.py,tile_scheduler.py}` | compile cache, CuTe DSL fixes, TensorMap manager, scheduler helpers |
| Microbench / profiling notes | `microbenchmarks/gpu_pipe_microbench.*`, `docs/sm120_ncu_profiling.md`, `AI/*` | pipe microbenchmarks, SM100/SM120 notes, reproduction cases |

## Search Patterns

```bash
rg -n "rmsnorm|layernorm|softmax|cross_entropy|gemm|epilogue|blackwell|hopper|cute|TMA|WGMMA|tcgen05" quack benchmarks microbenchmarks tests docs
rg -n "H100|B200|B300|CUDA 12.9|CUDA 13|heuristic|matmul" README.md docs quack benchmarks
```

## Candidate Use

- QuACK can be a baseline seed when the task asks for CuTe DSL or QuACK-style
  kernels.
- Preserve Apache-2.0 notice context, exact source path, commit, copied files,
  and first delta.
- Keep QuACK benchmarks as prior art, but build a task-local harness so results
  are comparable to the target baseline.

## NCU Focus

| Kernel family | First metrics |
| --- | --- |
| Memory-bound kernels | DRAM throughput, global sectors, issue stalls, active cycles |
| GEMM / epilogue | tensor pipe %, L2/DRAM bytes, register pressure, epilogue ALU |
| Blackwell kernels | tcgen05/tensor pipe metrics, TMA traffic, occupancy, stalls |
