#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
target_root="${CODEX_HOME:-$HOME/.codex}/skills"

mkdir -p "$target_root"

if [ "$#" -gt 0 ]; then
  skill_dirs=()
  for skill_name in "$@"; do
    skill_dirs+=("$repo_root/skills/$skill_name")
  done
else
  skill_dirs=("$repo_root"/skills/*)
fi

for skill_dir in "${skill_dirs[@]}"; do
  if [ ! -d "$skill_dir" ]; then
    echo "Missing skill directory: $skill_dir" >&2
    exit 1
  fi

  skill_name="$(basename "$skill_dir")"
  destination="$target_root/$skill_name"

  mkdir -p "$destination"
  cp -R "$skill_dir"/. "$destination"/
  echo "Installed $skill_name -> $destination"
done

echo "Done. Restart Codex to reload installed skills."
