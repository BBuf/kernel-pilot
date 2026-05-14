#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
codex_home="${CODEX_HOME:-$HOME/.codex}"
skills_root="$codex_home/skills"

mkdir -p "$skills_root"

rm -rf "$skills_root/kernel-pilot" "$skills_root/kernel-knowledge" "$skills_root/profile-evidence"
cp -R "$repo_root/skills/kernel-knowledge" "$skills_root/kernel-knowledge"
cp -R "$repo_root/skills/profile-evidence" "$skills_root/profile-evidence"

python3 - "$skills_root/kernel-knowledge/SKILL.md" "$repo_root" <<'PY'
from pathlib import Path
import sys

skill_file = Path(sys.argv[1])
repo_root = sys.argv[2]
text = skill_file.read_text(encoding="utf-8")
text = text.replace("{{KERNEL_KNOWLEDGE_ROOT}}", repo_root)
skill_file.write_text(text, encoding="utf-8")
PY

rm -rf "$repo_root/.pytest_cache"
find "$repo_root" -type d -name "__pycache__" -prune -exec rm -rf {} +

echo "Installed Codex skills:"
echo "  $skills_root/kernel-knowledge"
echo "  $skills_root/profile-evidence"
echo
echo "Restart Codex and open /skills to verify."
