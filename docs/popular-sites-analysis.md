# Popular Sites Analysis

Snapshot date: 2026-05-20.

This expansion used Similarweb's 2026 Top 100 pages as the popularity signal:
`https://www.similarweb.com/blog/research/market-research/most-visited-websites/`.
It then filtered for pages that are useful as public copy references. A site
was added only when the public page produced enough extractable copy to create a
practical `VOICE.md` profile.

## Selection Rules

- Prefer globally or US-popular web brands with clear public pages.
- Prefer pages with meaningful headings, CTAs, paragraph rhythm, and enough copy
  to benchmark.
- Use reference-only public pages. If the homepage is mostly app shell or
  blocked, use an official about/product page from the same organization.
- Exclude pages with near-zero extractable text, blocked fetches, or mostly
  feed/search/current-event noise.
- Keep the public profile redacted: no source nouns, raw CTAs, navigation
  labels, screenshots, logos, or brand assets.

## Added Profiles

| Profile | Reference | Words | Sentence | Headings | CTA | Tone | Use |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| Brave | `https://brave.com/` | 1826 | 10.6 | 7 | 9 | balanced, action-oriented, technical, trust-forward | privacy-first browser and search copy |
| Canva | `https://www.canva.com/about/` | 1549 | 6 | 12 | 6 | short and direct, action-oriented, trust-forward | accessible creator-tool positioning |
| Discord | `https://discord.com/` | 767 | 17.3 | 12 | 5 | balanced, action-oriented, technical, trust-forward | casual community-product copy |
| Disney+ | `https://www.disneyplus.com/` | 3386 | 10.1 | 2 | 3 | balanced | franchise entertainment subscription copy |
| LinkedIn | `https://www.linkedin.com/` | 1238 | 14 | 12 | 5 | balanced, action-oriented, trust-forward | career and professional-network copy |
| Microsoft | `https://www.microsoft.com/en-us/ai` | 3369 | 10.9 | 12 | 12 | balanced, action-oriented, technical, trust-forward | broad AI product-ecosystem copy |
| Netflix | `https://www.netflix.com/` | 629 | 8.4 | 12 | 5 | short and direct, action-oriented | direct entertainment subscription copy |
| PayPal | `https://www.paypal.com/us/business` | 1341 | 6.5 | 12 | 12 | short and direct, action-oriented, trust-forward | consumer and business payments copy |
| Pinterest | `https://www.pinterest.com/about/` | 514 | 12.4 | 8 | 7 | balanced, action-oriented | visual discovery and inspiration copy |
| Prime Video | `https://www.primevideo.com/` | 1151 | 5.6 | 6 | 4 | short and direct, action-oriented | catalog-led entertainment copy |
| Reddit | `https://www.redditinc.com/` | 685 | 11.5 | 7 | 2 | balanced, trust-forward | community and conversation-platform copy |
| Roblox | `https://corp.roblox.com/` | 575 | 11.2 | 12 | 6 | balanced, action-oriented | youth gaming and creator-platform copy |
| Samsung | `https://www.samsung.com/` | 2066 | 6.5 | 12 | 2 | short and direct | consumer hardware ecosystem copy |
| Spotify | `https://www.spotify.com/us/premium/` | 1014 | 5.4 | 12 | 8 | short and direct, action-oriented | music and audio subscription copy |
| TikTok | `https://www.tiktok.com/about` | 4890 | 24 | 12 | 4 | explanatory, action-oriented | creator and entertainment-platform copy |
| WhatsApp | `https://www.whatsapp.com/` | 580 | 10.8 | 8 | 3 | balanced, trust-forward | privacy-forward consumer utility copy |
| Zillow | `https://www.zillow.com/mortgages/` | 3788 | 14.7 | 12 | 12 | balanced, action-oriented, technical | real-estate finance and marketplace copy |
| Zoom | `https://www.zoom.com/` | 1920 | 7.8 | 12 | 12 | short and direct, action-oriented | meeting and collaboration SaaS copy |

## Excluded Or Redirected

| Candidate | Decision | Reason |
| --- | --- | --- |
| Google / YouTube / Facebook / Instagram | Excluded | Primarily app/search/feed shells for this extractor; low public writing-contract value. |
| Reddit homepage | Redirected to Reddit Inc. | The homepage exposed near-zero extractable public copy. |
| Pinterest homepage | Redirected to about page | The homepage exposed near-zero extractable public copy. |
| Twitch homepage | Excluded | The public page exposed near-zero extractable copy; about page was usable but lower priority. |
| Amazon homepage | Excluded | The public homepage exposed too little reusable copy; corporate pages were less useful for product copy. |
| Booking.com / Indeed / Etsy | Excluded | Fetch was blocked or returned insufficient copy during review. |
| Weather / ESPN / NYTimes | Deferred | Popular, but live news/feed surfaces are volatile and less reusable as stable copy profiles. |

## Implementation Notes

The sentence metric was hardened during this pass. The analyzer now derives
sentence shape from paragraph-like blocks first and only falls back to broader
page text when needed. This prevents card-heavy or JS-rendered pages from
producing unrealistic 80-120 word sentence targets.
