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
- navigation vocabulary;
- sentence length;
- claim boundaries;
- words to reuse and words to avoid.

`site2voice` targets that gap with a deterministic `VOICE.md` generator.

## New Evidence Path

The project now includes `site2voice bench`, which measures whether candidate
copy follows a source voice profile. This turns `VOICE.md` from a descriptive
artifact into a testable workflow:

```bash
site2voice SOURCE --out VOICE.md
site2voice bench SOURCE before.md after.md
```

The benchmark scores sentence shape, vocabulary overlap, CTA shape, heading
shape, tone labels, claim boundaries, and copy safety.

## Product Bet

The README should be short:

```bash
site2voice https://example.com --out VOICE.md
```

The output should answer:

- What does this site sound like?
- What CTAs does it use?
- What vocabulary should an agent reuse?
- What claims must the agent avoid inventing?

## Boundaries

- No LLM dependency.
- No screenshot or brand asset copying.
- Do not paste long source paragraphs into the generated file.
- Treat the output as a writing/style brief, not legal brand guidance.

## References

- [DESIGN.md library](https://designmd.app/)
- [Better Stack guide to DESIGN.md](https://betterstack.com/community/guides/ai/design-md-ai/)
- [DESIGN.MD by Parallect coverage](https://chatgate.ai/post/design-md-by-parallect)
- [DesignMD URL-to-DESIGN.md generator](https://www.designmd.cc/)
