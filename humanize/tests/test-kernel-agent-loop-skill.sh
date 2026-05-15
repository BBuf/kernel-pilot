#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

skill_file="$PROJECT_ROOT/skills/humanize-kernel-agent-loop/SKILL.md"
install_script="$PROJECT_ROOT/scripts/install-skill.sh"

fail() {
    echo "FAIL: $*" >&2
    exit 1
}

[[ -f "$skill_file" ]] || fail "missing kernel agent loop skill"

grep -q 'humanize-kernel-agent-loop' "$install_script" \
    || fail "install script does not install humanize-kernel-agent-loop"
grep -q -- '--kernelpilot-root' "$install_script" \
    || fail "install script cannot hydrate KernelPilot root"

grep -q 'Candidate implementation language is user-directed' "$skill_file" \
    || fail "skill does not support user-directed candidate stacks"
grep -q 'baseline kernel can be the starting point' "$skill_file" \
    || fail "skill does not allow baseline-derived candidates"
grep -q 'from-scratch kernel' "$skill_file" \
    || fail "skill does not honor from-scratch baseline exclusion"
grep -q 'comparison-only' "$skill_file" \
    || fail "skill does not make excluded baselines comparison-only"
grep -q 'kernel-knowledge' "$skill_file" \
    || fail "skill does not use kernel-knowledge naming"
if grep -q 'Kernel''Wiki' "$skill_file"; then
    fail "skill still uses old kernel knowledge naming"
fi
grep -q 'Nsight Compute' "$skill_file" \
    || fail "skill does not require Nsight Compute evidence"
grep -q '50 new code-first sources' "$skill_file" \
    || fail "skill does not require plateau research expansion"
grep -q 'by-topic/index.md' "$skill_file" \
    || fail "skill does not route cross-repository PR topic pages"
grep -q 'open-watchlist.md' "$skill_file" \
    || fail "skill does not mention open PR watchlist"
grep -q 'artifacts/lineage.jsonl' "$skill_file" \
    || fail "skill does not require lineage tracking"
grep -q 'setup-rlcr-loop.sh' "$skill_file" \
    || fail "skill does not start Humanize RLCR"

echo "PASS: kernel agent loop skill is wired"
