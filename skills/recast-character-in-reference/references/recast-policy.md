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
Edit target locks:
- Pose/crop/camera:
- Face proportion fingerprint:
- Facial-feature construction:
- Expression/gaze:
- Hand/crop logic:
- Linework:
- Lighting:
- Glow/specular profile:
- Medium/rendering:
- Detail density:
- Background style:
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
- Background:
- Magic/glow:
- Props:

Omit:
- Lore/personality:
- Quality/style adjectives:
- Conflicting pose/camera/gaze prose:
- Full prop/background inventories:
```

The final edit prompt should use the map, not the raw character sheet.

## Replacement Rules

### Hair

Replace color, length, and major silhouette only if requested. Preserve the source hair construction:

- mass-first or strand-first strategy
- clump size
- strand density
- highlight shape
- line tint and opacity
- edge breaks and flyaways
- polish level

Avoid adding more hair detail than the source supports.

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

Background content follows the character/request, but style and complexity follow the source.

If the source background is simple, blurred, or low-detail:

- use one faint background cue
- keep it soft and low contrast
- avoid full scenery, prop clusters, text, signs, bokeh fields, and decorative filler

If the source background is detailed, preserve the same detail density and rendering method while swapping content.

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
Edit the attached image. Treat it as the structure lock and preserve its pose, crop, camera feeling, face proportion fingerprint, facial-feature construction, expression, gaze, hand placement, linework, lighting, rendering method, background style, detail density, and polish ceiling.

Make only these visible replacements:
- <hair replacement>
- <eye replacement>
- <skin/mark replacement>
- <outfit cue>
- <one or two accessory cues>
- <compressed background cue if requested>

Keep the source art method: <specific linework, eye rendering, hair construction, skin shading, lighting, glow/specular profile, and finish>.

Outfit/accessory budget: <concrete cap>.
Background budget: <concrete cap>.
Glow budget: <concrete cap>.

Do not redraw the image as a new character illustration. Do not change pose, facial construction, expression, hand placement, crop, linework, lighting, rendering style, or polish level.
```

## Anti-Redraw Negative Prompt

Avoid:

- full redraw from scratch
- new pose, new head angle, new hand placement, new crop, or new camera
- different face ratio, rounder anime face, chibi face, doll face, photoreal face, or shifted features
- copied source traits that were replaced by the character prompt
- character-sheet inventory pressure
- complex new outfit detail outside the visible crop
- extra accessories beyond the source budget
- full scenic background when the source is simple or blurred
- global glow, aura, bloom haze, sparkle fields, neon rim light, glowy skin fog, or plastic mobile-game polish
- cleaner, smoother, glossier, more symmetrical, more detailed, or more AI-polished finish than the source
- mismatched line color, heavier outlines, vector-clean curves, or missing broken/lost contours

## Example Translation

User intent:

```text
Use this manhwa girl image. My character has violet eyes, silver-lavender hair, a moon hair clip, a tiny stellar mark under the eye, a star choker, cream cardigan, blue dress, and a balcony tea background.
```

Patch map:

```text
Replace:
- brown/black hair -> silver-lavender hair using the same source hair construction
- gray eyes -> violet-blue eyes using the same source iris/catchlight method
- source outfit -> cream cardigan edge plus midnight-blue neckline
- add tiny stellar mark below left eye
- add one moon hair clip or small star choker if crop allows

Compress:
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
Pose/crop/camera preserved: pass/fail
Face proportion fingerprint preserved: pass/fail
Facial-feature construction preserved: pass/fail
Expression/gaze preserved: pass/fail
Hand/crop logic preserved: pass/fail/not visible
Linework fingerprint preserved: pass/fail
Lighting preserved: pass/fail
Glow/specular profile preserved: pass/fail
Medium/rendering preserved: pass/fail
Polish ceiling preserved: pass/fail
Hair replacement correct: pass/fail
Eye replacement correct: pass/fail
Mark/species trait correct: pass/fail/not requested
Outfit cue patched without over-detail: pass/fail
Accessory cue patched within budget: pass/fail
Background content patched within source complexity: pass/fail
Character-sheet pressure controlled: pass/fail
No full-redraw drift: pass/fail
No text/watermark/signature: pass/fail
```
