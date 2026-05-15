# KernelPilot

KernelPilot is a Humanize-based kernel agent loop for GPU kernel optimization. It
vendors a patched [PolyArch/humanize](https://github.com/PolyArch/humanize)
runtime and adds kernel-knowledge plus Nsight Compute profile guidance for
evidence-driven kernel iteration.

KernelPilot keeps optimization work in a clean standalone repo, but it does not
force one kernel language. Use the implementation system the user asks for, or
the baseline's system when the user does not specify one: CUDA C++/PTX, Triton,
CuTe DSL, TileLang, CUTLASS/CuTe, ThunderKittens, torch.compile/Inductor, or
another framework-specific kernel stack. The baseline kernel is a valid starting
point: copy or adapt it into the standalone repo when license and attribution
allow, then track provenance, deltas, benchmarks, profiles, and lineage.
If the user explicitly asks for a from-scratch kernel or says not to use the
baseline implementation, treat the baseline only as a correctness/performance
comparison target and do not copy, adapt, or pattern-match its kernel code.

## Install

Fresh install:

```bash
git clone https://github.com/BBuf/kernel-pilot.git
cd kernel-pilot
./scripts/install-codex-skills.sh
```

Update an existing checkout:

```bash
git pull --ff-only
./scripts/install-codex-skills.sh
```

Restart Codex after installation, then open `/skills` and check that these
skills are visible:

- `humanize-kernel-agent-loop`
- `kernel-knowledge`
- `profile-evidence`

If Codex shows `hook needs review`, open **`/hooks`** and approve the Humanize
Stop hook. Use **`/permissions`** to switch to Full Access, then continue after
Codex shows **`Permissions updated to Full Access`**.

This installs:

- patched Humanize skills
- `humanize-kernel-agent-loop`
- `kernel-knowledge`
- `profile-evidence`

`kernel-knowledge` includes copied AKO4ALL CUDA/CUTLASS/NCU references plus a
PR-driven production knowledge layer. The current scan covers 32 CUDA-kernel
sources, including SGLang, vLLM, TensorRT-LLM, PyTorch, FlashAttention,
FlashInfer, CUTLASS/CuTe, DeepGEMM, Triton, TileLang, QuACK, DeepSeek
TileKernels, ThunderKittens, CCCL/CUB, CUDA samples, CUDA library samples,
cuDNN frontend, NVBench, GPU Mode reference kernels and KernelBot, NVIDIA
Developer Blog code samples, Lei Mao GEMM, Simon Boehm SGEMM, Colfax code,
ModernGPU, Hugging Face kernels, and Tencent hpc-ops.
The knowledge layout is split into `knowledge/routing/` for lightweight topic
and source routing, `knowledge/references/prs/` for PR case notes,
`knowledge/references/source-guides/` for code maps, and
`knowledge/references/blogs/` for article-to-code maps.
The PR layer keeps all filtered CUDA-kernel PRs, not a small curated top-N. It
also has cross-repository topic pages and an open PR watchlist.
Refresh it with `python3 scripts/refresh_pr_knowledge.py --since 2024-05-15`.

## Prompt Card

Baseline-derived optimization:

```text
[$humanize-kernel-agent-loop] I want to optimize SGLang's H100 int8_scaled_mm kernel on H100. Use the existing SGLang/CUTLASS kernel as the baseline and starting point. Work in a clean standalone repo, keep provenance/lineage, and use the most appropriate kernel language for the candidate.
```

From-scratch optimization:

```text
[$humanize-kernel-agent-loop] I want to optimize SGLang's H100 int8_scaled_mm kernel on H100. Implement the candidate kernel from scratch and use the existing SGLang/CUTLASS kernel only as the correctness/performance comparison baseline. Work in a clean standalone repo and keep provenance/lineage.
```

## Monitor

Open another terminal in the same target repo:

```bash
source "${HUMANIZE_RUNTIME_ROOT:-${CODEX_HOME:-$HOME/.codex}/skills/humanize}/scripts/humanize.sh"
humanize monitor rlcr
```

Keep the monitor outside the Codex TUI.
