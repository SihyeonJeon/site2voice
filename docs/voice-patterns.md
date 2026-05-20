# Voice Patterns

`site2voice` does not try to copy a brand, magazine, or topic. It extracts
measurable writing signals that help an agent write new copy in a nearby
register without pasting source prose, importing source-specific nouns, or
implying affiliation with the reference source.

## Editorial / Magazine

What to measure:

- short section labels mixed with longer descriptive paragraphs;
- whether named entities, places, seasons, materials, products, and collaborators
  are content boundaries rather than reusable style;
- restrained adjectives before concrete nouns;
- headline length and whether titles read like indexes, blurbs, or news alerts;
- CTA words such as `read`, `explore`, `view`, `subscribe`, or `join`.

Good source families:

- EYESMAG-style Korean fashion and lifestyle indexing;
- Highsnobiety/Hypebeast-style culture and product trend coverage;
- Monocle/Wallpaper-style design, city, travel, and object language;
- Dazed/i-D-style youth culture and fashion framing.

Use synthetic fixtures for checked-in examples. Use live URLs only for local
analysis or public packs that remove paragraph samples and keep only derived
copy signals.

## Product / Developer Sites

What to measure:

- outcome-first headings;
- short conversion CTAs;
- whether technical nouns and integration terms should stay source-specific;
- proof language, customer claims, security claims, and performance claims;
- whether copy starts with user value or implementation detail.

Good source families:

- Stripe, Vercel, Linear, GitHub, and other public product pages.

These sources are useful contrast sets. They expose whether candidate copy is
accidentally drifting from editorial voice into SaaS launch-page voice.

## Agent Handoff

Give the agent the generated `VOICE.md`, then score the result:

```bash
site2voice https://example.com --out VOICE.md --max-snippets 0
site2voice bench https://example.com before.md after.md
```

The first command gives the agent a copy profile with an `Output Contract`:
sentence range, heading target, paragraph target, CTA verbs, content boundaries,
and benchmark gates. The second command verifies whether the resulting copy
moved closer to the reference profile while staying inside copy-safety and
claim-safety gates.
