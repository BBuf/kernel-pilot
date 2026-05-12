# KernelPilot

KernelPilot is a small, stdlib-only framework for agent-driven GPU kernel
optimization. It is designed to work with coding agents such as Codex, Claude
Code, OpenCode, or any comparable agent that can read files, edit code, run
commands, and preserve iteration state.

KernelPilot is inspired by the AVO paper
([arXiv:2603.24517](https://arxiv.org/abs/2603.24517)). The shared idea is to
replace fixed variation operators with an agent loop that reads prior attempts,
consults a curated knowledge base, edits code, runs correctness and performance
checks, and records the outcome. KernelPilot adapts that style of loop for
practical CUDA, Triton, CUTLASS, CuTe, and CuTe DSL kernel work.

## Highlights

- **Agent-neutral workflow**: use the same task files and prompts with Codex,
  Claude Code, OpenCode, or another file-editing coding agent.
- **Single-lineage optimization**: keep one disciplined candidate trajectory per
  operator, including failed attempts and redirect reasons.
- **Correctness-first scoring**: correctness failure gives score zero before any
  latency result is considered.
- **Full-case performance gates**: a candidate must cover every configured case,
  avoid per-case regressions, and reach the target geomean speedup.
- **Reference-only knowledge base**: reference repositories are linked by GitHub
  URL and used for hypotheses, measurement style, and debugging. They are not
  implementation sources to copy from.
- **Target-project separation**: the target repository is supplied per task. It
  can provide wrappers, tests, benchmarks, and integration points, but existing
  optimized target kernels are excluded from candidate input.
- **Stdlib-only core**: the framework itself avoids runtime dependencies, making
  it easy to drop into a clean kernel development environment.

## Core Workflow

1. Define one kernel task with semantic spec, forbidden source files,
   correctness gates, benchmark cases, baseline latency, and target speedup.
2. Generate a focused agent prompt from task metadata, repository references,
   and lineage.
3. Implement one candidate at a time from the semantic spec.
4. Run correctness first, then benchmark every configured case.
5. Record both wins and failed directions so the next iteration has context.

## Prompt Card

> [!TIP]
> **KernelPilot Agent Prompt**
>
> Copy this into Codex, Claude Code, OpenCode, or another coding agent.
>
> ```text
> Use the KernelPilot workflow to continuously optimize one GPU kernel.
>
> - Operator: <kernel operator name or entry point>
> - Target speedup: <for example 1.10x>
> - Target repository: <GitHub repository URL or checked-out worktree for the target project>
> - Target hardware: <optional GPU target; leave unset if not fixed>
> - Runtime environment: <optional user-managed shell, SSH host, CI runner, or other environment>
>
> Requirements:
> 1. Locate the operator entry points, tests, benchmarks, shape/dtype
>    distributions, and current baseline in the target project.
> 2. Create or update a KernelPilot task directory for this operator. Record the
>    semantic spec, forbidden files, correctness gates, benchmark cases,
>    baseline, and lineage.
> 3. Read only approved reference repositories for hypotheses and validation
>    methods. Do not copy external kernel code.
> 4. Implement one from-scratch candidate at a time.
> 5. Run correctness first, then benchmark every configured case.
> 6. Record failed directions in lineage notes before changing direction.
> 7. Finish only when correctness passes, every case is non-regressing, and the
>    geomean speedup reaches the target.
> 8. Final response must include changed files, baseline-vs-candidate table,
>    acceleration source, correctness commands, and benchmark commands.
> ```

The longer template lives in
[templates/kernel-goal-prompt.md](templates/kernel-goal-prompt.md).

## Layout

- `kernelpilot/`: task config loader, prompt builder, lineage store, scoring,
  knowledge-base rendering, and stagnation hints.
- `references/`: method notes plus the repository-link kernel-source catalog
  used as the knowledge base before edits.
- `templates/`: reusable prompts, including the agent goal prompt template.
- `scripts/`: helper scripts for refreshing repository reference metadata.
- `tests/`: focused tests for config loading, prompt generation, scoring,
  lineage, and reference rendering.

Task directories and run artifacts are intentionally user-created inputs. Keep
operator-specific reproductions, lineage, and benchmark results outside the
framework tree unless they are meant to be reviewed as examples.

## Contract

KernelPilot intentionally separates semantics from existing optimized kernel
implementations.

A candidate starts from:

- the operator semantic spec in the task file;
- a trusted reference expression or test oracle;
- benchmark shape and dtype contracts;
- previous lineage entries, if any;
- approved repository references.

A candidate must not copy or pattern-match from the optimized baseline kernel or
the current target implementation. Target-project tests and wrappers may be used
as correctness or integration oracles after the candidate exists.

## Reference Repositories

Print the relevant reference map before editing:

```bash
python -m kernelpilot.cli refs --lane "CUDA C++ JIT"
```

The current catalog includes repository links and URL-based docs/blogs:

- [BBuf/AI-Infra-Auto-Driven-SKILLS gpu-kernel-ako4all references](https://github.com/BBuf/AI-Infra-Auto-Driven-SKILLS/tree/main/skills/gpu-kernel-ako4all/references)
- [NVIDIA/cutlass](https://github.com/NVIDIA/cutlass)
- [NVIDIA/cuda-samples](https://github.com/NVIDIA/cuda-samples)
- [NVIDIA/cccl](https://github.com/NVIDIA/cccl)
- [NVIDIA/CUDALibrarySamples](https://github.com/NVIDIA/CUDALibrarySamples)
- [NVIDIA/cudnn-frontend](https://github.com/NVIDIA/cudnn-frontend)
- [NVIDIA/nvbench](https://github.com/NVIDIA/nvbench)
- [NVIDIA/cuda-tile](https://github.com/NVIDIA/cuda-tile)
- [triton-lang/triton](https://github.com/triton-lang/triton)
- [tile-ai/tilelang](https://github.com/tile-ai/tilelang)
- [gpu-mode/reference-kernels](https://github.com/gpu-mode/reference-kernels)
- [gpu-mode/kernelbot](https://github.com/gpu-mode/kernelbot)
- [gpu-mode/Triton-Puzzles](https://github.com/gpu-mode/Triton-Puzzles)
- [HazyResearch/ThunderKittens](https://github.com/HazyResearch/ThunderKittens)
- [leimao/CUDA-GEMM-Optimization](https://github.com/leimao/CUDA-GEMM-Optimization)
- [ColfaxResearch/cutlass-kernels](https://github.com/ColfaxResearch/cutlass-kernels)
- [moderngpu/moderngpu](https://github.com/moderngpu/moderngpu)
- [huggingface/kernels](https://github.com/huggingface/kernels)
- [flashinfer-ai/flashinfer](https://github.com/flashinfer-ai/flashinfer)
- [Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention)
- [Tencent/hpc-ops](https://github.com/Tencent/hpc-ops)
- [deepseek-ai/DeepGEMM](https://github.com/deepseek-ai/DeepGEMM)
- [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/)
- [CUDA C++ Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)
- [PTX ISA](https://docs.nvidia.com/cuda/parallel-thread-execution/)
- [Nsight Compute Profiling Guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/)
- [Blackwell Tuning Guide](https://docs.nvidia.com/cuda/blackwell-tuning-guide/index.html)
- [Hopper Tuning Guide](https://docs.nvidia.com/cuda/hopper-tuning-guide/index.html)
- [Ampere Tuning Guide](https://docs.nvidia.com/cuda/ampere-tuning-guide/index.html)
- [NVIDIA Developer Blog CUDA articles](https://developer.nvidia.com/blog/tag/cuda/)
- [Colfax Research](https://research.colfax-intl.com/)
- [Simon Boehm CUDA Matmul](https://siboehm.com/articles/22/CUDA-MMM)
- [Lei Mao CUDA Programming](https://leimao.github.io/blog/CUDA-Programming/)
- [Yifan Yang CUDA Matmul](https://yang-yifan.github.io/blogs/reg_tile/reg_tile.html)

The target project is supplied per task or prompt. It is not part of the
reference repository catalog.

## Minimal Use

Validate a task set:

```bash
python -m kernelpilot.cli validate \
  --taskset <taskset.json>
```

Generate the next iteration prompt for a task:

```bash
python -m kernelpilot.cli prompt \
  --taskset <taskset.json> \
  --task <task-id>
```

Compare a candidate benchmark JSON against the matching baseline:

```bash
python -m kernelpilot.cli compare \
  --taskset <taskset.json> \
  --task <task-id> \
  --result <candidate-result.json>
```

Expected candidate result format:

```json
{
  "correct": true,
  "measurements": [
    {"case_id": "n=4194304", "latency_us": 10.9}
  ]
}
```
