# Research

## What Exists

DESIGN.md-style repos and services give AI coding agents visual design context:
colors, typography, spacing, layout patterns, and component guidance.

Observed categories:

- DESIGN.md libraries for ready-made visual systems.
- URL-to-DESIGN.md generators for design tokens and visual patterns.
- Agent memory files such as `AGENTS.md`, `CLAUDE.md`, and `DESIGN.md`.

## Gap

Visual style is only half of what an agent needs. When generating landing pages,
docs, onboarding flows, and UI microcopy, the agent also needs:

- message hierarchy;
- CTA language;
- navigation label shape;
- sentence length;
- claim boundaries;
- source-specific terms to avoid transferring.

`site2voice` targets that gap with a deterministic, reference-only `VOICE.md`
copy profile generator.

## New Evidence Path

The project now includes `site2voice bench`, which measures whether candidate
copy follows a reference copy profile. This turns `VOICE.md` from a descriptive
artifact into a testable workflow:

```bash
site2voice SOURCE --out VOICE.md
site2voice bench SOURCE before.md after.md
```

The benchmark scores sentence shape, lexical variety, CTA shape, heading shape,
tone labels, claim boundaries, and copy safety.

## Product Bet

The README should be short:

```bash
site2voice https://example.com --out VOICE.md
```

The output should answer:

- What measurable writing pattern appears in the reference copy?
- What CTA verb shape does it use?
- Which source-specific terms should stay out of unrelated projects?
- What claims must the agent avoid inventing?

## Boundaries

- No LLM dependency.
- No screenshot or brand asset copying.
- Do not paste source paragraphs into public generated files.
- Do not publish source nouns, raw CTAs, or navigation labels as reusable style.
- Treat the output as a writing contract, not legal brand guidance.
- Do not imply official approval, affiliation, or permission to impersonate a
  reference source.

## References

- [DESIGN.md library](https://designmd.app/)
- [Better Stack guide to DESIGN.md](https://betterstack.com/community/guides/ai/design-md-ai/)
- [DESIGN.MD by Parallect coverage](https://chatgate.ai/post/design-md-by-parallect)
- [DesignMD URL-to-DESIGN.md generator](https://www.designmd.cc/)
