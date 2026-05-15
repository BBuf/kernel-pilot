# Kernel Knowledge Base

This directory is a PR/source map for GPU kernel optimization. It
points Codex to production pull requests, kernel diffs, tests, benchmarks,
source maps, and the profiler signals that are usually relevant for a topic.
The PR layer keeps all filtered CUDA optimization PRs from the registered
source repositories; it is not capped to a curated top-N list. A PR must carry
CUDA/NVIDIA target evidence, a real kernel/source change, and an
optimization/performance mechanism before it enters this corpus.
PyTorch, DeepSeek TileKernels, sample repos, blog/code companion repos, puzzle
repos, and source catalogs are source-only; inspect their source guides and
current code directly instead of querying PRs.

The knowledge base is both reference material and a route to baseline-derived
candidate code. Candidate kernels should use the implementation system requested
by the user, or the active baseline kernel's system when unspecified: CUDA
C++/PTX, Triton, CuTe DSL, TileLang, CUTLASS/CuTe, ThunderKittens,
torch.compile/Inductor, or another framework-specific kernel stack. Baseline
kernel code may be copied or adapted into the standalone repo when license and
attribution allow; record exact provenance, copied files, and deltas before
mutating it.

## Layout

```text
knowledge/
├── index.json
├── routing/
│   ├── frameworks/
│   │   ├── sglang.md
│   │   ├── vllm.md
│   │   ├── tensorrt-llm.md
│   │   ├── pytorch.md
│   │   ├── flash-attention.md
│   │   ├── flashinfer.md
│   │   ├── cutlass.md
│   │   ├── cccl-cub.md
│   │   ├── triton.md
│   │   ├── deepgemm.md
│   │   ├── thunderkittens.md
│   │   ├── tilelang.md
│   │   ├── cute-dsl.md
│   │   ├── quack.md
│   │   ├── tilekernels.md
│   │   ├── veitner-blog.md
│   │   ├── colfax-research.md
│   │   └── cuda-blog-kernels.md
│   └── topics/
│       ├── attention.md
│       ├── matmul-gemm.md
│       ├── moe.md
│       ├── normalization.md
│       ├── rope.md
│       ├── activation-fusion.md
│       ├── sampling.md
│       ├── quantization-fp8.md
│       ├── kv-cache.md
│       └── communication.md
├── references/
│   ├── index.md
│   ├── prs/
│   │   ├── index.md
│   │   ├── pr-index.json
│   │   ├── pr-scan-cache.json
│   │   ├── open-watchlist.md
│   │   ├── by-topic/
│   │   │   ├── index.md
│   │   │   ├── gemm_quant.md
│   │   │   ├── attention_kv.md
│   │   │   └── ...
│   │   ├── sglang.md
│   │   ├── vllm.md
│   │   ├── tensorrt-llm.md
│   │   ├── flash-attention.md
│   │   ├── flashinfer.md
│   │   ├── cutlass.md
│   │   ├── deepgemm.md
│   │   ├── triton.md
│   │   ├── tilelang.md
│   │   ├── quack.md
│   │   ├── thunderkittens.md
│   │   ├── cccl-cub.md
│   │   ├── tencent-hpc-ops.md
│   │   └── ...
│   ├── blogs/
│   │   ├── index.md
│   │   ├── veitner.md
│   │   ├── colfax.md
│   │   ├── nvidia-cuda.md
│   │   ├── simon-boehm-sgemm.md
│   │   ├── lei-mao-cuda.md
│   │   └── yifan-yang-matmul.md
│   ├── ako4all/
│   │   ├── ako4all-kernel-loop.md
│   │   ├── cuda-cpp-kernel-reference.md
│   │   ├── cutlass-cpp-kernel-reference.md
│   │   ├── profiling-debugging-reference.md
│   │   └── ...
│   └── source-guides/
│       ├── sglang.md
│       ├── vllm.md
│       ├── tensorrt-llm.md
│       ├── pytorch.md
│       ├── flash-attention.md
│       ├── flashinfer.md
│       ├── cutlass.md
│       ├── deepgemm.md
│       ├── triton.md
│       ├── tilelang.md
│       ├── cute-dsl.md
│       ├── quack.md
│       ├── tilekernels.md
│       ├── thunderkittens.md
│       ├── veitner-blog.md
│       ├── colfax-research.md
│       └── cuda-blog-kernels.md
```

## Usage Rules

1. Start from `routing/topics/` and `routing/frameworks/` before picking an
   optimization direction.
2. Use `references/index.md` to select deep reference files instead of loading
   the full reference tree.
3. Read the relevant `references/source-guides/<repo>.md` page. For PR-driven
   production repos, also read `references/prs/<repo>.md` in the same knowledge
   pass. PR diffs explain why optimizations landed; source guides and direct
   code scans show the current implementation, callable wrappers, tests,
   benchmarks, and candidate code locations.
4. For source-only repos such as PyTorch, DeepSeek TileKernels, sample repos,
   blog/code companion repos, puzzle repos, and source catalogs, skip PR lookup
   and inspect source guides plus current source paths directly.
5. If the bottleneck is clearer than the source repository, read
   `references/prs/by-topic/index.md` and the matching topic page.
6. Use `references/prs/open-watchlist.md` only as volatile current context; open
   PRs must be re-checked on GitHub before copying code or trusting benchmark
   claims.
7. Prefer PR/source evidence for PR-driven repos and source-only evidence for
   source-only repos before docs, blogs, or articles.
8. Log every source-derived idea with framework, PR number when available,
   source path or symbol, hypothesis, measured result, and do-not-reread key.
9. After two consecutive weak rounds (<1% improvement), read at least 50 new
   code-first sources before prose sources, then record a do-not-reread key for
   each source.
10. Keep the source framework checkout read-only when the task asks for a
   standalone optimization repo, but copy/adapt the baseline kernel into the
   standalone repo when it is the best starting point and provenance is tracked.
11. If the user explicitly asks for a from-scratch kernel or says not to use the
   baseline implementation, treat baseline kernel code as comparison-only:
   benchmark/profile it, but do not copy, adapt, or pattern-match it.

## Refreshing PR Knowledge

The PR layer is generated from GitHub and can be refreshed with:

```bash
python3 scripts/refresh_pr_knowledge.py --since 2024-05-15
```

The generated cache is kept at `references/prs/pr-scan-cache.json` so the pages
can be regenerated quickly with `--use-cache` after tuning filters or formatting.
