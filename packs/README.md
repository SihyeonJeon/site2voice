# Voice Packs

Full reference-only copy profile packs generated from public websites.

These packs are public artifacts: they keep derived copy metrics and
benchmark contracts, but remove source paragraph samples, source nouns,
raw CTAs, navigation labels, screenshots, logos, and brand assets.

They are not official brand guidelines, endorsements, or permission to
impersonate a reference source. Reference names identify measurement
sources only.

For the fastest path, use the single-file [VOICE.md collection](../voices).

## Use

```bash
curl -L https://raw.githubusercontent.com/SihyeonJeon/site2voice/main/voices/stripe.md -o VOICE.md
```

Then tell your agent:

```text
Use @VOICE.md as a copy contract for headings, CTA shape, paragraph rhythm, and UI microcopy.
```

## Packs

| Pack | Category | Words | Sentence | CTA | Use |
| --- | --- | ---: | ---: | ---: | --- |
| [Anthropic](anthropic/VOICE.md) | AI research and product | 1064 | 34.3 | 3 | measured AI safety and product copy |
| [Apple](apple/VOICE.md) | consumer hardware | 2998 | 20.1 | 9 | minimal premium product copy |
| [EYESMAG](eyesmag/VOICE.md) | Korean fashion and lifestyle media | 769 | 12.8 | 1 | Korean fashion and lifestyle editorial intro copy |
| [Figma](figma/VOICE.md) | design collaboration | 1544 | 57.2 | 12 | creative collaboration copy |
| [GitHub](github/VOICE.md) | developer platform | 1628 | 40.7 | 12 | developer ecosystem copy |
| [Highsnobiety](highsnobiety/VOICE.md) | fashion and culture media | 1716 | 22.3 | 3 | commerce-aware culture editorial copy |
| [Hypebeast](hypebeast/VOICE.md) | streetwear and culture media | 993 | 47.3 | 1 | trend-led culture editorial copy |
| [Linear](linear/VOICE.md) | developer productivity | 797 | 12.9 | 8 | precise product-team positioning |
| [Monocle](monocle/VOICE.md) | global affairs and culture media | 2686 | 67.2 | 7 | polished city, design, and affairs copy |
| [Notion](notion/VOICE.md) | workspace productivity | 635 | 14.8 | 5 | simple workspace and AI-product copy |
| [OpenAI](openai/VOICE.md) | AI research and product | 554 | 46.2 | 5 | research-to-product institutional copy |
| [Shopify](shopify/VOICE.md) | commerce platform | 1699 | 22.1 | 2 | merchant-growth product copy |
| [Stripe](stripe/VOICE.md) | financial infrastructure | 1748 | 15.7 | 12 | technical trust-forward SaaS copy |
| [Vercel](vercel/VOICE.md) | developer platform | 2035 | 34.5 | 11 | performance and deployment copy |
| [Wallpaper](wallpaper/VOICE.md) | design and architecture media | 2072 | 74 | 2 | design, interiors, and architecture editorial copy |

Regenerate:

```bash
PYTHONPATH=src python3 scripts/build_packs.py
```
