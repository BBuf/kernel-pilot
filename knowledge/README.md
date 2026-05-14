# Kernel Knowledge Base

This directory is a code-first map for GPU kernel optimization. It points Codex
to production kernels, tests, benchmarks, open issues or PRs, and the profiler
signals that are usually relevant for a topic.

The knowledge base is **reference material, not candidate code**. Candidate
kernels should be written as native CUDA C++ (`.cu` / `.cuh`) unless the user
explicitly asks otherwise. Python, Triton, CuTe DSL, CUTLASS, or framework code
can define semantics, shapes, tests, benchmarks, and hypotheses, but should not
be copied into a candidate kernel body.

## Layout

```text
knowledge/
├── index.json
├── references/
│   ├── index.md
│   ├── ako4all/
│   │   ├── ako4all-kernel-loop.md
│   │   ├── cuda-cpp-kernel-reference.md
│   │   ├── cutlass-cpp-kernel-reference.md
│   │   ├── profiling-debugging-reference.md
│   │   └── ...
│   └── frameworks/
│       ├── sglang.md
│       ├── vllm.md
│       ├── tensorrt-llm.md
│       ├── pytorch.md
│       ├── flashinfer.md
│       └── cutlass.md
├── frameworks/
│   ├── sglang.md
│   ├── vllm.md
│   ├── tensorrt-llm.md
│   ├── pytorch.md
│   ├── flash-attention.md
│   ├── flashinfer.md
│   ├── cutlass.md
│   ├── cccl-cub.md
│   ├── triton.md
│   ├── deepgemm.md
│   ├── thunderkittens.md
│   └── tilelang.md
└── topics/
    ├── attention.md
    ├── matmul-gemm.md
    ├── moe.md
    ├── normalization.md
    ├── rope.md
    ├── activation-fusion.md
    ├── sampling.md
    ├── quantization-fp8.md
    ├── kv-cache.md
    └── communication.md
```

## Usage Rules

1. Start from framework pages and topic pages before picking an optimization
   direction.
2. Use `references/index.md` to select deep reference files instead of loading
   the full reference tree.
3. Prefer source code, tests, benchmarks, and open PRs/issues before docs,
   blogs, or articles.
4. Log every source-derived idea with framework, path or URL, hypothesis, and
   measured result.
5. After two consecutive weak rounds (<1% improvement), read at least 50 new
   code-first sources before prose sources, then record a do-not-reread key for
   each source.
6. Keep the source framework repo read-only when the task asks for a standalone
   optimization repo.
