# Art Analysis Framework

Use this reference to produce professional, technical analysis of drawing, painting, and illustration style.

## Technical Style Card

Start with a compact card for ordinary critique or study notes. When the output will feed image generation, style transfer, or another skill, expand this into a full card and follow it with the Generation Handoff Packet below.

```text
Detected style family:
Medium feel:
Medium classification/confidence:
Medium evidence:
Surface/material cues:
Linework:
Linework fingerprint:
Shape/proportion language:
Face proportion fingerprint:
Facial-feature construction:
Value structure:
Color system:
Color handling/local-color policy:
Rendering mode:
Edge hierarchy:
Material treatment:
Brush/layer behavior:
Eye rendering/coloring:
Hair construction:
Accessory/detail rendering:
Imperfection/polish profile:
Polish ceiling:
Glow/specular profile:
Glow budget:
Composition/focal path:
Detail-density budget:
Palette/background budget:
```

## Style Transfer Fingerprint

When the analysis will be used for image generation, add this compact fingerprint after the style card:

```text
Always-on style anchors to preserve:
- <linework fingerprint, value range, rendering mode, edge behavior, lighting, background style, detail density>

Content-specific reference traits not to copy:
- <identity, exact outfit, exact hair/eye colors, exact props/background content>

Allowed character replacements:
- <hair/eye/skin/outfit/local colors translated into the reference style>

Trait translation matrix:
- Character-controlled traits: <identity, hair color, eye color, skin tone, outfit, accessories, species traits, visible marks, explicit makeup>
- Reference-controlled construction: <pose, expression, crop, face proportion fingerprint, facial-feature construction, linework, shading method, hair construction, strand density, edge quality, glow/specular profile, polish level, medium/material behavior, background style>
- Compatibility rule: <preserve character traits while drawing them with the reference technique>

Visual budget:
- Line density:
- Contour authority:
- Detail density:
- Palette handling:
- Background complexity:
- Accessory/detail budget:
- Accessory/detail rendering strategy:
- Hair coloring/construction strategy:
- Strand density:
- Material/rendering complexity:
- Imperfection/polish ceiling:
- Glow/specular budget:

Drift risks:
- <what will most likely push the output away from the reference style>

Conditional risk flags:
- Eye visibility / occlusion risk:
- Face-mark integration risk:
- Hand/crop/anatomy risk:
- Pale/noisy or long-hair risk:
- Glow/magic pressure:
- Accessory/prop/background pressure:
- Palette/chroma pressure:
- Anatomy-like artifact risk:
```

Use this to prevent broad labels like "anime" or "polished" from overpowering the actual visual construction. A good transfer note says what to always preserve, what to reduce or omit, and which guards are conditional rather than automatically pasted into every first prompt.

## Generation Handoff Packet

When another skill will consume the analysis, especially `generate-character-from-reference`, the output must include a detailed generation handoff packet. This packet should be reusable as-is by the prompt compiler. It should not require the downstream skill to re-analyze the image or guess missing constraints from broad style labels.

Use this structure:

```text
Generation Handoff Packet
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
- Lash grouping:
- Sclera/eyelid tint:
- Hair rendering:
- Hair coloring:
- Hair coloring/construction strategy:
- Hair construction:
- Strand density:
- Skin rendering:
- Makeup/cosmetics:
- Clothing/material rendering:
- Accessory/detail rendering:
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
- Imperfection/polish profile:
- Polish ceiling:
- Glow budget:
- Finish/polish:

Always-on style anchors:
- Linework anchor:
- Face proportion / facial-feature construction anchor:
- Eye rendering/coloring method anchor:
- Hair coloring/construction anchor:
- Medium/material anchor:
- Lighting/value anchor:
- Glow/specular anchor:
- Background-style anchor:
- Detail-density anchor:
- Accessory/detail rendering anchor:
- Palette anchor:
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
- Identity:
- Hair/eye/outfit/accessories:
- Props/background/watermark/signature:

Visual budget and compression guidance:
- Safe character detail count:
- Outfit detail allowance:
- Accessory allowance:
- Background content allowance:
- Magic/glow/sparkle allowance:
- Specular/dappled-light allowance:
- What to hide, crop, or reduce:

Likely drift risks:
- <specific risks such as black outlines, dense hair strands, over-glossy skin, saturated palette, ornate accessories, full scenic background, cinematic lighting, fake paper texture, or over-clean AI polish>
```

The handoff packet must be concrete. For example, say "very thin warm gray-brown low-opacity lineart with broken/lost contours around pale hair" instead of "soft linework"; say "long narrow face, high forehead, almond eyes one eye-width apart, small low mouth, narrow pointed chin" instead of "pretty face"; say "hard white dappled sunlight spots only, no aura or global bloom" instead of "glowy"; say "one or two tiny accessory cues maximum" instead of "simple accessories"; say "background should remain a faint wash with one soft cue" instead of "minimal background". Mark a risk as conditional when it should only add prompt text for specific cases, such as one-eye occlusion, face marks near eyes, flawed hands, pale hair recolors, or dense background pressure.

## Trait Translation Matrix For Generation

When the analysis will guide a new character image, keep character identity separate from reference construction.

```text
Character-controlled:
- Hair color, eye color, skin tone, outfit, accessories, species traits, visible marks, explicit makeup, and requested background content.

Reference-controlled:
- Pose, facial expression, face proportion fingerprint, facial-feature construction, camera/crop, gesture, hand logic, style family, visible medium/material behavior, line quality, shading method, hair construction, strand density, edge hierarchy, glow/specular profile, polish level, background style, and rendering complexity.

Compatibility rule:
- Keep the character's visible traits, but render them with the reference's drawing method. For example, a new hair color should keep that color, while the strand count, clump grouping, highlight shape, line looseness, and edge breaks should come from the reference.
```

Do not treat character local colors or accessories as style drift by themselves. They become drift only when their saturation, finish, detail density, construction, or polish level breaks the reference's visual grammar.

## Medium And Material Diagnosis

Always separate what the medium appears to be from what the style family is. Do not collapse everything into "anime", "digital", or "watercolor style".

Use this format when medium matters:

```text
Medium classification:
- <traditional / scanned hand drawing / digital painting / digital imitation of traditional media / mixed media / 3D / photo-real / uncertain>

Confidence:
- <high / medium / low>

Visible evidence:
- <paper grain, pigment blooms, pencil tooth, ink pooling, marker overlap, gouache opacity, digital gradients, layer-like highlights, vector-clean edges, 3D speculars, etc.>

Medium lock for generation:
- <what must be preserved if the image is used as a style reference>
```

Common medium categories:

- **Graphite/pencil drawing**: toothy gray marks, pressure variation, smudging, erased edges, visible sketch construction.
- **Ink drawing / manga ink**: black line authority, ink pooling at intersections, hatching, screentone or black/white value design.
- **Watercolor**: pigment blooms, granulation, uneven washes, backruns, soft bleeding edges, paper white used as highlight.
- **Gouache**: matte opaque color, chunky flat shapes, dry-brush edges, visible paint body but less gloss than oil/acrylic.
- **Marker / alcohol marker**: translucent overlap bands, smooth but slightly streaked fills, limited blending, paper bleed.
- **Colored pencil / pastel**: grainy tooth, layered strokes, soft powdery transitions, visible hand pressure.
- **Oil/acrylic-like paint**: thick paint body, brush ridges, impasto or blocky strokes, modeled form through value/color.
- **Scanned hand drawing**: physical paper texture, uneven line darkness, scan noise, slight paper tint, analog imperfections.
- **Digital line art / cel shading**: crisp pressure-sensitive lineart, clean flats, clipped shadow layers, controlled edge softness.
- **Digital painting**: smooth gradients, airbrush glazing, layer-mode-like highlights, clean undo-polished edges, no physical pigment behavior.
- **Digital watercolor imitation**: watercolor-like blooms or paper overlay, but too uniform/repeatable or combined with digital-sharp details.
- **3D render**: physically consistent lighting, smooth geometry, material shaders, camera/lens behavior, specular reflections.

When uncertain, say "reads as" or "medium feel" rather than overclaiming. For generation prompts, use visible behavior instead of provenance claims:

- Prefer: "watercolor-like pigment blooms on textured paper, uneven wash edges."
- Avoid: "real watercolor" when the image may be digital imitation.
- Prefer: "scanned pencil-and-ink feel with paper grain and uneven line density."
- Avoid: "hand drawn" without visible evidence.

## Imperfection And Polish Profile

A style match is not only about features and colors; it is also about how finished or imperfect the drawing feels. Always identify whether the reference has a rough, handmade, scanned, loose, clean, glossy, or highly polished finish.

Look for:

- **Line irregularity**: wobble, pressure jumps, uneven contour, scratchy marks, visible corrections, broken line segments.
- **Fill irregularity**: uneven opacity, patchy flats, imperfect gradients, marker overlap, pigment blooms, paper tooth, dry-brush edges.
- **Edge imperfection**: lost edges, unclosed contours, slightly misregistered color, soft bleed, rough highlight borders.
- **Digital polish**: ultra-clean curves, perfectly smooth gradients, uniform glow, excessive strand regularity, plastic skin, hyper-sharp accessories.
- **Polish ceiling**: the maximum cleanliness and detail precision the generated image should have before it starts looking like a different style.

For generation notes, write both what to preserve and what to avoid:

```text
Imperfection/polish lock:
- Preserve <specific natural roughness or clean finish>.
- Do not exceed this polish level with <over-smooth skin, too many hair strands, glossy perfect gradients, hyper-detailed jewelry, etc.>.
```

## Linework Fingerprint

Look for:

- **Tapered lineart**: pressure-sensitive strokes that thin at the ends.
- **Line weight hierarchy**: thicker silhouette/occlusion lines, thinner interior details.
- **Line thickness range**: hairline-thin, medium manga contour, heavy ink, variable brush, or almost outline-free.
- **Line opacity**: opaque black, translucent gray, tinted brown/mauve, locally colored, or low-opacity sketch line.
- **Colored lineart / line tinting**: line color shifts to brown, mauve, blue, or local color instead of black.
- **Broken contour**: interrupted outlines that let light or background dissolve the edge.
- **Lost-and-found line**: line disappears in bright or low-contrast areas, reappears near focal points.
- **Contour authority**: firm graphic outline, soft tentative contour, sketchy repeated contour, or barely-there edge suggestion.
- **Line density**: sparse selective lines, moderate descriptive lines, dense strand/detail lines, or heavy hatch texture.
- **Pressure rhythm**: smooth digital taper, wobbling handmade taper, scratchy repeated strokes, or blunt uniform vector line.
- **Line-to-fill relationship**: line sits on top clearly, blends into local color, is partially covered by paint, or only appears at occlusion points.
- **Hatching / blush hatching**: parallel strokes used for value, blush, texture, or emotional heat.
- **Cross-contour lines**: lines that wrap around form to show volume.
- **Sketch retention**: rough underdrawing energy intentionally left visible.
- **Ink pooling**: thicker dark deposits at corners, intersections, lashes, mouth gaps, folds, or hair clumps.

Describe where the line is sharpest and where it relaxes. The sharpest lines usually reveal the focal point.

When a reference will guide image generation, write a linework lock:

```text
Linework fingerprint lock:
- Line color/tint:
- Thickness range:
- Opacity:
- Taper/pressure rhythm:
- Broken/lost contour behavior:
- Line density:
- Contour authority:
- Line-to-fill relationship:
- Focal line hierarchy:
- Avoid:
```

For example: "very thin warm gray-brown lineart, low to medium opacity, loose handmade taper, broken contours around pale hair and sleeve, sparse selective interior lines, soft contour authority, lines often dissolve into pale fills; avoid crisp black manga outlines and uniform clean vector curves."

## Shape And Anatomy Language

Identify the stylization logic:

- **Graphic simplification**: anatomy reduced into clean readable shapes.
- **Semi-real stylization**: realistic form cues with anime/manga feature proportions.
- **Feature economy**: nose, mouth, ear, and facial planes minimized.
- **Silhouette design**: outer contour readability and pose clarity.
- **Gesture line**: implied flow through head, spine, shoulders, hand, hair, or fabric.
- **Proportion language**: elongated limbs, large eyes, small mouth, fashion proportions, chibi compression, heroic scale.

Avoid only saying "anatomy is good". Say what is simplified, what is emphasized, and what is omitted.

## Face Proportion Fingerprint

When a reference will guide generation, analyze the face as a construction system, not only as a beauty type.

Record:

- Head shape: oval, heart, round, long, angular, V-line, soft square, or stylized hybrid.
- Face ratio: face length versus width, forehead height, cheek fullness, jaw taper, chin length/point.
- Feature placement: vertical spacing from hairline to brow, brow to nose, nose to mouth, mouth to chin.
- Eye system: eye size relative to face width, eye spacing, eye tilt, upper/lower lid shape, brow distance, eyelid fold height.
- Nose system: bridge length, nose tip shape, nostril marking, side-plane simplification, and whether the nose is line-driven or value-driven.
- Mouth system: width, vertical placement, lip fullness, corner treatment, mouth gap value, and edge softness.
- Facial asymmetry and camera distortion: head tilt, three-quarter turn, cheek compression, jaw angle, and perspective effects.
- Style risk: what happens if the generator makes the face rounder, younger, more chibi, more generic anime, more photoreal, or more doll-like.

For generation, write a face proportion lock:

```text
Face proportion lock:
- Head/face shape:
- Face length/width:
- Eye size/spacing/tilt:
- Brow/nose/mouth placement:
- Jaw/chin/cheek construction:
- Feature simplification:
- Avoid:
```

Do not let character identity erase the reference's facial construction. The new character's face traits should be translated through the reference's head ratio, eye placement, nose/mouth simplification, and jaw/chin language unless the user explicitly provides a separate face or identity reference that overrides it.

## Value And Lighting

Use value terms precisely:

- **High-key value range**: mostly light values, few dark accents.
- **Low-key value range**: mostly dark values, limited bright accents.
- **Grouped shadows**: shadow masses simplified into connected shapes.
- **Ambient occlusion**: darker contact shadows in creases, under chin, eyelids, fingers, folds.
- **Core shadow**: soft transition defining round form.
- **Cast shadow**: object shadow falling onto another form.
- **Rim light**: bright edge light separating silhouette.
- **Specular highlight**: sharp bright reflection on glossy surfaces.
- **Diffuse highlight**: broad soft light on matte surfaces.

Explain the hierarchy: where the darkest darks and brightest lights are placed, and how they steer the eye.

## Glow, Bloom, And Specular Control

Separate these effects carefully:

- **Specular highlight**: hard or soft bright reflection on glossy skin, lips, eyes, hair, jewelry, or wet surfaces.
- **Dappled light**: leaf/window-shaped light patches cast onto the subject, often with irregular edges and directional logic.
- **Rim light**: edge separation along the silhouette.
- **Bloom/glow**: light bleeding outward into surrounding pixels or atmosphere.
- **Magic/aura**: subject-generated light, sparkles, floating particles, or supernatural illumination.
- **Bokeh**: out-of-focus background or foreground light shapes, not the same as character glow.

For generation notes, set a glow/specular lock:

```text
Glow/specular lock:
- Preserve:
- Allow:
- Forbid:
- Maximum sparkle/magic count:
```

If the reference has glossy highlights or dappled light but no aura, say so explicitly. For example: "Preserve hard white skin highlight patches and leaf-like dappled light; forbid global bloom, magical aura, floating sparkle fields, neon rim light, and glowy skin haze."

## Color Analysis

Separate:

- **Local color**: the object's inherent color.
- **Light color**: hue of highlights.
- **Shadow color**: hue of shaded planes.
- **Undertone**: subtle skin, fabric, or atmosphere hue below surface color.
- **Temperature contrast**: warm skin vs cool shadow, warm light vs cool background.
- **Saturation control**: focal areas often have higher chroma than supporting areas.
- **Limited palette**: a controlled range of hues repeated across the image.
- **Selective color**: mostly monochrome or neutral image with a few colored accents.

For character generation, separate color identity from color treatment:

- **Character color identity**: the requested hair, eye, skin, outfit, accessory, or mark color.
- **Reference color treatment**: how that color is handled through value, chroma, temperature, opacity, blending, and lighting.
- If the character says lavender hair and the reference uses sparse, mass-first hair, keep lavender as the local color but draw it with the reference's strand density, highlight shapes, edge looseness, and polish level.
- If the reference is monochrome or very low-color, translate character colors into controlled value/tint behavior rather than saturated new palette blocks, unless the user explicitly asks for vivid color.

Useful color phrases:

- warm peach skin base
- rose/mauve shadow glaze
- cool blue-gray occlusion
- desaturated pastel palette
- high-chroma focal accent
- color dodge / additive highlight feel
- multiply-layer shadow feel

## Rendering Modes

Name the rendering system:

- **Hard cel shading**: flat colors with crisp shadow shapes.
- **Soft cel shading**: simplified shadows with softened edges.
- **Painterly blending**: brush strokes blend form gradually.
- **Airbrush glazing**: soft translucent color passes, common in blush/skin.
- **Marker wash**: flat but translucent color fields with visible overlaps.
- **Watercolor diffusion**: soft blooms, uneven pigment edges, paper texture.
- **Gouache-like opacity**: matte opaque color, chunky clean shapes.
- **Ink wash**: monochrome values built through diluted ink layers.
- **Impasto/oil feel**: thick visible strokes and paint body.
- **Vector-flat**: clean geometric fills, crisp edges, minimal texture.

For digital art, talk about visible layer behavior only when inferable:

- flats
- multiply shadows
- overlay/color-dodge highlights
- clipped layers
- lineart tinting
- overpaint pass
- texture overlay

Frame workflow guesses as "likely" or "the image reads as".

## Skin Rendering

Analyze:

- Base hue and undertone.
- Blush placement: cheeks, nose, eyelids, ears, fingers, joints, collarbone.
- Shadow hue: peach, mauve, gray, blue, brown.
- Transition type: soft gradient, cel edge, painterly stroke, stipple.
- Highlight type: matte diffuse or glossy specular.
- Subsurface cues: red/pink at thin skin, knuckles, nose, lips, eyelids.
- Occlusion cues: under chin, nostrils, lips, collarbone, fingers.

Professional phrasing:

- "soft airbrush skin glazing"
- "subsurface pinks around the nose and knuckles"
- "hard-edged specular accents over a soft blush base"
- "ambient occlusion in warm mauve rather than neutral gray"

## Eye Rendering

Break eyes into layers:

1. Sclera value and tint.
2. Iris base color.
3. Pupil and upper iris shadow.
4. Lower iris gradient or glow.
5. Catchlights and secondary sparkles.
6. Lash clustering and lash silhouette.
7. Eyelid/tear duct redness.
8. Lower lid texture, tear beads, glitter, or makeup.

Also record the eye coloring strategy:

- Iris color structure: flat fill, radial gradient, vertical gradient, ringed iris, layered flecks, painterly strokes, or glassy depth.
- Value grouping: dark upper iris shadow, pupil merge, lower-iris light pool, rim line, or soft diffuse iris.
- Highlight behavior: hard white specular dots, polygonal gems, wet streaks, soft bloom, or minimal/no catchlight.
- Line/color integration: black lash silhouette, colored lash line, soft eyelid line, red waterline, or makeup-tinted contour.
- Character generation rule: eye color follows the character, while iris layering, catchlight shape, lash grouping, sclera tint, eyelid redness, and gloss/matte finish follow the reference.

Useful terms:

- layered iris rendering
- glassy iris depth
- wet eye highlight pass
- lash clustering
- upper-lid occlusion shadow
- lower-lid rim light
- tear-gem highlights

## Lip Rendering

Analyze:

- Edge softness vs interior sharpness.
- Mouth gap value and hue.
- Gloss highlight shape.
- Volume shadow under lower lip.
- Saturation concentration.

Useful terms:

- wet lip rendering
- soft outer edge, hard specular interior
- cherry/mauve base with dark red occlusion
- small high-value specular ticks

## Hair Rendering

Identify the hair strategy:

- **Mass-first hair**: large shape groups before individual strands.
- **Strand-based rendering**: many fine lines define texture.
- **Negative-space hair**: light hair kept mostly white, defined by outline and shadow.
- **Ribbon hair**: clumps drawn as flat twisting ribbons.
- **Block highlight**: large graphic highlight shapes.
- **Flyaway strokes**: loose outer strands for softness.
- **Silhouette feathering**: outer edge broken by thin strands.

Also record:

- Strand density: sparse, moderate, dense, or hyper-dense.
- Clump scale: broad locks, medium ribbons, tiny strands, or loose scribble.
- Edge behavior: smooth silhouette, broken contour, feathered flyaways, lost edges.
- Highlight shape: block highlight, thin rim ticks, soft wash, glossy streaks, or paper-white gaps.
- Polish risk: whether adding more strands, smoother highlights, or perfect gradients would make the new image look unlike the reference.

Describe how shadows and highlights reveal volume. For pale hair, note whether the artist relies on lineart, soft shadow, or background contrast to preserve readability. For character generation, hair color can change with the character, but construction, strand density, highlight logic, and edge behavior should follow the reference.

## Accessory And Detail Rendering

Accessories should be analyzed by rendering method, not only by count.

Look for:

- Scale: tiny cue, focal object, repeated motif, or ornate cluster.
- Detail level: silhouette-only, simplified icon, line-plus-flat, or fully rendered material.
- Material behavior: metal shine, bead/glass sparkle, fabric ribbon, leather, gem, charm, or tech prop.
- Integration: cropped, partially hidden, blended into hair/clothing, or sharply separated.
- Style compatibility: whether the reference supports extra detail, or whether small accents should stay simplified.

For generation notes, say how character accessories should be translated. Example: "Allow character earrings as two tiny line-and-highlight cues, with the same loose contour and low-detail polish as the reference; do not render ornate gem facets if the reference has no comparable precision."

## Fabric And Material Rendering

For clothing and props, identify:

- Fabric weight: knit, silk, cotton, leather, sheer, denim, wool.
- Fold type: tension folds, compression folds, pipe folds, zigzag folds, drapery folds.
- Edge thickness: cuff, seam, hem, collar.
- Surface reflectivity: matte, satin, glossy, metallic.
- Texture rendering: actual texture vs implied texture.

Useful terms:

- simplified cloth shading
- broad fold grouping
- seam-line economy
- matte fabric with low specular response
- satin highlight banding
- translucent sleeve treatment
- knit texture suggested by line rhythm

## Edge Hierarchy

Always inspect edges:

- **Hard edges**: focal features, crisp shadow boundaries, glossy highlights.
- **Soft edges**: skin gradients, blush, atmospheric background.
- **Lost edges**: light hair into light background, white sleeve into pale backdrop.
- **Textured edges**: pencil, dry brush, paper grain, watercolor bloom.

Explain why it matters: edge control guides the eye more strongly than detail count.

## Composition And Crop

Analyze:

- Crop type: extreme close-up, bust, waist-up, three-quarter, full body.
- Camera angle: front, profile, three-quarter, top-down, low angle.
- Foreground/midground/background layering.
- Focal path: where the viewer looks first, second, third.
- Framing devices: hand, hair, sleeve, window, fabric, props.
- Negative space and value balance.
- Tangents or intentional cropping.

Professional phrasing:

- "foreground hand framing"
- "face-dominant crop"
- "focal triangle between eyes and mouth"
- "asymmetrical crop balanced by hair mass"
- "tight portrait framing compresses emotional distance"

## Style Family Signals

Use family labels only after visible evidence:

- **Manga/anime**: line-first construction, simplified nose/mouth, large expressive eyes, stylized hair clumps.
- **Manhwa/webtoon**: clean tapered line, polished gradients, fashion proportions, smooth digital shading.
- **Fashion illustration**: elongated silhouette, garment emphasis, selective rendering, confident pose economy.
- **Painterly realism**: form modeled by value/color rather than line, varied brush edges.
- **Ink illustration**: line weight and black/white value structure carry the image.
- **Watercolor/gouache**: pigment behavior, paper texture, blooms, matte opacity.
- **Concept art**: readable design shapes, material callouts, cinematic value grouping.

Do not claim a specific artist unless the user asks and there is sufficient evidence; prefer "in the direction of" or "reads as".

## Reconstruction Notes

When the user wants "cach ve" or prompt guidance, give a reproducible construction:

1. Start with pose/crop/gesture.
2. Block silhouette and large shape masses.
3. Add lineart and line-weight hierarchy.
4. Lay flat colors.
5. Group values and shadow shapes.
6. Render focal materials first: eyes, lips, face, hair, hands.
7. Control edges: sharp at focal points, soft elsewhere.
8. Add specular/highlight pass.
9. Add texture/noise/sparkle only if visible.
10. Final color balance and line tinting.

## Prompt Translation Template

Use this only when the user wants image-generation prompt language:

```text
Style/medium: <detected style family + visible medium feel>
Medium/material behavior: <traditional/digital/mixed/uncertain + visible evidence such as paper grain, pigment bloom, ink pooling, pencil tooth, digital gradients, layer-like highlights>
Linework: <line weight, taper, line color, contour behavior>
Value/lighting: <high/low key, shadow grouping, highlight type>
Color: <palette, undertones, saturation, temperature>
Rendering: <cel/soft/painterly/airbrush/etc>
Materials: <skin/hair/fabric/gloss/texture behavior>
Eye rendering/coloring: <iris layering, gradient/ring/fleck behavior, catchlight shape, lash grouping, sclera tint, eye-color treatment>
Hair construction: <mass/strand strategy, strand density, highlight shapes, edge behavior>
Accessory/detail rendering: <allowed detail scale, simplification method, material treatment>
Imperfection/polish: <line/fill roughness or clean finish + maximum polish level>
Composition: <crop, camera, framing, focal path>
Avoid: <style drift, unwanted lighting, unwanted material, unwanted crop>
```

## Common Weak Answers To Avoid

Avoid:

- "It is anime style with soft colors" without explaining line, value, and rendering.
- "High quality" as a substitute for brushwork or finish.
- Listing objects instead of visual construction.
- Over-attributing tools or software.
- Ignoring background and edge hierarchy.
- Ignoring how color and value create the focal point.

Replace with:

- "The image uses high-key values with dark accents reserved for pupils, lashes, and mouth occlusion."
- "The hair is negative-space rendered: large white masses are preserved and only selectively described by warm gray linework."
- "The skin uses airbrush glazing plus hard specular ticks, creating a wet/glass-skin effect."
