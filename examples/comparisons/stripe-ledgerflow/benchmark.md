# Voice Benchmark

Reference: `https://stripe.com/`

## Reference Profile

- Tone: balanced, action-oriented
- Average sentence length: 15.7 words
- Lexicon: `stripe`, `read`, `payments`, `story`, `financial`, `business`, `how`, `commerce`, `products`, `crypto`, `billing`, `businesses`
- CTAs: `Sign in`, `Start now`, `Contact sales`, `Get started`, `Sign up with Google`, `Create a card issuing program`, `Watch now`, `Explore no-code`

## Scores

| Candidate | Result | Overall | Sentence | Lexicon | CTA | Tone | Heading | Claim safety | Copy safety |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `output-with-voice` | **FAIL** | 63.1 | 79.7 | 40.0 | 100.0 | 0.0 | 49.2 | 100.0 | 100.0 |
| `output-without-voice` | **FAIL** | 54.7 | 74.1 | 10.0 | 75.0 | 0.0 | 79.2 | 100.0 | 100.0 |

## Why This Is Useful

The score is deterministic. It checks measurable voice signals and gates against unsupported claims and copied spans.

## Candidate Evidence

- `output-with-voice` reused source lexicon: `payments`, `read`, `revenue`, `story`; longest shared run: 4 words.
- `output-without-voice` reused source lexicon: `payments`; longest shared run: 2 words.
