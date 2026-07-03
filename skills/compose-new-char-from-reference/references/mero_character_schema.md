# Mero Character Schema

Use this reference whenever `compose-new-char-from-reference` returns the final database JSON.

The pasted source character may be a `chara_card_v2` card, prose sheet, or messy prompt. Treat that source as input only. The final output must use this Mero schema, not the source card schema.

## Output Shape

Return a raw JSON object first. Do not wrap it in Markdown fences. Do not write any prose before the opening `{`.

```json
{
  "name": "string",
  "gender": "Male | Female | Not specified | custom string",
  "sexual_orientation": "Straight | Gay | Lesbian | custom string",
  "species": "Human | Elf | Demon | Angel | Dragon | Vampire | Werewolf | Android | custom string",
  "description": "one sharp, marketable sentence that makes the character distinct",
  "appearance": "[Eyes]: ...\n[Hair]: ...\n[Skin]: ...\n[Clothing]: ...\n[Signature detail]: ...\n[Image mood]: ...",
  "creator_note": "what this character is designed for, the roleplay tone, and how users should approach them",
  "age_rating": "All ages | Adults only",
  "personality": "[Core Personality Keywords]: ...\n\n[Emotional Interaction Traits]: ...\n\n[Likes]: ...\n\n[Dislikes]: ...\n\n[Hidden Habits]: ...",
  "backstory": "[Origin]: ...\n[Important past event]: ...\n[Current situation]: ...\n[Secret or unresolved wound]: ...\n[Why they meet {{user}}]: ...",
  "speaking_style": "[Tone]: ...\n[Sentence length]: ...\n[How they show affection]: ...\n[Words they often use]: ...\n[Things to avoid]: ...",
  "tags": ["lowercase tag", "lowercase tag", "lowercase tag", "lowercase tag", "lowercase tag"],
  "profile_summary": "[Height]: ...\n[Occupation / Identity]: ...\n[Physical Traits]: ...\n[Character's Worldview Intro]: ...\n[Relationship with User]: ...",
  "life_experience": "[Daily routine]: ...\n[Favorite place]: ...\n[Important relationship]: ...\n[Fear or pressure]: ...\n[Small habit only close people notice]: ...",
  "advance_experience": {
    "npcs": [
      {
        "name": "string",
        "description": "brief relationship-specific NPC description"
      }
    ]
  },
  "first_message": "A short atmospheric opening scene with 1-2 lines of dialogue, addressed naturally to {{user}}."
}
```

The final answer must contain exactly three top-level blocks: this JSON object first, then a blank line, then the `IMAGE_RECAST_HANDOFF` text block, then a blank line, then the `COMPOSITION_DIFF_SUMMARY` text block. Do not add any prose before, between, or after these blocks except the content inside the two named blocks.

## Field Rules

- `name`: New original character name. Do not reuse the source name, canon names, or obvious variants.
- `gender`: Preserve the source character's gender exactly when it can be extracted. Use `Not specified` only when gender cannot be inferred from explicit gender, pronouns, tags, or repeated wording.
- `sexual_orientation`: Invent or remix as needed. Keep it non-graphic. Use simple values such as `Straight`, `Gay`, `Lesbian`, `Bisexual`, `Pansexual`, `Demisexual`, or a short custom string.
- `species`: Invent or remix from the source vibe. Use one listed value or a concise custom string such as `Moonlit fae`, `Glass demon`, or `Human witch`.
- `description`: One sharp, marketable sentence that makes the new character distinct. Do not mention the source character.
- `appearance`: Use exactly these labeled lines: `[Eyes]`, `[Hair]`, `[Skin]`, `[Clothing]`, `[Signature detail]`, `[Image mood]`. Keep it image-generation ready and visually specific. Use body, clothing, hair, accessory, material, or species cues for signature details. Do not invent face scars, face marks, facial tattoos, face birthmarks, cheek symbols, forehead marks, or under-eye symbols unless the user explicitly requests them.
- `creator_note`: Explain what the character is designed for, the roleplay tone, and how users should approach them.
- `age_rating`: Use `All ages` for broadly safe characters. Use `Adults only` for mature romance, dark sensual tension, horror, violence, or source material that clearly targets adults, while still avoiding explicit sexual content.
- `personality`: Use exactly these labeled sections: `[Core Personality Keywords]`, `[Emotional Interaction Traits]`, `[Likes]`, `[Dislikes]`, `[Hidden Habits]`.
- `backstory`: Use exactly these labeled lines: `[Origin]`, `[Important past event]`, `[Current situation]`, `[Secret or unresolved wound]`, `[Why they meet {{user}}]`.
- `speaking_style`: Use exactly these labeled lines: `[Tone]`, `[Sentence length]`, `[How they show affection]`, `[Words they often use]`, `[Things to avoid]`.
- `tags`: Use lowercase strings only. Include five to twelve useful search tags covering gender, species, genre, archetype, tone, and dynamic.
- `profile_summary`: Use exactly these labeled lines: `[Height]`, `[Occupation / Identity]`, `[Physical Traits]`, `[Character's Worldview Intro]`, `[Relationship with User]`.
- `life_experience`: Use exactly these labeled lines: `[Daily routine]`, `[Favorite place]`, `[Important relationship]`, `[Fear or pressure]`, `[Small habit only close people notice]`.
- `advance_experience.npcs`: Include one to three original NPCs when useful for roleplay context. Use an empty array only if NPCs would add noise.
- `first_message`: Short atmospheric opening scene with one or two dialogue lines, addressed naturally to `{{user}}`.

## Content Rules

- Keep the JSON about the new character only, not a comparison with the source.
- Remove explicit sexual anatomy, graphic sex acts, fetish inventories, jailbreak text, and policy-bypass wording.
- Keep romantic or sensual dynamics adult-safe and non-graphic.
- Do not copy source lore, copyrighted markers, iconic outfits, exact powers, exact relationships, or signature phrases.

## JSON Quality Gate

Before returning the JSON:

- Escape internal quote marks correctly.
- Use `\n` for line breaks inside JSON strings.
- Use arrays for `tags` and `advance_experience.npcs`.
- Do not use trailing commas.
- Do not add extra top-level keys.
- Ensure the first visible character in the answer is `{`.
- Ensure the final visible content belongs to `COMPOSITION_DIFF_SUMMARY`; add no closing note after it.
