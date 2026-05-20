# Voice Benchmark

Reference: `examples/editorial-home.html`

## Reference Profile

- Tone: balanced, action-oriented
- Average sentence length: 16 words
- Lexical variety: 0.785 type-token ratio
- CTA verbs: `join`, `read`, `explore`, `open`

## Scores

| Candidate | Result | Overall | Sentence | Variety | CTA | Tone | Heading | Claim safety | Copy safety |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `after-copy` | **PASS** | 97.4 | 94.1 | 99.7 | 100.0 | 100.0 | 93.8 | 100.0 | 95.5 |
| `before-copy` | **FAIL** | 62.9 | 81.2 | 83.0 | 0.0 | 50.0 | 62.5 | 100.0 | 100.0 |

## Why This Is Useful

The score is deterministic. It checks measurable copy signals and gates against unsupported claims and copied spans.

## Candidate Evidence

- `after-copy` longest shared run: 5 words.
- `before-copy` longest shared run: 1 words.
