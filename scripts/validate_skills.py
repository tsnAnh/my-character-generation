#!/usr/bin/env python3
"""Validate this repository's Codex skill bundle."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}$")
FORBIDDEN_SKILL_DOCS = {
    "README.md",
    "INSTALLATION_GUIDE.md",
    "QUICK_REFERENCE.md",
    "CHANGELOG.md",
}


def parse_frontmatter(skill_md: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    text = skill_md.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not lines or lines[0].strip() != "---":
        return {}, ["SKILL.md must start with YAML frontmatter"]

    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        return {}, ["SKILL.md frontmatter must close with ---"]

    metadata: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:end], start=2):
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"Invalid frontmatter line {line_number}: {line}")
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")

    return metadata, errors


def validate_agent_metadata(skill_dir: Path, skill_name: str) -> list[str]:
    errors: list[str] = []
    agent_file = skill_dir / "agents" / "openai.yaml"

    if not agent_file.exists():
        return ["Missing agents/openai.yaml"]

    text = agent_file.read_text(encoding="utf-8")
    required_fields = [
        "display_name:",
        "short_description:",
        "default_prompt:",
    ]
    for field in required_fields:
        if field not in text:
            errors.append(f"agents/openai.yaml missing {field}")

    if f"${skill_name}" not in text:
        errors.append("agents/openai.yaml default_prompt must mention the skill as $skill-name")

    return errors


def validate_reference_links(skill_dir: Path, skill_md: Path) -> list[str]:
    errors: list[str] = []
    text = skill_md.read_text(encoding="utf-8")
    links = re.findall(r"\]\((references/[^)]+)\)", text)

    for link in links:
        if not (skill_dir / link).exists():
            errors.append(f"Referenced file does not exist: {link}")

    return errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_name = skill_dir.name
    skill_md = skill_dir / "SKILL.md"

    if not NAME_RE.fullmatch(skill_name):
        errors.append("Skill folder name must be lowercase hyphen-case under 64 chars")

    if not skill_md.exists():
        return errors + ["Missing SKILL.md"]

    metadata, frontmatter_errors = parse_frontmatter(skill_md)
    errors.extend(frontmatter_errors)

    allowed_keys = {"name", "description"}
    extra_keys = set(metadata) - allowed_keys
    missing_keys = allowed_keys - set(metadata)

    if extra_keys:
        errors.append(f"Unexpected frontmatter keys: {', '.join(sorted(extra_keys))}")
    if missing_keys:
        errors.append(f"Missing frontmatter keys: {', '.join(sorted(missing_keys))}")
    if metadata.get("name") != skill_name:
        errors.append(f"Frontmatter name must match folder name: {skill_name}")
    if not metadata.get("description", "").strip():
        errors.append("Frontmatter description must be non-empty")

    for forbidden in FORBIDDEN_SKILL_DOCS:
        if (skill_dir / forbidden).exists():
            errors.append(f"Do not include {forbidden} inside skill folders")

    errors.extend(validate_reference_links(skill_dir, skill_md))
    errors.extend(validate_agent_metadata(skill_dir, skill_name))

    return errors


def main() -> int:
    if not SKILLS_DIR.exists():
        print("Missing skills/ directory", file=sys.stderr)
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        print("No skill folders found", file=sys.stderr)
        return 1

    failed = False
    for skill_dir in skill_dirs:
        errors = validate_skill(skill_dir)
        if errors:
            failed = True
            print(f"FAIL {skill_dir.relative_to(ROOT)}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {skill_dir.relative_to(ROOT)}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
