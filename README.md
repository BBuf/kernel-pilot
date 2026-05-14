# Kernel Knowledge Pack

This repo is now a lightweight support pack for Codex kernel work. It does not
run a custom loop. Use the upstream **Humanize** skills for iteration and review,
and use this repo only for:

- `knowledge/`: code-first GPU kernel references by framework and topic.
- `references/`: source catalog for kernels, benchmarks, docs, and tuning notes.
- `kernel-knowledge`: a Codex skill that makes the local knowledge pack visible
  to Humanize-driven kernel optimization loops.
- `profile-evidence`: an Nsight Compute skill for turning `ncu` metrics into one
  concrete next optimization edit.

## Install

Install or refresh the local kernel knowledge and Nsight/profile skills:

```bash
cd <this-repo>
./scripts/install-codex-skills.sh
```

Install Humanize from upstream:

```bash
tmp_dir="$(mktemp -d)" && \
git clone --depth 1 https://github.com/PolyArch/humanize.git "$tmp_dir/humanize" && \
"$tmp_dir/humanize/scripts/install-skills-codex.sh"
```

Restart Codex after installing or refreshing skills.

## Humanize In Codex

Use Humanize from the target work repo, not from this knowledge-pack repo.

1. Open Codex in the repo where the work should happen.
2. In `/skills`, select the Humanize skill for the current step.
3. Add machine/project skills as needed, for example **`h100`**.
4. Add **`kernel-knowledge`** so the loop reads this repo's knowledge pack.
5. Add **`profile-evidence`** when the task needs Nsight Compute analysis.
6. Paste the prompt for that step.

Typical flow:

```text
humanize-gen-plan
Turn this rough kernel optimization request into a concrete implementation plan:
<draft>
```

```text
humanize-refine-plan
Refine this reviewed plan and remove resolved comments:
<plan path or pasted plan>
```

```text
humanize-rlcr
Run the Humanize RLCR loop on:
<plan path>
```

If Codex shows `hook needs review`, open **`/hooks`** and approve the Humanize
Stop hook. Use **`/permissions`** to switch to Full Access, then continue after
**`Permissions updated to Full Access`**.

On newer Codex versions, the upstream installer may still check the old
`codex_hooks` feature name. If `codex features list` shows `hooks true` and
`~/.codex/hooks.json` points to `loop-codex-stop-hook.sh`, the hook install is
already in place.

### Monitor Dashboard

Open another terminal in the same work repo where `.humanize/` was created:

```bash
source "${HUMANIZE_RUNTIME_ROOT:-${CODEX_HOME:-$HOME/.codex}/skills/humanize}/scripts/humanize.sh"
humanize monitor rlcr
```

This shows the Humanize loop dashboard for the latest RLCR session. Keep this
terminal separate from the Codex TUI. Press `Ctrl-C` to stop monitoring.

Other monitors:

```bash
humanize monitor skill   # all skill invocations
humanize monitor codex   # Codex invocations only
```

## Prompt Card

```text
I want to optimize the SGLang diffusion fused_norm_scale_shift operator on H100. Use the humanize-rlcr, h100, kernel-knowledge, and profile-evidence skills.
```
