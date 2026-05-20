# site2voice

**Drop-in `VOICE.md` files. Pick a website voice, save it in your repo, and your agent writes less generic copy.**

`DESIGN.md` tells agents how UI should look. `VOICE.md` tells them how copy should sound.

**No install. No JSON. No generation step.**

## Voices

| Voice | Tone | Best for |
| --- | --- | --- |
| [Apple](voices/apple.md) | premium, minimal | product launches |
| [Anthropic](voices/anthropic.md) | measured, institutional | AI safety and product pages |
| [EYESMAG](voices/eyesmag.md) | concise, culture-led | Korean fashion and lifestyle copy |
| [Figma](voices/figma.md) | collaborative, creative | design-tool pages |
| [GitHub](voices/github.md) | developer-first | platform and ecosystem copy |
| [Highsnobiety](voices/highsnobiety.md) | editorial, commerce-aware | culture and fashion launches |
| [Hypebeast](voices/hypebeast.md) | trend-led | streetwear and culture blurbs |
| [Linear](voices/linear.md) | precise, product-team | SaaS positioning |
| [Monocle](voices/monocle.md) | polished, global | city, design, and affairs copy |
| [Notion](voices/notion.md) | simple, workspace | productivity pages |
| [OpenAI](voices/openai.md) | research-to-product | AI product pages |
| [Shopify](voices/shopify.md) | merchant-growth | commerce pages |
| [Stripe](voices/stripe.md) | calm, technical | fintech and SaaS copy |
| [Vercel](voices/vercel.md) | performance-led | developer platform pages |
| [Wallpaper](voices/wallpaper.md) | design-editorial | architecture and interiors copy |

## Use

Download one voice as `VOICE.md`:

```bash
curl -L https://raw.githubusercontent.com/SihyeonJeon/site2voice/main/voices/stripe.md -o VOICE.md
```

Tell Claude Code, Codex, Cursor, or Copilot:

```text
Use @VOICE.md for headings, CTAs, navigation labels, and UI microcopy.
```

Each file is a plain Markdown writing brief with sentence rhythm, heading
shape, CTA verbs, content boundaries, claim boundaries, and a benchmark target.

These are not official brand guidelines. They are derived style briefs from
public pages, built to help agents write nearby copy without pasting source
prose.

## Before / After

Same LedgerFlow prompt, scored against Stripe:

| Candidate | Result | Overall | Variety | CTA | Copy safety |
| --- | --- | ---: | ---: | ---: | ---: |
| Without `VOICE.md` | FAIL | 60.4 | 40.5 | 50.0 | 100.0 |
| With `VOICE.md` | PASS | 91.0 | 45.8 | 100.0 | 96.2 |

See the [full comparison](examples/comparisons/stripe-ledgerflow/README.md).

## Optional CLI

Generate a new voice from any public URL:

```bash
pipx install site2voice
site2voice init https://example.com
```

Validate generated copy:

```bash
site2voice bench https://example.com draft.md --strict
```

Need `voice.json` or an agent prompt too? Use the full [context packs](packs).

## Status

[![PyPI](https://img.shields.io/pypi/v/site2voice.svg)](https://pypi.org/project/site2voice/)
[![CI](https://github.com/SihyeonJeon/site2voice/actions/workflows/ci.yml/badge.svg)](https://github.com/SihyeonJeon/site2voice/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Develop

```bash
python3 -m pip install -e .
make test
make bench-ci
```

## License

MIT
