<div align="center">

# KernelPilot

**A Codex + Humanize workflow for GPU kernel tuning: local CUDA knowledge,
Nsight Compute digests, and clean standalone benchmark repos.**

[![GitHub stars](https://img.shields.io/github/stars/BBuf/kernel-pilot?style=social)](https://github.com/BBuf/kernel-pilot/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/BBuf/kernel-pilot?style=social)](https://github.com/BBuf/kernel-pilot/forks)
[![Last commit](https://img.shields.io/github/last-commit/BBuf/kernel-pilot?style=flat-square)](https://github.com/BBuf/kernel-pilot/commits/main)
[![CUDA PR corpus](https://img.shields.io/badge/CUDA_kernel_PRs-607-2ea44f?style=flat-square)](knowledge/references/prs/)
[![Open watchlist](https://img.shields.io/badge/open_PR_watchlist-280-8250df?style=flat-square)](knowledge/references/prs/open-watchlist.md)

**Works well with
[AI-Infra-Auto-Driven-SKILLS](https://github.com/BBuf/AI-Infra-Auto-Driven-SKILLS).**

</div>

KernelPilot is for long GPU-kernel tuning runs, the kind where the useful facts
are easy to lose: which baseline was copied, which shape regressed, what NCU
said, and which source idea has already been tried.

It wraps [Humanize RLCR](https://github.com/PolyArch/humanize) for kernel work.
Codex plans the task, creates a standalone repo, builds candidates, runs tests
and benchmarks, records provenance, profiles representative cases, and lets the
Humanize stop hook decide whether another round is needed.

It is designed to sit next to
[AI-Infra-Auto-Driven-SKILLS](https://github.com/BBuf/AI-Infra-Auto-Driven-SKILLS):
that repo carries broader serving/profiler/SGLang playbooks, while this repo
keeps the kernel-loop machinery and CUDA knowledge pack.

## What Is Here

| Signal | What makes it useful |
| --- | --- |
| **Humanize Kernel Agent Loop** | One Codex skill does the plan, refinement, standalone repo setup, RLCR startup, benchmark/profile loop, and stop-hook review. |
| **607 CUDA optimization PRs** | PR notes from SGLang, vLLM, TensorRT-LLM, FlashAttention, FlashInfer, CUTLASS/CuTe, DeepGEMM, TileLang, CCCL/CUB, and similar repos. |
| **280 open PR watchlist entries** | Current CUDA optimization work is kept separate from merged evidence. Open PRs must be re-checked before use. |
| **Code-first knowledge routing** | Topic pages, source guides, PR notes, blog-to-code maps, and AKO4ALL references tell Codex what to read first. |
| **Nsight Compute feedback loop** | `profile-evidence` turns NCU metrics into a bottleneck call and one next edit. |
| **Clean standalone repos** | Candidate kernels live in isolated repos with their own bindings, tests, benchmarks, ledgers, lineage, and artifacts. |
| **Baseline-aware, language-flexible** | Use CUDA C++/PTX, Triton, CuTe DSL, TileLang, CUTLASS/CuTe, ThunderKittens, or the baseline's own kernel stack unless the user asks for from-scratch work. |

## What You Can Do

| Goal | Start here |
| --- | --- |
| Run a full kernel optimization loop in Codex | [`humanize-kernel-agent-loop`](humanize/skills/humanize-kernel-agent-loop/) |
| Route Codex through CUDA PR/source knowledge before editing | [`kernel-knowledge`](skills/kernel-knowledge/) |
| Turn NCU reports into concrete next kernel edits | [`profile-evidence`](skills/profile-evidence/) |
| Inspect the PR-driven kernel corpus by framework | [`knowledge/references/prs/`](knowledge/references/prs/) |
| Inspect kernel ideas by bottleneck family | [`knowledge/references/prs/by-topic/`](knowledge/references/prs/by-topic/) |
| Use broader serving, profiler, incident, and model optimization skills | [`AI-Infra-Auto-Driven-SKILLS`](https://github.com/BBuf/AI-Infra-Auto-Driven-SKILLS) |

## How The Loop Works

1. **Scoped knowledge pass**: read the target topic, target framework, matching
   source guide, and the PR page only when that repo is PR-driven. Source-only
   repos go straight to source files, tests, and benchmarks.
2. **Standalone setup**: create a fresh repo with torch bindings, correctness
   tests, benchmarks, ledgers, lineage, and profile artifact folders.
3. **Baseline evidence**: run baseline correctness/benchmark and collect one
   representative NCU digest before the first profile-driven edit.
4. **Evidence loop**: implement one candidate, test it, benchmark it, collect
   NCU on regressions/plateaus/surprising wins, and record every attempt.
5. **Review gate**: Humanize RLCR reviews the round and either stops cleanly or
   writes the next round prompt.

After two consecutive weak rounds with less than 1% geomean improvement,
KernelPilot expands the search: read at least 50 new code-first sources before
prose sources and log do-not-reread keys so the next round does not repeat the
same reading.

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
PR scan covers 9 PR-driven CUDA optimization repos. PyTorch, DeepSeek
TileKernels, Triton, QuACK, ThunderKittens, sample repos, blog/code companion
repos, puzzle repos, source catalogs, and any repo with fewer than 10 selected
CUDA optimization PRs are intentionally source-only.

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
  playbooks for serving benchmarks, torch-profiler triage, SGLang optimization,
  production incidents, model PR histories, and GPU-kernel AKO4ALL workflows.
- [Humanize](https://github.com/PolyArch/humanize): the RLCR loop runtime that
  KernelPilot specializes for GPU kernel work.
