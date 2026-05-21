# Request With SITE.md + VOICE.md

This request used the same task prompt, with `packs/stripe/SITE.md` and
`packs/stripe/VOICE.md` provided as additional context above it.

Reproduce locally:

```bash
cat packs/stripe/SITE.md packs/stripe/VOICE.md \
  examples/comparisons/stripe-ledgerflow-web/prompt.md
```

The important control is that the task prompt is unchanged. Only the context
above the prompt changes.
