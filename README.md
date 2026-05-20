# site2voice

**Turn any website into agent-ready copy context. Then test whether the agent followed it.**

[![PyPI](https://img.shields.io/pypi/v/site2voice.svg)](https://pypi.org/project/site2voice/)
[![CI](https://github.com/SihyeonJeon/site2voice/actions/workflows/ci.yml/badge.svg)](https://github.com/SihyeonJeon/site2voice/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

![site2voice terminal demo](https://raw.githubusercontent.com/SihyeonJeon/site2voice/main/assets/demo.svg)

```bash
pipx install site2voice

site2voice init https://example.com
site2voice bench https://example.com draft.md --strict
```

No LLM dependency. No browser dependency. Just a small Python CLI that extracts
measurable voice signals and turns them into files coding agents can use.

## Why

Agents are getting better at building interfaces, but they still guess the
words: headings, CTAs, navigation labels, claim boundaries, and product tone.

`DESIGN.md` gives agents visual taste. `site2voice` gives them copy taste.

## What You Get

```text
.site2voice/
  VOICE.md          human-readable writing brief
  voice.json        machine-readable voice profile
  agent-prompt.md   drop-in instruction for Codex, Claude Code, Cursor, etc.
```

The profile includes:

- heading shape, sentence rhythm, paragraph length, CTA shape;
- repeated vocabulary and CTA verbs;
- deterministic tone labels;
- unsupported-claim detection;
- copied-span detection.

## Benchmark

`site2voice bench` scores candidate copy against a source voice profile and can
fail CI when the copy drifts.

```bash
site2voice bench examples/editorial-home.html examples/after-copy.md --strict
```

Example fixture:

| Candidate | Result | Overall | Lexicon | Copy safety |
| --- | --- | ---: | ---: | ---: |
| `after-copy` | PASS | 83.8 | 70.0 | 93.2 |
| `before-copy` | FAIL | 36.6 | 0.0 | 100.0 |

The score rewards measurable voice alignment without rewarding verbatim copying.

## Commands

```bash
# Generate one Markdown brief
site2voice https://example.com --out VOICE.md

# Generate an agent-ready context pack
site2voice init https://example.com --dir .site2voice

# Write JSON for custom pipelines
site2voice https://example.com --format json --out voice.json

# Gate candidate copy in CI
site2voice bench https://example.com draft.md \
  --fail-under 75 \
  --min-copy-safety 85 \
  --min-claim-safety 75
```

## What It Is Not

- Not an official brand guideline.
- Not a DESIGN.md visual-token extractor.
- Not a crawler for private pages or authenticated apps.
- Not a tool for copying another site's prose.

## Develop

```bash
python3 -m pip install -e .
make test
make bench-ci
```

## Docs

- [Benchmark](docs/benchmark.md)
- [CI usage](docs/ci.md)
- [Agent workflows](docs/agent-workflows.md)
- [Voice patterns](docs/voice-patterns.md)
- [JSON schema](schemas/voice.schema.json)
- [Market position](docs/market-position.md)
- [Research](docs/research.md)
- [Source candidates](docs/source-candidates.md)
- [Awesome eligibility](docs/awesome-eligibility.md)
- [Roadmap](docs/roadmap.md)

## License

MIT
