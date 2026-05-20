# site2voice Agent Prompt

Use `VOICE.md` as the source of truth for landing-page copy, headings, CTAs,
navigation labels, and UI microcopy.

Before shipping new copy, run a benchmark against the source:

```bash
site2voice bench https://www.figma.com/ path/to/candidate.md --strict
```

Rules:

- Treat the `Output Contract` section in `VOICE.md` as the measurable
  pass/fail target.
- Reuse rhythm, CTA shape, and information order; bring your own product nouns.
- Do not transfer source-specific nouns from the reference site.
- Keep unsupported security, performance, customer, pricing, or AI claims out.
- Treat `voice.json` as machine-readable evidence, not as brand approval.
