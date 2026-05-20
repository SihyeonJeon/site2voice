# site2voice Agent Prompt

Use `VOICE.md` as the source of truth for landing-page copy, headings, CTAs,
navigation labels, and UI microcopy.

Before shipping new copy, run a benchmark against the source:

```bash
site2voice bench https://www.shopify.com/ path/to/candidate.md --strict
```

Rules:

- Reuse the observed vocabulary, not full source paragraphs.
- Keep unsupported security, performance, customer, pricing, or AI claims out.
- Treat `voice.json` as machine-readable evidence, not as brand approval.
