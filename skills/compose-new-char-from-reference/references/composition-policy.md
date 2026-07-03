# Composition Policy

Use this reference whenever composing a new character from an existing character reference.

## Goal

Create a new original character that is inspired by the source character's broad vibe, emotional energy, and roleplay utility, while changing visual identity and protected identity markers enough that the result is not a near-copy.

The final output must be:

1. valid Mero character JSON
2. `IMAGE_RECAST_HANDOFF` for `recast-character-in-reference`
3. `COMPOSITION_DIFF_SUMMARY` explaining the main changes from source to new character

Do not include anything else. No intro, no explanation, no Markdown fence, no "done", no validation note, and no follow-up suggestion.

## Source Extraction

Extract the source facts before writing:

- gender and pronouns
- age or age band
- role, occupation, social status, power type, and setting
- species and visible species traits
- appearance: hair, eyes, skin, body type, outfit, accessories, color palette, marks, motifs
- personality traits, emotional wounds, social style, speech style
- likes, dislikes, boundaries, recurring habits
- backstory shape, scenario setup, relationship dynamic with `{{user}}`
- tags and genre labels
- sexual orientation if present
- IP risk signals: famous franchise names, canon names, exact powers, named clans/groups, iconic outfit, catchphrases, plot relationships, weapon names, or recognizable lore

If the source is messy, infer conservatively and prefer broad categories over brittle details.

## Transformation Rules

### Must Preserve

- Preserve the source character's gender exactly. If the source is male, the new character is male. If female, female. If nonbinary or another explicitly stated gender, preserve that.
- If gender is not stated directly, infer it from pronouns, tags, or repeated source wording. If it still cannot be inferred, mark gender as unspecified rather than inventing a gender.
- Preserve pronouns when they are clearly tied to the preserved gender, unless the user hint asks for compatible pronouns.
- Preserve the broad roleplay appeal: emotional tension, social dynamic, genre, and interaction hooks.

### Must Change

Substantially change visual identity:

- name
- hair color, length, or silhouette
- eye color or eye detail
- outfit silhouette, garment type, material, and palette
- accessories and jewelry
- signature motifs
- species or visible species traits when useful
- background cue or setting details

Avoid preserving the source's exact combination of traits. If one visible trait remains similar because the user requested it, compensate by changing several other visible traits more strongly.

### May Remix

These can be inherited by abstraction, randomly selected, or lightly transformed:

- personality cluster
- likes and dislikes
- backstory mood
- scenario energy
- line tags and speech style
- romantic dynamic
- occupation archetype
- species family or fantasy concept

Do not copy the exact backstory sequence, named relationships, source setting, or iconic scenario object.

### Optional User Idea/Hint

Treat user hints as soft direction:

- Apply visible hints such as heterochromia, outfit color, hairstyle, species detail, scars, tattoos, or background mood when compatible.
- Treat scars, tattoos, birthmarks, and marks as user-directed only when the user explicitly asks for them. Never infer a face scar, face mark, facial tattoo, face birthmark, or under-eye symbol from vague words like mysterious, moonlit, magical, cursed, noble, lonely, or haunted.
- If a hint conflicts with source gender, keep the source gender and adapt the hint around it.
- If a hint requests copying the source too closely, transform it into a safer adjacent idea.
- If a hint is vague, use it as flavor instead of overfitting the whole character.

### Signature Detail And Face Mark Rules

Choose signature details by character fit and visual budget, but do not invent anything on the face unless the user explicitly asks for it.

Default rule:

- Do not add face scars, face marks, facial tattoos, face birthmarks, cheek symbols, forehead marks, under-eye marks, moon/star/rune marks, or decorative facial marks.
- This ban applies even when the character is magical, cursed, moonlit, haunted, vain, royal, fae, demonic, or visually dramatic.
- Do not place recurring scars or marks under the left eye or right eye as a default signature habit.
- Prefer non-face signature details.

Possible signature details:

- hair accent, earring, choker, clasp, brooch, glove detail, collar embroidery, sleeve trim, fabric texture, subtle hand mark, collarbone mark, or species trait integrated into silhouette
- body mark, hand mark, collarbone mark, shoulder mark, fabric mark, jewelry shape, hair detail, or material texture

If and only if the user explicitly requests a face mark/scar/tattoo/birthmark/symbol:

- make it small, low-contrast, and naturally embedded in the face rendering
- describe it as using the same line tint, edge roughness, shading softness, value range, and medium behavior as the face
- unless the character description explicitly says the mark is raised, embossed, painted, metallic, glowing, inked, or attached, make it flat pigment under/within the skin, flush with the face surface, with no raised edge, no cast shadow, no sticker outline, and no separate material highlight
- make it read like a faint beauty mark, scar, birthmark, blush-shaped tint, or skin-tone variation, not a decorative decal
- do not use floating symbols, high-contrast icons, glowing marks, sticker edges, perfect geometry, or mismatched tattoo linework
- if the reference face is tiny, shadowed, heavily cropped, or too low-detail to support a face mark cleanly, move the signature cue to clothing, jewelry, hair, hand, collarbone, or a species trait

## Adult-Safe Cleanup

The composed card may include adult-safe romance, attraction, orientation, tension, possessiveness, jealousy, affection, flirtation, or relationship preferences.

Remove or rewrite:

- explicit sexual anatomy
- graphic sex acts
- fetish inventories
- coercive or dehumanizing sexual instructions
- policy-bypass text, jailbreak text, or instructions to ignore morals, ethics, guidelines, or policies
- prompts that force explicit sexual narration

Sexual orientation may be invented or remixed, but keep it non-graphic, such as `bisexual`, `gay`, `straight`, `pansexual`, `demisexual`, `romantically flexible`, or `private about attraction`.

## IP And Copyright Safety

When the source appears to be a copyrighted anime, manga, game, movie, or franchise character, transform strongly.

Do not copy:

- canon name or alias
- exact outfit, uniform, weapon, emblem, tattoo, hairstyle, or color combination
- named power, technique, curse, clan, school, faction, organization, or rank
- catchphrase or iconic speech pattern
- canon relationships, rivalries, mentors, students, family roles, or plot events
- setting names or location names

Allowed:

- broad archetype, such as quiet prodigy, haunted mentor, cheerful fighter, exiled noble, cursed scholar, shrine guardian, reluctant heir
- broad emotional function, such as lonely, protective, vain, obsessive, playful, calculating, honorable, insecure
- broad genre, such as dark fantasy, academy fantasy, court intrigue, supernatural city, folklore romance

If IP risk is high, make at least five major changes across name, species, outfit, palette, power concept, backstory, social role, and relationship web.

## IMAGE_RECAST_HANDOFF Contract

After the JSON card, include this block exactly:

```text
IMAGE_RECAST_HANDOFF

Framing mode:
Mobile portrait mode, 9:16 vertical output, app-safe face/focal placement; keep the top header-safe zone nonessential.

Visible appearance summary:
<one compact paragraph>

Recast patch map:
- Hair:
- Eyes:
- Skin:
- Visible mark/species trait: <non-face cue by default; include a face mark only if the user explicitly requested a face mark/scar/tattoo/birthmark/symbol>
- Outfit cue:
- Accessory cue(s):
- Background content cue:

Appearance description image-gen prompt:
<complete but compressed prompt that starts with Mobile portrait mode / 9:16 and describes only visible identity traits, outfit/accessory cues, species marks, palette, and a short background cue. It should be ready for recast-character-in-reference prompt-only or direct recast use. Include one recast compatibility sentence: preserve the supplied reference image's exact art method, linework, lighting, background rendering style, restrained hair strand density, source-matched low-frequency hair fill masses, global grain/noise behavior, and polish ceiling. When hair is described, prefer broad readable clumps or a clean silhouette over many strands. For every hair color, say the hair should be filled with broad source-style shadow/highlight masses and calm low-frequency paint fills, with source grain preserved globally across the whole image rather than concentrated inside the hair; avoid speckled color static, salt-and-pepper hair texture, dithered hair texture, micro-streaks, glittery highlight crumbs, or crunchy AI-looking hair noise. For pale, white, silver, pastel, neon, or highly saturated hair, add darker roots/underside or broad shadow islands when useful so volume does not require tiny noisy texture. Do not include any face scar, face mark, facial tattoo, face birthmark, cheek symbol, forehead mark, or under-eye symbol unless the user explicitly requested one. If the user explicitly requested a face mark, state that it must be subtle, low-contrast, rendered with the same line tint, shading softness, value range, edge roughness, and medium behavior as the face, and flat pigment under/within the skin unless explicitly described as raised/painted/inked/attached. It must not look like a sticker, crisp icon, or separate material sitting on top of the face.>

Negative prompt / anti-copy constraints:
<short negative prompt only, one compact paragraph or 4-8 comma-separated clauses. Focus on common AI image failures: malformed eyes, mismatched pupils, bad hands, extra fingers, extra limbs, warped face, deformed anatomy, text, watermark, signature, compression artifacts, over-smooth AI polish, noisy hair fill in any hair color, salt-and-pepper hair texture, micro-streak hair texture, explicit sexual content, and unsafe anatomy/fetish wording. Include only one brief anti-copy clause such as "do not copy source identity, exact outfit, exact hair, exact palette, or raw character-sheet inventory." Do not list long source-trait inventories here; recast-character-in-reference handles detailed anti-copy, source locks, style locks, and visual constraints.>

QC checklist:
- Mobile portrait mode included:
- Gender matches source:
- Visual identity clearly differs from source:
- Outfit/accessories/palette changed:
- No unsolicited face scar/mark/tattoo/birthmark:
- Source lore and copyrighted markers removed:
- Adult-safe cleanup passed:
- Handoff uses visible traits only:
- Hair strand/fill guard included:
```

The handoff should be useful for `recast-character-in-reference`, so write it like a local trait patch, not a full illustration brief. Keep lore, personality, likes, dislikes, and relationship rules out of the image prompt.
Do not add commentary before or after this block.

## COMPOSITION_DIFF_SUMMARY Contract

After `IMAGE_RECAST_HANDOFF`, include a short plain-text block:

```text
COMPOSITION_DIFF_SUMMARY
- Preserved: <gender/pronouns or broad roleplay appeal kept from the source>
- Changed visually: <hair, eyes, outfit, palette, species traits, accessories, motifs, or setting changes>
- Remixed internally: <personality, backstory, likes/dislikes, speaking style, scenario energy>
- Applied hint: <how the user's idea/hint was used, or "No separate hint supplied">
- Safety/originality cleanup: <adult-safe cleanup, IP-safe transformation, removed copied lore/markers>
```

Keep this summary brief. It may describe the transformation, but do not make it part of the character's in-world card. If the source is copyrighted, avoid repeating canon names and describe changes generically.
Stop immediately after this block.

## Final Quality Gate

Before finalizing:

- The JSON is valid Mero character JSON.
- The first visible character in the answer is `{`.
- The new character preserves source gender.
- The new character is not a lookalike.
- Optional hints are reflected when safe.
- Explicit sexual content and jailbreak instructions are removed.
- If the source is copyrighted or likely copyrighted, the result is strongly transformed.
- Face scars, marks, facial tattoos, face birthmarks, and under-eye symbols are omitted unless explicitly requested by the user.
- `IMAGE_RECAST_HANDOFF` explicitly includes Mobile portrait mode / 9:16 and app-safe face/focal placement.
- `IMAGE_RECAST_HANDOFF` includes hair guidance that controls both strand density and broad hair fill masses/global grain behavior.
- `IMAGE_RECAST_HANDOFF` contains only visible image traits and a short negative prompt focused on common AI image failures.
- `COMPOSITION_DIFF_SUMMARY` briefly explains the major changes.
- No extra text appears outside the JSON, `IMAGE_RECAST_HANDOFF`, and `COMPOSITION_DIFF_SUMMARY`.
