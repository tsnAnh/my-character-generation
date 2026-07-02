# Generation Policy

Use this reference when building prompts or judging output for `generate-character-from-reference`.

## Priority Order

1. 9:16 mobile portrait output and safe face/focal placement win for final canvas, orientation, and subject placement.
2. A separate pose reference, when provided, wins for pose, camera, crop, silhouette, and hand placement only.
3. Primary reference wins for facial expression, pose idea, camera feeling, hand logic, composition intent, lighting behavior, art style, linework fingerprint, visible medium/material behavior, eye rendering/coloring method, iris layering, catchlight shape, hair coloring method, hair construction, strand density, detail density, palette handling, background complexity, edge hierarchy, imperfection/polish level, and rendering complexity.
4. Character description wins for identity, appearance, outfit, accessories, species, local colors, visible marks, explicit makeup, and requested background content. Translate those traits through the reference visual grammar instead of replacing them with reference identity traits.
5. Makeup follows the reference by default. Explicit character makeup is combined with the reference cosmetic rendering.
6. Background content changes according to character/requested scene, but background style and complexity strictly follow the reference.
7. Mood/color reference controls atmosphere only and does not override character local colors, primary-reference lighting behavior, or the primary-reference visual budget unless explicitly requested.

## Trait Translation Matrix

Use this matrix for every character and every reference. Do not hard-code a specific character, outfit, palette, or reference type.

```text
Character-controlled traits:
- Hair color, eye color, skin tone, outfit, accessories, species traits, visible marks/scars/tattoos, explicit makeup, and requested background content.

Reference-controlled construction:
- Pose, facial expression, camera/crop, gesture, hand logic, style family, visible medium/material behavior, linework fingerprint, shading method, eye rendering/coloring method, iris layering, catchlight shape, lash grouping, sclera tint, hair coloring method, hair construction, strand density, edge quality, imperfection/polish level, detail density, palette handling, background style, and rendering complexity.

Compatibility rule:
- Keep character traits, but draw them with the reference technique. Character eye color can change from the reference; iris layering, catchlight shape, lash grouping, sclera tint, and eye finish should not drift away from the reference. Character hair color can change from the reference; base color handling, strand count, clump grouping, highlight shape, edge breaks, and polish level should not drift away from the reference.
```

Character local colors and accessories are not style drift by themselves. They become drift only when their saturation, detail density, construction, finish, or polish level breaks the reference visual grammar.

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
- Style drift risks:
- Finish/polish:
```

Use `analyze-art-drawing` for this phase when available. Pull concrete terms from its analysis: medium/material classification, medium evidence, linework fingerprint, line weight hierarchy, line color/tint, line opacity, tapered/broken/lost contour, line density, contour authority, line-to-fill relationship, cel/soft cel/painterly/airbrush rendering, multiply-like shadows, highlight logic, edge hierarchy, eye color treatment, iris layer structure, catchlight shape, lash grouping, hair color treatment, hair mass/strand strategy, fabric fold grouping, background detail density, and lighting design.

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
- <medium/material behavior, style family, linework, value range, edge hierarchy, render density, eye rendering/coloring method, hair coloring/construction, strand density, imperfection/polish level, lighting, background complexity>

Character trait locks:
- <hair color, eye color, skin tone, outfit, accessories, species traits, visible marks, explicit makeup, requested background content>

Reference construction locks:
- <pose, expression, camera/crop, hand logic, linework, shading method, eye rendering/coloring, iris layering, catchlight shape, lash grouping, hair coloring method, hair construction, strand density, edge quality, polish ceiling, background style>

Allowed character replacements:
- <identity, hair/eye/skin/outfit/local colors translated into the reference style>

Suppress or reduce:
- <character details that would add too much detail, palette complexity, accessory rendering precision, props, background, glow, over-clean polish, or a different rendering family>
```

This contract must shape the final prompt. Do not paste all three sections if the user only wants a direct generation; use them internally to keep the prompt disciplined.

## Known Failure Preflight

Before calling image generation, run a prompt preflight. A known hard failure must be guarded in the first prompt, not discovered only after QC. If a reference visibly contains one of these constraints, the final prompt must contain a concrete positive lock and concrete avoid line for it.

Required guards:

- **Linework fingerprint**: line color/tint, thickness range, opacity, taper/pressure rhythm, broken/lost contour behavior, line density, contour authority, line-to-fill relationship.
- **Hair construction**: mass-first or strand-first strategy, strand density, clump scale, highlight shape, edge behavior, and whether extra strands are forbidden.
- **Polish ceiling**: whether the output must preserve roughness, line wobble, uneven fill, loose edges, imperfect gradients, scanned texture, or restrained digital polish.
- **Eye rendering/coloring**: eye color fidelity plus iris layering, catchlight shape, lash grouping, sclera tint, eyelid redness, and gloss/matte finish.
- **Character local colors**: hair, eyes, skin, outfit, marks, and accessory colors from the character description.
- **Accessory/detail rendering**: which accessories are allowed as small cues, which are hidden/cropped/simplified, and what material precision is forbidden.
- **Background complexity**: whether the background must remain plain, abstract, faint, low-detail, or scene-rich.
- **Pose/expression/hand crop**: pose source, expression source, hand visibility, occlusion, and anatomy simplification.

Preflight rules:

- If a known hard-failure axis is relevant and the prompt lacks a concrete guard, revise the prompt before generation.
- Do not rely on generic phrases such as "strictly match style", "same linework", "high quality", "not too detailed", or "follow reference" as a guard.
- For every high-risk axis, use visible terms from the reference analysis. Example: "very thin warm gray-brown low-opacity lineart with broken/lost contours" is a guard; "soft anime linework" is not.
- If the generated image fails a defined hard-failure axis and the prompt did not include its guard, classify it as a prompt-compiler miss, not a normal reroll.
- Reroll is reserved for model noncompliance after the prompt preflight passed, or for a newly observed failure mode not yet defined in the policy.

## Visual Budget And Character Compression

The reference image sets the maximum visual budget.

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
- Hair: preserve the character's hair color, but match the reference hair construction first. If the reference uses negative-space or mass-first hair with sparse strand lines, draw the new hair as broad masses with the character local color controlled by the reference value/chroma system; do not render every strand, add glossy perfect gradients, or turn the whole image into a saturated color wash.
- Hair coloring: translate the character hair color through the reference's base-mass fill, shadow hue, highlight shape, line tint, opacity, edge looseness, and value range. The color should read as the character's hair color, but the coloring method should read as the reference.
- Outfit: match the reference fabric detail level. If the reference sleeve is broad, pale, and simply shaded, do not add dense cable-knit, lace, jewelry chains, or full outfit detail.
- Accessories: if the character has accessories, include readable style-matched cues when the crop and detail budget allow. If the reference has few or no accessories, allow one or two small accents and treat the rest as hidden, cropped, or simplified; do not render accessory precision beyond the reference polish ceiling.
- Background: if the reference background is plain or abstract, use one faint scene cue only. Do not draw a full city, room, balcony, fairy lights, props, or hanging decorations.
- Glow/magic: if the reference has no strong glow, keep magical traits as tiny local accents, not global light effects.
- Palette: preserve the reference value range, dominant temperature, chroma discipline, and color blending behavior. Character colors should remain identifiable as local colors, but should not become a new global palette system unless the reference has comparable color intensity.
- Imperfection/polish: match the reference finish. If the reference has rough line edges, uneven fill opacity, imperfect gradients, scanned texture, or handmade looseness, preserve those artifacts. If the reference is clean digital, keep that clean finish but do not exceed it with extra gloss, hyper-detail, or perfectly regular AI polish.

## Character Description Filtering

Extract only visible generation data:

- Name or identity label, only if useful.
- Species/fantasy type if visible.
- Gender/presentation and apparent age range.
- Face shape and signature facial traits.
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
- Linework fingerprint: line color/tint, thickness range, opacity, taper/pressure rhythm, broken/lost contour behavior, line density, contour authority, focal line hierarchy, and line-to-fill relationship.
- Face simplification, eye rendering/coloring, iris layering, catchlight shape, lash grouping, nose/mouth treatment.
- Hair coloring method, hair shape language, strand density, highlight blocks.
- Skin shading, blush, shadow hue, highlight type.
- Clothing fold simplification and material finish.
- Accessory/detail rendering scale and simplification.
- Background rendering treatment.
- Lighting direction, shadow softness, highlight placement, contrast, and ambient fill.
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

## Prompt Template

Use this order for first-pass prompts.

```text
Generate a 9:16 mobile portrait image, regardless of the reference image's aspect ratio.
Keep the main subject's face/focal center comfortably inside the frame, not too close to the top or bottom edge. This framing rule wins over the reference crop.

Use the attached image as the primary visual reference.
Make the result feel like the reference image was redrawn with a different character identity.
Strictly match the reference pose idea, facial expression, gaze direction, head angle, camera feeling, hand placement, hand visibility/crop, composition intent, linework fingerprint, face simplification, eye rendering/coloring method, iris layering, catchlight shape, lash grouping, hair coloring method, hair construction, strand density, skin shading, clothing shading, makeup/cosmetic rendering, lighting direction, shadow softness, highlight placement, contrast, background rendering treatment, and overall finish.

Reference visual grammar:
<compact technical style card>

Character trait locks:
Preserve the new character's visible traits: <hair color, eye color, skin tone, outfit, accessories, species traits, visible marks, explicit makeup, requested background content>. Do not replace these with the reference character's identity traits.

Reference construction locks:
Draw those character traits using the reference construction: <pose, expression, camera/crop, hand logic, linework fingerprint, shading method, eye rendering/coloring, iris layering, catchlight shape, lash grouping, hair coloring method, hair construction, strand density, edge quality, accessory/detail rendering, background style>. Eye color follows the character; iris layering, catchlight shape, lash grouping, sclera tint, eyelid redness, and eye finish follow the reference. Hair color follows the character; hair base-fill method, shadow hue behavior, strand density, clump grouping, highlight shape, edge behavior, and polish level follow the reference.

Known failure guards:
- Linework guard: <specific line color/tint, thickness range, opacity, taper rhythm, broken/lost contour behavior, line density, contour authority, line-to-fill relationship>. Avoid <specific linework drift such as black outlines, crisp vector curves, dense interior line detail, heavy contour authority>.
- Hair guard: <specific mass/strand strategy, allowed strand density, clump scale, highlight shape, edge behavior>. Avoid <extra strands, glossy perfect gradients, over-polished hair volume, wrong construction>.
- Polish guard: <specific imperfection/polish ceiling>. Avoid <cleaner/smoother/glossier/more detailed output than reference>.
- Eye guard: <specific iris/catchlight/lash/sclera strategy>. Avoid <extra iris complexity, wrong catchlights, over-glossy eyes>.
- Detail/background/accessory guard: <specific visual budget>. Avoid <ornate accessories, busy background, extra props, full outfit exposition when the reference does not support it>.

Medium/material lock:
Preserve the reference's visible medium behavior exactly: <traditional/scanned/digital/mixed/3D/uncertain medium feel + visible evidence>. Apply the same surface texture, line material, pigment/brush/layer behavior, edge artifacts, and finish to character and background. Do not convert the reference into a cleaner digital style, traditional-media texture, 3D render, photo-realism, or another medium unless explicitly requested.

Imperfection/polish ceiling:
Do not make the result cleaner, smoother, glossier, more detailed, or more AI-polished than the reference. Preserve the reference's natural imperfections or clean finish: <line wobble, uneven fill, loose edge, rough gradient, scanned/paper artifact, digital brush/layer behavior, or other finish cues>.

Style fidelity contract:
Preserve the reference detail density, palette handling, edge hierarchy, eye rendering/coloring, hair coloring/construction, strand density, accessory/detail rendering, background complexity, and rendering complexity.
Translate character details into that visual budget. If a character detail would make the image more ornate, more colorful, more cinematic, more accessory-heavy, more background-heavy, or more polished than the reference, simplify it to a style-matched cue instead of changing the core character trait.

Lighting lock:
<same light direction, shadow softness, highlight placement, contrast, ambient fill, background falloff>

Pose/expression lock:
<one precise sentence describing pose/expression/hand crop from the reference>
Ignore any conflicting pose, gesture, gaze, crop, camera, body-turn, shoulder-turn, or hand-action wording from the character description.

Makeup rule:
<inherit reference makeup by default OR combine explicit character makeup with reference makeup rendering>

Character appearance:
<compact visible traits only>

Background:
<scene content from character/request, rendered strictly in the reference background style and reference background complexity; keep to one faint cue if reference background is simple>

Do not copy the reference character identity, hair color, eye color, outfit, accessories, species, watermark, signature, or background content unless explicitly requested.
```

## Negative Prompt / Anti-Slop

Avoid:

- Landscape output, horizontal output, square output, or copying a non-9:16 reference aspect ratio.
- Face/focal center too close to top or bottom edge.
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
- Different lighting direction, stronger cinematic lighting, excessive glow, glossy plastic skin.
- Copying reference identity, outfit, hair/eye color, accessories, or species.
- Losing or changing character hair color, eye color, outfit colors, skin tone, visible marks, or signature accessories without an explicit reason.
- Linework drift: wrong line color/tint, too-black outlines, too-thick contours, uniform vector-like strokes, too-clean taper, too many interior lines, missing broken/lost contours, or stronger contour authority than the reference.
- Eye color rendered with the wrong reference method: different iris layering, wrong catchlight shape, too much iris detail, different lash grouping, wrong sclera tint, or more glossy/perfect eye rendering than the reference.
- Over-rendered hair when the reference uses simple hair masses.
- Hair color rendered with the wrong reference method: many more strands, cleaner gradients, glossier highlights, different shadow/highlight shape language, or more perfect clump geometry than the reference.
- New dominant palette that overpowers the reference palette.
- Saturated character colors rendered as a new global palette system instead of reference-style local colors.
- Omitting all character accessories when the crop and detail budget can support small style-matched cues.
- Ornate jewelry, chains, gems, detailed accessories, or full outfit exposition when the reference is low-accessory or low-detail.
- Detailed fabric texture when the reference fabric is broadly simplified.
- Full scenic environment when the reference background is plain or minimal.
- Character-sheet pressure: too many requested traits visible at once, making the result look like a different illustration style.
- Medium drift: clean digital polish from a hand-drawn/scanned/watercolor/marker reference, fake paper grain on a clean digital reference, glossy 3D shading from a flat or drawn reference, or photo-real rendering from an illustration reference.
- Polish drift: cleaner, smoother, glossier, more symmetrical, more perfect, or more AI-polished than the reference.

Prefer:

- 9:16 mobile portrait output.
- Safe face/focal placement.
- Same reference pose idea, expression, camera feeling, hand/crop logic.
- Same visible medium/material behavior and surface finish.
- Same detected style family, linework fingerprint, rendering, lighting, background style, and finish.
- Same reference detail density, palette handling, background complexity, accessory/detail rendering, eye rendering/coloring, hair coloring/construction, strand density, and polish ceiling.
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
- Detected style family, pose-source compliance, linework fingerprint match, line color/tint match, line thickness/opacity match, broken/lost contour match, line density/contour authority match, character local color fidelity, eye color fidelity, eye rendering/coloring strategy match, hair color fidelity, hair coloring/construction match, strand-density match, medium/material match, detail-density match, palette handling match, background complexity match, accessory/detail rendering compliance, polish ceiling match, character-sheet pressure controlled, 9:16 mobile portrait output, safe placement, makeup rule, background content source, crop safety, and no watermark/signature/text all pass.
- Hands/anatomy pass when hands are visible.

## One-Reroll Rule

Generate one initial image only after Known Failure Preflight passes. Reroll automatically at most once, only for model noncompliance after the prompt contained the relevant hard guard, or for a newly observed failure not yet covered by this policy.

Do not use reroll to compensate for a missing prompt guard. If a failure was already defined in this policy and the first prompt did not explicitly guard it, the correct action is to fix the prompt compiler or policy wording, then generate again with the missing guard present. Label that as a prompt-compiler miss, not as a normal reroll.

Hard QC failures:

- Wrong style family.
- Pose/expression follows character-description prose instead of the reference.
- Output is not 9:16 mobile portrait.
- Face/focal center is too close to top/bottom.
- Character identity is wrong or reference identity was copied.
- Makeup inheritance/blending failed.
- Background style/content rule failed.
- Medium/material behavior drifted away from the reference.
- Linework fingerprint drifted away from the reference.
- Character local colors, eye color, hair color, or signature accessories drifted away from the character description.
- Eye rendering/coloring, hair coloring/construction, strand density, detail density, palette handling, background complexity, accessory/detail rendering, polish ceiling, or character-sheet pressure control failed.
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

Accessory/prop pressure failure:
Show at most one or two small character accents if the reference is low-accessory. Hide, crop, or omit the rest. Do not add chains, gems, decorative charms, full outfit details, or prop clusters unless the reference has similar accessory density.

Hair strategy failure:
Preserve the character's hair color, but match the reference hair coloring and construction. If the reference uses large hair masses with sparse strand lines and lost edges, keep that strategy; use the same base-fill method, shadow hue behavior, highlight shape, line tint, edge looseness, strand density, and polish level. Avoid dense strand rendering, saturated global wash, cleaner gradients, and over-polished hair volume.

Polish ceiling failure:
Do not make the image cleaner, smoother, glossier, more symmetrical, more detailed, or more AI-polished than the reference. Restore the reference finish cues such as line wobble, uneven fill, loose edges, rough gradients, scanned/paper artifacts, or restrained digital brush/layer behavior.

9:16 or placement failure:
Final output must be 9:16 mobile portrait. Reframe the reference pose into 9:16 vertical composition and keep the face/focal center comfortably inside the frame, away from the top and bottom edges.

Hand failure:
Preserve reference hand placement, action, visibility, crop, and occlusion. If cropped or hidden in the reference, keep it cropped or hidden. Simplify only visible fingers.
```
