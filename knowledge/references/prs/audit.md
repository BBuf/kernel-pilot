# PR Knowledge Coverage Audit

Scan window: merged or updated since `2024-05-15`.

## What Was Scanned

| Repository | Filtered merged pool | Knowledge merged PRs | Open watchlist entries |
| --- | ---: | ---: | ---: |
| `NVIDIA/cutlass` | 26 | 26 | 8 |
| `sgl-project/sglang` | 80 | 80 | 45 |
| `vllm-project/vllm` | 91 | 91 | 39 |
| `flashinfer-ai/flashinfer` | 127 | 127 | 64 |
| `deepseek-ai/DeepGEMM` | 20 | 20 | 11 |
| `NVIDIA/TensorRT-LLM` | 121 | 121 | 49 |
| `Dao-AILab/flash-attention` | 46 | 46 | 34 |
| `triton-lang/triton` | 7 | 7 | 22 |
| `tile-ai/tilelang` | 34 | 34 | 13 |
| `Dao-AILab/quack` | 9 | 9 | 3 |
| `HazyResearch/ThunderKittens` | 6 | 6 | 5 |
| `NVIDIA/cccl` | 62 | 62 | 17 |
| `Tencent/hpc-ops` | 5 | 5 | 3 |

## Source-Only Repositories

These repositories are excluded from PR scanning and should be queried through source guides or current source trees.

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

## Filter Policy

- Keep PRs only when they have CUDA/NVIDIA target evidence, a real kernel/source change, and an optimization/performance mechanism.
- Keep CUDA optimization PRs across the registered knowledge repositories, including implementation, runtime dispatch, tuning, benchmark-backed speed work, profiler evidence, and kernel-family feature additions.
- Filter obvious non-CUDA backend work such as MPS, ROCm, AMD-only, MUSA, Ascend, Intel, CPU-only, Metal, RVV, and RISC-V PRs unless the same PR also carries CUDA/NVIDIA kernel evidence.
- Filter release-only, CI-only, dependency-bump, formatting, copyright-header, MyPy, doc-only, cookbook-only, example-path-only, and correctness-only PRs.
- Keep major release PRs only when their changed paths expose real kernel/API source files and the title/body points to kernel features.

## Evidence Captured Per PR

- PR URL and stable source key, for example `vllm-project/vllm#42236`.
- Primary and secondary kernel categories.
- Changed-path buckets: kernel, benchmark, test, wrapper, docs, other.
- Short human-readable summary.
- Transfer recipe and first NCU metrics to inspect.
- Matched search queries in `pr-index.json` for traceability.

## Retrieval Strategy

1. Use the repository PR page and the matching source guide together when the baseline framework is PR-driven.
2. For source-only repositories, skip PR lookup and use the source guide or source catalog plus current source tree.
3. Use `by-topic/index.md` when the bottleneck category is known but the best source repository is not, then open source guides for every promising repository.
4. Use `open-watchlist.md` only for fresh ideas, and re-check GitHub plus the current source tree before trusting the code or benchmark claim.
5. Log every source-derived idea in `artifacts/source-idea-ledger.md` with PR key when available, source path or symbol, opened tests/benchmarks, hypothesis, result, and do-not-reread key.

## Known Gaps

- DeepSeek TileKernels has little public PR history, so source-guide and direct code scan are mandatory paired evidence for that repo.
- GitHub search can miss PRs whose titles and bodies use generic wording. When optimizing a specific kernel, still run path-based `gh pr list` or `gh search prs` for that exact file/function name and inspect current source paths.
- Open PR entries are intentionally volatile and should not be treated as merged production evidence.
- The corpus is intentionally CUDA-first. Non-CUDA backend PRs are filtered out unless they also contain CUDA/NVIDIA kernel evidence.

## Refresh Command

```bash
python3 scripts/refresh_pr_knowledge.py --since 2024-05-15
```
