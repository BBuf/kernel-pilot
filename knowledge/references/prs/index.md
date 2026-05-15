# PR-Driven Kernel Knowledge

This layer follows the kernel-knowledge design implied by MIT Kernel Mafia: production pull requests are treated as first-class evidence because many real optimization recipes live in PR diffs, review threads, tests, benchmarks, and follow-up fixes rather than in official documentation.

## Read Order

1. Start with the target topic and framework routing pages.
2. Read the matching source guide under `knowledge/references/source-guides/`.
3. Read the matching PR page below and open only PR categories relevant to the current bottleneck.
4. If the bottleneck is known but the source repository is unclear, use `by-topic/index.md`.
5. Record each used PR in the source idea ledger with repo, PR number, changed paths, hypothesis, measured result, and do-not-reread key.

## Repository PR Pages

| Repository | PR guide | CUDA optimization PRs | Filtered pool |
| --- | --- | ---: | ---: |
| `NVIDIA/cutlass` | [`cutlass.md`](cutlass.md) | 26 | 26 |
| `pytorch/pytorch` | [`pytorch.md`](pytorch.md) | 1 | 1 |
| `sgl-project/sglang` | [`sglang.md`](sglang.md) | 80 | 80 |
| `vllm-project/vllm` | [`vllm.md`](vllm.md) | 91 | 91 |
| `flashinfer-ai/flashinfer` | [`flashinfer.md`](flashinfer.md) | 127 | 127 |
| `deepseek-ai/DeepGEMM` | [`deepgemm.md`](deepgemm.md) | 20 | 20 |
| `NVIDIA/TensorRT-LLM` | [`tensorrt-llm.md`](tensorrt-llm.md) | 121 | 121 |
| `Dao-AILab/flash-attention` | [`flash-attention.md`](flash-attention.md) | 46 | 46 |
| `triton-lang/triton` | [`triton.md`](triton.md) | 7 | 7 |
| `tile-ai/tilelang` | [`tilelang.md`](tilelang.md) | 34 | 34 |
| `Dao-AILab/quack` | [`quack.md`](quack.md) | 9 | 9 |
| `deepseek-ai/TileKernels` | [`tilekernels.md`](tilekernels.md) | 0 | 0 |
| `HazyResearch/ThunderKittens` | [`thunderkittens.md`](thunderkittens.md) | 6 | 6 |
| `NVIDIA/cccl` | [`cccl-cub.md`](cccl-cub.md) | 62 | 62 |
| `NVIDIA/cuda-samples` | [`cuda-samples.md`](cuda-samples.md) | 1 | 1 |
| `NVIDIA/CUDALibrarySamples` | [`cuda-library-samples.md`](cuda-library-samples.md) | 0 | 0 |
| `NVIDIA/cudnn-frontend` | [`cudnn-frontend.md`](cudnn-frontend.md) | 0 | 0 |
| `NVIDIA/nvbench` | [`nvbench.md`](nvbench.md) | 0 | 0 |
| `NVIDIA/cuda-tile` | [`cuda-tile.md`](cuda-tile.md) | 0 | 0 |
| `gpu-mode/reference-kernels` | [`gpu-mode-reference-kernels.md`](gpu-mode-reference-kernels.md) | 0 | 0 |
| `gpu-mode/kernelbot` | [`gpu-mode-kernelbot.md`](gpu-mode-kernelbot.md) | 0 | 0 |
| `gpu-mode/Triton-Puzzles` | [`triton-puzzles.md`](triton-puzzles.md) | 0 | 0 |
| `NVIDIA-developer-blog/code-samples` | [`nvidia-blog-code-samples.md`](nvidia-blog-code-samples.md) | 4 | 4 |
| `leimao/CUDA-GEMM-Optimization` | [`leimao-cuda-gemm.md`](leimao-cuda-gemm.md) | 1 | 1 |
| `siboehm/SGEMM_CUDA` | [`siboehm-sgemm.md`](siboehm-sgemm.md) | 0 | 0 |
| `ColfaxResearch/cutlass-kernels` | [`colfax-cutlass-kernels.md`](colfax-cutlass-kernels.md) | 3 | 3 |
| `ColfaxResearch/cfx-article-src` | [`colfax-article-src.md`](colfax-article-src.md) | 1 | 1 |
| `simveit/effective_transpose` | [`simveit-effective-transpose.md`](simveit-effective-transpose.md) | 0 | 0 |
| `simveit/load_and_store` | [`simveit-load-and-store.md`](simveit-load-and-store.md) | 0 | 0 |
| `moderngpu/moderngpu` | [`moderngpu.md`](moderngpu.md) | 0 | 0 |
| `huggingface/kernels` | [`huggingface-kernels.md`](huggingface-kernels.md) | 0 | 0 |
| `Tencent/hpc-ops` | [`tencent-hpc-ops.md`](tencent-hpc-ops.md) | 5 | 5 |

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

When two consecutive optimization rounds improve the best geomean by less than 1%, prefer unread PRs and code diffs first. Read at least 50 new code-first sources before prose sources; a PR diff, linked test, benchmark, or changed kernel file counts as a code-first source when it is recorded with a do-not-reread key.

## Refresh Command

```bash
python3 scripts/refresh_pr_knowledge.py --since 2024-05-15
```
