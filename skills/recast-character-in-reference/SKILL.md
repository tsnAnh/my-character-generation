---
name: recast-character-in-reference
description: Recast or patch a supplied character reference image using a character prompt while preserving the original image's pose, face proportion fingerprint, facial-feature construction, expression, hand/crop logic, linework, lighting, rendering method, medium/material behavior, detail density, polish ceiling, and background style. Use when the user wants imagegen to edit the reference character by changing only identity traits, hair color, eye color, skin tone, visible marks, outfit cues, accessories, and compressed background content instead of generating a new character from scratch. Especially useful for "change the outfit", "make this reference into my OC", "patch these character traits into this image", "keep the art/pose/face but replace hair/eyes/clothes/accessories/background", or avoiding fantasy-glowy redraw drift.
---

# Recast Character In Reference

## Core Behavior

Use this skill for reference-locked character edits. Treat the supplied image as the edit target, not merely a style reference. The goal is to keep the original drawing structure and patch in the character prompt's visible traits.

This skill is stricter than `generate-character-from-reference`:

- `generate-character-from-reference` may redraw a new image from a reference style.
- `recast-character-in-reference` should preserve the source image's geometry and composition, then replace only named local traits.

Use the installed `imagegen` skill/tool when generating directly. Use the installed `analyze-art-drawing` skill when available to describe what must remain locked.

## Required Inputs

- One primary image, labeled as the edit target.
- A character prompt, sheet, or visible trait list.
- Target mode: direct image edit/generation, or prompt-only.

Optional inputs:

- A separate background request.
- A separate pose reference only if the user explicitly says the source pose should change.

## Workflow

1. Label the supplied image as `edit target / structure lock`.
2. If the image is only available as a local file and built-in imagegen will be used, inspect it first so it is visible in the conversation.
3. Use `analyze-art-drawing` when available to capture: face proportion fingerprint, facial-feature construction, linework fingerprint, hair/eye rendering, lighting, glow/specular profile, background style, detail density, and polish ceiling.
4. Read [references/recast-policy.md](references/recast-policy.md) before writing a direct edit prompt or judging output.
5. Split the character prompt into a patch map:
   - Replace: hair color, eye color, skin tone, visible marks, species traits, outfit color/silhouette cues, and a small number of accessories.
   - Preserve: pose, crop, camera, expression, face proportion fingerprint, facial-feature construction, hand placement, linework, lighting, glow/specular behavior, medium/material behavior, rendering method, detail density, and polish ceiling.
   - Compress: background, outfit details, accessories, magic/glow, props, and lore-driven motifs.
   - Omit: backstory, personality prose, relationship text, quality words, generic style labels, pose prose that conflicts with the source, and detail inventories that exceed the source image budget.
6. Build a strict edit contract before prompting:
   - Structure locks from the source image.
   - Local trait replacements from the character prompt.
   - Hard caps for accessory count, background content, glow/magic, and outfit detail.
   - Negative constraints against full redraw, new pose, new face construction, different style family, and fantasy-glowy polish.
7. For direct work, call image generation/editing once by default. Reroll at most once only if a locked axis fails despite a concrete prompt guard.
8. For prompt-only work, return the patch map, final edit prompt, negative prompt, and QC checklist.

## Non-Negotiable Rules

- The image is an edit target. Do not treat it as loose inspiration.
- Preserve the source pose, expression, face proportion fingerprint, facial-feature construction, hand/crop logic, camera feeling, linework, lighting, rendering method, background style, and polish ceiling.
- Replace only visible local traits named by the character prompt.
- Character local colors are allowed, but must be translated through the source image's value range, chroma handling, line tint, and lighting.
- Background content can change only at the same complexity level as the source background. If the source background is simple or blurred, compress the new background into one or two faint cues.
- Character magic/glow words must not create global glow unless the source image already has global glow. Convert magical traits into tiny local marks or small accessory highlights.
- Do not copy source identity traits that the character prompt replaces, such as the source hair color, eye color, outfit, accessories, species, or background content.
- Do not change the face construction unless the user supplies a separate face/identity reference or explicitly requests it.
- Do not make the result cleaner, smoother, glossier, more ornate, more detailed, more fantasy-polished, or more AI-generated than the source.

## Prompt Construction

Use this order:

1. Edit-target declaration: preserve the attached image's structure.
2. Source locks: pose, crop, expression, face construction, hand logic, linework, medium, lighting, glow/specular profile, detail density, and polish ceiling.
3. Patch map: concise visible character replacements only.
4. Outfit/accessory compression: one or two visible cues when the crop allows.
5. Background patch: same style and complexity as the source.
6. Glow/specular guard: local highlights only unless the source has global glow.
7. Negative constraints: no full redraw, no new pose, no new face, no style drift, no fantasy glow, no raw character-sheet inventory.

## Output

For direct generation, keep the user-facing response short: generated image, concise QC result, and any major issue or reroll reason.

For prompt-only mode, return:

```text
Source locks:
Patch map:
Compressed character traits:
Final edit prompt:
Negative prompt / anti-redraw:
QC checklist:
```

Do not paste the full character sheet into the final edit prompt. Condense it into visible patches and a short background cue.
