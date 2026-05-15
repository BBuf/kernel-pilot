# CUDA Blog Companion Kernels

Repositories and sources:

- <https://github.com/NVIDIA-developer-blog/code-samples>
- <https://github.com/NVIDIA/cuda-samples>
- <https://github.com/leimao/CUDA-GEMM-Optimization>
- <https://github.com/siboehm/SGEMM_CUDA>
- <https://github.com/ColfaxResearch/cutlass-kernels>

Deep reference: `knowledge/references/source-guides/cuda-blog-kernels.md`

This page routes to classic CUDA optimization blog posts and their companion
repositories: coalescing, matrix transpose, shared-memory bank conflicts,
stepwise GEMM, CUTLASS/CuTe tutorials, and tensor-core introductions.

## When to read this framework

- A kernel is memory-bound and needs coalescing, shared-memory, or bank-conflict
  intuition.
- A GEMM or transpose candidate needs a simple human-readable optimization
  progression before framework-specific work.
- Plateau research needs code plus explanatory prose, not prose alone.

## Reuse / Copy Rules

- Prefer using these as explanatory references and small repro patterns.
- If a companion repo provides the best baseline seed, copy/adapt only when
  license / attribution are handled and record exact source, commit, and delta.
