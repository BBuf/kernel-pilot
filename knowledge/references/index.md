# kernel-knowledge References

This directory holds the detailed reference layer for KernelPilot. Keep
`knowledge/routing/frameworks/*.md` and `knowledge/routing/topics/*.md` as
lightweight routing pages; load files here only when the task needs the extra
detail.

## Core Kernel Loop References

Read these for loop discipline, CUDA implementation, profiling, and architecture
specifics:

| Need | Read |
| --- | --- |
| Iteration loop, harness layout, validation gates | `ako4all/ako4all-kernel-loop.md` |
| CUDA C++ / PTX candidate work | `ako4all/cuda-cpp-kernel-reference.md`, `ako4all/cuda-cpp/cuda-cpp-overview.md` |
| Triton candidate or baseline work | `ako4all/triton-kernel-reference.md`, `ako4all/triton/triton-overview.md` |
| CUTLASS / CuTe candidate or baseline work | `ako4all/cutlass-cpp-kernel-reference.md`, `ako4all/cutlass-cpp/cutlass-cpp-overview.md` |
| CuTe DSL candidate or baseline work | `ako4all/cute-dsl-kernel-reference.md`, `ako4all/cute-dsl/cute-dsl-overview.md` |
| Nsight Compute / Nsight Systems evidence | `ako4all/profiling-debugging-reference.md` |
| Hopper H100 tuning | `ako4all/nvidia-architecture-reference.md`, `ako4all/architectures/sm90-optimization-guide.md` |
| Kernel templates and debugging | `ako4all/kernel-templates.md`, `ako4all/troubleshooting.md` |
| Paired PR/source production case notes | `prs/index.md`, `prs/pr-index.json`, `source-guides/` |
| Cross-repository PR lookup by kernel family | `prs/by-topic/index.md` |
| Current open PR watchlist | `prs/open-watchlist.md` |
| Blog-to-code source maps | `blogs/index.md` |

The full copied AKO4ALL attribution is preserved in
`ako4all/source-attribution.md`.

## Source Deep Guides

Read one of these when the target kernel or baseline comes from a specific
source collection:

| Source | Deep guide |
| --- | --- |
| SGLang | `source-guides/sglang.md` |
| vLLM | `source-guides/vllm.md` |
| TensorRT-LLM | `source-guides/tensorrt-llm.md` |
| PyTorch | `source-guides/pytorch.md` |
| FlashAttention | `source-guides/flash-attention.md` |
| FlashInfer | `source-guides/flashinfer.md` |
| CUTLASS / CuTe | `source-guides/cutlass.md` |
| DeepGEMM | `source-guides/deepgemm.md` |
| Triton | `source-guides/triton.md` |
| TileLang | `source-guides/tilelang.md` |
| CuTe DSL | `source-guides/cute-dsl.md` |
| QuACK | `source-guides/quack.md` |
| DeepSeek TileKernels | `source-guides/tilekernels.md` |
| ThunderKittens | `source-guides/thunderkittens.md` |
| CCCL / CUB | `source-guides/cccl-cub.md` |
| Veitner blog and code | `source-guides/veitner-blog.md` |
| Colfax Research blog and code | `source-guides/colfax-research.md` |
| CUDA blog companion kernels | `source-guides/cuda-blog-kernels.md` |

## Paired PR + Source Deep References

Read the matching PR guide and source guide together when a repository matches
the target kernel or when the loop enters plateau-driven research. PRs explain
optimization history, review context, tests, and benchmark evidence; source
guides show the current implementation and concrete code paths to inspect.

| Source | PR guide |
| --- | --- |
| SGLang | `prs/sglang.md` |
| vLLM | `prs/vllm.md` |
| TensorRT-LLM | `prs/tensorrt-llm.md` |
| PyTorch | `prs/pytorch.md` |
| FlashAttention | `prs/flash-attention.md` |
| FlashInfer | `prs/flashinfer.md` |
| CUTLASS / CuTe | `prs/cutlass.md` |
| DeepGEMM | `prs/deepgemm.md` |
| Triton | `prs/triton.md` |
| TileLang | `prs/tilelang.md` |
| QuACK | `prs/quack.md` |
| DeepSeek TileKernels | `prs/tilekernels.md` |
| ThunderKittens | `prs/thunderkittens.md` |
| CCCL / CUB | `prs/cccl-cub.md` |

If the bottleneck is known but the best source repository is unclear, start from
`prs/by-topic/index.md`, then open the matching source guide for every promising
repository. The topic pages group PRs by GEMM/quantization, attention/KV,
MoE/routing, norm/elementwise, memory primitives, scheduler/autotune,
architecture pipeline, compiler/runtime, and benchmark/test evidence.

Use `prs/open-watchlist.md` for fresh open PR ideas only after re-checking the
linked PR on GitHub. Open PRs are volatile and should be logged separately from
merged production evidence.

## Blog Deep References

Read one of these when prose explains the optimization but the implementation
should come from a companion repo or standalone candidate:

| Blog source | Deep guide |
| --- | --- |
| Veitner / Simon's blog | `blogs/veitner.md` |
| Colfax Research | `blogs/colfax.md` |
| NVIDIA CUDA Developer Blog | `blogs/nvidia-cuda.md` |
| Simon Boehm SGEMM Worklog | `blogs/simon-boehm-sgemm.md` |
| Lei Mao CUDA Programming | `blogs/lei-mao-cuda.md` |
| Yifan Yang CUDA Matmul | `blogs/yifan-yang-matmul.md` |

## Use Rules

- Prefer paired production PRs and source code, tests, benchmarks, and open
  PRs/issues before docs or blogs.
- During plateau research, inspect repository PR pages together with matching
  source guides, then by-topic PR pages together with relevant source guides,
  then open PR watchlist plus current source scan, then blog/code references.
- Use the user-requested candidate stack, or the active baseline kernel's stack
  when unspecified.
- Baseline kernels may seed candidates in the standalone repo when
  license/attribution allow; keep the source checkout read-only unless the user
  asks for an in-place framework patch.
- Log every source-derived idea with PR number when available, source path or
  symbol, hypothesis, result, and a do-not-reread key.
