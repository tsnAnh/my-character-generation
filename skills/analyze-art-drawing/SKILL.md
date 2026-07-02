---
name: analyze-art-drawing
description: Professional art drawing and illustration analysis. Use when the user asks to analyze an artwork, reference image, character art, manga/anime/manhwa panel, concept art, sketch, painting, or generated image with focus on linework, drawing technique, hair construction, strand density, medium/material diagnosis, traditional hand-drawn vs digital art cues, rendering workflow, color handling, accessory/detail rendering, imperfection/polish profile, material feel, brushwork, visual style, art school/tradition, composition, style-transfer fidelity, and how to recreate or prompt the style in technical detail.
---

# Analyze Art Drawing

## Core Behavior

Analyze the image like a traditional paper artist, digital painter, art director, and style-reference prompt engineer. Focus on how the image is built, not only what it depicts.

Always describe concrete visible drawing behavior:

- Medium/material diagnosis: traditional hand drawing, pencil, ink, watercolor, gouache, marker, acrylic/oil-like paint, scanned paper, digital painting, digital watercolor imitation, cel-shaded digital, 3D render, photo/AI-rendered look, or mixed media. Give confidence and visible evidence.
- Linework: contour, taper, weight hierarchy, line color, opacity, broken/lost lines, line density, contour authority, hatching, cross-contour, sketch energy, and whether the line feels clean, rough, confident, hesitant, loose, or barely-there.
- Shape design: silhouette, proportion language, stylization, anatomy simplification, feature design.
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
- Brush/media feel: pencil, ink, marker, gouache, watercolor, oil, acrylic, digital brush, layer mode behavior.
- Composition: crop, camera, gesture, framing, visual flow, focal path.
- Style lineage: anime, manga, manhwa, webtoon, fashion illustration, concept art, cel animation, painterly realism, watercolor, ink wash, etc.

Do not stop at vibe words such as "soft", "pretty", "clean", "high quality", or "anime style". Translate them into technical mechanisms.

## Workflow

1. Identify the visible medium/material family and style family first. Separate true physical-media evidence from digital imitation or uncertain medium feel.
2. Build a technical style card before the prose analysis.
3. Analyze the image by construction layers: sketch/line, flats, values, shadows, highlights, texture, final polish.
4. Name specific rendering techniques and explain where they appear.
5. If the analysis will feed image generation or style matching, separate style-transfer locks from content-specific reference details. Include a trait translation matrix, linework fingerprint, hair construction, strand density, imperfection/polish profile, detail-density, palette, background, accessory/detail, and rendering-complexity budgets.
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
