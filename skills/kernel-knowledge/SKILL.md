---
name: kernel-knowledge
description: Use when optimizing GPU kernels with Humanize or Codex and the agent should consult the local kernel knowledge pack before planning, choosing optimization directions, or doing plateau research. Covers code-first framework/topic lookup, source provenance, baseline-derived candidates, and user-directed kernel stacks.
---

# Kernel Knowledge

Use this skill as the knowledge layer for GPU-kernel optimization loops. It does
not run the loop; pair it with `humanize-gen-plan`, `humanize-refine-plan`, or
`humanize-rlcr`.

## Knowledge Root

The installer hydrates this path:

```text
{{KERNEL_KNOWLEDGE_ROOT}}
```

If the path is not hydrated, locate the repo containing `knowledge/index.json`
and `references/kernel-source-catalog.md`.

## Required Use

Before writing a plan or choosing a kernel edit:

1. Read `knowledge/README.md`.
2. Read `knowledge/routing/topics/index.md`.
3. Read `knowledge/references/index.md` to choose the detailed reference layer.
4. Pick and read the most relevant topic pages, for example:
   - normalization or fused norm: `knowledge/routing/topics/normalization.md`
   - elementwise fusion: `knowledge/routing/topics/activation-fusion.md`
   - GEMM or tensor cores: `knowledge/routing/topics/matmul-gemm.md`
   - attention or KV cache: `knowledge/routing/topics/attention.md`,
     `knowledge/routing/topics/kv-cache.md`
5. Pick and read relevant framework pages, usually starting with:
   - `knowledge/routing/frameworks/sglang.md` for SGLang work
   - `knowledge/routing/frameworks/vllm.md`, `flashinfer.md`, `flash-attention.md`,
     `cutlass.md`, `deepgemm.md`, `triton.md`, `tilelang.md`,
     `cute-dsl.md`, `quack.md`, `tilekernels.md`, `thunderkittens.md`,
     `veitner-blog.md`, `colfax-research.md`, or `cuda-blog-kernels.md`
     when the topic points there
6. Read the matching PR guide under `knowledge/references/prs/` before prose
   references. Each PR entry records what changed, where it came from, changed
   paths, and the optimization recipe to test. The PR pages keep all filtered
   CUDA optimization PRs, not a curated top-N; each entry must have CUDA/NVIDIA
   target evidence, a real kernel/source change, and an optimization/performance
   mechanism. Search the full relevant page for the kernel family, dtype,
   backend, architecture, and bottleneck terms.
7. If the bottleneck is known but the best source repository is unclear, read
   `knowledge/references/prs/by-topic/index.md` and the matching topic page.
8. Read `knowledge/references/prs/open-watchlist.md` only for volatile current
   ideas, and re-check linked GitHub PRs before trusting code or benchmark
   claims.
9. Read the matching deep source guide under
   `knowledge/references/source-guides/` for PyTorch, TensorRT-LLM, SGLang, vLLM,
   FlashAttention, FlashInfer, CUTLASS, DeepGEMM, Triton, TileLang, CuTe DSL,
   QuACK, DeepSeek TileKernels, ThunderKittens, Veitner blog/code, Colfax
   blog/code, or CUDA blog companion kernels.
10. For implementation/profiling mechanics, read the copied AKO4ALL references:
   - CUDA C++: `knowledge/references/ako4all/cuda-cpp-kernel-reference.md`
   - Triton: `knowledge/references/ako4all/triton-kernel-reference.md`
   - CUTLASS/CuTe prior art:
     `knowledge/references/ako4all/cutlass-cpp-kernel-reference.md`
   - CuTe DSL:
     `knowledge/references/ako4all/cute-dsl-kernel-reference.md`
   - Profiling: `knowledge/references/ako4all/profiling-debugging-reference.md`
   - H100: `knowledge/references/ako4all/architectures/sm90-optimization-guide.md`
11. Read `references/kernel-source-catalog.md` before broader research.
12. During plateau research or when a source is blog-driven, read
   `knowledge/references/blogs/index.md` and the matching blog page before
   opening companion code.

## Research Rules

- Prefer production PRs, code, tests, benchmarks, and open PRs/issues before
  blogs or articles.
- Treat `knowledge/references/prs/` as the primary corpus for CUDA optimization
  optimization ideas. Use source guides and blogs to explain or extend PR/code
  evidence, not as the first stop.
- Read order during plateau expansion is: merged repository PR pages,
  cross-repository by-topic PR pages, open PR watchlist, source guides, then
  blog/code references.
- Candidate implementation language is user-directed. Use CUDA C++/PTX,
  Triton, CuTe DSL, TileLang, CUTLASS/CuTe, ThunderKittens,
  torch.compile/Inductor, or a framework-specific kernel stack when the user or
  baseline calls for it.
- If the user does not specify a language, prefer the active baseline kernel's
  implementation system before inventing a new stack.
- Baseline kernels can seed candidate implementations. Copy or adapt baseline
  code into the standalone repo only when license and attribution allow, and
  record exact source path/URL, commit, license/notice, copied files, and delta
  in the source ledger and lineage.
- If the user explicitly asks for a from-scratch kernel or says not to use the
  baseline implementation, do not copy, adapt, or pattern-match the baseline
  kernel code. Use that baseline only for correctness, benchmark, profiler, and
  API comparison.
- When optimizing a kernel from a framework repo, keep that source checkout
  read-only for standalone work unless the user explicitly asks for an in-place
  patch.
- For standalone optimization work, create a fresh git repo with its own torch
  binding, correctness tests, benchmarks, attempt ledger, optimization ledger,
  and profiling artifacts.

## Loop Ledger Expectations

Record every source-derived idea with:

- source repo or local knowledge file
- exact PR number, path, or URL
- hypothesis tested
- measured result
- do-not-reread key

Only add rows to the optimization ledger for correct versions that improve
performance. Keep a separate attempt ledger for every tried version, including
versions that fail correctness or do not improve speed.

After two consecutive weak rounds (<1% improvement over the prior best), perform
a research expansion before editing again: read at least 50 new code-first
sources before prose sources and log them with do-not-reread keys. Count PR
diffs, changed kernel files, linked tests, and benchmark files as separate
code-first sources only when each one is recorded in the ledger.
