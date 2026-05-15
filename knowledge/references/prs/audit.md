# PR Knowledge Coverage Audit

Scan window: merged or updated since `2024-05-15`.

## What Was Scanned

| Repository | Filtered merged pool | Knowledge merged PRs | Open watchlist entries |
| --- | ---: | ---: | ---: |
| `NVIDIA/cutlass` | 140 | 140 | 82 |
| `pytorch/pytorch` | 39 | 39 | 108 |
| `sgl-project/sglang` | 304 | 304 | 121 |
| `vllm-project/vllm` | 297 | 297 | 139 |
| `flashinfer-ai/flashinfer` | 261 | 261 | 113 |
| `deepseek-ai/DeepGEMM` | 58 | 58 | 18 |
| `NVIDIA/TensorRT-LLM` | 348 | 348 | 116 |
| `Dao-AILab/flash-attention` | 194 | 194 | 76 |
| `triton-lang/triton` | 92 | 92 | 89 |
| `tile-ai/tilelang` | 231 | 231 | 26 |
| `Dao-AILab/quack` | 26 | 26 | 8 |
| `deepseek-ai/TileKernels` | 1 | 1 | 5 |
| `HazyResearch/ThunderKittens` | 53 | 53 | 14 |
| `NVIDIA/cccl` | 458 | 458 | 98 |
| `NVIDIA/cuda-samples` | 15 | 15 | 22 |
| `NVIDIA/CUDALibrarySamples` | 2 | 2 | 0 |
| `NVIDIA/cudnn-frontend` | 14 | 14 | 0 |
| `NVIDIA/nvbench` | 62 | 62 | 8 |
| `NVIDIA/cuda-tile` | 0 | 0 | 0 |
| `gpu-mode/reference-kernels` | 31 | 31 | 7 |
| `gpu-mode/kernelbot` | 85 | 85 | 12 |
| `gpu-mode/Triton-Puzzles` | 7 | 7 | 0 |
| `NVIDIA-developer-blog/code-samples` | 16 | 16 | 1 |
| `leimao/CUDA-GEMM-Optimization` | 2 | 2 | 0 |
| `siboehm/SGEMM_CUDA` | 1 | 1 | 2 |
| `ColfaxResearch/cutlass-kernels` | 3 | 3 | 1 |
| `ColfaxResearch/cfx-article-src` | 4 | 4 | 2 |
| `simveit/effective_transpose` | 0 | 0 | 0 |
| `simveit/load_and_store` | 0 | 0 | 0 |
| `moderngpu/moderngpu` | 7 | 7 | 0 |
| `huggingface/kernels` | 81 | 81 | 8 |
| `Tencent/hpc-ops` | 8 | 8 | 3 |

## Filter Policy

- Keep PRs that touch kernels, runtime dispatch, JIT/compiler lowering, tuning configs, benchmarks, tests, or profiler evidence.
- Keep CUDA-kernel-related PRs across the registered knowledge repositories, including implementation, runtime dispatch, tuning, benchmark, testing, and profiling changes.
- Filter obvious non-CUDA backend work such as MPS, ROCm, AMD-only, MUSA, Ascend, Intel, CPU-only, Metal, RVV, and RISC-V PRs unless the same PR also carries CUDA/NVIDIA kernel evidence.
- Filter release-only, CI-only, dependency-bump, formatting, copyright-header, MyPy, doc-only, cookbook-only, and example-path-only PRs.
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
