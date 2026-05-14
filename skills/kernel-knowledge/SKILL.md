---
name: kernel-knowledge
description: Use when optimizing GPU kernels with Humanize or Codex and the agent should consult the local kernel knowledge pack before planning, choosing optimization directions, or doing plateau research. Covers code-first framework/topic lookup, source provenance, and hard naive CUDA candidate rules.
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
2. Read `knowledge/topics/index.md`.
3. Pick and read the most relevant topic pages, for example:
   - normalization or fused norm: `knowledge/topics/normalization.md`
   - elementwise fusion: `knowledge/topics/activation-fusion.md`
   - GEMM or tensor cores: `knowledge/topics/matmul-gemm.md`
   - attention or KV cache: `knowledge/topics/attention.md`,
     `knowledge/topics/kv-cache.md`
4. Pick and read relevant framework pages, usually starting with:
   - `knowledge/frameworks/sglang.md` for SGLang work
   - `knowledge/frameworks/vllm.md`, `flashinfer.md`, `flash-attention.md`,
     `cutlass.md`, `deepgemm.md`, or `triton.md` when the topic points there
5. Read `references/kernel-source-catalog.md` before broader research.

## Research Rules

- Prefer code, tests, benchmarks, and open PRs/issues before blogs or articles.
- Treat external kernels as prior art. Do not copy tuned kernel bodies.
- Candidate kernels must be naive, hand-written CUDA C++ kernels in `.cu` /
  `.cuh`, even when the baseline is Python, Triton, CuTe DSL, CUTLASS, or
  framework-specific code.
- Do not use Triton, CuTe DSL, CUTLASS, ThunderKittens, torch.compile, library
  dispatch, or framework DSLs as candidate implementations. They may only be
  used as prior art, baseline behavior, or benchmark references.
- When optimizing a kernel from a framework repo, keep that repo read-only unless
  the user explicitly asks for an in-place patch.
- For standalone optimization work, create a fresh git repo with its own torch
  binding, correctness tests, benchmarks, attempt ledger, optimization ledger,
  and profiling artifacts.

## Loop Ledger Expectations

Record every source-derived idea with:

- source repo or local knowledge file
- exact path or URL
- hypothesis tested
- measured result
- do-not-reread key

Only add rows to the optimization ledger for correct versions that improve
performance. Keep a separate attempt ledger for every tried version, including
versions that fail correctness or do not improve speed.

After two consecutive weak rounds (<1% improvement over the prior best), perform
a research expansion before editing again: read at least 50 new code-first
sources before prose sources and log them with do-not-reread keys.
