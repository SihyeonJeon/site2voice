# DESIGN.md vs SITE.md / VOICE.md

`DESIGN.md`, `SITE.md`, and `VOICE.md` are repo-local context files for AI
agents, but they solve different problems.

| File | Primary Job | Typical Signals | Output Risk |
| --- | --- | --- | --- |
| `DESIGN.md` | Visual identity and UI system | Colors, typography, spacing, components, layout, depth, responsive behavior | Visual imitation, trade dress, brand asset misuse |
| `SITE.md` | Page-structure contract | Page archetype, section order, section jobs, conversion pressure, content boundaries | Source business model, offer, audience, or claim leakage |
| `VOICE.md` | Copy behavior and writing contract | Sentence rhythm, heading shape, CTA shape, paragraph rhythm, claim boundaries | Source prose reuse, brand impersonation, unsupported claims |

`site2voice` does not implement the `DESIGN.md` visual spec. It does not extract
colors, fonts, component tokens, screenshots, logos, or layout systems. It
extracts structural and copy signals and writes compact Markdown contracts that
an agent can follow before generating landing-page sections, headings, CTAs,
docs, and UI microcopy.

## Context Stack

When all files are present, responsibilities must not overlap:

| Context | Owns | Override Rule |
| --- | --- | --- |
| Project brief | Product category, audience, facts, domain nouns, examples, offers, claims | Always overrides reference context for meaning and subject matter |
| `DESIGN.md` | Colors, typography, spacing, layout grid, components, motion, imagery style | Owns visual implementation |
| `SITE.md` | Page architecture, section order, section jobs, conversion path | Owns information architecture only |
| `VOICE.md` | Sentence rhythm, heading behavior, CTA shape, claim boundaries | Owns copy behavior only |

For example, using an athletic retail reference for an education product should
not introduce reference-category nouns, catalog logic, cultural context, or
campaign assumptions. `SITE.md` and `VOICE.md` should shape the page and copy;
the project brief supplies the subject.

## Why This Exists Separately

Visual context does not tell an agent how to structure or write a page. A page
can match a visual system and still sound generic, overclaimed, or off-market.
`site2voice` targets that missing layer:

- which section jobs should appear;
- how the first screen should move from outcome to action;
- how long sentences tend to be;
- how headings are shaped;
- whether CTAs are short and action-led;
- which claims must not be invented;
- whether candidate copy copied spans from the reference.

## How It Avoids Brand Cloning

Public `SITE.md` and `VOICE.md` profiles are intentionally constrained:

- no source paragraph samples;
- no source nouns or recommended vocabulary;
- no raw CTA labels;
- no navigation labels;
- no screenshots, logos, fonts, colors, or visual assets;
- explicit rules against transferring product names, domain nouns, and market
  claims;
- benchmark gates for copy safety and claim safety.

The reference site name identifies the measurement source only. It does not
mean the profile is official, endorsed, affiliated, or safe for impersonation.

## Format Difference

`DESIGN.md` commonly uses a machine-readable token layer plus a prose rationale
layer. Generated `SITE.md` and `VOICE.md` files are intentionally shorter and
agent-facing:

```text
SITE.md
  Site Summary
  Page Blueprint
  Section Recipes
  Rhetorical Pattern
  Agent Instructions
  Content Boundary
  Measurement

VOICE.md
  Voice Summary
  Scope
  Style Fingerprint
  Agent Rules
  Output Contract
  Evidence
  Do / Don't
```

For scripts and CI, `site2voice` also emits `voice.json` and supports:

```bash
site2voice bench SOURCE candidate.md --strict
```

That benchmark path is the main difference: the file is not only descriptive.
It gives the agent measurable gates and lets a project reject copy that is
off-profile, overclaimed, or too close to the source text. `SITE.md` carries the
human-readable structure contract; `VOICE.md` carries the measurable copy
contract.
