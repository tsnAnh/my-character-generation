---
name: analyze-art-drawing
description: Professional art drawing and illustration analysis. Use when the user asks to analyze an artwork, reference image, character art, manga/anime/manhwa panel, concept art, sketch, painting, or generated image with focus on linework, drawing technique, face proportion fingerprint, facial-feature construction, hair construction, strand density, medium/material diagnosis, traditional hand-drawn vs digital art cues, rendering workflow, color handling, glow/specular profile, accessory/detail rendering, imperfection/polish profile, material feel, brushwork, visual style, art school/tradition, composition, style-transfer fidelity, and how to recreate or prompt the style in technical detail.
---

# Analyze Art Drawing

## Core Behavior

Analyze the image like a traditional paper artist, digital painter, art director, and style-reference prompt engineer. Focus on how the image is built, not only what it depicts.

Always describe concrete visible drawing behavior:

- Medium/material diagnosis: traditional hand drawing, pencil, ink, watercolor, gouache, marker, acrylic/oil-like paint, scanned paper, digital painting, digital watercolor imitation, cel-shaded digital, 3D render, photo/AI-rendered look, or mixed media. Give confidence and visible evidence.
- Linework: contour, taper, weight hierarchy, line color, opacity, broken/lost lines, line density, contour authority, hatching, cross-contour, sketch energy, and whether the line feels clean, rough, confident, hesitant, loose, or barely-there.
- Shape design: silhouette, proportion language, stylization, anatomy simplification, feature design.
- Face proportion fingerprint: head shape, face length/width, forehead-to-eye/nose/mouth/chin spacing, eye size/spacing/tilt, brow placement, nose and mouth construction, cheek volume, jaw/chin shape, and feature simplification.
- Value: high-key/low-key range, focal contrast, darkest accents, shadow grouping.
- Color: palette, hue temperature, saturation, local color, undertones, color harmony.
- Eye rendering: eye shape, iris layering, pupil treatment, sclera tint, lash grouping, eyelid redness, catchlight shape, tear/glitter accents, and eye-color handling.
- Rendering: cel shading, soft shading, painterly blend, glazing, airbrush, impasto, marker wash, watercolor-like diffusion.
- Edge control: hard/soft/lost edges, focal edge hierarchy, rim separation.
- Materials: skin, hair, fabric, metal, glass, paper grain, gloss, translucency, texture.
- Hair construction: mass-first versus strand-first drawing, strand density, clump grouping, edge breaks, flyaways, highlight shapes, and over-detail risks.
- Color handling: separate the object's local color from the reference palette treatment, value range, chroma discipline, undertones, and blending method.
- Accessory/detail rendering: how small details, jewelry, props, motifs, and clothing accents are simplified, cropped, grouped, or rendered.
- Imperfection/polish profile: line wobble, uneven opacity, loose or lost edges, imperfect fills, rough gradients, handmade artifacts, digital over-smoothing, and the maximum polish level the reference supports.
- Glow/specular profile: distinguish actual glow, bloom, aura, magic, sparkle fields, and bokeh from specular highlights, dappled light patches, glossy reflections, color-dodge-like accents, and rim light.
- Brush/media feel: pencil, ink, marker, gouache, watercolor, oil, acrylic, digital brush, layer mode behavior.
- Composition: crop, camera, gesture, framing, visual flow, focal path.
- Style lineage: anime, manga, manhwa, webtoon, fashion illustration, concept art, cel animation, painterly realism, watercolor, ink wash, etc.

Do not stop at vibe words such as "soft", "pretty", "clean", "high quality", or "anime style". Translate them into technical mechanisms.

When the analysis will feed another skill, image generation, style transfer, or character-from-reference workflow, produce a detailed reusable analysis packet. In that mode, the analysis is not a short user-facing critique; it is the source of truth for the downstream prompt compiler. Include concrete style anchors, conditional risk flags, budgets, and drift risks that the generator can reuse without re-inferring the style from the image or from generic labels. Do not turn every observation into first-prompt boilerplate; distinguish always-on art fidelity anchors from conditional guards that should appear only when the risk is active.

## Workflow

1. Identify the visible medium/material family and style family first. Separate true physical-media evidence from digital imitation or uncertain medium feel.
2. Build a technical style card before the prose analysis. If the analysis will feed generation, make this a full technical style card, not a compact summary.
3. Analyze the image by construction layers: sketch/line, flats, values, shadows, highlights, texture, final polish.
4. Name specific rendering techniques and explain where they appear.
5. If the analysis will feed image generation or style matching, separate style-transfer anchors from content-specific reference details. Include a trait translation matrix, linework fingerprint, face proportion fingerprint, facial-feature construction, hair construction, strand density, imperfection/polish profile, glow/specular profile, detail-density, palette, background, accessory/detail, and rendering-complexity budgets. Also include conditional risk flags and downstream compression recommendations: how much character outfit, accessory, magic/glow, prop, and background content the reference can safely support before style drift.
6. If the user wants prompt help, end with a compact style prompt block and negative constraints.
7. If the user asks whether the analysis is detailed enough, deepen the technique layer: brush behavior, edge hierarchy, value grouping, layer workflow, material rendering, and reconstruction steps.

## Output Shape

Use the user's language. For Vietnamese, write naturally in Vietnamese but keep professional art terms in English when they are standard.

Default structure:

```text
Style Family / Medium
Medium Diagnosis
Linework
Linework Fingerprint
Face Proportion Fingerprint
Value & Lighting
Color & Palette
Color Handling
Eye Rendering
Hair Construction
Rendering Technique
Material Treatment
Accessory Rendering
Edges & Texture
Imperfection / Polish Profile
Composition
Style Transfer Locks
Likely Workflow
Prompt/Replication Notes
```

Only include sections that help the task. Be specific enough that another artist could attempt a study from the analysis.

Generation handoff structure:

When another skill will consume the result, include this additional block after the main analysis. Fill every relevant line with concrete, observable language; do not leave broad labels such as "anime", "clean", or "detailed" standing alone.

```text
Generation Handoff Packet
Reference visual grammar:
- Detected style family:
- Medium/material classification and confidence:
- Medium evidence:
- Linework fingerprint:
- Face proportion fingerprint:
- Facial-feature construction:
- Face/skin rendering:
- Eye rendering/coloring method:
- Hair coloring/construction method:
- Clothing/material rendering:
- Lighting/value structure:
- Glow/specular profile:
- Color handling/local-color policy:
- Edge hierarchy:
- Background rendering style:
- Composition/crop/pose/hand logic:
- Detail-density budget:
- Palette/background budget:
- Accessory/detail budget:
- Imperfection/polish ceiling:
- Glow budget:

Always-on style anchors for downstream generation:
- Linework anchor:
- Face proportion / facial-feature construction anchor:
- Eye rendering method anchor:
- Hair construction / coloring method anchor:
- Medium/material anchor:
- Lighting/value anchor:
- Glow/specular anchor:
- Background-style anchor:
- Detail-density / palette anchor:
- Polish ceiling anchor:

Conditional risk flags:
- Eye visibility / occlusion risk:
- Face-mark integration risk:
- Hand/crop/anatomy risk:
- Pale/noisy or long-hair risk:
- Glow/magic pressure:
- Accessory/prop/background pressure:
- Palette/chroma pressure:
- Anatomy-like artifact risk:

Content-specific reference traits not to copy:
- Identity, exact outfit, exact hair/eye colors, accessories, props, watermark/signature, and background content:

Visual budget and compression guidance:
- Safe character detail count:
- Outfit detail allowance:
- Accessory allowance:
- Background content allowance:
- Magic/glow/sparkle allowance:
- Specular/dappled-light allowance:
- What to hide, crop, or reduce:

Likely drift risks:
- <specific ways a generated image will likely become too ornate, too polished, too colorful, too scenic, too line-heavy, or otherwise unlike the reference>
```

## Reference

For deeper terminology, checklists, and phrasing patterns, read [references/art-analysis-framework.md](references/art-analysis-framework.md) when:

- The user asks for "kỹ", "chi tiết", "professional", "chuyên ngành", "cách vẽ", "technique", "workflow", or "style prompt".
- The image has complex rendering, mixed media, stylized anime/manga/manhwa, fashion illustration, or painterly digital work.
- The output should help recreate the style in image generation prompts or artist study notes.

## Quality Bar

A good answer should:

- Mention visible evidence for each claim.
- Distinguish style label from technique.
- Distinguish local color from lighting color.
- Distinguish character-controlled local traits from reference-controlled drawing construction when analysis will support generation.
- Describe linework as a reproducible fingerprint: color/tint, opacity, thickness range, taper, pressure rhythm, broken/lost contour behavior, line density, and where lines disappear.
- Explain how line, value, edge, and color create the final look.
- Describe hair as a construction strategy, not only as color or length.
- State whether the image is rough, handmade, scanned, loose, clean, glossy, or over-polished, and what evidence supports that.
- Identify the strongest focal devices.
- Separate style invariants from reference identity/content that should not be copied.
- Call out likely style drift risks when the analysis will be used for image generation.
- Avoid inventing unseen software, brush names, layer modes, or artist names unless clearly framed as likely/inferred.
- Avoid copying the image into a generic image prompt without technical analysis.
