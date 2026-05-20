# site2voice Agent Prompt

Use `SITE.md` and `VOICE.md` together:

- `SITE.md`: page structure, section order, section jobs, and content boundaries.
- `VOICE.md`: sentence rhythm, CTA shape, paragraph rhythm, and benchmark gates.

Together they form a reference-only copy contract and page-structure contract.

Before shipping new copy, run a benchmark against the source:

```bash
site2voice bench https://discord.com/ path/to/candidate.md --strict
```

Rules:

- Treat the `Output Contract` section in `VOICE.md` as the measurable
  pass/fail target.
- Treat the `Page Blueprint` and `Section Recipes` sections in `SITE.md` as the
  page-structure target.
- Reuse rhythm, CTA shape, and information order; bring your own product nouns.
- Do not transfer source-specific nouns from the reference site.
- Keep unsupported security, performance, customer, pricing, or AI claims out.
- Do not imply brand affiliation, endorsement, or official guideline status.
- Treat `voice.json` and `site.json` as machine-readable evidence, not brand approval.
