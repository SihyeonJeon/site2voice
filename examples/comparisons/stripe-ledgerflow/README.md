# Stripe Voice Pack Comparison

This comparison uses the same task prompt twice:

1. without `VOICE.md`;
2. with `packs/stripe/VOICE.md` and its `Output Contract` provided above the same prompt.

The benchmark uses `https://stripe.com/` as the reference copy profile.

## Files

- [prompt.md](prompt.md): shared task prompt.
- [request-without-voice.md](request-without-voice.md): exact no-context request.
- [request-with-voice.md](request-with-voice.md): same prompt with Stripe `VOICE.md` added as context.
- [output-without-voice.md](output-without-voice.md): candidate output without the pack.
- [output-with-voice.md](output-with-voice.md): candidate output with the pack.
- [benchmark.md](benchmark.md): Markdown benchmark report.
- [benchmark.json](benchmark.json): machine-readable benchmark report.

## Result

| Candidate | Overall | Variety | CTA | Copy safety |
| --- | ---: | ---: | ---: | ---: |
| Without `VOICE.md` | 60.4 | 40.5 | 50.0 | 100.0 |
| With `VOICE.md` | 91.0 | 45.8 | 100.0 | 96.2 |

The injected pack improved the score by **30.6 points**, removed source-term
reuse from the reward signal, and raised CTA fit from **50.0** to **100.0**.

The output with `VOICE.md` passed the default strict gate. The difference is the
contract: it turns the copy brief into measurable target ranges for sentence
length, heading shape, CTA verbs, content boundaries, copy safety, and claim
safety.

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
