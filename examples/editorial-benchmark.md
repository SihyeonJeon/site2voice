# Voice Benchmark

Reference: `examples/editorial-home.html`

## Reference Profile

- Tone: explanatory
- Average sentence length: 21.4 words
- Lexicon: `city`, `archive`, `design`, `style`, `join`, `list`, `quiet`, `return`, `studio`, `object`, `current`, `index`
- CTAs: `Join the list`, `Explore rooms`

## Scores

| Candidate | Result | Overall | Sentence | Lexicon | CTA | Tone | Heading | Claim safety | Copy safety |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `after-copy` | **PASS** | 83.8 | 95.8 | 70.0 | 50.0 | 100.0 | 93.8 | 100.0 | 93.2 |
| `before-copy` | **FAIL** | 36.6 | 57.5 | 0.0 | 0.0 | 0.0 | 62.5 | 100.0 | 100.0 |

## Why This Is Useful

The score is deterministic. It checks measurable voice signals and gates against unsupported claims and copied spans.

## Candidate Evidence

- `after-copy` reused source lexicon: `collectors`, `current`, `follows`, `index`, `object`, `return`, `shopkeepers`; longest shared run: 5 words.
- `before-copy` reused source lexicon: none; longest shared run: 1 words.
