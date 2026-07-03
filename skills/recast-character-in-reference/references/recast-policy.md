# Recast Policy

Use this reference when editing or prompt-compiling for `recast-character-in-reference`.

## Why Recast Is Different From Generate

Generation asks the model to imagine a new image from a style reference. Recast asks the model to modify the supplied image while preserving its structure.

When fidelity matters, write edit prompts as local changes on top of a locked source:

```text
Keep X exactly.
Replace only Y.
Compress Z.
Avoid full redraw.
```

Do not write prompts as broad character art descriptions. Broad descriptions invite the model to reinterpret the entire character sheet as fantasy concept art.

## Patch Map

Build this map before prompting:

```text
Framing mode:
- Source-crop mode or Mobile portrait mode:
- App-safe focal placement:

Edit target locks:
- Pose/crop/camera:
- Style family / rendering model:
- Realism/flatness/abstraction balance:
- Face proportion fingerprint:
- Facial-feature construction:
- Subject form/material modeling:
- Expression/gaze:
- Hand placement/crop logic:
- Body/anatomy repair needed:
- Linework:
- Lighting:
- Glow/specular profile:
- Medium/rendering:
- Detail density:
- Hair mass/clump construction:
- Hair strand density:
- Hair fill masses/global grain behavior:
- Background style:
- Background/decor rendering method:
- Polish ceiling:

Replace from character prompt:
- Hair:
- Eyes:
- Skin:
- Visible mark/species trait:
- Outfit cue:
- Accessory cue(s):
- Background content cue:

Compress:
- Outfit details:
- Accessories:
- Background/decor content:
- Magic/glow:
- Props:
- Note: compression reduces content inventory only; it must not change the source style family, rendering model, form/material modeling, lighting, edge behavior, or medium complexity.

Omit:
- Lore/personality:
- Quality/style adjectives:
- Unsupported generic style labels:
- Conflicting pose/camera/gaze prose:
- Full prop/background inventories:
```

The final edit prompt should use the map, not the raw character sheet.

## Mobile Portrait Mode And App-Safe Focal Placement

Use Mobile portrait mode when the user asks for mobile, app, avatar, phone wallpaper, mobile portrait, 9:16, portrait output, or explicitly says "Mobile portrait mode".

Rules:

- Force final output to 9:16 vertical portrait.
- Preserve the source pose, hand placement, head angle, expression, face construction, linework, and crop feeling.
- Reframe by extending, simplifying, or reducing background in the source style; do not stretch the character or invent a new pose.
- Keep a top header-safe zone. The top 12-16% of the canvas should be background, hair edge, or nonessential atmosphere only.
- Keep eyes, facial marks, mouth, and key accessories below the likely app header.
- Keep the face/focal center in an app-safe upper-middle band, roughly 38-50% down from the top of the canvas.
- Keep the eye line roughly 30-42% down from the top of the canvas when the crop allows.
- Keep breathing room above the head and below visible hands/outfit cues.
- Avoid face placement that is too high, too low, too close to the top/bottom edge, or so off-center that app UI would cover the focal point.

Prompt guard:

```text
Mobile portrait mode: final output must be 9:16 vertical. Preserve the source pose and crop feeling, but reframe with source-style background so the face/focal center sits in the app-safe upper-middle band. Keep the top header-safe zone nonessential; no eyes, facial marks, mouth, or key accessories under the likely app header. Do not place the face too high, too low, or hard against any edge.
```

## Replacement Rules

### Body-Wide Anatomy And Basic Defects

Preserve the source pose, crop, body placement, and roughness, but do not preserve or accept malformed anatomy from the source, prompt pressure, or an intermediate output. Style fidelity is never a reason to accept a broken body part.

Inspect every visible body region before finalizing:

- eyes and pupils: aligned, plausible, not duplicated, melted, mismatched, or looking in impossible directions unless the source does
- face, nose, mouth, jaw, and chin: same construction as the source, not warped, duplicated, shifted, or collapsed
- neck, shoulders, collarbones, chest/torso, waist, and hips: plausible transitions, no broken joints, no impossible twist, no collapsed silhouette
- arms, elbows, wrists, hands, and fingers: plausible limb flow, no missing/extra segments, no fused/webbed/melted digits
- legs, knees, ankles, feet, and toes when visible: plausible placement, no missing/extra limbs, no broken joints, no deformed feet
- clothing, accessories, hair, rain, background marks, and highlights: must not read as extra anatomy, stray fingers, extra joints, unwanted limbs, or deformed body contours

If a visible body part is malformed, central, or hard to explain through crop/overlap/shadow, mark the result as a basic image-defect failure. Correct it locally if the rest of the image passes; otherwise reroll.

### Hands And Cropped Anatomy

Preserve hand placement, gesture direction, crop feeling, lighting, and source-style roughness. Do not preserve malformed anatomy from the source or from an intermediate output.

If the source hand is distorted, ambiguous, or missing/merging fingers, treat that as a repair target:

- Keep the same hand pose and approximate silhouette.
- Make the visible hand read as five plausible fingers unless one finger is naturally hidden by angle, palm overlap, sleeve/cuff, object contact, shadow, or crop.
- If only four fingers are visible, explicitly explain the fifth finger through natural occlusion, not omission.
- Keep fingers in the same rough linework and painterly finish as the source; do not over-render or make a clean anatomy study.
- Avoid extra fingers, four-finger hands with no occlusion logic, fused fingers, webbed fingers, melted palms, duplicate nails, broken knuckles, or warped wrists.
- Do not let accessory details, cuff embroidery, lace, glass-thread motifs, jewelry, rain streaks, magic effects, background lines, or white highlights spill onto the hand and read as webbing or stray anatomy.
- If the character prompt contains hand-adjacent details such as cuff embroidery or rings, place them on the clothing/accessory edge, not across the fingers, unless the user explicitly asks for hand markings or hand jewelry.

Hand preflight before prompting:

- Name whether the source hand is clean, flawed, cropped/ambiguous, or not visible.
- If flawed or ambiguous, add a correction line: "preserve hand placement/crop but repair the hand into plausible source-style anatomy."
- Add a visibility rule: "five fingers visible, or the fifth finger naturally hidden by overlap/crop/sleeve/shadow."
- Put malformed hands, missing fingers, extra fingers, fused/webbed fingers, melted palms, and white/stringy hand artifacts in the negative prompt.

### Hair

Replace color, length, and major silhouette only if requested. Preserve the source hair construction and keep hair mass-first unless the source is clearly strand-first:

- mass-first or strand-first strategy
- clump size
- strand density, with a bias toward fewer strands when uncertain
- fill texture frequency and noise scale
- shadow/highlight mass size
- highlight shape
- line tint and opacity
- edge breaks and flyaways
- polish level

Hair must read as masses first, strands second. Avoid adding more hair detail than the source supports. Hair must not become a field of many thin individual strands, glossy string-like locks, parallel separators, or AI-polished flyaway noise. If the source hair reads as broad masses, soft clumps, negative space, loose brush shapes, or sparse strands, keep that mass-first strategy and show only rare source-matched edge strands. If the source is already strand-heavy, match or reduce its strand density; do not increase strand count, regularity, or shine.

When the character prompt says "broad clumps", "minimal individual strands", "soft chunks", "simple hair shapes", or similar, treat that as a hard local trait. Use fewer, larger hair groups with minimal internal linework. Do not reinterpret those words as many separated locks.

Hair color fill is a separate lock from strand count. This applies to every hair color, not only pale or white hair. Recolor hair through the source's fill method:

- Use broad source-style shadow and highlight masses.
- Keep the texture low-frequency and medium-scale, not busy, crunchy, or hair-local.
- If the source has paper grain, scanned texture, brush grain, or uneven opacity, keep it global/source-matched across the image and do not concentrate extra noise inside the hair.
- The hair area should not become the noisiest region of the image. Hair interiors should read as calm paint/fill masses with large value islands before they read as texture.
- Avoid random speckled color static, salt-and-pepper texture, noisy dither, peppered value flecks, many tiny alternating color strokes, airbrushed micro-streaks, glittery highlight crumbs, over-sharpened hair texture, crunchy compression-like fill, or AI-looking color shimmer.
- Do not "solve" this by making the hair glossy, smooth plastic, clean vector, or hyper-rendered. The fix is source-matched broad paint/fill texture, not polish.
- For pale, white, silver, pastel, neon, or highly saturated hair, be extra strict: use slightly moderated colors, darker roots/underside or broad shadow islands when useful, and broad calm fills rather than tiny strokes or peppered texture.

Hair preflight before prompting:

- Name the source hair strategy: mass-first, strand-first, or ambiguous.
- Name the source hair fill strategy: broad blocky masses, flat fill, brush wash, marker streaks, paper/scanned grain, or other visible method.
- If mass-first or ambiguous, write a concrete cap such as "few broad clumps, minimal internal lines, rare edge strands only."
- Write a concrete fill cap such as "broad low-frequency hair color masses; source grain stays global, not concentrated inside hair; no speckled/dithered/micro-streak hair texture."
- Put the fill cap in the positive prompt whenever hair color changes; do not rely on negative prompts alone to prevent hair-local noise.
- Put dense flyaways, fine hair-line noise, glossy string hair, many separated locks, noisy hair fill in any hair color, speckled color static, salt-and-pepper hair texture, dithered hair texture, and hair micro-streaks in the negative prompt.

### Eyes

Replace eye color and tiny signature eye traits only. Preserve:

- eye shape and size
- eyelid construction
- iris layering
- pupil/rim treatment
- catchlight size and shape
- lash grouping
- sclera and eyelid tint
- gloss/matte finish

Do not convert simple eyes into galaxy eyes, jewel eyes, or hyper-detailed fantasy eyes.

### Face And Identity

The source face construction is a lock unless a separate face reference is provided.

Preserve:

- head/face shape
- face length and width
- forehead, eye, nose, mouth, and chin spacing
- jaw/chin/cheek construction
- nose and mouth simplification
- expression and gaze

Patch visible identity traits such as skin tone, mark, makeup color, or species detail without moving the facial features.

### Visible Marks And Species Traits

Face marks are allowed when they are requested, implied by the character description, or useful as a signature identity cue. The model may choose a face mark, non-face mark, accessory, clothing detail, hair cue, or species trait based on the character concept and the reference's visual budget.

If a face mark is used:

- Keep it tiny, low-contrast, and partially absorbed into the source face shading.
- Render it with the same line tint, edge roughness, opacity, value range, and medium behavior as the source face.
- Unless the prompt explicitly says the mark is raised, embossed, painted, metallic, glowing, inked, or attached, treat it as flat pigment under/within the skin, flush with the face surface. It should have no raised edge, no cast shadow, no sticker outline, and no separate material highlight.
- Make it feel like a faint birthmark, scar, blush-shaped tint, or skin-tone variation rather than a decorative decal.
- Avoid sticker-like marks, crisp emblem geometry, glowing runes, high-contrast under-eye icons, floating symbols, perfect tattoo linework, or marks that sit on top of the face instead of inside the drawing.
- If the source face is small, shadowed, heavily cropped, or low-detail, omit the face mark or move the signature cue to an accessory, clothing detail, hair cue, hand mark, collarbone mark, or species trait.

### Outfit

Patch only the visible garment regions in the crop. Convert full outfit inventories into one or two readable cues.

Example:

- Character prompt says: cream cardigan, midnight-blue dress, translucent star sleeves, crescent hem, ribbons.
- Tight portrait source supports: cream cardigan edge plus midnight-blue neckline, maybe one faint sleeve cue.
- Omit: hem, full dress construction, ribbon inventory, dense star pattern.

### Accessories

Use the source accessory budget. If the source has few small accessories, include one or two small cues:

- hair clip
- choker
- small earring
- tiny mark

Do not add ornate jewelry, gem facets, chains, charms, or repeated motifs unless the source already has comparable detail density.

### Background

Background content follows the character/request, but rendering style and complexity follow the source.

Treat source-only decorative motifs as replaceable background/decor content, not structure locks. This includes flowers, leaves, vines, foreground blur, paper stars, furniture, props, scenery, signs, or ornamental framing that are not part of the requested character identity.

Preserve:

- softness or blur level
- line/detail density
- color/value restraint
- lighting relationship to the character
- foreground/background depth behavior
- overall simplicity or density budget

Replace, reduce, or omit:

- source-specific flowers, leaves, plants, props, scenery, ornaments, or other decor when they are not in the character prompt
- source background subject matter that conflicts with the requested character environment

Example:

- If the source has yellow flowers but the character prompt asks for a cozy balcony, do not lock the flowers. Replace them with a faint balcony rail, soft twilight wash, or a few distant city-light dots in the same blurred, low-detail background style.
- If the source has blurred paper stars but the character prompt asks for a garden, paper stars can disappear; keep only the source's soft blur and complexity level.

If the source background is simple, blurred, or low-detail:

- use one faint background cue
- keep it soft and low contrast
- avoid full scenery, prop clusters, text, signs, bokeh fields, and decorative filler

If the source background is detailed, preserve the same detail density and rendering method while swapping content.

## Style-Family And Rendering-Model Lock

Before writing the source-look sentence, identify the source's visible style family, rendering model, medium behavior, and realism/flatness/abstraction balance. This lock comes before hair, outfit, background, or detail-budget corrections.

Use concrete source evidence, not a familiar label:

- semi-realistic painterly character illustration
- realistic-painterly fantasy illustration with stylized proportions
- anime-realistic hybrid with realistic skin planes and anatomical light modeling
- flat cel-shaded anime
- webtoon/manhwa clean-gradient style
- sketchy ink-and-wash drawing
- painterly realism with stylized facial proportions
- watercolor, gouache, marker, pencil, charcoal, oil/acrylic, collage, pixel art, 3D render, or photoreal camera/rendering behavior when visibly present

Do not let one familiar label override visible construction. Do not call a source "anime" just because it has stylized hair, fantasy traits, large-ish eyes, or attractive character design. Do not call a source "watercolor" because it is soft, "oil painting" because it is painterly, "3D" because it is glossy, or "photoreal" because it has realistic anatomy. Name the visible line, edge, fill, texture, lighting, material, and form-modeling behavior.

The rule is symmetric across art types:

- If the source is semi-realistic or realistic-painterly, keep its realistic planes, anatomical/material volume, and painterly edges.
- If the source is flat anime/cel-shaded, keep its flat construction, graphic shadows, and low material modeling.
- If the source is webtoon/manhwa, keep its clean line/gradient system and polish ceiling without pushing it toward painterly realism.
- If the source is watercolor, gouache, marker, pencil, charcoal, ink, or sketch, keep its medium texture, edge behavior, and imperfection profile.
- If the source is 3D, photoreal, pixel art, collage, or another format, keep that rendering model instead of converting it into illustration or painterly concept art.

Style-family lock examples:

```text
Preserve the source's semi-realistic painterly fantasy illustration style: realistic facial planes, anatomical collarbone and hand structure, natural top-light skin modeling, painterly fabric folds, stylized proportions, and illustration line/edge behavior. Do not simplify into flat anime, cel-shaded anime, webtoon, chibi, doll-like, mobile-game portrait, or clean fantasy character art.
```

```text
Preserve the source's flat cel-shaded anime style: simplified face planes, clean graphic shadows, crisp lineart, and low material modeling. Do not push it toward painterly realism, photoreal skin, or cinematic concept-art rendering.
```

```text
Preserve the source's watercolor-and-ink rendering model: pigment-like soft blooms, paper-grain texture, broken ink contours, matte color pooling, and low-gloss finish. Do not convert it into smooth digital anime, oil paint, 3D, or photoreal rendering.
```

Correction rule:

- When correcting excessive costume detail, ornate accessories, hair noise, or background clutter, reduce only those local inventories.
- Do not use vague phrases such as "lower detail", "simpler style", "more anime", "more realistic", "cleaner", "less realistic", or "more painterly" unless that is the source's actual direction.
- Say what local inventory should reduce while explicitly preserving the source rendering model. Example: "reduce ornate costume/background inventory while preserving the source's watercolor paper grain, soft pigment edges, and loose ink contours." For a realistic-painterly source, say: "reduce ornate costume/background inventory while preserving realistic facial planes, form/material modeling, anatomical lighting, painterly folds, and the original realism/flatness/abstraction balance."

## Source-Look Priority

Generic phrases like "same style" are too weak. Before writing the final edit prompt, name the source's concrete visual evidence and lock it as the first priority after pose/crop.

Capture only what is visible:

- linework: rough, clean, heavy, thin, broken, lost-and-found, sketchy, tapered, opaque, transparent, tinted, or black
- fill/shadow method: blocky paint fills, soft cel layers, watercolor wash, marker-like streaks, airbrush gradients, flat fills, or dry-brush texture
- edge behavior: hard edges, ragged edges, loose contours, negative-space gaps, imperfect overlaps, or polished vector edges
- finish: grainy, scanned, hand-finished, uneven opacity, imperfect sketch polish, restrained digital polish, or glossy clean finish
- lighting/specular: dappled highlights, matte shadows, local hard highlights, low-key value range, or no glow
- background method: dense painterly environment, soft compressed cue, blurred decor, flat color field, or simple dark void
- form/material evidence: realistic facial planes, anatomical hands/collarbones, natural skin value modeling, painterly fabric folds, stylized-flat simplification, graphic cel shadows, watercolor blooms, gouache opacity, pencil tooth, ink pooling, marker streaks, 3D material shading, photoreal camera behavior, pixel grid constraints, or collage cut edges

When the source looks like the Grimhilde-style sample, use concrete wording like:

```text
Preserve the rough expressive black-ink linework, blocky painterly shadow masses, broken/lost contours, dark low-key value range, grainy hand-finished texture, uneven fill opacity, and imperfect sketchy polish ceiling. Keep the background drawn with the same dark painterly density and line/fill texture if it must be extended for 9:16.
```

Do not add a different "better" art direction. Avoid words that push the model toward a new style family: cinematic concept art, ultra detailed, refined anime rendering, glossy fantasy illustration, clean mobile-game portrait, beautiful lighting, high quality, polished, rendered, dramatic glow, lower-detail anime, flat anime, webtoon, or photorealism unless the source visibly belongs there.

### Glow And Magic

Separate local marks from lighting effects.

Allowed by default:

- existing source specular highlights
- existing dappled light patches
- small jewelry shine
- one tiny local mark if the character requires it

Forbidden unless the source visibly has it:

- global bloom
- aura
- full-body glow
- sparkle fields
- neon rim light
- magical haze
- bokeh/orb backgrounds
- plastic/glass skin shine

Translate character words like "starlit", "glowing", "moonlight", or "magical" into tiny local cues, not a new lighting system.

## Edit Prompt Template

```text
Edit the attached image. Treat it as the structure lock and preserve its pose, crop, camera feeling, style family/rendering model, face proportion fingerprint, facial-feature construction, subject form/material modeling, expression, gaze, hand placement/crop logic, linework, lighting, rendering method, background style, detail density, and polish ceiling.

Framing mode: <source-crop mode OR Mobile portrait mode>. If Mobile portrait mode is active, force 9:16 vertical output, keep the face/focal center in the app-safe upper-middle band, reserve the top header-safe zone for nonessential background/hair only, and reframe by extending source-style background rather than changing pose or face construction.

Style-family / rendering-model lock: <specific visible art family, medium behavior, and realism/flatness/abstraction balance>. Preserve the source's actual rendering model: realistic-painterly form modeling, flat cel simplification, webtoon/manhwa gradients, watercolor/ink/gouache/pencil texture, 3D material shading, photoreal camera behavior, pixel-art constraints, collage edges, or whatever is visibly present. Do not convert the source into a more realistic, flatter, cleaner, glossier, more painterly, more anime-like, more 3D-like, or more photoreal style unless that is already the source's style.

Source-look priority: <specific visible style evidence: line tint/weight, broken or clean contours, fill/shadow method, edge behavior, texture/grain, background rendering, lighting/value range, and imperfect or clean polish ceiling>. Preserve this art method across the character and any extended background.

Make only these visible replacements:
- <hair replacement>
- <eye replacement>
- <skin/mark replacement; face marks are allowed when fitting, but must be subtle, source-style-integrated, and flush with/within the skin unless explicitly described as raised/painted/inked/attached. Move to accessory/clothing/species cue if the crop/style cannot support them>
- <outfit cue>
- <one or two accessory cues>
- <compressed background cue if requested>

Keep the source art method: <specific linework, eye rendering, hair construction, restrained hair strand density, source-matched low-frequency hair fill masses, global grain/noise behavior, skin shading, lighting, glow/specular profile, and finish>.

Body-wide anatomy guard: preserve pose, placement, and crop, but repair malformed visible anatomy across eyes, pupils, face, nose, mouth, jaw, neck, shoulders, collarbones, chest/torso, waist, hips, arms, elbows, wrists, hands, fingers, legs, knees, ankles, feet, toes, joints, and silhouette. Keep every repair in the source's rough linework, value range, lighting, texture, and polish level. Do not let clothing, cuffs, embroidery, thread motifs, jewelry, hair, rain, magic, background lines, or highlights attach to or read as any body part.

Hand-specific guard: preserve hand placement/crop but repair malformed, missing, extra, fused, or webbed fingers. A visible hand must show five plausible fingers, or the fifth finger must be naturally hidden by angle, palm overlap, sleeve/cuff, object contact, shadow, or crop. Keep the repair in the source's rough linework and polish level. Do not let cuff embroidery, thread motifs, jewelry, rain, magic, background lines, or white highlights spill onto the hand or read as webbing.

Outfit/accessory budget: <concrete cap>. Reduce only local costume/accessory inventory; do not change the source style family, rendering model, form/material modeling, or light behavior.
Background budget: <concrete cap>. Compress background content without flattening the source's rendering style or changing the overall realism/flatness/abstraction balance.
Glow budget: <concrete cap>.
Hair strand budget: match or reduce the source strand density; use broad clumps when the source is mass-first or ambiguous; avoid strand-by-strand rendering, dense flyaways, glossy string hair, or extra fine hair-line noise.
Hair simplification priority: if the character prompt requests broad clumps or minimal strands, use fewer larger clumps with minimal internal linework; do not split the hair into many thin locks.
Hair fill budget: for every hair color, recolor hair with broad source-style shadow/highlight masses and low-frequency paint/fill texture. Preserve source grain as global image/medium texture only, not concentrated inside the hair. Hair interiors should be calmer than the linework and should not become a speckle field. For pale, white, silver, pastel, neon, or highly saturated hair, use moderated color, darker roots/underside, or broad shadow islands when useful to create volume without tiny texture. Avoid speckled color static, salt-and-pepper hair texture, noisy dither, peppered value flecks, many tiny alternating strokes, airbrushed micro-streaks, glittery highlight crumbs, crunchy compression-like fill, or over-sharpened AI hair texture.

Do not redraw the image as a new character illustration. Do not change pose, style family/rendering model, facial construction, subject form/material modeling, expression, hand placement/crop logic, linework, lighting, background rendering method, hair strand density, or polish level.
```

## Pre-Final QC And Reroll Gate

Before returning a direct recast result, inspect the output itself. Passing the reference-lock check is necessary but not sufficient. The output must pass both gates:

1. Reference-lock gate: source pose/crop/camera, face construction, expression/gaze, hand placement/crop logic, style family/rendering model, linework, lighting, background style, hair construction, polish ceiling, and requested visible trait patches are preserved or correctly changed.
2. Basic image-defect gate: every visible body part and boundary is plausible in the output's own image space, including eyes, pupils, face, nose, mouth, jaw, neck, shoulders, collarbones, chest/torso, waist, hips, arms, elbows, wrists, hands, fingers, legs, knees, ankles, feet, toes, body proportions, clothing/accessory boundaries, text/watermarks, and artifact zones.

Treat these as hard reroll or correction blockers even if the source style looks correct:

- malformed, melted, fused, webbed, duplicated, missing, or extra visible body parts
- broken eyes or pupils, mismatched gaze, duplicated facial parts, warped face, deformed nose/mouth/jaw/chin, or shifted facial construction
- distorted neck, broken shoulders/collarbones, collapsed chest/torso, impossible waist/hip transition, or body silhouette that no longer makes anatomical sense
- malformed arms, elbows, wrists, hands, fingers, legs, knees, ankles, feet, or toes
- four-finger hands without natural occlusion logic
- accessories, embroidery, rain lines, hair strands, background strokes, clothing edges, or highlights that read as fingers, limbs, webbing, extra joints, unwanted facial features, or stray anatomy
- extra limbs, missing limbs, impossible joints, warped shoulders/wrists/ankles, or deformed anatomy
- text, watermark, signature, obvious compression/artifact patches, or disconnected image debris near the subject
- severe overpolish, style conversion, or detail noise that hides anatomy or makes the image read as AI-generated

Do not finalize an output just because it matches the reference art style, pose, or palette. If a basic defect is central, obvious, or on any visible body part, mark the QC as fail and use one correction or reroll when available.

Use a targeted correction when the rest of the image passes and the failure is local:

```text
Keep the generated character, source pose/crop, face construction, expression, style family/rendering model, source form/material modeling, lighting, linework, hair rendering, outfit cues, background style, and polish ceiling unchanged. Correct only the visible basic defect: repair malformed eyes/pupils/face/nose/mouth/neck/shoulders/chest/torso/arms/wrists/hands/fingers/hips/legs/feet/joints/body proportions or anatomy-like accessory/background artifacts into plausible source-style anatomy. If a hand is visible, it must show five plausible fingers, or the fifth finger must be naturally hidden by overlap/crop/sleeve/shadow. Keep the correction in the same roughness, line tint, value range, texture, and imperfect polish as the source.
```

Reroll instead of finalizing when the output has multiple basic defects, a visible anatomy defect cannot be isolated cleanly, the correction would require a new pose or new face/body construction, or the result would still be unusable for an app avatar despite style fidelity.

## Locked-Axis Correction Passes

If an output fails a locked axis, correct only that axis and keep every passing axis unchanged. Do not fix one local failure by changing the whole style family.

When correcting hair noise:

```text
Keep the generated character, source pose/crop, face construction, expression, style family/rendering model, source form/material modeling, lighting, linework, background style, and outfit cues unchanged. Correct only the hair fill/texture: broad source-style shadow/highlight masses, source grain stays global, no speckled/dithered/micro-streak hair texture.
```

When correcting ornate costume/background clutter:

```text
Keep the generated character, source pose/crop, face construction, expression, style family/rendering model, source form/material modeling, lighting, linework, hair rendering, and background rendering method unchanged. Reduce only the local costume/accessory/background inventory. Preserve the original medium behavior and realism/flatness/abstraction balance, whether that means painterly realism, flat cel shading, webtoon gradients, watercolor/ink texture, sketch roughness, 3D shading, photoreal behavior, pixel constraints, or another visible art type.
```

Avoid correction wording that says only "lower detail", "simplify", "less detailed", "more anime", "more realistic", "cleaner", or "more painterly". Those phrases can collapse or convert the source into the wrong art family.

## Placement Correction Pass

If a direct recast output fails Mobile portrait placement, produce one corrected output before finalizing. Treat this as a framing correction, not a new character reroll.

Use this targeted correction:

```text
Keep the generated character, patched traits, source art style, face construction, expression, hand placement, lighting, linework, and background style unchanged. Correct only the framing: make the canvas 9:16 vertical, move/reframe the face and focal center into the app-safe upper-middle band, keep eyes and facial marks below the likely app header, add source-style background padding where needed, and avoid placing the face too high, too low, or close to any edge.
```

Do not use a placement correction to alter hair color, eye color, outfit cues, accessories, lighting, glow, or style. If the available image tool cannot edit the existing result, rerun with the same prompt plus the placement correction line.

## Anti-Redraw Negative Prompt

Avoid:

- full redraw from scratch
- new pose, new head angle, new hand placement, new crop, or new camera
- different style family, unsupported style label, unsupported photoreal/anime/watercolor/3D/sketch/etc. label, style simplification, style upgrading, or loss of the source realism/flatness/abstraction balance
- flat anime, cel-shaded anime, webtoon/manhwa simplification, painterly realism, photorealism, 3D rendering, watercolor/ink conversion, oil-paint conversion, or clean mobile-game/fantasy character art unless the source visibly supports that direction
- loss of source-specific form/material modeling, medium texture, edge behavior, lighting logic, brush/pigment/line behavior, or camera/rendering behavior
- malformed eyes, mismatched pupils, duplicated facial parts, warped face, deformed nose/mouth/jaw/chin, distorted neck, broken shoulders/collarbones, collapsed chest/torso, impossible waist/hip transition, malformed arms/elbows/wrists, malformed legs/knees/ankles/feet, missing/extra limbs, impossible joints, collapsed proportions, or broken body silhouette
- malformed hands, missing fingers, four-finger hands without natural occlusion, extra fingers, fused fingers, webbed fingers, melted palms, duplicate nails, broken knuckles, warped wrists, or white/stringy hand artifacts
- cuff embroidery, lace, glass-thread motifs, jewelry, hair, clothing edges, rain streaks, magic effects, background lines, or white highlights spilling onto or reading as eyes, face parts, fingers, limbs, joints, webbing, or stray anatomy
- different face ratio, rounder anime face, chibi face, doll face, photoreal face, or shifted features
- copied source traits that were replaced by the character prompt
- character-sheet inventory pressure
- correcting excessive detail by converting the whole art style, flattening the rendering, or raising/lowering realism
- dense strand-by-strand hair, excessive flyaways, glossy string hair, many extra fine hair lines, or more regular/perfect hair clumps than the source
- many separated hair locks, parallel hair separators, wispy hair fields, over-drawn bangs, or hair that reads as individual strings instead of broad source-matched masses
- noisy hair fill in any hair color, speckled color static, salt-and-pepper hair texture, dithered hair texture, peppered value flecks, many tiny alternating color strokes, airbrushed micro-streaks, glittery highlight crumbs, crunchy compression-like hair texture, over-sharpened hair texture, or AI-looking color shimmer
- sticker-like facial marks, crisp emblem marks, floating face symbols, high-contrast under-eye icons, glowing runes, mismatched tattoo linework, or face marks that do not follow the source face rendering
- raised, embossed, cast-shadowed, sticker-outlined, painted-on, metallic, glowing, or separate-material face marks unless the prompt explicitly requests that physical treatment
- complex new outfit detail outside the visible crop
- extra accessories beyond the source budget
- full scenic background when the source is simple or blurred
- source-only decor locked as if it were character identity; unnecessary flowers/leaves/props preserved when the character prompt asks for a different environment
- global glow, aura, bloom haze, sparkle fields, neon rim light, glowy skin fog, or plastic mobile-game polish
- cleaner, smoother, glossier, more symmetrical, more detailed, or more AI-polished finish than the source
- mismatched line color, heavier outlines, vector-clean curves, or missing broken/lost contours
- unsafe mobile framing, face too high, face too low, focal point under a likely app header, cropped eyes, cropped facial mark, or important accessories hidden by header-safe UI

## Example Translation

User intent:

```text
Use this manhwa girl image. My character has violet eyes, silver-lavender hair, a moon hair clip, a tiny stellar mark under the eye, a star choker, cream cardigan, blue dress, and a balcony tea background.
```

Patch map:

```text
Framing mode:
- Mobile portrait mode: force 9:16 and keep face/focal center in app-safe upper-middle band.

Replace:
- brown/black hair -> silver-lavender hair using the same source hair construction
- gray eyes -> violet-blue eyes using the same source iris/catchlight method
- source outfit -> cream cardigan edge plus midnight-blue neckline
- add tiny stellar mark below left eye
- add one moon hair clip or small star choker if crop allows

Compress:
- source flowers/leaves -> replaceable decor; remove unless the character prompt requests flowers
- balcony tea background -> one faint balcony rail or tiny cup silhouette in the source background style
- star accessories -> one or two tiny cues only

Omit:
- full balcony scene, fairy lights, floating stars, pillows, tea setup, dense sleeve pattern, global glow

Preserve:
- source pose, face construction, expression, hand placement, crop, linework, dappled/specular light, background complexity, and polish ceiling
```

## QC Checklist

```text
Edit-target structure preserved: pass/fail
Basic image-defect gate passed: pass/fail
Visible anatomy/body-part plausibility passed: pass/fail
Pose/crop/camera preserved: pass/fail
Face proportion fingerprint preserved: pass/fail
Facial-feature construction preserved: pass/fail
Style family / rendering model preserved: pass/fail
Source form/material modeling preserved: pass/fail/not relevant
Expression/gaze preserved: pass/fail
Hand/crop logic preserved: pass/fail/not visible
Hand anatomy plausible: pass/fail/not visible
Five fingers or natural occlusion logic: pass/fail/not visible
No stray accessory/thread/web artifacts on hands: pass/fail/not visible
No obvious eye/face/neck/shoulder/torso/limb/hand/foot/text/watermark/artifact defects: pass/fail
Linework fingerprint preserved: pass/fail
Lighting preserved: pass/fail
Glow/specular profile preserved: pass/fail
Medium/rendering preserved: pass/fail
Polish ceiling preserved: pass/fail
Hair replacement correct: pass/fail
Hair mass/clump strategy preserved or simplified: pass/fail
No excessive strands/flyaways/string hair: pass/fail
Hair fill texture/noise source-matched and low-frequency: pass/fail
Eye replacement correct: pass/fail
Mark/species trait correct and style-integrated: pass/fail/not requested
Outfit cue patched without over-detail: pass/fail
Accessory cue patched within budget: pass/fail
Background content patched within source complexity: pass/fail
Character-sheet pressure controlled: pass/fail
No full-redraw drift: pass/fail
9:16 mobile portrait when requested: pass/fail/not requested
App-safe face/focal placement: pass/fail/not requested
Top header-safe zone clear of key facial features: pass/fail/not requested
No text/watermark/signature: pass/fail
```
