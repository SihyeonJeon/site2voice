# site2voice

**Generate `VOICE.md` from any website.**

`site2voice` reads website copy and writes a small Markdown brief that tells an
AI coding agent how the site sounds: headings, CTAs, navigation labels, sentence
shape, repeated vocabulary, and claim boundaries.

```bash
pipx install git+https://github.com/SihyeonJeon/site2voice

site2voice https://example.com --out VOICE.md
site2voice examples/saas-home.html --out examples/saas-VOICE.md
site2voice examples/saas-home.html --format json
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

## What It Does

- Reads a URL or local HTML file.
- Extracts title, meta description, headings, links, buttons, and paragraphs.
- Finds CTA candidates from short action-led links/buttons.
- Measures average sentence length.
- Builds a repeated-vocabulary lexicon.
- Writes Markdown or JSON.
- Uses only the Python standard library.

## What It Is Not

- Not an official brand guideline.
- Not a DESIGN.md visual-token extractor.
- Not a crawler for private pages or authenticated apps.
- Not an LLM prompt that copies a site's prose.

## Develop

```bash
python3 -m pip install -e .
make test
site2voice examples/saas-home.html --out examples/saas-VOICE.md
```

## Links

- [Research](docs/research.md)
- [Launch kit](docs/launch-kit.md)

## License

MIT
