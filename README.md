# Codex Character Art Skills

Public-ready Codex skills for character art analysis, reference-conditioned character generation, and reference-locked character recasting.

GitHub: https://github.com/tsnAnh/my-character-generation

This repository packages three related skills:

- `analyze-art-drawing`: analyzes illustration technique, medium feel, linework, eye rendering, hair construction, color handling, polish level, and style-transfer constraints.
- `generate-character-from-reference`: generates or compiles prompts for 9:16 mobile portrait character images from a reference image plus a character description, while preserving the reference's visual grammar and replacing the identity with the supplied character.
- `recast-character-in-reference`: treats the supplied image as an edit target and patches only character traits, outfit cues, accessories, and compressed background content into the existing pose, face construction, linework, lighting, and polish level. Includes Mobile portrait mode for forced 9:16 app-safe framing.

## Why This Repo Exists

These skills are designed as a small workflow:

1. Use `analyze-art-drawing` to turn a reference image into a technical style card.
2. Use `generate-character-from-reference` to translate a new character into that style without copying the reference character's identity.
3. Use `recast-character-in-reference` when the source image should behave like an edit target: keep the pose, face construction, hand/crop logic, linework, lighting, and finish, then patch only named character traits.
4. Keep the output disciplined around linework, hair/eye rendering, visible medium behavior, detail density, palette handling, and polish ceiling.

## Install

Clone the repo, then run:

```bash
git clone https://github.com/tsnAnh/my-character-generation.git
cd my-character-generation
./scripts/install.sh
```

The script installs every folder under `skills/` into:

```bash
${CODEX_HOME:-$HOME/.codex}/skills
```

Restart Codex after installing so the skills are discovered.

Install a single skill by passing its folder name:

```bash
./scripts/install.sh analyze-art-drawing
./scripts/install.sh generate-character-from-reference
./scripts/install.sh recast-character-in-reference
```

## Manual Install

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/analyze-art-drawing "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/generate-character-from-reference "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/recast-character-in-reference "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Using Skills In Codex

After installing and restarting Codex:

1. Open a Codex thread.
2. Attach or paste the reference image.
3. Paste the character prompt or visible trait list.
4. Start the request with the skill name, for example `Use $recast-character-in-reference...`.
5. Send the message.

Tip: if copy/paste does not turn `$recast-character-in-reference` into a skill chip, type `$` in the Codex composer and pick the skill from the menu. If it is missing, install the skill and restart Codex.

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

Patch an existing reference image with a character prompt:

```text
Use $recast-character-in-reference with this image and my character prompt. Keep the original pose, face construction, expression, hand placement, linework, lighting, and polish level. Patch only the hair, eyes, visible mark, outfit cues, accessories, and a compressed background cue.
```

Patch for mobile app portrait framing:

```text
Use $recast-character-in-reference in Mobile portrait mode with this image and my character prompt.
```

Use `$recast-character-in-reference` instead of `$generate-character-from-reference` when the source image should stay structurally intact and the task is closer to "change this character into my OC" than "make a new image in this style."

### Full Recast Example

In Codex, attach the reference image, then paste a message like this:

```text
Use $recast-character-in-reference with the attached image as the edit target / structure lock.

Keep the original pose, face construction, expression, hand placement, crop, linework, lighting, rendering method, and polish level. Patch only the visible character traits from my prompt.

Important background rule:
Treat flowers, leaves, vines, props, scenery, and other source-only decoration as background/decor content. They are not character structure locks. Replace or remove them if they do not match my character prompt, while keeping the source background's softness, lighting, and detail density.

Character prompt:
Name: Mira Veyl
Eyes: glossy violet-blue eyes with tiny star-shaped highlights
Hair: long silvery-lavender hair with soft waves and faint moonlit tips
Skin: warm porcelain with rosy shading
Signature mark: tiny constellation mark beneath her left eye
Outfit: cream knit cardigan over a midnight-blue dress
Accessories: moonstone hair clips, pearl earrings, thin silver choker with a tiny star charm
Background: cozy balcony nook above a dreamy twilight city, compressed into one or two faint cues
```

If you want a mobile portrait, say this in the first line instead:

```text
Use $recast-character-in-reference in Mobile portrait mode with the attached image as the edit target / structure lock.
```

For prompt-only output instead of direct generation, add:

```text
Prompt-only mode. Return the patch map, final edit prompt, negative prompt, and QC checklist.
```

## Skill Compliance

The skill folders follow the Codex skill anatomy:

- Each skill folder is named exactly after its `name` field.
- Each skill has a required `SKILL.md` with only `name` and `description` in YAML frontmatter.
- UI metadata lives in `agents/openai.yaml`.
- Long procedural detail lives in `references/` and is loaded by the skill only when needed.
- No extra README, changelog, install guide, or quick-reference files live inside individual skill folders.

Run the repo validator before publishing changes:

```bash
./scripts/validate_skills.py
```

## Repository Layout

```text
.
├── README.md
├── scripts/
│   ├── install.sh
│   └── validate_skills.py
└── skills/
    ├── analyze-art-drawing/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   └── references/art-analysis-framework.md
    ├── generate-character-from-reference/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   └── references/generation-policy.md
    └── recast-character-in-reference/
        ├── SKILL.md
        ├── agents/openai.yaml
        └── references/recast-policy.md
```

## Updating The Public Repo

After editing a skill, validate, commit, and push:

```bash
./scripts/validate_skills.py
git add README.md scripts skills
git commit -m "Update character art skills"
git push
```

## License

No license has been added yet. Add a `LICENSE` file before publishing if you want others to have explicit permission to reuse, modify, or redistribute the skills.
