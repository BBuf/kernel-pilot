# KernelPilot Knowledge Pack

This repo is the GPU-kernel knowledge pack used by the
[BBuf/humanize](https://github.com/BBuf/humanize) Codex fork.

The active workflow now lives in Humanize as one Codex skill:
`humanize-kernel-rlcr`. It combines plan generation, plan refinement, RLCR
startup, KernelPilot knowledge lookup, Nsight Compute profile guidance, and
plateau research rules. KernelPilot work has one hard implementation constraint:
candidate kernels must be naive, hand-written CUDA C++ in `.cu` / `.cuh`.
Triton, CuTe DSL, CUTLASS, ThunderKittens, torch.compile, library dispatch, and
framework DSLs may be used as references or baselines, but not as candidate
implementations.

This repo remains useful as the source of:

- `knowledge/`: code-first GPU kernel references by topic and framework.
- `references/`: kernel source catalog for kernels, benchmarks, docs, and
  tuning notes.

You do not need to install separate KernelPilot skills for the normal flow; the
Humanize fork bundles the knowledge and profile guidance into
`humanize-kernel-rlcr`.

## Install

Install the Humanize fork for Codex:

```bash
tmp_dir="$(mktemp -d)"
git clone --depth 1 https://github.com/BBuf/humanize.git "$tmp_dir/humanize"
"$tmp_dir/humanize/scripts/install-skills-codex.sh"
```

Restart Codex after installation.

The installer adds:

- `humanize-kernel-rlcr`
- Humanize runtime files and Stop hook
- bundled KernelPilot knowledge and Nsight profile references

If Codex shows `hook needs review`, open **`/hooks`** and approve the Humanize
Stop hook. Use **`/permissions`** to switch to Full Access, then continue after
Codex shows **`Permissions updated to Full Access`**.

## Use In Codex

Open Codex in the target work repo, not in this knowledge-pack repo.

In `/skills`, select only:

```text
humanize-kernel-rlcr
```

Then paste a short task prompt.

## Prompt Card

```text
I want to optimize the SGLang diffusion fused_norm_scale_shift operator on H100.
```

## Monitor

Open another terminal in the same target repo:

```bash
source "${HUMANIZE_RUNTIME_ROOT:-${CODEX_HOME:-$HOME/.codex}/skills/humanize}/scripts/humanize.sh"
humanize monitor rlcr
```

Keep the monitor outside the Codex TUI.
