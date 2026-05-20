# site2voice

**Generate `VOICE.md` from any website.**

`site2voice` reads website copy and writes a small Markdown brief that tells an
AI coding agent how the site sounds: headings, CTAs, navigation labels, sentence
shape, repeated vocabulary, and claim boundaries.

```bash
pipx install site2voice

site2voice https://example.com --out VOICE.md
```

From a repo clone, run the included benchmark fixture:

```bash
site2voice examples/saas-home.html --format json
site2voice bench examples/editorial-home.html examples/before-copy.md examples/after-copy.md
```

## Why

`DESIGN.md` helps agents stop guessing visual style. `VOICE.md` helps them stop
guessing copy style.

Drop the generated file into a project and tell the agent:

```text
Use @VOICE.md for landing-page copy, headings, CTAs, and UI microcopy.
```

## Output

```md
# VOICE.md

## Voice Summary

- Overall tone: explanatory, action-oriented, trust-forward.
- Sentence shape: about 20.4 words per sentence.
- Main vocabulary: `teams`, `security`, `pricing`, `launch`.
- Common CTAs: `Start free`, `Book a demo`, `See pricing`.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Do not invent compliance, security, customer, or performance claims.
```

The real output also includes a small style fingerprint for heading length,
paragraph rhythm, CTA shape, CTA verbs, and lexical variety.

## What It Does

- Reads a URL or local HTML file.
- Extracts title, meta description, headings, links, buttons, and paragraphs.
- Finds CTA candidates from short action-led links/buttons.
- Measures average sentence length.
- Extracts a compact style fingerprint: heading shape, paragraph rhythm,
  CTA shape, CTA verbs, and lexical variety.
- Builds a repeated-vocabulary lexicon.
- Writes Markdown or JSON.
- Benchmarks candidate copy against a source voice profile.
- Gates against unsupported claims and copied spans.
- Uses only the Python standard library.

## Benchmark

`site2voice bench` compares candidate copy against measurable source signals:
sentence length, vocabulary overlap, CTA shape, tone labels, heading shape,
claim boundaries, and copy safety.

```bash
site2voice bench examples/editorial-home.html \
  examples/before-copy.md \
  examples/after-copy.md \
  --out examples/editorial-benchmark.md
```

| Candidate | Result | Overall | Lexicon | Copy safety |
| --- | --- | ---: | ---: | ---: |
| `after-copy` | PASS | 83.8 | 70.0 | 93.2 |
| `before-copy` | FAIL | 36.6 | 0.0 | 100.0 |

The benchmark rewards measurable voice alignment without rewarding verbatim
copying.

## What It Is Not

- Not an official brand guideline.
- Not a DESIGN.md visual-token extractor.
- Not a crawler for private pages or authenticated apps.
- Not an LLM prompt that copies a site's prose.

## Develop

```bash
python3 -m pip install -e .
make test
make bench
site2voice examples/saas-home.html --out examples/saas-VOICE.md
```

## Links

- [Research](docs/research.md)
- [Benchmark](docs/benchmark.md)
- [Voice patterns](docs/voice-patterns.md)
- [Source candidates](docs/source-candidates.md)
- [Awesome eligibility](docs/awesome-eligibility.md)
- [Harness](docs/harness.md)
- [Launch kit](docs/launch-kit.md)

## License

MIT
