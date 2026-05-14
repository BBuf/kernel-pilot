# KernelPilot

KernelPilot is a Humanize-based kernel agent loop for CUDA optimization. It
vendors a patched [PolyArch/humanize](https://github.com/PolyArch/humanize)
runtime and adds kernel-knowledge plus Nsight Compute profile guidance for
evidence-driven kernel iteration.

Hard rule for KernelPilot-style work: candidate kernels must be naive,
hand-written CUDA C++ in `.cu` / `.cuh`. Triton, CuTe DSL, CUTLASS,
ThunderKittens, torch.compile, library dispatch, and framework DSLs may be used
as references or baselines, but not as candidate implementations.

## Install

```bash
./scripts/install-codex-skills.sh
```

Restart Codex after installation.

If Codex shows `hook needs review`, open **`/hooks`** and approve the Humanize
Stop hook. Use **`/permissions`** to switch to Full Access, then continue after
Codex shows **`Permissions updated to Full Access`**.

This installs:

- patched Humanize skills
- `humanize-kernel-agent-loop`
- `kernel-knowledge`
- `profile-evidence`

`kernel-knowledge` includes copied AKO4ALL CUDA/CUTLASS/NCU references plus
deep source-reading guides for SGLang, vLLM, TensorRT-LLM, PyTorch,
FlashInfer, and CUTLASS.

## Prompt Card

```text
[$humanize-kernel-agent-loop] I want to optimize SGLang's H100 int8_scaled_mm kernel on H100. Keep SGLang read-only as baseline/prior art. Implement candidates only as naive hand-written CUDA C++ in a clean standalone repo.
```

## Monitor

Open another terminal in the same target repo:

```bash
source "${HUMANIZE_RUNTIME_ROOT:-${CODEX_HOME:-$HOME/.codex}/skills/humanize}/scripts/humanize.sh"
humanize monitor rlcr
```

Keep the monitor outside the Codex TUI.
