# Competitive Review

Snapshot date: 2026-05-20.

## Awesome DESIGN.md

Observed repository: `VoltAgent/awesome-design-md`.

At review time, the repository had roughly:

- 81.6k stars;
- 9.8k forks;
- 71 `design-md/*/DESIGN.md` files.

Sample file sizes checked from the public repository:

| Reference | Lines |
| --- | ---: |
| Stripe | 487 |
| Apple | 562 |
| Figma | 578 |
| Notion | 821 |
| Vercel | 736 |
| WIRED | 497 |

The files are substantially more detailed than `VOICE.md` profiles because they
encode a visual system. Typical sections include:

- YAML front matter with colors, typography, radius, spacing, and components;
- prose overview;
- color roles;
- typography hierarchy;
- layout rules;
- elevation and depth;
- component styling;
- responsive behavior;
- do/don't guardrails;
- iteration notes.

The repo also positions each site folder as a small design kit, not just a
single Markdown file. Many folders include preview files alongside `DESIGN.md`.

## Site2voice Position

`site2voice` should not compete by claiming visual-design parity. Its useful
position is narrower:

```text
public copy -> VOICE.md -> agent writes copy -> benchmark gate
```

This is a copy contract, not a visual identity file. The public profiles are
short because they intentionally omit source prose, source nouns, raw CTAs,
navigation labels, logos, screenshots, colors, fonts, and layout tokens.

## Differentiators To Keep

- Benchmark path: `site2voice bench SOURCE candidate.md --strict`.
- Copy safety: penalizes copied spans and high overlap.
- Claim safety: penalizes unsupported security, performance, customer, pricing,
  and AI claims.
- Content boundary: source nouns are not treated as reusable style.
- Reference-only positioning: no official guideline or impersonation framing.

## Messaging Guardrails

Use:

> Generate reference-only `VOICE.md` copy profiles from public website copy,
> then benchmark whether AI-written copy follows the measurable profile without
> copying spans, source nouns, or unsupported claims.

Avoid:

- "Clone a brand voice."
- "Write exactly like Stripe/Apple/OpenAI."
- "Official voice guideline."
- "DESIGN.md for words" without immediately explaining the boundary.
- Any claim that source names grant permission to use protected brand identity.
