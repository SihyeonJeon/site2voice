# Voice Benchmark

Reference: `examples/editorial-home.html`

## Reference Profile

- Tone: explanatory
- Average sentence length: 21.4 words
- Lexical variety: 0.785 type-token ratio
- CTA verbs: `join`, `explore`

## Scores

| Candidate | Result | Overall | Sentence | Variety | CTA | Tone | Heading | Claim safety | Copy safety |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `after-copy` | **PASS** | 88.5 | 95.8 | 99.4 | 50.0 | 100.0 | 93.8 | 100.0 | 93.2 |
| `before-copy` | **FAIL** | 49.7 | 57.5 | 83.0 | 0.0 | 0.0 | 62.5 | 100.0 | 100.0 |

## Why This Is Useful

The score is deterministic. It checks measurable copy signals and gates against unsupported claims and copied spans.

## Candidate Evidence

- `after-copy` longest shared run: 5 words.
- `before-copy` longest shared run: 1 words.
