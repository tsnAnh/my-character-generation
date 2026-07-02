#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
target_root="${CODEX_HOME:-$HOME/.codex}/skills"

mkdir -p "$target_root"

for skill_dir in "$repo_root"/skills/*; do
  [ -d "$skill_dir" ] || continue

  skill_name="$(basename "$skill_dir")"
  destination="$target_root/$skill_name"

  mkdir -p "$destination"
  cp -R "$skill_dir"/. "$destination"/
  echo "Installed $skill_name -> $destination"
done

echo "Done. Restart Codex to reload installed skills."
