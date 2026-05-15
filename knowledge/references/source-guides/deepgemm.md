# DeepGEMM Deep Reference

Repository: <https://github.com/deepseek-ai/DeepGEMM>

PR case notes: `../prs/deepgemm.md`

Use this when the target involves FP8/FP4/BF16 GEMM, grouped GEMM, MoE GEMM,
MegaGEMM/MegaMoE-style layouts, JIT compilation, or DeepSeek-style attention
logit kernels.

## Read Order

1. Public API and Python wrapper.
2. JIT dispatch and cache path.
3. Heuristic tables for tile, cluster, schedule, and architecture selection.
4. Kernel implementation under `deep_gemm/include/deep_gemm/` and
   `csrc/jit_kernels/impls`.
5. Tests and benchmark harnesses for the same dtype and grouped layout.

## Code Map By Kernel Type

| Kernel type | Paths to inspect | What to extract |
| --- | --- |
| Public dispatch/API | `csrc/apis/{gemm.hpp,attention.hpp,mega.hpp,runtime.hpp,layout.hpp}`, `deep_gemm/__init__.py` | Python/C++ call contract, shape guards, runtime selection |
| JIT compile/cache | `csrc/jit/{compiler.hpp,cache.hpp,kernel_runtime.hpp,device_runtime.hpp,handle.hpp}` | NVRTC path, cache key, compile-time options |
| FP8/FP4/BF16 GEMM | `csrc/jit_kernels/impls/`, `deep_gemm/include/deep_gemm/impls/`, `tests/test_fp8_fp4.py`, `tests/test_bf16.py` | scale layout, tile/cluster shape, architecture split |
| Grouped/MoE GEMM | `csrc/apis/gemm.hpp`, `deep_gemm/legacy/*grouped_gemm.py`, `tests/test_mega_moe.py`, `deep_gemm/mega/` | `group_offsets`, grouped scheduling, tail behavior |
| Attention/logit kernels | `csrc/apis/attention.hpp`, `tests/test_attention.py` | DeepSeek-style attention logits and shape contracts |
| MMA/PTX wrappers | `deep_gemm/include/deep_gemm/mma/`, `deep_gemm/include/deep_gemm/ptx/` | WGMMA/tcgen05/PTX idioms |
| Scheduler/indexing | `deep_gemm/include/deep_gemm/scheduler/`, `csrc/indexing/main.cu` | persistent/grouped scheduling and indexing kernels |
| TileLang fused ops | `third-party/tilelang_ops/swiglu_apply_weight_to_fp8.py` | SwiGLU + weight application + FP8 cast schedule |
| Bench/test utilities | `deep_gemm/testing/{bench.py,numeric.py,utils.py}`, `tests/generators.py` | timing, numerical oracle, shape generation |

## Search Patterns

```bash
rg -n "grouped|fp8|fp4|block|scale|m_grouped|heuristic|jit|tcgen05|wgmma|tma" csrc deep_gemm tests
rg -n "Tile|Cluster|Schedule|num_stages|sm90|sm100|blackwell|hopper" csrc deep_gemm tests
```

## Candidate Use

- DeepGEMM can be a baseline seed when the task asks for DeepGEMM-style work and
  license / attribution are handled.
- Preserve exact commit, source paths, copied files, scale layout, tile/cluster
  config, and first delta.
- When not copying, translate scale layout, grouped-M scheduling, JIT heuristic
  shape buckets, and NCU hypotheses.

## NCU Focus

| Kernel family | First metrics |
| --- | --- |
| FP8 / FP4 GEMM | tensor pipe %, L2/DRAM bytes, scale-load traffic, active cycles |
| Grouped GEMM | tail imbalance, active cycles, long scoreboard, launch overhead |
| JIT-selected variants | compare tile/cluster/schedule against selected SASS and occupancy |
