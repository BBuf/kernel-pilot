# Kernel Source Catalog

This is the KernelPilot knowledge base `K` for GPU-kernel work. It tells the
agent which repository links to inspect before proposing an iteration, and
which sources are references rather than candidate-code inputs.

The machine-readable version is `kernel-source-catalog.json`.

## Reference Repositories

| Repository | Link | Read first |
| --- | --- | --- |
| `BBuf/AI-Infra-Auto-Driven-SKILLS` | https://github.com/BBuf/AI-Infra-Auto-Driven-SKILLS/tree/main/skills/gpu-kernel-ako4all/references | AKO loop discipline, CUDA C++, Triton, profiling, architecture notes |
| `flashinfer-ai/flashinfer` | https://github.com/flashinfer-ai/flashinfer | `csrc`, `csrc/fmha_v2/fmha`, `csrc/fmha_v2/fmha/hopper`, `csrc/fmha_v2/fmha/warpspec`, `benchmarks/bench_blackwell_attention.py` |
| `Dao-AILab/flash-attention` | https://github.com/Dao-AILab/flash-attention | `csrc/flash_attn/src`, `flash_attn/cute`, `benchmarks/benchmark_attn.py`, `benchmarks/bench_sm90.py` |
| `Tencent/hpc-ops` | https://github.com/Tencent/hpc-ops | `hpc/attention.py`, `hpc/group_gemm.py`, `hpc/normalization.py`, `hpc/rope.py`, `src/attention`, `src/group_gemm`, `src/normalization`, `src/rope`, `tests/` |
| `deepseek-ai/DeepGEMM` | https://github.com/deepseek-ai/DeepGEMM | `csrc/apis`, `csrc/jit`, `csrc/jit_kernels/heuristics`, `csrc/jit_kernels/impls`, `deep_gemm/include/deep_gemm`, `deep_gemm/testing`, `tests/` |

The target project is intentionally not listed as a reference repository. The
user supplies it per task or prompt, and the agent may use it for integration,
tests, benchmarks, and correctness oracles after a candidate exists.

## Usage Rules

1. Read references to identify hypotheses, contracts, and measurement style.
2. Do not copy external kernel code into a candidate.
3. For target-project task files, `forbidden_files` cannot seed a from-scratch
   candidate. They may be read later for integration or old-vs-new comparison.
4. Every source-derived idea must be logged in lineage notes with the repository
   link, source path, and exact hypothesis being tested.
