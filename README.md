# Codex Character Art Skills

Public-ready Codex skills for character art analysis, reference-conditioned character generation, and reference-locked character recasting.

GitHub: https://github.com/tsnAnh/my-character-generation

This repository packages four related skills:

- `analyze-art-drawing`: analyzes illustration technique, medium feel, linework, eye rendering, hair construction, color handling, polish level, and style-transfer constraints.
- `compose-new-char-from-reference`: composes a new original Mero character JSON object from a pasted reference character plus optional idea/hint text, then returns an `IMAGE_RECAST_HANDOFF` for image prompting and a short composition diff summary.
- `generate-character-from-reference`: generates or compiles prompts for 9:16 mobile portrait character images from a reference image plus a character description, while preserving the reference's visual grammar and replacing the identity with the supplied character.
- `recast-character-in-reference`: treats the supplied image as an edit target and patches only character traits, outfit cues, accessories, and compressed background content into the existing pose, face construction, linework, lighting, and polish level. Includes Mobile portrait mode for forced 9:16 app-safe framing and a body-wide anatomy QC gate before final output.

## Why This Repo Exists

These skills are designed as a small workflow:

1. Use `analyze-art-drawing` to turn a reference image into a technical style card.
2. Use `compose-new-char-from-reference` to create a new original character card and compact visible-trait handoff from a source character.
3. Use `generate-character-from-reference` to translate a new character into that style without copying the reference character's identity.
4. Use `recast-character-in-reference` when the source image should behave like an edit target: keep the pose, face construction, body/crop logic, linework, lighting, and finish, then patch only named character traits.
5. Keep the output disciplined around linework, hair/eye rendering, visible medium behavior, detail density, palette handling, and polish ceiling.

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
./scripts/install.sh compose-new-char-from-reference
./scripts/install.sh generate-character-from-reference
./scripts/install.sh recast-character-in-reference
```

## Manual Install

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/analyze-art-drawing "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/compose-new-char-from-reference "${CODEX_HOME:-$HOME/.codex}/skills/"
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

Compose a new character card from a pasted reference:

```text
Use $compose-new-char-from-reference, <paste character reference>.
Idea/hint: heterochromia, asymmetrical scholar coat, silver-black hair, moth-like species traits.
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
Use $recast-character-in-reference with this image and my character prompt. Keep the original pose, face construction, expression, body placement/crop logic, linework, lighting, and polish level. Repair malformed visible anatomy if the reference or output has flawed eyes, face, shoulders, torso, limbs, hands, feet, or joints. Patch only the hair, eyes, non-face visible trait, outfit cues, accessories, and a compressed background cue.
```

Patch for mobile app portrait framing:

```text
Use $recast-character-in-reference in Mobile portrait mode with this image and my character prompt.
```

Mobile portrait rule: when the request says Mobile portrait mode, mobile portrait, app avatar, phone wallpaper, or 9:16, the skill handles 9:16 output and app-safe face placement. You do not need to spell out the framing rules in the prompt.

Use `$recast-character-in-reference` instead of `$generate-character-from-reference` when the source image should stay structurally intact and the task is closer to "change this character into my OC" than "make a new image in this style."

## Prompt Guidance

For character cards, `compose-new-char-from-reference` returns only three blocks: raw Mero JSON, `IMAGE_RECAST_HANDOFF`, and `COMPOSITION_DIFF_SUMMARY`. The handoff is intentionally compact so it can be pasted into `recast-character-in-reference` without carrying lore, personality text, or a long character-sheet inventory into the image prompt.

Hair needs two separate controls:

- Strand density: keep hair as broad clumps or masses when the reference is mass-first. Avoid strand-by-strand rendering, dense flyaways, glossy string hair, and many thin separated locks.
- Fill texture/noise: recolor hair with broad source-style shadow/highlight masses and low-frequency paint/fill texture. Preserve only source-matched grain at the original scale. Avoid speckled color static, noisy dither, peppered value flecks, micro-streaks, glittery highlight crumbs, crunchy compression-like fill, or over-sharpened AI hair texture.

Useful recast prompt line:

```text
Hair fill budget: recolor hair with broad source-style shadow/highlight masses and low-frequency paint/fill texture. Preserve only source-matched grain at the original scale. Avoid speckled color static, noisy dither, micro-streaks, glittery highlight crumbs, crunchy compression-like fill, or over-sharpened AI hair texture.
```

Body placement is a structure lock, but anatomy mistakes are not. If the source or output has malformed visible anatomy, prompt the recast to keep the same pose/crop while repairing eyes, pupils, face, nose, mouth, neck, shoulders, chest/torso, arms, wrists, hands, fingers, hips, legs, feet, joints, proportions, and silhouette in the source style. A visible hand should have five plausible fingers, or the fifth finger should be naturally hidden by overlap, sleeve/cuff, shadow, angle, or crop. Keep cuff embroidery, jewelry, hair, rain, magic effects, background lines, and highlights from reading as stray body parts.

Do not invent face scars, face marks, facial tattoos, birthmarks, cheek symbols, forehead marks, or under-eye symbols by default. Use clothing, jewelry, hair, fabric texture, body marks, collarbone marks, hand marks, or species silhouette for signature details. If the user explicitly asks for a face mark, make it subtle, flat, low-contrast, and integrated into the source face rendering rather than a sticker-like icon on top of the skin.

Keep negative prompts short in `compose-new-char-from-reference`; focus on common AI failures such as bad hands, malformed eyes, deformed anatomy, text, watermark, over-smooth AI polish, noisy hair fill, and unsafe explicit content. `recast-character-in-reference` handles the detailed source locks, anti-copy constraints, hair guards, and body-wide anatomy QC.

### Full Recast Example

In Codex, attach the reference image, then paste a message like this:

```text
Use $recast-character-in-reference with the attached image as the edit target / structure lock.

Keep the original pose, face construction, expression, body placement, crop, linework, lighting, rendering method, and polish level. Patch only the visible character traits from my prompt.

Important background rule:
Treat flowers, leaves, vines, props, scenery, and other source-only decoration as background/decor content. They are not character structure locks. Replace or remove them if they do not match my character prompt, while keeping the source background's softness, lighting, and detail density.

Character prompt:
Name: Mira Veyl
Eyes: glossy violet-blue eyes with tiny star-shaped highlights
Hair: long silvery-lavender hair in broad soft waves, minimal individual strands, broad source-style shadow/highlight masses, source-matched grain only, no speckled/dithered/micro-streak hair texture
Skin: warm porcelain with rosy shading
Signature detail: tiny constellation embroidery on the collar clasp, not on the face
Outfit: cream knit cardigan over a midnight-blue dress
Accessories: moonstone hair clips, pearl earrings, thin silver choker with a tiny star charm
Background: cozy balcony nook above a dreamy twilight city, compressed into one or two faint cues

Body-wide anatomy guard:
Keep the original pose/body placement/crop, but repair malformed visible anatomy in the same source style. Eyes, pupils, face, nose, mouth, neck, shoulders, chest/torso, arms, wrists, hands, fingers, hips, legs, feet, joints, proportions, and silhouette must read plausibly wherever visible. Five fingers should be visible on a visible hand, or the fifth finger should be naturally hidden by overlap, sleeve/cuff, shadow, angle, or crop. Do not let jewelry, embroidery, hair, rain, magic, background lines, or white highlights read as stray anatomy.
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
    ├── compose-new-char-from-reference/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   └── references/
    │       ├── mero_character_schema.md
    │       └── composition-policy.md
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
