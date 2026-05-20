# DESIGN.md vs VOICE.md

`DESIGN.md` and `VOICE.md` are both repo-local context files for AI agents, but
they solve different problems.

| File | Primary Job | Typical Signals | Output Risk |
| --- | --- | --- | --- |
| `DESIGN.md` | Visual identity and UI system | Colors, typography, spacing, components, layout, depth, responsive behavior | Visual imitation, trade dress, brand asset misuse |
| `VOICE.md` | Copy behavior and writing contract | Sentence rhythm, heading shape, CTA verb shape, paragraph rhythm, information order, claim boundaries | Source prose reuse, brand impersonation, unsupported claims |

`site2voice` does not implement the `DESIGN.md` visual spec. It does not extract
colors, fonts, component tokens, screenshots, logos, or layout systems. It
extracts measurable copy signals and writes a compact Markdown contract that an
agent can follow before generating headings, CTAs, docs, landing-page sections,
and UI microcopy.

## Why This Exists Separately

Visual context does not tell an agent how to write. A page can match a visual
system and still sound generic, overclaimed, or off-market. `site2voice` targets
that missing layer:

- how long sentences tend to be;
- how headings are shaped;
- whether CTAs are short and action-led;
- whether the first screen starts with outcome, proof, or detail;
- which claims must not be invented;
- whether candidate copy copied spans from the reference.

## How It Avoids Brand Cloning

Public `VOICE.md` profiles are intentionally constrained:

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
layer. A generated `VOICE.md` is intentionally shorter and agent-facing:

```text
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
off-profile, overclaimed, or too close to the source text.
