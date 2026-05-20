# Voice Benchmark

Reference: `https://stripe.com/`

## Reference Profile

- Tone: balanced, action-oriented
- Average sentence length: 15.7 words
- Lexical variety: 0.301 type-token ratio
- CTA verbs: `sign`, `start`, `contact`, `get`, `create`, `watch`, `explore`, `see`

## Scores

| Candidate | Result | Overall | Sentence | Variety | CTA | Tone | Heading | Claim safety | Copy safety |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `output-with-voice` | **PASS** | 91.0 | 96.8 | 45.8 | 100.0 | 100.0 | 81.8 | 100.0 | 96.2 |
| `output-without-voice` | **FAIL** | 60.4 | 74.1 | 40.5 | 50.0 | 0.0 | 79.2 | 100.0 | 100.0 |

## Why This Is Useful

The score is deterministic. It checks measurable voice signals and gates against unsupported claims and copied spans.

## Candidate Evidence

- `output-with-voice` longest shared run: 6 words.
- `output-without-voice` longest shared run: 2 words.
