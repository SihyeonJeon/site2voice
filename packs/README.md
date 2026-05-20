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
| [Anthropic](anthropic/VOICE.md) | AI research and product | 1064 | 8.8 | 6 | measured AI safety and product copy |
| [Apple](apple/VOICE.md) | consumer hardware | 2998 | 13.0 | 9 | minimal premium product copy |
| [Brave](brave/VOICE.md) | browser and privacy technology | 1826 | 10.6 | 9 | privacy-first browser and search copy |
| [Canva](canva/VOICE.md) | design platform | 1549 | 6 | 6 | accessible creator-tool positioning |
| [Discord](discord/VOICE.md) | community communication | 767 | 17.3 | 5 | casual community-product copy |
| [Disney+](disneyplus/VOICE.md) | streaming entertainment | 3386 | 10.1 | 3 | franchise entertainment subscription copy |
| [EYESMAG](eyesmag/VOICE.md) | Korean fashion and lifestyle media | 769 | 13.1 | 1 | Korean fashion and lifestyle editorial intro copy |
| [Figma](figma/VOICE.md) | design collaboration | 1544 | 7 | 12 | creative collaboration copy |
| [GitHub](github/VOICE.md) | developer platform | 1628 | 10.0 | 12 | developer ecosystem copy |
| [Highsnobiety](highsnobiety/VOICE.md) | fashion and culture media | 1716 | 16.4 | 3 | commerce-aware culture editorial copy |
| [Hypebeast](hypebeast/VOICE.md) | streetwear and culture media | 993 | 6.2 | 1 | trend-led culture editorial copy |
| [Linear](linear/VOICE.md) | developer productivity | 797 | 10.6 | 9 | precise product-team positioning |
| [LinkedIn](linkedin/VOICE.md) | professional network | 1238 | 14 | 5 | career and professional-network copy |
| [Microsoft](microsoft/VOICE.md) | technology platform | 3369 | 10.9 | 12 | broad AI product-ecosystem copy |
| [Monocle](monocle/VOICE.md) | global affairs and culture media | 2696 | 6.4 | 7 | polished city, design, and affairs copy |
| [Netflix](netflix/VOICE.md) | streaming entertainment | 629 | 8.4 | 5 | direct entertainment subscription copy |
| [Notion](notion/VOICE.md) | workspace productivity | 635 | 4.9 | 6 | simple workspace and AI-product copy |
| [OpenAI](openai/VOICE.md) | AI research and product | 554 | 2.8 | 5 | research-to-product institutional copy |
| [PayPal](paypal/VOICE.md) | payments platform | 1341 | 6.5 | 12 | consumer and business payments copy |
| [Pinterest](pinterest/VOICE.md) | visual discovery platform | 514 | 12.4 | 7 | visual discovery and inspiration copy |
| [Prime Video](primevideo/VOICE.md) | streaming entertainment | 1151 | 5.6 | 4 | catalog-led entertainment copy |
| [Reddit](reddit/VOICE.md) | community platform | 685 | 11.5 | 2 | community and conversation-platform copy |
| [Roblox](roblox/VOICE.md) | gaming and creation platform | 575 | 11.2 | 6 | youth gaming and creator-platform copy |
| [Samsung](samsung/VOICE.md) | consumer electronics | 2066 | 6.5 | 2 | consumer hardware ecosystem copy |
| [Shopify](shopify/VOICE.md) | commerce platform | 1771 | 6.1 | 5 | merchant-growth product copy |
| [Spotify](spotify/VOICE.md) | audio streaming | 1014 | 5.4 | 8 | music and audio subscription copy |
| [Stripe](stripe/VOICE.md) | financial infrastructure | 1748 | 12.6 | 12 | technical trust-forward SaaS copy |
| [TikTok](tiktok/VOICE.md) | short-form video platform | 4890 | 24 | 4 | creator and entertainment-platform copy |
| [Vercel](vercel/VOICE.md) | developer platform | 2035 | 4.9 | 12 | performance and deployment copy |
| [Wallpaper](wallpaper/VOICE.md) | design and architecture media | 2110 | 7.2 | 2 | design, interiors, and architecture editorial copy |
| [WhatsApp](whatsapp/VOICE.md) | messaging platform | 580 | 10.8 | 3 | privacy-forward consumer utility copy |
| [Zillow](zillow/VOICE.md) | real estate marketplace | 3788 | 14.7 | 12 | real-estate finance and marketplace copy |
| [Zoom](zoom/VOICE.md) | work communication | 1920 | 7.8 | 12 | meeting and collaboration SaaS copy |

Regenerate:

```bash
PYTHONPATH=src python3 scripts/build_packs.py
```
