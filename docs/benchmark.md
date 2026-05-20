# Benchmark

`site2voice bench` checks whether candidate copy follows a source voice profile.
It is deterministic and uses only local text statistics.

```bash
site2voice bench examples/editorial-home.html \
  examples/before-copy.md \
  examples/after-copy.md \
  --out examples/editorial-benchmark.md
```

For CI, score the candidate you intend to ship:

```bash
site2voice bench examples/editorial-home.html examples/after-copy.md --strict
```

## Metrics

| Metric | What it checks |
| --- | --- |
| Sentence fit | Candidate average sentence length vs source average. |
| Lexicon fit | Whether candidate reuses source vocabulary without requiring exact prose. |
| CTA fit | Whether short action-led lines match observed CTA vocabulary. |
| Tone fit | Overlap between deterministic tone labels. |
| Heading fit | Whether heading length/shape is close to the source. |
| Claim safety | Penalizes unsupported security, performance, customer, pricing, and AI claims. |
| Copy safety | Penalizes long shared spans and high 5-gram overlap with source snippets. |

The reference profile also keeps a style fingerprint: average heading length,
average paragraph length, average CTA length, CTA verbs, lexical variety, and
punctuation counts.

Generated `VOICE.md` files convert those measurements into an `Output Contract`
so agents have target ranges before they write: sentence length, heading shape,
paragraph rhythm, CTA verbs, recommended terms, and pass gates.

## Gates

A candidate passes when:

- overall score is at least 75;
- copy safety is at least 85;
- claim safety is at least 75.

This matters because direct copying can look stylistically aligned while being
the wrong behavior. Copy safety is a gate, not just a metric.

Use custom gates when the default is too loose or too strict:

```bash
site2voice bench SOURCE candidate.md \
  --fail-under 80 \
  --min-copy-safety 90 \
  --min-claim-safety 90
```

## Example

| Candidate | Result | Overall | Sentence | Lexicon | CTA | Tone | Heading | Claim safety | Copy safety |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `after-copy` | PASS | 83.8 | 95.8 | 70.0 | 50.0 | 100.0 | 93.8 | 100.0 | 93.2 |
| `before-copy` | FAIL | 36.6 | 57.5 | 0.0 | 0.0 | 0.0 | 62.5 | 100.0 | 100.0 |

See [editorial-benchmark.md](../examples/editorial-benchmark.md).
