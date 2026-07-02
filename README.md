# Codex Character Art Skills

Public-ready Codex skills for character art analysis and reference-conditioned character generation.

This repository packages two related skills:

- `analyze-art-drawing`: analyzes illustration technique, medium feel, linework, eye rendering, hair construction, color handling, polish level, and style-transfer constraints.
- `generate-character-from-reference`: generates or compiles prompts for 9:16 mobile portrait character images from a reference image plus a character description, while preserving the reference's visual grammar and replacing the identity with the supplied character.

## Why This Repo Exists

These skills are designed as a small workflow:

1. Use `analyze-art-drawing` to turn a reference image into a technical style card.
2. Use `generate-character-from-reference` to translate a new character into that style without copying the reference character's identity.
3. Keep the output disciplined around linework, hair/eye rendering, visible medium behavior, detail density, palette handling, and polish ceiling.

## Install

Clone the repo, then run:

```bash
./scripts/install.sh
```

The script installs every folder under `skills/` into:

```bash
${CODEX_HOME:-$HOME/.codex}/skills
```

Restart Codex after installing so the skills are discovered.

## Manual Install

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/analyze-art-drawing "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/generate-character-from-reference "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Usage Examples

Analyze a reference image:

```text
Use $analyze-art-drawing to analyze this character art in Vietnamese. Focus on linework, hair construction, eye rendering, medium/material cues, polish level, and style-transfer locks.
```

Generate a new character from a reference:

```text
Use $generate-character-from-reference with this reference image and this character description. Generate a 9:16 mobile portrait. Preserve the reference art style, pose feeling, linework fingerprint, hair/eye rendering method, visible medium behavior, and polish level.
```

Prompt-only mode:

```text
Use $generate-character-from-reference in prompt-only mode. Return the reference visual grammar, filtered character appearance, final image prompt, negative prompt, and QC checklist.
```

## Repository Layout

```text
.
├── README.md
├── scripts/
│   └── install.sh
└── skills/
    ├── analyze-art-drawing/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   └── references/art-analysis-framework.md
    └── generate-character-from-reference/
        ├── SKILL.md
        ├── agents/openai.yaml
        └── references/generation-policy.md
```

## Publishing To GitHub

After committing locally, create a public GitHub repository and push:

```bash
git branch -M main
git remote add origin git@github.com:<your-user>/<repo-name>.git
git push -u origin main
```

Or with GitHub CLI:

```bash
gh repo create <repo-name> --public --source=. --remote=origin --push
```

## License

No license has been added yet. Add a `LICENSE` file before publishing if you want others to have explicit permission to reuse, modify, or redistribute the skills.
