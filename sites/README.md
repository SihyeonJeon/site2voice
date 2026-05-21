# SITE.md Collection

Drop-in reference-only page-structure profiles for AI agents.

`SITE.md` captures page architecture: section order, section jobs,
content boundaries, and agent instructions. It does not include visual
design tokens, source headings, raw CTAs, screenshots, logos, or brand assets.

Use it with the matching `VOICE.md`:

```bash
curl -L https://raw.githubusercontent.com/SihyeonJeon/site2voice/main/sites/stripe.md -o SITE.md
curl -L https://raw.githubusercontent.com/SihyeonJeon/site2voice/main/voices/stripe.md -o VOICE.md
```

Then tell your agent:

```text
Use @SITE.md for page structure and @VOICE.md for copy rhythm. Bring our own product nouns, facts, and claims.
```

## Sites

| Site | Archetype | Density | Conversion | Use |
| --- | --- | --- | --- | --- |
| [Anthropic](anthropic.md) | technical product landing | balanced | high | measured AI safety and product copy |
| [Apple](apple.md) | product landing | dense | high | minimal premium product copy |
| [Brave](brave.md) | technical product landing | dense | high | privacy-first browser and search copy |
| [Canva](canva.md) | product landing | dense | high | accessible creator-tool positioning |
| [Discord](discord.md) | community platform landing | balanced | high | casual community-product copy |
| [Disney+](disneyplus.md) | subscription landing | dense | medium | franchise entertainment subscription copy |
| [EYESMAG](eyesmag.md) | editorial index | balanced | low | Korean fashion and lifestyle editorial intro copy |
| [Figma](figma.md) | product landing | dense | high | creative collaboration copy |
| [GitHub](github.md) | technical product landing | dense | high | developer ecosystem copy |
| [Highsnobiety](highsnobiety.md) | editorial index | dense | medium | commerce-aware culture editorial copy |
| [Hypebeast](hypebeast.md) | editorial index | balanced | medium | trend-led culture editorial copy |
| [Linear](linear.md) | technical product landing | balanced | high | precise product-team positioning |
| [LinkedIn](linkedin.md) | community platform landing | dense | high | career and professional-network copy |
| [Microsoft](microsoft.md) | technical product landing | dense | high | broad AI product-ecosystem copy |
| [Monocle](monocle.md) | editorial index | dense | high | polished city, design, and affairs copy |
| [Netflix](netflix.md) | subscription landing | balanced | high | direct entertainment subscription copy |
| [Notion](notion.md) | product landing | balanced | high | simple workspace and AI-product copy |
| [OpenAI](openai.md) | technical product landing | balanced | high | research-to-product institutional copy |
| [PayPal](paypal.md) | commerce journey | dense | high | consumer and business payments copy |
| [Pinterest](pinterest.md) | community platform landing | balanced | high | visual discovery and inspiration copy |
| [Prime Video](primevideo.md) | subscription landing | balanced | medium | catalog-led entertainment copy |
| [Reddit](reddit.md) | community platform landing | balanced | medium | community and conversation-platform copy |
| [Roblox](roblox.md) | community platform landing | balanced | high | youth gaming and creator-platform copy |
| [Samsung](samsung.md) | product landing | dense | medium | consumer hardware ecosystem copy |
| [Shopify](shopify.md) | commerce journey | dense | high | merchant-growth product copy |
| [Spotify](spotify.md) | subscription landing | balanced | high | music and audio subscription copy |
| [Stripe](stripe.md) | technical product landing | dense | high | technical trust-forward SaaS copy |
| [TikTok](tiktok.md) | community platform landing | dense | medium | creator and entertainment-platform copy |
| [Vercel](vercel.md) | technical product landing | dense | high | performance and deployment copy |
| [Wallpaper](wallpaper.md) | editorial index | dense | medium | design, interiors, and architecture editorial copy |
| [WhatsApp](whatsapp.md) | community platform landing | balanced | medium | privacy-forward consumer utility copy |
| [Zillow](zillow.md) | marketplace landing | dense | high | real-estate finance and marketplace copy |
| [Zoom](zoom.md) | product landing | dense | high | meeting and collaboration SaaS copy |

Need machine-readable evidence or an agent prompt too? Use the full
[context packs](../packs).
