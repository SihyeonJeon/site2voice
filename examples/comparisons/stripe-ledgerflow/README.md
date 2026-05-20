# Stripe Voice Pack Comparison

This comparison uses the same task prompt twice:

1. without `VOICE.md`;
2. with `packs/stripe/VOICE.md` provided above the same prompt.

The outputs were generated with Claude CLI. The benchmark uses `https://stripe.com/`
as the reference voice.

## Files

- [prompt.md](prompt.md): shared task prompt.
- [request-without-voice.md](request-without-voice.md): exact no-context request.
- [request-with-voice.md](request-with-voice.md): same prompt with Stripe `VOICE.md` added as context.
- [output-without-voice.md](output-without-voice.md): generated result without the pack.
- [output-with-voice.md](output-with-voice.md): generated result with the pack.
- [benchmark.md](benchmark.md): Markdown benchmark report.
- [benchmark.json](benchmark.json): machine-readable benchmark report.

## Result

| Candidate | Overall | Lexicon | CTA | Copy safety |
| --- | ---: | ---: | ---: | ---: |
| Without `VOICE.md` | 54.7 | 10.0 | 75.0 | 100.0 |
| With `VOICE.md` | 63.1 | 40.0 | 100.0 | 100.0 |

The injected pack improved the score by **8.4 points**, raised lexicon overlap
from **10.0** to **40.0**, and raised CTA fit from **75.0** to **100.0**.

Neither output passed the default strict gate. That is useful signal: the pack
pushes the model toward the reference voice, but stronger output contracts are
still needed for fully automatic pass/fail copy generation.

## Reproduce

```bash
claude -p < examples/comparisons/stripe-ledgerflow/prompt.md \
  > examples/comparisons/stripe-ledgerflow/output-without-voice.md

cat packs/stripe/VOICE.md examples/comparisons/stripe-ledgerflow/prompt.md \
  | claude -p \
  > examples/comparisons/stripe-ledgerflow/output-with-voice.md

site2voice bench https://stripe.com/ \
  examples/comparisons/stripe-ledgerflow/output-without-voice.md \
  examples/comparisons/stripe-ledgerflow/output-with-voice.md \
  --out examples/comparisons/stripe-ledgerflow/benchmark.md
```

