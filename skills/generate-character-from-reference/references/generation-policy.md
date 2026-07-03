# Generation Policy

Use this reference when building prompts or judging output for `generate-character-from-reference`.

## Priority Order

1. 9:16 mobile portrait output and safe face/focal placement win for final canvas, orientation, and subject placement.
2. A separate pose reference, when provided, wins for pose, camera, crop, silhouette, and hand placement only.
3. Primary reference wins for facial expression, face proportion fingerprint, facial-feature construction, pose idea, camera feeling, hand logic, composition intent, lighting behavior, glow/specular profile, art style, linework fingerprint, visible medium/material behavior, eye rendering/coloring method, iris layering, catchlight shape, hair coloring method, hair construction, restrained strand density, detail density, palette handling, background complexity, edge hierarchy, imperfection/polish level, and rendering complexity.
4. Character description wins for identity, appearance, outfit, accessories, species, local colors, visible marks, explicit makeup, and requested background content. Translate those traits through the reference visual grammar instead of replacing them with reference identity traits.
5. Makeup follows the reference by default. Explicit character makeup is combined with the reference cosmetic rendering.
6. Background content changes according to character/requested scene, but background style and complexity strictly follow the reference.
7. Mood/color reference controls atmosphere only and does not override character local colors, primary-reference lighting behavior, or the primary-reference visual budget unless explicitly requested.

## Trait Translation Matrix

Use this matrix for every character and every reference. Do not hard-code a specific character, outfit, palette, or reference type.

```text
Character-controlled traits:
- Hair color, eye color, skin tone, outfit, accessories, species traits, subtle visible marks/scars/tattoos, explicit makeup, and requested background content.

Reference-controlled construction:
- Pose, facial expression, face proportion fingerprint, facial-feature construction, camera/crop, gesture, hand logic, style family, visible medium/material behavior, linework fingerprint, shading method, glow/specular profile, eye rendering/coloring method, iris layering, catchlight shape, lash grouping, sclera tint, hair coloring method, hair construction, restrained strand density, edge quality, imperfection/polish level, detail density, palette handling, background style, and rendering complexity.

Compatibility rule:
- Keep character traits, but draw them with the reference technique. Character eye color can change from the reference; iris layering, catchlight shape, lash grouping, sclera tint, and eye finish should not drift away from the reference. Character hair color can change from the reference; base color handling, restrained strand count, clump grouping, highlight shape, edge breaks, and polish level should not drift away from the reference.
```

Character local colors and accessories are not style drift by themselves. They become drift only when their saturation, detail density, construction, hair strand density, finish, or polish level breaks the reference visual grammar.

## Reference Analysis Card

Before prompting, translate the reference into visible drawing behavior. Avoid broad labels alone.

```text
Reference visual grammar:
- Detected style family:
- Medium feel:
- Medium/material classification:
- Medium confidence:
- Medium evidence:
- Surface/material cues:
- Linework:
- Linework fingerprint:
- Line color/tint:
- Line thickness/opacity:
- Taper/pressure rhythm:
- Broken/lost contour behavior:
- Line density:
- Contour authority:
- Line-to-fill relationship:
- Face rendering:
- Face proportion fingerprint:
- Facial-feature construction:
- Eye rendering:
- Eye coloring:
- Iris layering:
- Catchlight shape:
- Hair rendering:
- Hair coloring:
- Skin rendering:
- Makeup/cosmetics:
- Clothing/material rendering:
- Color system:
- Color handling/local-color policy:
- Lighting:
- Glow/specular profile:
- Value/shadow structure:
- Edge hierarchy:
- Background rendering:
- Composition/crop:
- Pose/expression:
- Hand/crop logic:
- Detail-density budget:
- Palette handling:
- Background complexity:
- Accessory/detail budget:
- Accessory/detail rendering:
- Hair coloring/construction strategy:
- Hair construction:
- Strand density:
- Imperfection/polish profile:
- Polish ceiling:
- Glow budget:
- Style drift risks:
- Finish/polish:
```

Use `analyze-art-drawing` for this phase when available. Pull concrete terms from its analysis: medium/material classification, medium evidence, linework fingerprint, line weight hierarchy, line color/tint, line opacity, tapered/broken/lost contour, line density, contour authority, line-to-fill relationship, cel/soft cel/painterly/airbrush rendering, multiply-like shadows, highlight logic, edge hierarchy, eye color treatment, iris layer structure, catchlight shape, lash grouping, hair color treatment, hair mass/strand strategy, fabric fold grouping, background detail density, and lighting design.

## Analysis Handoff Contract

`generate-character-from-reference` should consume the detailed Generation Handoff Packet from `analyze-art-drawing` whenever that skill is available. The packet is the source of truth for the reference's visual grammar, budgets, style anchors, conditional risk flags, and drift risks. Do not replace it with a generic style summary, and do not re-infer looser budgets from the raw character sheet.

The downstream generator must reuse these packet fields directly:

- Reference visual grammar: medium/material behavior, style family, face proportion, facial-feature construction, linework, face/eye/hair/skin/clothing/background rendering, color handling, lighting, glow/specular behavior, edges, composition, pose, expression, hand/crop logic, and finish.
- Always-on style anchors: face proportion, facial-feature construction, linework, eye rendering method, hair construction, medium/material behavior, lighting/value structure, glow/specular behavior, background style, detail density, accessory/detail rendering, palette handling, and polish ceiling.
- Conditional risk flags: eye occlusion/malformed eye risk, face-mark integration risk, hand/crop risk, pale/noisy or long-hair risk, glow/magic pressure, ornate accessory pressure, dense background/prop pressure, palette pressure, and anatomy-like artifact risk.
- Visual budget and compression guidance: safe character detail count, outfit allowance, accessory allowance, background allowance, magic/glow/sparkle allowance, specular/dappled-light allowance, and what to hide, crop, or reduce.
- Drift risks: the specific ways the generated image will likely become too ornate, too polished, too colorful, too scenic, too line-heavy, or otherwise unlike the reference.

If the packet is missing an always-on style anchor or active conditional risk field, fill that field by analyzing the primary reference before prompting. Do not generate from an incomplete packet when the missing field affects linework, hair construction, eye rendering, polish ceiling, detail density, accessory budget, background complexity, palette handling, or pose/hand/crop.

## Medium / Material Lock

Preserve the reference's visible medium behavior across the whole generated image. Classify the reference as one of:

- Traditional or scanned hand drawing: pencil, ink, watercolor, gouache, marker, colored pencil, mixed physical media.
- Digital art: digital line art, cel shading, airbrush painting, painterly digital, digital watercolor imitation, webtoon/manhwa polish.
- 3D/render/photo-real or mixed media.
- Uncertain medium feel, when provenance is not visually reliable.

Use visible evidence, not assumptions. If uncertain, prompt the observable behavior rather than claiming a provenance:

- Use "watercolor-like pigment blooms, uneven wash edges, paper texture" instead of "real watercolor" when unsure.
- Use "scanned hand-drawn ink feel, uneven line density, paper grain" when analog cues are visible.
- Use "digital airbrush glazing, clipped clean highlights, pressure-sensitive lineart" when digital cues are visible.

Do not convert a traditional-looking reference into clean digital anime polish, glossy 3D, photo-real rendering, or vector-flat art. Do not convert a digital reference into paper grain or watercolor unless the reference visibly has those cues.

## Style Fidelity Contract

Before writing the prompt, make a short contract:

```text
Reference invariants:
- <medium/material behavior, style family, face proportion fingerprint, facial-feature construction, linework, value range, edge hierarchy, render density, eye rendering/coloring method, hair coloring/construction, restrained strand density, imperfection/polish level, glow/specular profile, lighting, background complexity>

Character trait locks:
- <hair color, eye color, skin tone, outfit, accessories, species traits, visible marks, explicit makeup, requested background content>

Reference construction locks:
- <pose, expression, face proportion fingerprint, facial-feature construction, camera/crop, hand logic, linework, shading method, glow/specular behavior, eye rendering/coloring, iris layering, catchlight shape, lash grouping, hair coloring method, hair construction, restrained strand density, edge quality, polish ceiling, background style>

Allowed character replacements:
- <identity, hair/eye/skin/outfit/local colors translated into the reference style>

Suppress or reduce:
- <character details that would add too much detail, palette complexity, accessory rendering precision, props, background, glow, over-clean polish, or a different rendering family>
```

This contract must shape the final prompt. Do not paste all three sections if the user only wants a direct generation; use them internally to keep the prompt disciplined.

## Style Anchors And Conditional Guards

Before calling image generation, run a prompt preflight. The first prompt must always include the reference's core visual grammar, but it should not paste the full hard QC checklist into every prompt. Use three layers:

- **Always-on style anchors**: medium/rendering model, style family, face proportion, facial-feature construction, linework, eye rendering/coloring method, hair construction/coloring method, restrained strand density, detail density, palette handling, lighting/value structure, glow/specular behavior, background style, and polish ceiling.
- **Conditional prompt guards**: short positive lock plus targeted negative constraint for risks that are active in the reference, character sheet, or request.
- **Hard QC gates**: always inspect the output after generation for style-lock failures and basic eye/face/hand/body/crop/artifact defects, even when the first prompt stayed compact.

Always-on anchor examples:

- **Face construction anchor**: head shape, face length/width, feature spacing, eye size/spacing/tilt, brow/nose/mouth construction, jaw/chin/cheek shape, and feature simplification.
- **Linework anchor**: line color/tint, thickness range, opacity, taper/pressure rhythm, broken/lost contour behavior, line density, contour authority, line-to-fill relationship.
- **Eye rendering anchor**: character eye color can change, but iris layering, catchlight shape, lash grouping, sclera tint, eyelid redness, and gloss/matte finish follow the reference.
- **Hair construction anchor**: character hair color can change, but mass/strand strategy, restrained strand density, clump scale, highlight shape, edge behavior, fill method, and polish level follow the reference.
- **Medium/polish anchor**: preserve visible medium behavior, texture, roughness or clean finish, value structure, and polish ceiling exactly.

Conditional guard triggers:

- **Eye visibility/occlusion**: include only when source eyes are unclear/malformed, one eye is naturally hidden, hair/headwear/marks cross the eye area, or the edit/reframe exposes more face plane.
- **Face mark**: include only when the character prompt requests/implies a face mark or the prompt compiler chooses one as a signature cue.
- **Hands/anatomy**: include only when hands/body parts are visible and flawed/ambiguous, hand-adjacent details are requested, or accessories/background strokes may read as anatomy.
- **Hair noise**: include detailed hair fill/noise guard only when hair color changes, hair is pale/silver/pastel/neon/saturated, the prompt requests long hair, or the source is mass-first/low-strand and likely to drift.
- **Glow/magic**: include only when character/request uses glowing, magical, moonlight, starlit, sparkle, aura, or similar terms.
- **Accessory/background pressure**: include only when character/request has dense outfit, accessories, props, or scenic background beyond the reference budget.
- **Palette pressure**: include when character local colors are much more saturated or numerous than the reference palette.

Preflight rules:

- If an always-on style anchor is missing or an active conditional risk lacks a concrete guard, revise the prompt before generation.
- Do not rely on generic phrases such as "strictly match style", "same linework", "high quality", "not too detailed", or "follow reference" as a guard.
- For every active high-risk axis, use visible terms from the reference analysis. Example: "very thin warm gray-brown low-opacity lineart with broken/lost contours" is a guard; "soft anime linework" is not.
- For character-sheet pressure, use the analysis packet's visual budget to write numeric or concrete caps where possible. Example: "show only the constellation mark plus one tiny jewelry cue; compress the city scene into one faint background wash" is a guard; "keep it simple" is not.
- If the generated image fails a defined active risk and the prompt did not include its guard, classify it as a prompt-compiler miss, not a normal reroll.
- Reroll is reserved for model noncompliance after the prompt preflight passed, or for a newly observed failure mode not yet defined in the policy.

## Visual Budget And Character Compression

The reference image sets the maximum visual budget.

Before writing the final prompt, run a hard compression gate using the Generation Handoff Packet from `analyze-art-drawing`. This gate converts the raw character sheet into a compressed visible-traits list. The final prompt must use this compressed list, not the full character sheet.

Hard compression gate:

```text
Reference budget readout:
- Crop/detail capacity:
- Outfit detail allowance:
- Accessory allowance:
- Background content allowance:
- Magic/glow/sparkle allowance:
- Hair strand/rendering allowance:
- Palette/chroma allowance:
- Polish ceiling:
- Glow/specular allowance:

Compressed character traits to prompt:
- Identity/face/skin:
- Eye color and eye-specific trait:
- Hair color and silhouette:
- Visible mark/signature trait:
- Outfit cue(s):
- Accessory cue(s):
- Background cue(s):
- Magic/glow cue(s):
- Specular/dappled-light cue(s):

Suppressed raw character-sheet details:
- <details hidden, cropped, omitted, or reduced because they exceed the reference visual budget>
```

The gate must be strict. If the reference is tight, low-accessory, plain-background, low-detail, high-key, or restrained, write hard caps such as "one outfit cue", "one or two accessory cues", "one faint background cue", or "no global glow". If the prompt still contains full outfit inventories, full prop clusters, full background scenes, dense accessory lists, or unbounded sparkle/glow after this gate, the prompt has failed preflight.

If the reference is low-detail, high-key, plain-background, tight close-up, or low-accessory:

- Keep the generated image low-detail outside the focal face/eyes/lips/hand.
- Convert outfit details into one or two visible cues near the crop instead of full garment exposition.
- Convert accessories into tiny style-matched accents; crop, hide, or simplify extras only when the reference-style crop cannot support them.
- Convert background content into faint cues only.
- Preserve character local colors, but express them through the reference value range, chroma discipline, opacity, lighting, and blending method.
- Do not add detail just because the character sheet contains it.

If the reference is ornate, detailed, full-scene, or high-accessory, more character detail may be shown, but still match the same density and rendering method.

Use these compression rules:

- Eyes: preserve the character's eye color, but match the reference eye coloring method. Use the same iris layering, upper-iris shadow, lower-iris glow or flat fill, pupil treatment, rim line, catchlight shape, sclera tint, lash grouping, eyelid redness, tear/glitter accents, and eye gloss/matte finish.
- Hair: preserve the character's hair color, but match the reference hair construction first. If the reference uses negative-space or mass-first hair with sparse strand lines, draw the new hair as broad masses with the character local color controlled by the reference value/chroma system; do not render every strand, add glossy perfect gradients, turn the hair into thin string-like locks, or turn the whole image into a saturated color wash. When in doubt, reduce strand count and simplify into larger clumps instead of adding fine hair-line detail.
- Hair coloring: translate the character hair color through the reference's base-mass fill, shadow hue, highlight shape, line tint, opacity, edge looseness, and value range. The color should read as the character's hair color, but the coloring method should read as the reference. Do not use more individual strands, flyaways, glossy separators, or perfectly regular hair ribbons than the reference.
- Outfit: match the reference fabric detail level. If the reference sleeve is broad, pale, and simply shaded, do not add dense cable-knit, lace, jewelry chains, or full outfit detail.
- Accessories: if the character has accessories, include readable style-matched cues when the crop and detail budget allow. If the reference has few or no accessories, allow one or two small accents and treat the rest as hidden, cropped, or simplified; do not render accessory precision beyond the reference polish ceiling.
- Background: if the reference background is plain or abstract, use one faint scene cue only. Do not draw a full city, room, balcony, fairy lights, props, or hanging decorations.
- Glow/magic: if the reference has no strong glow, keep magical traits as tiny local accents, not global light effects. If the reference has glossy skin or dappled light, preserve those as specular/dappled highlights, not as aura, bloom, haze, sparkle fields, or neon rim light.
- Palette: preserve the reference value range, dominant temperature, chroma discipline, and color blending behavior. Character colors should remain identifiable as local colors, but should not become a new global palette system unless the reference has comparable color intensity.
- Imperfection/polish: match the reference finish. If the reference has rough line edges, uneven fill opacity, imperfect gradients, scanned texture, or handmade looseness, preserve those artifacts. If the reference is clean digital, keep that clean finish but do not exceed it with extra gloss, hyper-detail, or perfectly regular AI polish.

## Character Description Filtering

Extract only visible generation data:

- Name or identity label, only if useful.
- Species/fantasy type if visible.
- Gender/presentation and apparent age range.
- Face shape and signature facial traits.
- Face proportion traits only when they are character-defining; otherwise translate the character through the reference face proportion fingerprint.
- Eye color and eye-specific features.
- Hair color, length, volume, texture, silhouette, and signature shape.
- Skin tone and visible marks/scars/tattoos.
- Body build if visually relevant.
- Explicit makeup or cosmetic styling.
- Outfit, accessories, props, and local color palette.
- One short emotional tone if it does not override the reference expression.
- One short background/scene line if requested.

Ignore by default:

- Backstory, lore, relationship prose, speaking style, habits, likes/dislikes, hidden vulnerability, abstract personality, and metaphors.
- Quality/style prose from the character sheet, such as high detail, premium polish, soft anime, cinematic, mobile avatar, refined shading, elegant color harmony, or similar.
- Background lists and prop clusters that would exceed the reference background complexity.
- Accessory lists as full literal inventories when they exceed the reference accessory/detail budget. Keep signature accessories as style-matched cues when visible.
- Pose, gesture, gaze, camera, crop, body-turn, hand-action, or expression wording that conflicts with the primary or pose reference.

Keep pose prose from the character description only when:

- The user explicitly says it overrides the reference pose.
- The only visual reference is style-only.
- It is a required prop interaction that can be adapted without changing the reference pose idea.
- It does not conflict with reference pose/camera/gaze/expression/hand placement.

## 9:16 Mobile Portrait And Safe Placement

Default output is always 9:16 mobile portrait, even if the reference is square, landscape, ultrawide, or tightly cropped.

Do:

- Preserve reference pose idea, facial expression, camera feeling, and composition intent.
- Reframe into 9:16 vertical mobile composition with the face/focal center comfortably inside the frame.
- Keep modest breathing room above the head/face and below important subject areas.
- Extend background space as needed while matching the reference background drawing style.
- Keep important hands, face, outfit, props, and signature details readable.

Do not:

- Output landscape, horizontal, square, or the reference aspect ratio when it is not 9:16.
- Place the face or focal center hard against the top or bottom edge.
- Crop away important hands/outfit/identity details to force the pose.
- Add large unrelated empty bands.

## Pose, Expression, And Hands

Primary reference controls:

- Body angle, head tilt, gaze direction, mouth shape, brow/eye openness, blush/emotional beat.
- Camera feeling, crop feeling, composition intent.
- Hand placement, hand action, hand visibility, crop, and occlusion.

If a hand is cropped or hidden in the reference, keep it cropped or hidden. Do not invent a full visible hand. If a hand rests on hip/waist/lower back, keep the wrist connected to the bent arm, use a simple palm edge, grouped fingers, and keep clothing folds separate from fingers.

If pose prose in the character description conflicts with the reference, add a prompt line:

```text
Ignore any conflicting pose, gesture, gaze, crop, camera, body-turn, shoulder-turn, or hand-action wording from the character description. Use character description for appearance only.
```

## Strict Art Style

The generated image should feel like the reference was redrawn with a different character identity.

Match:

- Visible medium/material behavior: paper grain, pigment bloom, ink pooling, pencil tooth, marker overlap, gouache opacity, digital gradients, layer-like highlights, vector-clean edges, 3D shader behavior, or other observed cues.
- Detected style family.
- Face proportion fingerprint: head shape, face length/width, feature spacing, eye size/spacing/tilt, nose/mouth placement, jaw/chin/cheek construction, and feature simplification.
- Linework fingerprint: line color/tint, thickness range, opacity, taper/pressure rhythm, broken/lost contour behavior, line density, contour authority, focal line hierarchy, and line-to-fill relationship.
- Face simplification, eye rendering/coloring, iris layering, catchlight shape, lash grouping, nose/mouth treatment.
- Hair coloring method, hair shape language, restrained strand density, highlight blocks.
- Skin shading, blush, shadow hue, highlight type.
- Clothing fold simplification and material finish.
- Accessory/detail rendering scale and simplification.
- Background rendering treatment.
- Lighting direction, shadow softness, highlight placement, contrast, and ambient fill.
- Glow/specular profile: distinguish hard highlights, dappled light, rim light, and bokeh from bloom, aura, magic glow, and sparkle fields.
- Texture/grain/noise level and polish.
- Imperfection profile and polish ceiling: line wobble, uneven fills, loose edges, imperfect gradients, scan/paper artifacts, clean digital finish, or other visible finish cues.

Avoid style drift:

- Do not convert realism into anime, anime into realism, manhwa into painterly fantasy, line art into glossy 3D, or simple flat background into cinematic scenery unless the user explicitly requests a style change.
- Do not convert hand-drawn, watercolor, marker, gouache, pencil, ink, or scanned-paper references into clean digital polish; do not add traditional paper/pigment artifacts to a clearly digital reference unless those artifacts are visible.
- Do not add decorative sparkle, glow, cinematic rim light, or photoreal detail unless present in the reference.
- Do not make the result cleaner, smoother, glossier, more symmetrical, more detailed, or more AI-polished than the reference.
- Do not replace loose, pale, low-opacity, broken, or barely-there reference linework with crisp black manga outlines, uniform vector curves, heavier contour authority, or dense interior detail lines.

## Makeup Rule

If character description has no makeup instruction, inherit the reference makeup/cosmetic treatment:

- Eyeliner shape/intensity.
- Eyeshadow placement/softness.
- Blush placement/intensity.
- Lip color, gloss/matte finish, and edge softness.
- Contour, highlight, freckles, beauty marks, tear/glitter details, or cosmetic surface treatment.
- Overall makeup level: bare, natural, daily, glam, stylized, theatrical.

If character makeup is specified, combine rather than replace:

- Preserve reference placement logic, finish, intensity family, edge softness, and stylization.
- Add character-specified color/motif/finish where compatible.
- If character makeup conflicts with reference makeup, keep reference visible cosmetic structure and translate the character makeup subtly.

If character says no makeup or natural bare face, reduce intensity toward natural while preserving the reference cosmetic rendering style as subtle shading/finish.

## Background Rule

Background style follows the reference; background content follows the character/requested scene.
This keeps the priority order unchanged: character/requested scene chooses the background idea, while the primary reference's background complexity and style decide how much of that idea can appear. If the reference background is simple, compress the character/requested scene into one faint cue instead of drawing the full scene.

Match the reference background:

- Line presence or absence.
- Shading method.
- Blur/detail balance.
- Texture/grain level.
- Color separation.
- Lighting simplification.
- Finish/polish.

Do not copy:

- Reference room, city, props, object identities, signage, watermark, signature, or exact backdrop content.

If the reference has plain/no/abstract background:

- Keep the new background simple.
- Use faint silhouettes, soft color wash, tiny motifs, or lightly indicated props only when needed.
- Avoid crowded scenery, random props, cinematic lighting, bokeh/orbs, excessive sparkles, and AI-slop filler.

## Face Proportion Rule

Reference facial construction is part of style, not optional decoration. Unless the user supplies a separate identity/face reference or explicitly asks to change the face type, preserve the primary reference's face proportion fingerprint while replacing identity traits.

Match:

- Head and face shape.
- Face length/width ratio.
- Forehead, brow, eye, nose, mouth, and chin spacing.
- Eye size relative to face width, eye spacing, and eye tilt.
- Brow placement and eyelid construction.
- Nose bridge, tip, nostril, and side-plane simplification.
- Mouth width, lip volume, mouth-corner treatment, and vertical placement.
- Jaw taper, chin length/shape, cheek fullness, and camera distortion from head tilt.

Avoid:

- Generic anime face, rounder/chibi face, doll face, photoreal face, or a different age impression.
- Moving the eyes, nose, or mouth into a different facial ratio while preserving only surface colors.
- Letting the character sheet's broad face words override the reference facial construction.

Prompt guard example:

```text
Face proportion guard: preserve the reference's long narrow heart/oval face, high forehead, large almond eyes with slight upward tilt, small narrow nose bridge, small low soft mouth, tapered jaw and pointed chin. Translate the new character's identity through this face construction. Avoid rounder chibi proportions, generic anime spacing, doll-like cheeks, wider eyes, bigger mouth, or photoreal facial planes.
```

## Glow / Specular Rule

Do not use "glow" as a synonym for every bright mark. Separate the reference's lighting effects before prompting.

Preserve:

- Hard specular skin, lip, eye, jewelry, or hair highlights when visible.
- Dappled sunlight patches when they are cast onto the subject.
- Small local magical glow only when the character requires it and the reference budget supports it.

Forbid unless the reference visibly has it:

- Global glow haze.
- Bloom around the whole character.
- Magic aura.
- Floating sparkle fields.
- Neon/cinematic rim light.
- Bokeh/orb backgrounds that replace the reference background style.
- Over-glossy plastic skin or glassy 3D sheen.

If the reference reads as hand-drawn, scanned, or hand-finished digital, preserve the slight line/fill irregularity and do not turn the image into smooth glowy mobile-game polish.

## Prompt Template

Use this order for first-pass prompts. Keep the prompt surgical: include the always-on style anchors, compressed character traits, and only the conditional guards that are active for this reference/request. Do not paste the whole QC checklist into the first prompt.

```text
Generate a 9:16 mobile portrait image, regardless of the reference image's aspect ratio.
Keep the main subject's face/focal center comfortably inside the frame, not too close to the top or bottom edge. This framing rule wins over the reference crop.

Use the attached image as the primary visual reference.
Make the result feel like the reference image was redrawn with a different character identity.
Strictly match the reference pose idea, facial expression, gaze direction, head angle, camera feeling, hand placement, hand visibility/crop, composition intent, face proportion fingerprint, facial-feature construction, linework fingerprint, face simplification, eye rendering/coloring method, iris layering, catchlight shape, lash grouping, hair coloring method, hair construction, restrained strand density, skin shading, clothing shading, makeup/cosmetic rendering, lighting direction, glow/specular profile, shadow softness, highlight placement, contrast, background rendering treatment, and overall finish.

Always-on style anchors from the reference:
<compact concrete anchors from analyze-art-drawing: medium/rendering model, linework, face proportion and facial-feature construction, eye rendering method, hair construction/fill method, palette/color handling, lighting/value structure, glow/specular behavior, background style, detail density, and polish ceiling>

Compressed character trait locks:
Preserve the new character's visible traits after the hard compression gate: <face/skin, hair color, eye color, subtle visible marks/species traits, one or more outfit/accessory/background cues only within the packet's visual budget>. Do not replace these with the reference character's identity traits. Do not paste the raw character sheet or full accessory/background inventory here. Face marks are allowed when they fit the character description or identity cue; if included, render them tiny, low-contrast, and integrated with the reference face line tint, shading softness, edge roughness, value range, and medium behavior. Unless the prompt explicitly says the mark is raised, embossed, painted, metallic, glowing, inked, or attached, treat it as flat pigment under/within the skin, flush with the face surface, with no raised edge, cast shadow, sticker outline, or separate material highlight.

Reference construction locks:
Draw those character traits using the reference construction: <pose, expression, face proportion fingerprint, facial-feature construction, camera/crop, hand logic, linework fingerprint, shading method, glow/specular behavior, eye rendering/coloring, iris layering, catchlight shape, lash grouping, hair coloring method, hair construction, restrained strand density, edge quality, accessory/detail rendering, background style>. Eye color follows the character; iris layering, catchlight shape, lash grouping, sclera tint, eyelid redness, and eye finish follow the reference. Hair color follows the character; hair base-fill method, shadow hue behavior, restrained strand density, clump grouping, highlight shape, edge behavior, and polish level follow the reference.

Conditional guards used:
<List only active guards and keep them short. Examples: face-mark integration, one-eye/covered-eye logic, visible-hand repair, pale/noisy hair fill, glow/magic as local-only, ornate accessory cap, simple-background cap, palette compression, anatomy-like artifact prevention. If no extra risk is active, write "none beyond style anchors, compression budget, and QC gates.">

Medium/material lock:
Preserve the reference's visible medium behavior exactly: <traditional/scanned/digital/mixed/3D/uncertain medium feel + visible evidence>. Apply the same surface texture, line material, pigment/brush/layer behavior, edge artifacts, and finish to character and background. Do not convert the reference into a cleaner digital style, traditional-media texture, 3D render, photo-realism, or another medium unless explicitly requested.

Imperfection/polish ceiling:
Do not make the result cleaner, smoother, glossier, more detailed, or more AI-polished than the reference. Preserve the reference's natural imperfections or clean finish: <line wobble, uneven fill, loose edge, rough gradient, scanned/paper artifact, digital brush/layer behavior, or other finish cues>.

Style fidelity contract:
Preserve the reference detail density, palette handling, edge hierarchy, eye rendering/coloring, hair coloring/construction, restrained strand density, accessory/detail rendering, background complexity, and rendering complexity.
Translate character details into that visual budget. If a character detail would make the image more ornate, more colorful, more cinematic, more accessory-heavy, more background-heavy, or more polished than the reference, simplify it to a style-matched cue instead of changing the core character trait.

Lighting lock:
<same light direction, shadow softness, highlight placement, contrast, ambient fill, background falloff>

Pose/expression lock:
<one precise sentence describing pose/expression/hand crop from the reference>
Ignore any conflicting pose, gesture, gaze, crop, camera, body-turn, shoulder-turn, or hand-action wording from the character description.

Makeup rule:
<inherit reference makeup by default OR combine explicit character makeup with reference makeup rendering>

Character appearance:
<compact visible traits from the compression gate only>

Background:
<compressed scene content from character/request, rendered strictly in the reference background style and reference background complexity; obey the packet's background allowance, such as one faint cue if reference background is simple>

Targeted negative constraints:
Always avoid full redraw, different art family, medium shift, cleaner/glossier polish, wrong pose/expression/crop, copied reference identity, raw character-sheet inventory, text, watermark, and signature. Add only the active negatives from the conditional guards above.
```

## Negative Prompt / Anti-Slop

Use this as a targeted negative bank, not as a paragraph to paste in full. First-pass prompts should include the always-on anti-redraw/style negatives plus only active conditional risks. The full list remains the QC/reroll reference.

Avoid:

- Landscape output, horizontal output, square output, or copying a non-9:16 reference aspect ratio.
- Face/focal center too close to top or bottom edge.
- Face proportion drift: wrong head/face shape, wrong face length/width, shifted eye/nose/mouth/chin spacing, generic anime face, rounder/chibi face, doll face, photoreal planes, or wrong age impression.
- Generic front-facing portrait when the reference has a different pose or expression.
- Hybrid pose made by mixing character-description prose with the reference pose.
- New gaze, expression, camera angle, body turn, or hand action not present in the reference.
- Invented visible hands when the reference hand is cropped/hidden.
- Extra fingers, melted fingers, floating support hand, broken wrist, clothing folds fused into fingers.
- Character/background style mismatch.
- Background rendered in a different style from the reference.
- Copied reference background content.
- Complex background when the reference has plain/no/simple background.
- Random props, crowded decorative elements, text, watermark, signature.
- Different lighting direction, stronger cinematic lighting, global glow, bloom haze, magic aura, sparkle fields, neon rim light, glowy mobile-game polish, or glossy plastic skin when not present in the reference.
- Copying reference identity, outfit, hair/eye color, accessories, or species.
- Losing or changing character hair color, eye color, outfit colors, skin tone, visible marks, or signature accessories without an explicit reason.
- Linework drift: wrong line color/tint, too-black outlines, too-thick contours, uniform vector-like strokes, too-clean taper, too many interior lines, missing broken/lost contours, or stronger contour authority than the reference.
- Eye color rendered with the wrong reference method: different iris layering, wrong catchlight shape, too much iris detail, different lash grouping, wrong sclera tint, or more glossy/perfect eye rendering than the reference.
- Face mark rendered as a detached sticker, crisp icon, high-contrast emblem, glowing rune, raised/cast-shadowed decal, separate-material mark, or mismatched tattoo instead of matching the reference face rendering.
- Over-rendered hair when the reference uses simple hair masses.
- Hair color rendered with the wrong reference method: many more strands, strand-by-strand rendering, dense flyaway fields, glossy string hair, cleaner gradients, glossier highlights, different shadow/highlight shape language, or more perfect clump geometry than the reference.
- New dominant palette that overpowers the reference palette.
- Saturated character colors rendered as a new global palette system instead of reference-style local colors.
- Omitting all character accessories when the crop and detail budget can support small style-matched cues.
- Ornate jewelry, chains, gems, detailed accessories, or full outfit exposition when the reference is low-accessory or low-detail.
- Detailed fabric texture when the reference fabric is broadly simplified.
- Full scenic environment when the reference background is plain or minimal.
- Character-sheet pressure: too many requested traits visible at once, making the result look like a different illustration style.
- Medium drift: clean digital polish from a hand-drawn/scanned/watercolor/marker reference, fake paper grain on a clean digital reference, glossy 3D shading from a flat or drawn reference, or photo-real rendering from an illustration reference.
- Polish drift: cleaner, smoother, glossier, more symmetrical, more perfect, or more AI-polished than the reference.
- Glow/specular drift: turning reference specular highlights or dappled light into aura, bloom, haze, bokeh/orb fields, magical sparkle, or global skin glow.

Prefer:

- 9:16 mobile portrait output.
- Safe face/focal placement.
- Same reference pose idea, expression, camera feeling, hand/crop logic.
- Same face proportion fingerprint and facial-feature construction.
- Same visible medium/material behavior and surface finish.
- Same detected style family, linework fingerprint, rendering, lighting, background style, and finish.
- Same glow/specular behavior: preserve only the reference's highlight type and glow budget.
- Same reference detail density, palette handling, background complexity, accessory/detail rendering, eye rendering/coloring, hair coloring/construction, restrained strand density, and polish ceiling.
- Compact character appearance replacement.
- Simple, style-consistent background content.

## QC Checklist

Score after generation:

```text
Style match: 1-5
Detected style family match: pass/fail
Pose idea match: 1-5
Pose-source compliance: pass/fail
Facial expression match: 1-5
Face proportion fingerprint match: pass/fail
Facial-feature construction match: pass/fail
Character identity match: 1-5
Linework fingerprint match: pass/fail
Line color/tint match: pass/fail
Line thickness/opacity match: pass/fail
Broken/lost contour match: pass/fail
Line density/contour authority match: pass/fail
Character local color fidelity: pass/fail
Eye color fidelity: pass/fail
Eye rendering/coloring strategy match: pass/fail
Hair color fidelity: pass/fail
Hair coloring/construction match: pass/fail
Strand-density match: pass/fail
Avoided copying reference identity: pass/fail
Makeup rule compliance: pass/fail
Lighting match: 1-5
Glow/specular profile match: pass/fail
Background style match: 1-5
Background content source compliance: pass/fail
Medium/material match: pass/fail
Detail-density match: pass/fail
Palette handling match: pass/fail
Background complexity match: pass/fail
Accessory/detail rendering compliance: pass/fail
Polish ceiling match: pass/fail
Character-sheet pressure controlled: pass/fail
9:16 mobile portrait output: pass/fail
Safe face/focal placement: pass/fail
Hands/anatomy: pass/fail/not visible
Crop/aspect safety: pass/fail
No watermark/signature/text: pass/fail
```

Minimum acceptable result:

- Style, pose idea, facial expression, character identity, lighting, and background style are 4 or higher.
- Detected style family, pose-source compliance, face proportion fingerprint match, facial-feature construction match, linework fingerprint match, line color/tint match, line thickness/opacity match, broken/lost contour match, line density/contour authority match, character local color fidelity, eye color fidelity, eye rendering/coloring strategy match, hair color fidelity, hair coloring/construction match, strand-density match with no extra fine hair-line noise, medium/material match, glow/specular profile match, detail-density match, palette handling match, background complexity match, accessory/detail rendering compliance, polish ceiling match, character-sheet pressure controlled, 9:16 mobile portrait output, safe placement, makeup rule, background content source, crop safety, and no watermark/signature/text all pass.
- Hands/anatomy pass when hands are visible.

## One-Reroll Rule

Generate one initial image only after style-anchor and conditional-guard preflight passes. Reroll automatically at most once, only for model noncompliance after the prompt contained the relevant active guard, or for a newly observed failure not yet covered by this policy.

Do not use reroll to compensate for a missing active prompt guard. If a failure was predictable from this policy, the reference, or the character prompt and the first prompt did not explicitly guard it, the correct action is to fix the prompt compiler or policy wording, then generate again with the missing guard present. If the first prompt includes raw character-sheet pressure that should have been suppressed by the hard compression gate, also label that as a prompt-compiler miss, not as a normal reroll.

Hard QC failures:

- Wrong style family.
- Pose/expression follows character-description prose instead of the reference.
- Output is not 9:16 mobile portrait.
- Face/focal center is too close to top/bottom.
- Character identity is wrong or reference identity was copied.
- Face proportion fingerprint or facial-feature construction drifted away from the reference.
- Makeup inheritance/blending failed.
- Background style/content rule failed.
- Medium/material behavior drifted away from the reference.
- Linework fingerprint drifted away from the reference.
- Character local colors, eye color, hair color, or signature accessories drifted away from the character description.
- Eye rendering/coloring, face mark integration, hair coloring/construction, strand density or extra hair-line noise, glow/specular behavior, detail density, palette handling, background complexity, accessory/detail rendering, polish ceiling, or character-sheet pressure control failed.
- Lighting strongly mismatches reference.
- Hands/anatomy/crop fails.
- Watermark, signature, text, extra character, or copied reference outfit/hair/color appears.

For reroll, change only the single highest-impact issue. Do not rewrite the entire prompt or generate unlimited variants.

Targeted fix lines:

```text
Style failure:
Preserve the detected reference style family exactly and apply the same linework, face/eye/hair/skin/clothing rendering, lighting, background treatment, and finish to the entire image. Do not convert the image into another art family.

Linework fingerprint failure:
Preserve the reference linework fingerprint exactly: same line color/tint, thickness range, opacity, taper/pressure rhythm, broken/lost contour behavior, line density, contour authority, focal line hierarchy, and line-to-fill relationship. Do not use crisp black manga outlines, uniform vector-like curves, heavier contour authority, dense interior detail lines, or cleaner lineart than the reference.

Face proportion failure:
Preserve the reference face proportion fingerprint exactly: same head/face shape, face length-to-width ratio, forehead/eye/nose/mouth/chin spacing, eye size/spacing/tilt, brow height, nose bridge/tip simplification, mouth size/placement, cheek volume, jaw taper, and chin shape. Translate the new character identity through this construction. Do not make the face rounder, chibi, doll-like, photoreal, younger/older, or generically anime.

Medium/material failure:
Preserve the reference visible medium behavior exactly. If the reference reads as hand-drawn, scanned paper, pencil, ink, watercolor, gouache, marker, or mixed traditional media, keep the same paper/pigment/line artifacts and avoid clean digital polish. If the reference reads as digital art, keep the same digital brush/layer/edge behavior and do not add fake traditional texture. If the medium is uncertain, match only the visible surface behavior and finish.

Pose failure:
Match the primary reference pose idea closely: same crop feeling, head angle, gaze direction, hand placement, hand visibility/crop, and main gesture. Ignore conflicting pose/camera/gaze/hand wording from the character description.

Expression failure:
Match the primary reference facial expression closely: same eye openness, gaze, brow feeling, mouth shape, blush intensity, and emotional beat.

Identity failure:
Keep the reference pose/expression/style, but replace hair, eyes, skin, outfit, accessories, species, and local colors with the character description.

Character local color failure:
Preserve the character's local colors exactly: hair color, eye color, skin tone, outfit colors, accessory colors, and visible marks. Translate those colors through the reference value range, chroma discipline, opacity, lighting, and blending method without replacing them with the reference character's colors.

Eye rendering/coloring failure:
Preserve the character's eye color, but match the reference eye rendering method exactly: same iris layering, upper-iris shadow, lower-iris glow or flat fill, pupil treatment, rim line, catchlight shape, sclera tint, lash grouping, eyelid redness, tear/glitter accents, and gloss/matte finish. Do not add extra iris complexity or cleaner glossy highlights beyond the reference.

Makeup failure:
If character makeup is unspecified, inherit the reference makeup/cosmetic treatment. If specified, combine it with the reference placement, finish, intensity family, edge softness, and stylization.

Background failure:
Use the requested/character scene content, but render it with the same background line treatment, shading method, blur/detail balance, texture, lighting simplification, and finish as the reference. Do not copy reference background content.

Detail-density failure:
Reduce everything outside the reference focal areas. Match the reference detail density exactly. Omit or simplify accessories, fabric texture, background props, and extra hair strands that make the image more ornate than the reference.

Palette failure:
Keep the reference value range, chroma discipline, temperature balance, and blending behavior. Preserve character local colors, but render them with the reference's palette handling rather than turning them into a new global color system.

Glow/specular failure:
Preserve only the reference's observed light effects: hard specular highlights, dappled light patches, small local shine, rim light, or bokeh only if visible in the reference. Remove global glow haze, bloom around the character, magical aura, floating sparkle fields, neon/cinematic rim light, glowy skin fog, and plastic mobile-game gloss unless the reference clearly has those effects.

Accessory/prop pressure failure:
Show at most one or two small character accents if the reference is low-accessory. Hide, crop, or omit the rest. Do not add chains, gems, decorative charms, full outfit details, or prop clusters unless the reference has similar accessory density.

Hair strategy failure:
Preserve the character's hair color, but match the reference hair coloring and construction. If the reference uses large hair masses with sparse strand lines and lost edges, keep that strategy; use the same base-fill method, shadow hue behavior, highlight shape, line tint, edge looseness, restrained strand density, and polish level. Avoid dense strand rendering, strand-by-strand detail, excessive flyaways, glossy string hair, many extra fine hair lines, saturated global wash, cleaner gradients, and over-polished hair volume.

Polish ceiling failure:
Do not make the image cleaner, smoother, glossier, more symmetrical, more detailed, or more AI-polished than the reference. Restore the reference finish cues such as line wobble, uneven fill, loose edges, rough gradients, scanned/paper artifacts, or restrained digital brush/layer behavior.

9:16 or placement failure:
Final output must be 9:16 mobile portrait. Reframe the reference pose into 9:16 vertical composition and keep the face/focal center comfortably inside the frame, away from the top and bottom edges.

Hand failure:
Preserve reference hand placement, action, visibility, crop, and occlusion. If cropped or hidden in the reference, keep it cropped or hidden. Simplify only visible fingers.
```
