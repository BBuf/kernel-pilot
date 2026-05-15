# PR Knowledge Coverage Audit

Scan window: merged or updated since `2024-05-15`.

## What Was Scanned

| Repository | Filtered merged pool | Knowledge merged PRs | Open watchlist entries |
| --- | ---: | ---: | ---: |
| `NVIDIA/cutlass` | 26 | 26 | 8 |
| `pytorch/pytorch` | 1 | 1 | 12 |
| `sgl-project/sglang` | 80 | 80 | 45 |
| `vllm-project/vllm` | 91 | 91 | 39 |
| `flashinfer-ai/flashinfer` | 127 | 127 | 64 |
| `deepseek-ai/DeepGEMM` | 20 | 20 | 11 |
| `NVIDIA/TensorRT-LLM` | 121 | 121 | 49 |
| `Dao-AILab/flash-attention` | 46 | 46 | 34 |
| `triton-lang/triton` | 7 | 7 | 22 |
| `tile-ai/tilelang` | 34 | 34 | 13 |
| `Dao-AILab/quack` | 9 | 9 | 3 |
| `deepseek-ai/TileKernels` | 0 | 0 | 0 |
| `HazyResearch/ThunderKittens` | 6 | 6 | 5 |
| `NVIDIA/cccl` | 62 | 62 | 17 |
| `NVIDIA/cuda-samples` | 1 | 1 | 0 |
| `NVIDIA/CUDALibrarySamples` | 0 | 0 | 0 |
| `NVIDIA/cudnn-frontend` | 0 | 0 | 0 |
| `NVIDIA/nvbench` | 0 | 0 | 0 |
| `NVIDIA/cuda-tile` | 0 | 0 | 0 |
| `gpu-mode/reference-kernels` | 0 | 0 | 0 |
| `gpu-mode/kernelbot` | 0 | 0 | 0 |
| `gpu-mode/Triton-Puzzles` | 0 | 0 | 0 |
| `NVIDIA-developer-blog/code-samples` | 4 | 4 | 0 |
| `leimao/CUDA-GEMM-Optimization` | 1 | 1 | 0 |
| `siboehm/SGEMM_CUDA` | 0 | 0 | 0 |
| `ColfaxResearch/cutlass-kernels` | 3 | 3 | 0 |
| `ColfaxResearch/cfx-article-src` | 1 | 1 | 0 |
| `simveit/effective_transpose` | 0 | 0 | 0 |
| `simveit/load_and_store` | 0 | 0 | 0 |
| `moderngpu/moderngpu` | 0 | 0 | 0 |
| `huggingface/kernels` | 0 | 0 | 0 |
| `Tencent/hpc-ops` | 5 | 5 | 3 |

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

1. Use the repository PR page when the baseline framework is known.
2. Use `by-topic/index.md` when the bottleneck category is known but the best source repository is not.
3. Use `open-watchlist.md` only for fresh ideas, and re-check GitHub before trusting the code or benchmark claim.
4. Log every PR-derived idea in `artifacts/source-idea-ledger.md` with source key, opened paths, hypothesis, result, and do-not-reread key.

## Known Gaps

- DeepSeek TileKernels has little public PR history, so source-guide and direct code scan should dominate for that repo.
- GitHub search can miss PRs whose titles and bodies use generic wording. When optimizing a specific kernel, still run path-based `gh pr list` or `gh search prs` for that exact file/function name.
- Open PR entries are intentionally volatile and should not be treated as merged production evidence.
- The corpus is intentionally CUDA-first. Non-CUDA backend PRs are filtered out unless they also contain CUDA/NVIDIA kernel evidence.

## Refresh Command

```bash
python3 scripts/refresh_pr_knowledge.py --since 2024-05-15
```
