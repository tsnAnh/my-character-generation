---
name: recast-character-in-reference
description: Recast or patch a supplied character reference image using a character prompt while preserving source pose, crop, face construction, expression, hand/crop logic, apparent scale, linework, lighting, rendering model, medium behavior, style-family balance, detail density, polish ceiling, hair construction, grain/noise behavior, and background style. Use when imagegen should edit a reference character by changing only local identity traits, colors, visible marks, outfit cues, accessories, and compressed background content instead of redrawing from scratch. Supports source-crop and Mobile portrait 9:16 modes with app-safe focal placement, canvas extension without poster redraw, targeted conditional guards for eye/hand/hair/background risks, strict art-fidelity QC, and hard basic-anatomy failure gates. Triggers include make this into my OC, change outfit, patch traits, keep art/pose/face but replace hair/eyes/clothes/accessories/background, mobile portrait, app avatar, 9:16, and avoid fantasy-glowy redraw drift.
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
- Output mode: source-crop mode or Mobile portrait mode.

## Workflow

1. Label the supplied image as `edit target / structure lock`.
2. If the image is only available as a local file and built-in imagegen will be used, inspect it first so it is visible in the conversation.
3. Use `analyze-art-drawing` when available to capture: style family/rendering model, realism/flatness/abstraction balance, face proportion fingerprint, facial-feature construction, subject form/material modeling, linework fingerprint, hair/eye rendering, lighting, glow/specular profile, background style, detail density, and polish ceiling.
4. Read [references/recast-policy.md](references/recast-policy.md) before writing a direct edit prompt or judging output.
5. Choose the framing mode:
   - Source-crop mode: preserve the source aspect and crop feeling unless the user asks otherwise.
   - Mobile portrait mode: force 9:16 output when the user asks for mobile, app, avatar, portrait, phone wallpaper, 9:16, or explicitly says Mobile portrait mode.
   - Mobile portrait mode is a canvas-extension task, not a poster redraw: preserve the apparent character scale, source crop logic, and visible body-region inventory; add or remove source-style background padding instead of zooming out, revealing a full costume, inventing a room, or adding a foreground prop stage.
6. Split the character prompt into a patch map:
   - Replace: hair color, eye color, skin tone, subtle visible marks, species traits, outfit color/silhouette cues, and a small number of accessories.
   - Preserve: pose, crop, camera, expression, face proportion fingerprint, facial-feature construction, hand placement/crop logic, linework, lighting, glow/specular behavior, medium/material behavior, rendering method, style-family/rendering-model balance, subject form/material modeling, detail density, background rendering style, polish ceiling, hair mass/clump construction, restrained source hair strand density, source-matched broad hair fill masses, and global grain/noise behavior.
   - Correct: malformed source anatomy and output anatomy defects across all visible body parts, including eyes, pupils, face, nose, mouth, neck, shoulders, chest/torso, arms, wrists, hands, fingers, hips, legs, feet, joints, body proportions, and accessory/background artifacts that read as stray anatomy, while keeping the original pose/placement/crop feeling.
   - Compress: background, source decorative motifs, outfit details, accessories, magic/glow, props, and lore-driven motifs. Compression reduces content inventory only; it must not change the source's style family, rendering model, form/material modeling, lighting, edge behavior, medium behavior, or polish ceiling. When the source background is void/simple, compress dense room and prop prompts into one or two barely readable cues and omit foreground props unless the source already has comparable foreground prop logic.
   - Omit: backstory, personality prose, relationship text, quality words, unsupported generic style labels, pose prose that conflicts with the source, and detail inventories that exceed the source image budget.
7. Classify prompt guidance into three layers before prompting:
   - Style anchors are always included: source pose/crop/camera, apparent scale, face construction, eye construction, hand/crop logic, linework, lighting, medium/rendering model, subject form/material modeling, hair construction, background style, detail density, and polish ceiling.
   - Conditional prompt guards are included only when the source, character prompt, or requested edit actually creates that risk: one-eye/covered-eye reads, malformed source eyes, face marks near eyes, hair/headwear crossing eyes, flawed visible hands, pale/noisy hair recolors, heavy accessories, dense scenery, glow/magic, app framing, or anatomy-like accessory/background marks.
   - Hard QC gates are always evaluated after generation: basic eye, face, hand, body, artifact, text/watermark, style-lock, and framing failures are never accepted just because the prompt was concise.
8. Before the first generation/edit prompt, build a first-pass failure-prevention ledger:
   - Identify predictable prompt-pressure risks from the source and character prompt: style/polish upgrade, over-ornamented costume, full scenic background, zoom-out/poster redraw, new foreground prop plane, glow/magic bloom, hair strand/noise drift, facial/eye occlusion, hands/cropped anatomy, app framing, text/watermark, and accessory/background marks that can read as anatomy.
   - For each active risk, write one short positive source-budget guard and one targeted negative constraint into the first prompt. Do not copy the full QC checklist or every possible anatomy/style failure into the first prompt.
   - Treat polish/detail drift as a first-prompt locking problem whenever it is foreseeable from words such as royal, luxurious, cinematic, fantasy, ornate, magic, detailed interior, architecture, prop inventory, long hair, silver/pastel hair, jewelry, lace, armor, or similar pressure. Lock the source polish ceiling before local character traits.
9. Build a strict edit contract before prompting:
   - Structure locks from the source image.
   - Style-family/rendering-model lock: name the source's visible style family, medium behavior, degree of realism/flatness/abstraction, and form/material modeling before any detail-reduction language. Do not add labels such as anime, webtoon, photoreal, concept art, cel-shaded, watercolor, sketch, 3D, or oil-paint unless the source visibly supports them.
   - Source-look priority: name concrete visible style evidence from the source instead of relying on generic "same style" wording.
   - Local trait replacements from the character prompt.
   - Hard caps for accessory count, background content, foreground props, glow/magic, outfit detail, and character scale/crop drift.
   - Hair fill budget: when hair color changes or the character prompt creates pale/saturated/long-hair risk, include this as a positive prompt guard, not only a negative constraint: recolor with source-matched broad fill/shadow masses and global/source-level grain only; do not concentrate high-frequency speckle, dither, micro-streaks, glitter flecks, or crunchy texture inside the hair.
   - Eye visibility budget: include explicit occlusion logic only when the source has one visible eye, unclear/malformed eyes, hair/headwear/marks crossing the eye area, or the edit/reframe exposes more face plane. Otherwise use the default compact lock: preserve source eye construction; only change eye color if requested.
   - App-safe focal placement when Mobile portrait mode is active.
   - Negative constraints against full redraw, new pose, new face construction, different style family, and fantasy-glowy polish, plus only the active conditional risks from the ledger.
10. For direct work, call image generation/editing once by default, then inspect the actual produced bitmap before finalizing. If the built-in tool saves a file, open that saved output with `view_image` or an equivalent image viewer; do not infer QC from tool success, prompt intent, or a partial chat preview. If the output cannot be inspected, state that QC is unverified and do not call it pass. Run both a reference-lock check and a basic image-defect check. Style match alone is not enough: malformed anatomy anywhere on visible body parts, broken eyes or pupils, missing second eye when the face plane/crop implies it should exist, one-eyed/cyclops read, warped face/nose/mouth, distorted neck/shoulders/chest/torso, broken arms/wrists/hands/fingers, broken hips/legs/feet, extra/missing limbs, impossible joints, collapsed body proportions, accidental text/watermarks, severe artifacts, accessory/background lines that read as anatomy, scale/crop drift, poster-like redraw, or scenic background replacement are hard failures and must trigger a reroll or one targeted correction even when the source style was partly preserved.
11. Choose correction/reroll priority by severity, not by aesthetic preference:
   - First handle central basic image defects: missing/blank/covered eyes, one-eyed read, broken pupils, face, nose, mouth, neck/shoulders/torso, limbs, hands/fingers, body proportions, anatomy-like artifacts, text/watermarks, and unsafe app framing.
   - Then handle identity/structure locks: wrong pose/crop, wrong face construction, wrong expression/gaze, wrong hair/eye/skin/outfit trait, or missing required mark/accessory.
   - Then handle locked-axis style/detail issues: hair noise, ornate costume/accessory inventory, background clutter, glow/polish drift, or medium/style-family drift.
   - Do not spend the only correction pass on broad polish/detail cleanup while a central eye, face, hand, body, placement, or artifact defect remains. If both a central basic defect and severe global style conversion exist, reroll with strengthened first-pass locks instead of using a local style cleanup.
12. If Mobile portrait mode output is badly placed, perform one targeted framing correction that keeps all style and character patches unchanged while extending/reframing the canvas. Use any remaining reroll for the highest-severity failure that can be isolated. When a predictable style/detail failure occurred because the first prompt did not lock it, update the next prompt/policy guard rather than treating it as an ordinary aesthetic correction.
13. For prompt-only work, return the framing mode, patch map, conditional guards used, final edit prompt, targeted negative prompt, and QC checklist.

## Non-Negotiable Rules

- The image is an edit target. Do not treat it as loose inspiration.
- Preserve the source pose, expression, face proportion fingerprint, facial-feature construction, hand/crop logic, apparent character scale, visible body-region inventory, camera feeling, linework, lighting, rendering method, style-family/rendering-model balance, background style, and polish ceiling.
- Preserve the source's visible art method with concrete terms: line weight, line tint, broken/lost contours, brush or fill texture, shadow block shape, highlight shape, edge roughness, grain/noise, and imperfect hand-finished polish.
- Preserve the source's style-family/rendering-model balance across all art types. Match whatever the source visibly uses: realistic-painterly form modeling, flat cel simplification, webtoon/manhwa gradients, watercolor/ink/gouache/pencil texture, oil/acrylic-like paint body, 3D material shading, photoreal camera/skin behavior, collage, pixel/sprite constraints, or any other visible medium. If the source is semi-realistic, keep its realistic planes and material volume; if it is flat anime/cel-shaded, keep its flatness; if it is sketch, watercolor, ink, gouache, 3D, or photoreal, preserve that rendering model instead of upgrading, simplifying, or converting it.
- Replace only visible local traits named by the character prompt.
- Character local colors are allowed, but must be translated through the source image's value range, chroma handling, line tint, and lighting.
- Background content can change only at the same complexity level as the source background. If the source background is simple, void, dark, or blurred, compress the new background into one or two faint cues and omit readable prop clusters, foreground still-life setups, detailed architecture, mirrors, windows, candles, tables, papers, cups, bottles, or floor reflections unless the source already has comparable foreground/background inventory.
- Treat source-only decorative motifs such as flowers, leaves, vines, paper stars, props, foreground blur, ornaments, signs, or scenery as background/decor content, not character structure locks. Preserve their rendering style, softness, complexity, and lighting relationship; replace, reduce, or omit their subject matter when the character prompt asks for different background content.
- Character magic/glow words must not create global glow unless the source image already has global glow. Convert magical traits into tiny local marks or small accessory highlights.
- Do not copy source identity traits that the character prompt replaces, such as the source hair color, eye color, outfit, accessories, species, or background content.
- Do not change the face construction unless the user supplies a separate face/identity reference or explicitly requests it.
- Do not make the result cleaner, smoother, glossier, more ornate, more detailed, more fantasy-polished, more realistic, flatter, more anime-like, more webtoon-like, more photoreal, more painterly, more 3D-like, or more AI-generated than the source.
- Lock foreseeable polish, detail, background, glow, hair-noise, and ornamentation drift in the first prompt. A later correction pass should not be used as the main defense against predictable prompt-pressure drift when a hard visual defect also needs attention.
- Basic image defects are not source-style fidelity. Do not accept malformed anatomy on any visible body part, broken eyes, warped facial features, distorted neck/shoulders/chest/torso, broken arms/wrists/hands/fingers, broken hips/legs/feet, impossible joints, collapsed proportions, accidental text/watermarks, severe artifacts, or anatomy-like accessory/background tangles just because the pose, palette, or art style matches the reference.
- A one-eyed read is a hard face defect unless the source has the same unmistakable one-eye occlusion/crop logic. If hair, shadow, headwear, face angle, or paint strokes hide the second eye, the hiding mechanism must be anatomically and compositionally clear. If enough face surface is visible for two eyes, the output must include two plausible eyes with aligned pupils in the source construction.
- Body-part anatomy errors are not style. Preserve the source's pose, crop, and roughness, but repair output defects in eyes, pupils, face, nose, mouth, neck, shoulders, collarbones, chest/torso, arms, wrists, hands, fingers, hips, legs, feet, joints, and visible body silhouette whenever those areas are visible.
- Hand placement is a structure lock; hand anatomy errors are not. If the source hand is malformed, ambiguous, or missing a finger, repair it in the source style while keeping the pose, placement, crop, lighting, and roughness. A visible hand should have five plausible fingers unless one is naturally hidden by angle, palm overlap, sleeve/cuff, object contact, or crop. Do not create four-finger hands, extra fingers, fused fingers, webbed fingers, melted palms, or white/stringy web-like artifacts around hands. Do not let cuff embroidery, glass-thread details, lace, jewelry, magic, rain, or background lines spill onto the fingers unless the user explicitly asks for that visible hand detail.
- Hair must read as masses first, strands second. Do not add strand-by-strand hair detail, dense flyaway fields, glossy string hair, many wispy separators, or extra fine hair-line noise beyond the source. If the source hair is mass-first, sparse, loose, sketchy, or ambiguous, use a few broad clumps with minimal internal lines and only rare source-matched edge strands. If the character prompt says broad clumps, minimal strands, soft chunks, or similar, prioritize that over any temptation to add more strand detail.
- Hair color fill must also match the source's texture scale. For every hair color, recolor hair with broad source-style shadow/highlight masses and calm low-frequency paint texture. Preserve source grain as a global image/medium trait only, not as hair-local noise; do not add random speckled color static, salt-and-pepper texture, noisy dither, many tiny value flecks, airbrushed micro-streaks, glittery highlight crumbs, crunchy compression-like texture, or over-sharpened AI hair noise. Apply this more strictly for pale, white, silver, pastel, or highly saturated hair colors because noise is more visible there.
- Face marks are allowed when requested or implied by the character description. If a face mark is used, make it subtle and integrated into the source face rendering: same line tint, edge roughness, shading softness, value range, and medium behavior. Unless the prompt explicitly says the mark is raised, embossed, painted, metallic, glowing, inked, or attached, treat it as flat pigment under/within the skin, flush with the face surface, with no raised edge, no cast shadow, and no sticker-like outline. Avoid sticker-like, emblem-like, glowing, crisp geometric, or mismatched tattoo marks.
- In Mobile portrait mode, final output must be 9:16. Preserve the source pose, apparent character scale, and crop feeling by extending or reducing background, not by stretching the character, zooming out, revealing a new full costume/body region, inventing a detailed scene, or turning a tight crop into a poster composition.
- In Mobile portrait mode, keep the face/focal center in an app-safe vertical band. The top header-safe zone should contain background or nonessential hair/background only; eyes, facial marks, mouth, and key accessories must not sit under a likely app header. Avoid placing the face too high, too low, or hard against any edge.

## Prompt Construction

Use this order:

1. Edit-target declaration: preserve the attached image's structure.
2. Framing mode: source-crop or Mobile portrait mode with 9:16 app-safe focal placement.
3. Always-on style anchors: pose, crop, apparent character scale, visible body-region inventory, expression, face construction, default eye construction, hand placement/crop logic, linework, medium, lighting, glow/specular profile, style-family/rendering-model balance, subject form/material modeling, detail density, hair mass/clump construction, restrained hair strand density, background style, and polish ceiling.
4. Style-family/rendering-model lock: one sentence naming the source's visible art family and degree of realism/flatness/abstraction without unsupported generic labels. For any source, state what must remain true: realistic-painterly modeling, flat cel simplification, webtoon gradient polish, watercolor/ink/gouache/sketch texture, 3D material shading, photoreal camera behavior, pixel-art constraints, etc.
5. Source-look lock: one sentence with concrete observed style evidence. For rough painterly ink references, include terms like rough expressive ink linework, blocky painterly shadows, broken/lost contours, grainy hand-finished texture, and imperfect sketchy polish ceiling when those cues are visible.
6. Conditional guard ledger: list only active first-pass risks and their short guards. Do not include the full hard QC checklist in the prompt.
7. Patch map: concise visible character replacements only; keep facial marks subtle and source-style-integrated, or convert them into accessory/clothing/species cues only if the crop/style cannot support a clean face mark.
8. Anatomy guard: include a compact body-wide anatomy guard only when visible anatomy is flawed, hand-adjacent details are requested, or accessories/background strokes may read as anatomy. Always keep this as QC even when omitted from the first prompt.
9. Eye visibility guard: include only when the source has one visible eye, unclear/malformed eyes, or the edit creates eye-occlusion risk. Default line for ordinary cases: preserve source eye construction, eyelid/pupil/catchlight logic, gaze, and only change eye color if requested.
10. Outfit/accessory compression: one or two visible cues when the crop allows. Compression must target costume/background inventory, not the source's style family, rendering model, form/material modeling, value structure, texture, or edge complexity.
11. Background/decor patch: same rendering style, softness, lighting, and complexity as the source; content may be replaced by the character/request, and source-only decorative motifs should not be preserved unless they match the character/request. For void/simple references, write "background as dark padding with one or two faint cues only; no foreground prop plane and no readable room inventory."
12. Glow/specular guard: local highlights only unless the source has global glow.
13. Targeted negative constraints: always include no full redraw, no new pose, no new face construction, no style-family/rendering-model drift, no medium shift, no polish upgrade, no raw character-sheet inventory, no text/watermark, and no unsafe mobile placement when applicable. Add eye, hand, hair-noise, anatomy-like artifact, glow, accessory, or background negatives only when the conditional guard ledger marks those risks active.

## Output

For direct generation, keep the user-facing response short after inspecting the actual output bitmap: generated image, concise QC result, and any major issue or reroll reason. Do not report pass/fail from memory or prompt intent. If the output was not inspected, say so plainly and mark QC unverified.

For prompt-only mode, return:

```text
Framing mode:
Source locks:
Patch map:
Conditional guards used:
Compressed character traits:
Final edit prompt:
Targeted negative prompt / anti-redraw:
QC checklist:
```

Do not paste the full character sheet into the final edit prompt. Condense it into visible patches and a short background cue.
