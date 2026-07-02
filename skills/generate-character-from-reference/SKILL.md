---
name: generate-character-from-reference
description: Generate mobile portrait character images from a reference image plus a character description. Use when the user wants imagegen to strictly follow the reference art style, linework fingerprint, visible medium/material behavior, hand-drawn or digital art cues, pose, facial expression, lighting, rendering, eye rendering/coloring, hair construction/coloring, strand density, imperfection/polish level, detail density, palette handling, accessory/detail rendering, and background style while replacing the reference identity with the supplied character/OC appearance. Applies analyze-art-drawing style analysis, trait translation, 9:16 vertical framing, safe focal placement, visual-budget control, makeup blending, background-content separation, prompt construction, QC, and one targeted reroll.
---

# Generate Character From Reference

## Core Behavior

Use this skill for reference-conditioned character image generation. The reference image controls visual language, visible medium/material behavior, pose idea, expression, lighting, hair construction, strand density, rendering polish, and background style. The character description controls identity, appearance, outfit, accessories, species, local colors, and requested scene content.

Use a generic trait translation matrix for every character and every reference:

- Character-controlled traits: identity, hair color, eye color, skin tone, outfit, accessories, species traits, visible marks, explicit makeup, and requested background content.
- Reference-controlled construction: pose, expression, camera/crop, linework fingerprint, shading method, eye rendering/coloring method, hair construction/coloring method, strand density, edge quality, polish level, medium/material behavior, detail density, and background style.
- Compatibility rule: keep character traits, but draw them using the reference's technique and visual budget.

When the user asks to generate directly, build the prompt first, then use the available image generation workflow/tool. If image generation is unavailable in the current environment, return the final prompt instead of pretending generation happened. When the user asks for prompt only, return the final prompt and QC checklist without generating.

## Required Inputs

- Primary reference image.
- Character description or character sheet.
- Target: generate image directly or prompt only.

Optional inputs:

- Style-only reference, only when explicitly labeled as style-only.
- Pose reference, only when explicitly supplied for pose/camera/crop/silhouette/hand placement.
- Mood/color reference, only for atmosphere and lighting direction.

## Workflow

1. Label each input image by role: primary reference, style-only reference, pose reference, or mood/color reference.
2. Use the installed `analyze-art-drawing` skill when available to analyze the primary reference. Build a compact technical style card covering style family, medium/material classification, medium evidence, linework fingerprint, line color/tint, thickness range, opacity, taper/pressure rhythm, broken/lost contour behavior, line density, contour authority, face/eye/hair/skin/clothing/background rendering, eye coloring, iris layering, catchlight shape, hair coloring, hair construction, strand density, color handling, lighting, edges, imperfection/polish profile, accessory/detail rendering, composition, pose, expression, makeup, detail density, palette handling, and background complexity.
3. Read [references/generation-policy.md](references/generation-policy.md) before constructing the generation prompt or judging QC.
4. Build a style fidelity contract and trait translation matrix: reference invariants, character trait locks, reference construction locks, allowed character replacements, and suppressed character-sheet details. If a character detail would increase detail density, palette complexity, background complexity, accessory/detail complexity, or rendering complexity beyond the reference, simplify it into a style-matched cue rather than dropping core identity traits.
5. Filter the character description. Keep visible identity and appearance details that fit the reference visual budget, especially character local colors and signature accessories/marks. Remove lore, relationship prose, habits, abstract personality, style adjectives, quality words, background over-description, and any pose/camera/gaze/gesture/hand-action wording that conflicts with the reference.
6. Build known-failure guards before the final prompt. For every hard QC axis in the policy, add a concrete guard when the reference indicates risk: linework fingerprint, hair strand density, polish ceiling, eye rendering, palette handling, accessory/detail budget, background complexity, pose/expression, hands/crop, and character local color fidelity. Do not generate until these guards are explicit, observable, and written as positive locks plus negative constraints.
7. Build the final prompt in this order:
   1. 9:16 mobile portrait output lock and safe face/focal placement.
   2. Reference role and strict style/pose/expression lock.
   3. Reference visual grammar card.
   4. Character trait locks.
   5. Reference construction locks, including linework fingerprint lock.
   6. Known failure guards.
   7. Medium/material lock.
   8. Imperfection/polish ceiling.
   9. Style fidelity contract and style-matched detail budget.
   10. Lighting and background-style lock.
   11. Pose/expression summary and hand/crop safety.
   12. Makeup inheritance or makeup blending rule.
   13. Compact character appearance.
   14. Background content from character/requested scene, rendered in reference background style.
   15. Negative constraints.
8. Run prompt preflight against the policy checklist before generation. If the prompt is missing a guard for a defined hard-failure mode, revise the prompt first instead of generating.
9. Generate one initial image by default with the available image generation tool/workflow.
10. Run QC using the policy checklist. Reroll at most once, and only for a model miss or newly observed failure after prompt preflight passed. If the failure was already defined but the prompt lacked the required guard, treat it as a prompt-compiler miss, fix the prompt/skill guard, and do not describe it as an ordinary reroll reason.

## Non-Negotiable Rules

- Final output is always 9:16 mobile portrait unless the user explicitly changes this skill's policy.
- 9:16 vertical framing and safe face/focal placement win over the reference crop.
- Reference art style must apply to the whole image, including character and background.
- Reference linework fingerprint must apply to the whole image: line color/tint, thickness range, opacity, taper rhythm, broken/lost contours, line density, contour authority, focal line hierarchy, and line-to-fill relationship.
- Reference visible medium/material behavior must apply to the whole image. If the reference reads as hand-drawn, watercolor, marker, gouache, ink, pencil, scanned paper, digital painting, digital cel shading, 3D, or mixed media, preserve that visible behavior instead of converting it to another medium.
- Reference detail density, palette handling, background complexity, accessory/detail rendering, edge hierarchy, and rendering complexity must apply to the whole image.
- Reference hair construction, strand density, edge behavior, highlight logic, and polish ceiling must apply to the whole image. Character hair color can change; the way the hair is drawn should not.
- Reference eye rendering, iris layering, catchlight shape, lash grouping, sclera tint, eyelid redness, and eye gloss/matte finish must apply to the whole image. Character eye color can change; the way the eyes are colored and rendered should not.
- Generated output must not become cleaner, smoother, glossier, more detailed, or more AI-polished than the reference. Preserve natural roughness, line/fill imperfection, or clean finish exactly as observed.
- Primary reference pose idea, facial expression, gaze, camera feeling, hand placement, and composition intent win over conflicting character-description pose prose.
- Character description wins for character identity, hair, eyes, skin, outfit, accessories, species, and local colors.
- Character local colors must be preserved unless the user explicitly asks for monochrome or color changes. If the reference is monochrome or low-color, translate those colors into the same restrained value/chroma discipline instead of saturated palette blocks.
- Character details are translated through the reference visual budget. If the reference is minimal, high-key, plain-background, or low-detail, compress character outfit/accessory/background details into small cues rather than rendering the full character sheet.
- Character accessories are allowed when present in the character description. Include them as style-matched readable cues when crop and detail budget permit; simplify, crop, or reduce extras only when they would exceed the reference's detail density or polish level.
- Do not copy the reference character identity, exact outfit, hair color, eye color, accessories, species, watermark, signature, or background content unless explicitly requested.
- If character makeup is unspecified, follow the reference makeup/cosmetic rendering. If character makeup is specified, combine it with the reference makeup placement, finish, intensity family, and stylization.
- Background content comes from the character description or requested scene; background drawing style comes from the reference. If the reference has no clear background, keep the new background simple and avoid filler.

## Output

For direct generation, keep the user-facing response short: generated image, a concise QC result, and any major issue or reroll reason.

For prompt-only work, return:

```text
Reference visual grammar:
Filtered character appearance:
Final image prompt:
Negative prompt / anti-slop:
QC checklist:
```

Do not paste the user's full character sheet into the final image prompt. Condense it into visible traits and a short scene line.
