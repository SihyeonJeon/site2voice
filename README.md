# site2voice

**Drop-in `SITE.md` and `VOICE.md` profiles. Pick a public web pattern, save two files, and your agent gets page structure plus copy rhythm.**

`site2voice` is not a visual design-system library and not a brand-cloning tool.
It turns public pages into compact, reference-only context files:

- `SITE.md`: section order, page jobs, structure recipes, and content boundaries.
- `VOICE.md`: sentence rhythm, heading shape, CTA shape, claim boundaries, and benchmark gates.

**No install. No JSON. No generation step.**

**Not official. Not affiliated. Not permission to impersonate a brand.**

## Context Stack

Use the files together without overlapping responsibilities:

| Context | Owns | Must not supply |
| --- | --- | --- |
| Project brief | product category, audience, facts, domain nouns, examples, offer, claims | reference-site nouns |
| `DESIGN.md` | colors, typography, spacing, layout grid, components, motion, imagery style | copy rhythm or claims |
| `SITE.md` | page structure, section order, section jobs, conversion path | colors, fonts, product category |
| `VOICE.md` | sentence rhythm, heading behavior, CTA shape, claim boundaries | product nouns, visual design |

This prevents an athletic retail reference from leaking its products or cultural
context into an unrelated education, finance, healthcare, or developer product.

## Featured Profiles

| Profile | Tone | Best for |
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

The full collection now includes **33 reference-only profiles**, including
popular web products such as [Canva](voices/canva.md),
[LinkedIn](voices/linkedin.md), [Netflix](voices/netflix.md),
[TikTok](voices/tiktok.md), [WhatsApp](voices/whatsapp.md), [Zoom](voices/zoom.md),
and [PayPal](voices/paypal.md). See the [full collection](voices) and the
[SITE.md collection](sites), plus the [popular-sites analysis](docs/popular-sites-analysis.md).

## Use

Download one structure profile and one copy profile:

```bash
curl -L https://raw.githubusercontent.com/SihyeonJeon/site2voice/main/sites/stripe.md -o SITE.md
curl -L https://raw.githubusercontent.com/SihyeonJeon/site2voice/main/voices/stripe.md -o VOICE.md
```

Tell Claude Code, Codex, Cursor, or Copilot:

```text
Use @SITE.md for page structure and @VOICE.md for copy rhythm. Bring our own product nouns, facts, and claims.
```

Each file is plain Markdown. Public profiles remove source nouns, raw CTAs,
navigation labels, paragraph samples, logos, screenshots, and brand assets.
Use `SITE.md` when building a web page; use `VOICE.md` when writing headings,
CTAs, UI copy, and launch copy.

Reference names identify the public page used for measurement. They do not
imply sponsorship, endorsement, affiliation, or permission to reuse protected
brand identity. See [Brand Usage](BRAND_USAGE.md).

## Not DESIGN.md

`DESIGN.md` describes visual identity: colors, typography, spacing, components,
layout, and responsive behavior. `SITE.md` describes page structure: section
order, section jobs, page archetype, and content boundaries. `VOICE.md`
describes writing behavior: rhythm, CTA shape, claim safety, and copy-safety
gates.

Read the full comparison in [DESIGN.md vs SITE.md / VOICE.md](docs/design-md-comparison.md)
and the dated [competitive review](docs/competitive-review.md).

## Before / After

Same LedgerFlow prompt, scored against Stripe:

| Candidate | Result | Overall | Variety | CTA | Copy safety |
| --- | --- | ---: | ---: | ---: | ---: |
| Without `VOICE.md` | FAIL | 63.8 | 40.5 | 25.0 | 100.0 |
| With `VOICE.md` | PASS | 91.1 | 45.8 | 100.0 | 96.2 |

See the [full comparison](examples/comparisons/stripe-ledgerflow/README.md).

For a visible web result, see the
[SITE.md + VOICE.md web comparison](examples/comparisons/stripe-ledgerflow-web).
It shows the same HTML landing-page prompt with and without the context files,
including screenshots and a `reference-fit` score.

## Optional CLI

Generate a new context pack from any public URL:

```bash
pipx install site2voice
site2voice init https://example.com
```

Generate only a page-structure file:

```bash
site2voice site https://example.com --out SITE.md
```

Validate generated copy:

```bash
site2voice bench https://example.com draft.md --strict
```

Need `site.json`, `voice.json`, or an agent prompt too? Use the full [context packs](packs).

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
