#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

skill_dir="$PROJECT_ROOT/skills/ncu-report"
skill_file="$skill_dir/SKILL.md"
metrics_file="$skill_dir/references/metrics.md"
examples_file="$skill_dir/references/examples.md"
script_file="$skill_dir/scripts/ncu_report_digest.py"
install_script="$PROJECT_ROOT/scripts/install-skill.sh"
kernel_skill="$PROJECT_ROOT/skills/humanize-kernel-agent-loop/SKILL.md"

fail() {
    echo "FAIL: $*" >&2
    exit 1
}

[[ -f "$skill_file" ]] || fail "missing ncu-report skill"
[[ -f "$metrics_file" ]] || fail "missing ncu-report metrics reference"
[[ -f "$examples_file" ]] || fail "missing ncu-report examples reference"
[[ -f "$script_file" ]] || fail "missing ncu-report digest helper"

grep -q '"ncu-report"' "$install_script" \
    || fail "install script does not install ncu-report"
grep -q 'kernel-knowledge' "$install_script" \
    || fail "install script does not install kernel-knowledge"
grep -q 'sync_kernel_knowledge_skill' "$install_script" \
    || fail "install script does not sync the KernelPilot knowledge skill"
grep -q 'validate_kernelpilot_root' "$install_script" \
    || fail "install script does not require a valid KernelPilot root"
grep -q 'KernelPilot PR evidence bundles not found' "$install_script" \
    || fail "install script does not validate PR evidence bundle path"
grep -q 'profile first, diagnose second, optimize third' "$skill_file" \
    || fail "skill does not encode profiling-grounded rule"
grep -q 'SourceCounters' "$skill_file" \
    || fail "skill does not require source-correlated counters"
grep -q 'PmSampling' "$skill_file" \
    || fail "skill does not require PM sampling evidence"
grep -q 'PTX / SASS Analysis' "$skill_file" \
    || fail "skill does not include PTX/SASS analysis"
grep -q 'report.ncu-rep' "$skill_file" \
    || fail "skill does not preserve ncu report artifacts"
grep -q 'exactly one next edit' "$skill_file" \
    || fail "skill does not force a single concrete edit"
grep -q 'smsp__warp_issue_stalled_long_scoreboard' "$metrics_file" \
    || fail "metrics reference lacks long scoreboard metric"
grep -q 'smsp__warp_issue_stalled_short_scoreboard' "$metrics_file" \
    || fail "metrics reference lacks short scoreboard metric"
grep -q 'sm__inst_executed_pipe_tensor' "$metrics_file" \
    || fail "metrics reference lacks tensor pipe metric"
grep -q 'l1tex__data_bank_conflicts' "$metrics_file" \
    || fail "metrics reference lacks shared bank conflict metric"
grep -q 'Blackwell Pipeline Bubble Check' "$examples_file" \
    || fail "examples lack Blackwell pipeline bubble flow"
grep -q 'cuobjdump --dump-ptx' "$examples_file" \
    || fail "examples lack PTX extraction"
grep -q 'nvdisasm' "$examples_file" \
    || fail "examples lack SASS disassembly"
grep -q 'ncu_report_digest.py' "$examples_file" \
    || fail "examples do not show digest helper usage"
grep -q 'ncu-report' "$kernel_skill" \
    || fail "kernel agent loop does not call ncu-report"

python3 -m py_compile "$script_file"

echo "PASS: ncu-report skill is wired"
