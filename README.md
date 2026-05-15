<div align="center">

# KernelPilot

**Humanize-powered GPU kernel agent loops with PR-driven kernel knowledge,
Nsight Compute evidence, and clean standalone optimization repos.**

[![GitHub stars](https://img.shields.io/github/stars/BBuf/kernel-pilot?style=social)](https://github.com/BBuf/kernel-pilot/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/BBuf/kernel-pilot?style=social)](https://github.com/BBuf/kernel-pilot/forks)
[![Last commit](https://img.shields.io/github/last-commit/BBuf/kernel-pilot?style=flat-square)](https://github.com/BBuf/kernel-pilot/commits/main)
[![CUDA PR corpus](https://img.shields.io/badge/CUDA_kernel_PRs-2840-2ea44f?style=flat-square)](knowledge/references/prs/)
[![Open watchlist](https://img.shields.io/badge/open_PR_watchlist-1079-8250df?style=flat-square)](knowledge/references/prs/open-watchlist.md)

**Part of the same AI-infra agent ecosystem as
[AI-Infra-Auto-Driven-SKILLS](https://github.com/BBuf/AI-Infra-Auto-Driven-SKILLS).**

</div>

KernelPilot is for engineers who want an agent to keep optimizing a real GPU
kernel after the first obvious rewrite is done.

It turns [Humanize RLCR](https://github.com/PolyArch/humanize) into a
kernel-specialized loop: plan, refine, build a clean standalone repo, implement
candidates, run correctness tests, benchmark, collect Nsight Compute evidence,
record provenance, and continue from review feedback. The point is not another
prompt template. The point is to give Codex the memory, process, and profiler
discipline needed to do kernel work without constant human steering.

If [AI-Infra-Auto-Driven-SKILLS](https://github.com/BBuf/AI-Infra-Auto-Driven-SKILLS)
is the agent playbook pack for serving, profiler triage, SGLang operations, and
model-family PR intelligence, KernelPilot is the autonomous kernel optimization
lab that plugs into that ecosystem.

If this saves you one failed benchmark loop, one lost NCU insight, or one
forgotten upstream kernel PR, a star helps more AI-infra engineers find it.

## Why Star It

| Signal | What makes it useful |
| --- | --- |
| **Humanize Kernel Agent Loop** | One Codex skill handles planning, refinement, standalone repo setup, RLCR startup, benchmark/profile iteration, and review-gated progress. |
| **634 CUDA optimization PRs** | Production PR knowledge from PR-driven repos such as SGLang, vLLM, TensorRT-LLM, FlashAttention, FlashInfer, CUTLASS/CuTe, DeepGEMM, Triton, TileLang, QuACK, ThunderKittens, CCCL/CUB, and more. |
| **313 open PR watchlist entries** | Fresh CUDA optimization ideas from PR-driven repos are tracked separately from merged evidence, so agents can explore current work without confusing it with production truth. |
| **Code-first knowledge routing** | Topic pages, source guides, PR notes, blog-to-code maps, and AKO4ALL references tell the agent what to read before choosing an optimization direction. |
| **Nsight Compute feedback loop** | `profile-evidence` converts NCU metrics into bottleneck classifications, regression explanations, and one concrete next edit. |
| **Clean standalone repos** | Candidate kernels live in isolated repos with their own bindings, tests, benchmarks, ledgers, lineage, and artifacts. |
| **Baseline-aware, language-flexible** | Use CUDA C++/PTX, Triton, CuTe DSL, TileLang, CUTLASS/CuTe, ThunderKittens, or the baseline's own kernel stack unless the user asks for from-scratch work. |

## What You Can Do

| Goal | Start here |
| --- | --- |
| Run an end-to-end autonomous kernel optimization loop in Codex | [`humanize-kernel-agent-loop`](humanize/skills/humanize-kernel-agent-loop/) |
| Route an agent through CUDA PR/source knowledge before editing | [`kernel-knowledge`](skills/kernel-knowledge/) |
| Turn NCU reports into concrete next kernel edits | [`profile-evidence`](skills/profile-evidence/) |
| Inspect the PR-driven kernel corpus by framework | [`knowledge/references/prs/`](knowledge/references/prs/) |
| Inspect kernel ideas by bottleneck family | [`knowledge/references/prs/by-topic/`](knowledge/references/prs/by-topic/) |
| Use broader serving, profiler, incident, and model optimization skills | [`AI-Infra-Auto-Driven-SKILLS`](https://github.com/BBuf/AI-Infra-Auto-Driven-SKILLS) |

## How The Loop Works

1. **Knowledge pass**: read topic/framework routing, then inspect source guides
   plus PR pages for PR-driven repos; source-only repos use code guides and
   source scans directly.
2. **Standalone setup**: create a fresh repo with torch bindings, correctness
   tests, benchmarks, ledgers, lineage, and profile artifact folders.
3. **Evidence loop**: implement one candidate, test it, benchmark it, collect
   NCU when useful, and record every attempt.
4. **Review gate**: Humanize RLCR reviews the round and either stops cleanly or
   emits the next round prompt.

After two consecutive weak rounds with less than 1% geomean improvement,
KernelPilot forces a research expansion: read at least 50 new code-first
sources before prose sources and log do-not-reread keys so long-context loss
does not erase what the agent already learned.

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

## Knowledge Base

`kernel-knowledge` includes copied AKO4ALL CUDA/CUTLASS/NCU references plus a
PR-driven production knowledge layer plus source-only code guides. The current
PR scan covers 13 PR-driven CUDA optimization repos; PyTorch, DeepSeek
TileKernels, sample repos, blog/code companion repos, puzzle repos, and source
catalogs are intentionally source-only.

The knowledge layout is split into:

- `knowledge/routing/` for lightweight topic and source routing
- `knowledge/references/prs/` for PR case notes
- `knowledge/references/source-guides/` for code maps
- `knowledge/references/blogs/` for article-to-code maps

The PR layer keeps all filtered CUDA optimization PRs for PR-driven repos, not a
small curated top-N. It also has cross-repository topic pages and an open PR
watchlist.

Refresh it with:

```bash
python3 scripts/refresh_pr_knowledge.py --since 2024-05-15
```

## Prompt Cards

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

## Related

- [AI-Infra-Auto-Driven-SKILLS](https://github.com/BBuf/AI-Infra-Auto-Driven-SKILLS):
  agent-ready playbooks for serving benchmarks, torch-profiler triage, SGLang
  optimization, production incidents, model PR histories, and GPU-kernel
  AKO4ALL workflows.
- [Humanize](https://github.com/PolyArch/humanize): the RLCR loop runtime that
  KernelPilot specializes for GPU kernel work.
