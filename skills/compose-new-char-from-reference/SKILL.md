---
name: compose-new-char-from-reference
description: Compose a new original character from a pasted reference character card, prose sheet, or messy mixed text. Use when the user asks to create, remix, derive, or compose a new character from an existing character while returning a database-ready Mero character JSON object plus an IMAGE_RECAST_HANDOFF for recast-character-in-reference image prompting. Supports optional idea/hint text such as eye colors, outfit direction, hair, species, vibe, or concept constraints; preserves source gender while changing appearance, outfit, species traits, and copyrighted identity enough to avoid near-copying. The image handoff is always Mobile portrait mode / 9:16 and must not invent face scars, face marks, facial tattoos, birthmarks, or under-eye symbols unless the user explicitly asks for them.
---

# Compose New Char From Reference

## Core Behavior

Use this skill to turn one pasted character reference into a new original character profile and an image-generation handoff. The output is text only and must contain exactly three top-level blocks: one raw Mero character JSON object, one `IMAGE_RECAST_HANDOFF`, and one `COMPOSITION_DIFF_SUMMARY`. The image handoff must always be Mobile portrait mode / 9:16.

Do not generate an image. Do not call image tools. This skill prepares the character data and the visible-trait prompt that another skill can use.

## Required Inputs

- Source character reference: JSON card, prose sheet, pasted prompt, or messy mixed text.

Optional inputs:

- `Idea`, `hint`, `goi y`, or similar direction for the new character's eyes, hair, outfit, species, mood, role, color palette, or relationship dynamic.
- Database-specific field preferences if the user supplies them.

## Workflow

1. Read [references/mero_character_schema.md](references/mero_character_schema.md) before writing the JSON output.
2. Read [references/composition-policy.md](references/composition-policy.md) before deriving the new character.
3. Parse the source reference and extract:
   - gender and pronouns
   - age band, role, archetype, occupation, setting, species
   - appearance, outfit, accessories, palette, signature motifs
   - personality, likes, dislikes, backstory vibe, scenario, tags, speaking style
   - sexual orientation if present, without preserving explicit sexual content
   - IP/copyright risk signals
4. Apply the user's idea/hint as soft direction unless it conflicts with gender preservation, originality, adult-safe cleanup, or IP-safety rules.
5. Compose a substantially new character:
   - preserve source gender exactly
   - invent or transform visual identity, outfit, palette, accessories, species traits, and signature motifs
   - use signature details on the body, clothing, hair, accessories, material texture, or species silhouette; do not invent face scars, face marks, facial tattoos, birthmarks, or under-eye symbols unless the user explicitly asks for them
   - remix personality, interests, line tags, scenario energy, and backstory vibe without copying source lore
   - invent sexual orientation if useful, kept non-graphic
   - strongly transform any copyrighted/anime/game/media reference into an original character
6. Return the output in exactly this order:
   - raw Mero character JSON object first, with no commentary before the opening `{`
   - a blank line
   - `IMAGE_RECAST_HANDOFF` block with visible-trait prompt details
   - a blank line
   - `COMPOSITION_DIFF_SUMMARY` block with a short human-readable summary of what changed from the source
7. Stop immediately after `COMPOSITION_DIFF_SUMMARY`. Do not add any notes, caveats, explanations, validation commentary, or follow-up suggestions.

## Output Rules

- The JSON must be valid and parseable. Do not include comments, trailing commas, Markdown fences, or prose inside the JSON block.
- After the JSON, include `IMAGE_RECAST_HANDOFF` as plain text.
- After `IMAGE_RECAST_HANDOFF`, include `COMPOSITION_DIFF_SUMMARY` as plain text.
- Do not include any text outside those three top-level blocks. No greeting, no apology, no "here is", no analysis, no closing note, no usage instruction, and no extra Markdown.
- Keep character-card prose immersive but database-friendly.
- Keep the image handoff compressed to visible traits only: hair, eyes, skin, non-face marks or explicitly requested face marks, species traits, outfit cues, accessories, and a short background cue.
- The `IMAGE_RECAST_HANDOFF` must explicitly say Mobile portrait mode / 9:16 and include app-safe face/focal placement.
- The image prompt should include a short recast compatibility line: preserve the supplied reference image's exact art method, linework, lighting, background rendering style, restrained hair strand density, source-matched low-frequency hair fill masses, global grain/noise behavior, and polish ceiling. Do not use generic quality/style adjectives that invite a new art direction.
- When describing hair, prefer broad readable clumps or a clean silhouette over many strands. For every hair color, specify that hair should be filled with broad source-style shadow/highlight masses and calm low-frequency paint fills, with source grain preserved globally across the whole image rather than concentrated inside the hair; avoid speckled color static, salt-and-pepper hair texture, dithered hair texture, micro-streaks, glittery highlight crumbs, or crunchy AI-looking hair noise. For pale, white, silver, pastel, neon, or highly saturated hair, add darker roots/underside or broad shadow islands when useful so volume does not require tiny noisy texture.
- Keep `Negative prompt / anti-copy constraints` short. Focus mostly on common AI image failures such as malformed eyes, bad hands, extra fingers, extra limbs, deformed anatomy, warped face, text, watermark, signature, artifacts, overpolish, noisy hair fill in any hair color, salt-and-pepper hair texture, and unsafe explicit content. Do not list long source-trait inventories there; recast-character-in-reference handles source locks, anti-copy, and detailed visual constraints.
- Do not invent face scars, face marks, facial tattoos, face birthmarks, under-eye symbols, cheek symbols, forehead marks, or decorative facial marks. This includes small scars and moon/star/rune marks under either eye. Use accessories, clothing, hair, jewelry, hand/collarbone/body marks, species silhouette, or material texture as the signature detail instead.
- Only include a face mark when the user explicitly requests a facial mark/scar/tattoo/birthmark/symbol in the idea/hint or source-to-new direction. If an explicit face mark is used, describe it as subtle and integrated into the image's face rendering: same line tint, same shading softness, same value range, same edge roughness, and no sticker-like, emblem-like, crisp icon, floating symbol, or mismatched graphic mark. Unless the user explicitly says the mark is raised, embossed, painted, metallic, glowing, inked, or attached, specify that the mark is flat pigment under/within the skin, flush with the face surface, with no raised edge, cast shadow, sticker outline, or separate material highlight.
- Do not paste full lore, personality, relationship rules, or raw character-sheet inventories into the image prompt.
- Remove explicit sexual anatomy, graphic sex instructions, fetish inventories, and policy-bypass or jailbreak text from the composed card.
- Do not mention that the new character was copied, derived, or transformed from a specific source character in the final card.
- The diff summary can mention source-to-new changes, but keep it brief and do not reveal copyrighted source names unless the user explicitly supplied and asked to discuss them.
