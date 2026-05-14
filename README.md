# KernelPilot Knowledge Pack

This repo is a GPU-kernel knowledge pack. It is no longer a Humanize fork and it
does not provide `humanize-kernel-rlcr`.

Use the original [PolyArch/humanize](https://github.com/PolyArch/humanize)
Codex skills for RLCR. Use this repo only as reference material for kernel
optimization: code-first knowledge, source catalogs, and Nsight Compute profile
guidance.

Hard rule for KernelPilot-style work: candidate kernels must be naive,
hand-written CUDA C++ in `.cu` / `.cuh`. Triton, CuTe DSL, CUTLASS,
ThunderKittens, torch.compile, library dispatch, and framework DSLs may be used
as references or baselines, but not as candidate implementations.

## Install Humanize

Install upstream Humanize for Codex:

```bash
tmp_dir="$(mktemp -d)"
git clone --branch dev --depth 1 https://github.com/PolyArch/humanize.git "$tmp_dir/humanize"
"$tmp_dir/humanize/scripts/install-skills-codex.sh"
```

Restart Codex after installation.

If Codex shows `hook needs review`, open **`/hooks`** and approve the Humanize
Stop hook. Use **`/permissions`** to switch to Full Access, then continue after
Codex shows **`Permissions updated to Full Access`**.

## Optional Knowledge Skills

To expose this knowledge pack as separate Codex skills:

```bash
./scripts/install-codex-skills.sh
```

That installs:

- `kernel-knowledge`
- `profile-evidence`

## Prompt Card

```text
I want to optimize SGLang's H100 int8_scaled_mm kernel. Use Humanize RLCR. Use this KernelPilot knowledge pack as reference material only, and implement candidate kernels only as naive hand-written CUDA C++.
```

## Monitor

Open another terminal in the same target repo:

```bash
source "${HUMANIZE_RUNTIME_ROOT:-${CODEX_HOME:-$HOME/.codex}/skills/humanize}/scripts/humanize.sh"
humanize monitor rlcr
```

Keep the monitor outside the Codex TUI.
