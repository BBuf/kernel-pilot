# PR-Driven Kernel Knowledge

This layer follows the kernel-knowledge design implied by MIT Kernel Mafia: production pull requests are treated as first-class evidence because many real optimization recipes live in PR diffs, review threads, tests, benchmarks, and follow-up fixes rather than in official documentation.

## PR/Source Read Order

1. Start with the target topic and framework routing pages.
2. Read the matching source guide under `knowledge/references/source-guides/`.
3. For PR-driven repositories listed below, also read the matching PR page in the same knowledge pass.
4. For source-only repositories, including repositories with fewer than 10 selected CUDA optimization PRs, skip PR lookup and inspect the linked source guide or source catalog plus current code paths directly.
5. Use PRs for optimization history, review context, tests, and benchmark evidence; use source guides and direct source scans for the current implementation, wrappers, tests, benchmark entry points, and candidate code locations.
6. If the bottleneck is known but the source repository is unclear, use `by-topic/index.md`, then open the matching source guide for each promising repository.
7. Record each source-derived idea in the source idea ledger with repo, PR number when available, source path or symbol, hypothesis, measured result, and do-not-reread key.

## Repository PR Pages

| Repository | PR guide | CUDA optimization PRs | Filtered pool |
| --- | --- | ---: | ---: |
| `NVIDIA/cutlass` | [`cutlass.md`](cutlass.md) | 26 | 26 |
| `sgl-project/sglang` | [`sglang.md`](sglang.md) | 80 | 80 |
| `vllm-project/vllm` | [`vllm.md`](vllm.md) | 91 | 91 |
| `flashinfer-ai/flashinfer` | [`flashinfer.md`](flashinfer.md) | 127 | 127 |
| `deepseek-ai/DeepGEMM` | [`deepgemm.md`](deepgemm.md) | 20 | 20 |
| `NVIDIA/TensorRT-LLM` | [`tensorrt-llm.md`](tensorrt-llm.md) | 121 | 121 |
| `Dao-AILab/flash-attention` | [`flash-attention.md`](flash-attention.md) | 46 | 46 |
| `tile-ai/tilelang` | [`tilelang.md`](tilelang.md) | 34 | 34 |
| `NVIDIA/cccl` | [`cccl-cub.md`](cccl-cub.md) | 62 | 62 |

## Source-Only Repositories

These repositories are intentionally not queried through PR pages. Use the linked source guide or source catalog, then inspect current code paths directly.

| Repository | Source reference | Reason |
| --- | --- | --- |
| `pytorch/pytorch` | [`source`](../source-guides/pytorch.md) | PyTorch is too large/noisy for useful PR recall; use source guide and current source scan. |
| `deepseek-ai/TileKernels` | [`source`](../source-guides/tilekernels.md) | Little public PR history; use source guide and current source scan. |
| `NVIDIA/cuda-samples` | [`source`](../source-guides/cuda-blog-kernels.md) | Sample/code repository; PR history is not the optimization knowledge layer. |
| `NVIDIA/CUDALibrarySamples` | [`source`](../../../references/kernel-source-catalog.md) | Sample/code repository; PR history is not the optimization knowledge layer. |
| `NVIDIA/cudnn-frontend` | [`source`](../../../references/kernel-source-catalog.md) | Sample/API repository; use source/catalog references directly. |
| `NVIDIA/nvbench` | [`source`](../../../references/kernel-source-catalog.md) | Benchmark methodology repository; use source/catalog references directly. |
| `NVIDIA/cuda-tile` | [`source`](../../../references/kernel-source-catalog.md) | Experimental source repository; use source/catalog references directly. |
| `gpu-mode/reference-kernels` | [`source`](../../../references/kernel-source-catalog.md) | Reference-kernel repository; use source/catalog references directly. |
| `gpu-mode/kernelbot` | [`source`](../../../references/kernel-source-catalog.md) | Competition/tooling repository; use source/catalog references directly. |
| `gpu-mode/Triton-Puzzles` | [`source`](../../../references/kernel-source-catalog.md) | Educational code repository; use source/catalog references directly. |
| `NVIDIA-developer-blog/code-samples` | [`source`](../source-guides/cuda-blog-kernels.md) | Blog companion code; use source guide and code paths directly. |
| `leimao/CUDA-GEMM-Optimization` | [`source`](../source-guides/cuda-blog-kernels.md) | Blog/worklog companion code; use source guide and code paths directly. |
| `siboehm/SGEMM_CUDA` | [`source`](../source-guides/cuda-blog-kernels.md) | Blog/worklog companion code; use source guide and code paths directly. |
| `ColfaxResearch/cutlass-kernels` | [`source`](../source-guides/colfax-research.md) | Blog/tutorial companion code; use source guide and code paths directly. |
| `ColfaxResearch/cfx-article-src` | [`source`](../source-guides/colfax-research.md) | Blog/tutorial companion code; use source guide and code paths directly. |
| `simveit/effective_transpose` | [`source`](../source-guides/veitner-blog.md) | Blog companion code; use source guide and code paths directly. |
| `simveit/load_and_store` | [`source`](../source-guides/veitner-blog.md) | Blog companion code; use source guide and code paths directly. |
| `moderngpu/moderngpu` | [`source`](../../../references/kernel-source-catalog.md) | Classic code archive; use source/catalog references directly. |
| `huggingface/kernels` | [`source`](../../../references/kernel-source-catalog.md) | Reusable code/package repository; use source/catalog references directly. |
| `triton-lang/triton` | [`source`](../source-guides/triton.md) | Only 7 selected CUDA optimization PRs after filtering (<10); use source guide and current source scan. |
| `Dao-AILab/quack` | [`source`](../source-guides/quack.md) | Only 9 selected CUDA optimization PRs after filtering (<10); use source guide and current source scan. |
| `HazyResearch/ThunderKittens` | [`source`](../source-guides/thunderkittens.md) | Only 6 selected CUDA optimization PRs after filtering (<10); use source guide and current source scan. |
| `Tencent/hpc-ops` | [`source`](../../../references/kernel-source-catalog.md) | Only 5 selected CUDA optimization PRs after filtering (<10); use source guide and current source scan. |

## Cross-Repository Topic Pages

Use [`by-topic/index.md`](by-topic/index.md) to inspect PRs by kernel family across all repositories.

## Coverage Audit

Use [`audit.md`](audit.md) to inspect scan methodology, filtering rules, repository coverage, and known gaps.

## Open PR Watchlist

Use [`open-watchlist.md`](open-watchlist.md) for current open PRs. Re-run the refresh script before relying on these entries because open PRs move quickly.

## Categories

| Category | Meaning |
| --- | --- |
| `gemm_quant` | GEMM / Quantization |
| `attention_kv` | Attention / KV / Decode |
| `moe_routing` | MoE / Routing |
| `norm_elementwise` | Norm / Elementwise / Epilogue |
| `memory_primitives` | Memory / Primitives |
| `scheduler_autotune` | Scheduler / Autotune |
| `arch_pipeline` | Architecture / Pipeline |
| `compiler_runtime` | Compiler / Runtime |
| `benchmark_test` | Benchmark / Test Evidence |
| `kernel_other` | Other Kernel Cases |

## Expansion Rule

When two consecutive optimization rounds improve the best geomean by less than 1%, read paired PR/source evidence first. Read at least 50 new code-first sources before prose sources; a PR diff, source file, symbol, linked test, benchmark, or changed kernel file counts as a code-first source when it is recorded with a do-not-reread key.

## Refresh Command

```bash
python3 scripts/refresh_pr_knowledge.py --since 2024-05-15
```
