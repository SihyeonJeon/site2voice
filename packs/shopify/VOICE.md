# VOICE.md

Source: `https://www.shopify.com/`

Use this file to keep AI-generated pages, docs, and UI copy aligned with the observed website voice.

## Voice Summary

- Overall tone: **explanatory, action-oriented, trust-forward**.
- Sentence shape: about **20.4 words** per sentence.
- Main vocabulary: `english`, `shopify`, `espa`, `store`, `commerce`, `sidekick`, `fran`, `ais`, `build`, `app`, `dev`, `checkout`.
- Common CTAs: `Start for free`, `Get a stunning store`, `Build custom storefronts`, `Build for AI`, `Build apps`.
- Navigation labels: `Skip to Content`, `Sidekick Your commerce-obsessed AI assistant.`, `Website Builder`, `Themes`, `Domains`, `Customer Accounts`, `Sidekick`, `Online`, `AI Chats`, `Point of Sale`.

## Style Fingerprint

- Heading shape: about **5.4 words** per heading.
- Paragraph rhythm: about **4.5 words** per paragraph sample.
- CTA shape: about **3 words** per CTA.
- CTA verbs: `start`, `get`, `build`.
- Lexical variety: **0.25** type-token ratio.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Reuse the observed vocabulary, but do not copy full marketing paragraphs.
- Keep headings specific; avoid generic labels like `Powerful features` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Output Contract

- Keep average sentence length between **15.3 and 25.5 words**.
- Keep headings near **5.4 words**; avoid generic one-word section labels unless the source uses them.
- Keep paragraph blocks near **4.5 words**.
- Keep CTAs near **3.0 words** and start them with: `start`, `get`, `build`.
- Use at least **4** of these terms where natural: `english`, `shopify`, `espa`, `store`, `commerce`, `sidekick`, `fran`, `ais`, `build`, `app`, `dev`, `checkout`.
- Keep the first screen structure close to: specific headline, short proof/value sentence, one or two action CTAs.
- If writing a candidate file, run:
  `site2voice bench https://www.shopify.com/ path/to/candidate.md --strict`
- Revise until overall >= **75**, copy safety >= **85**, and claim safety >= **75**.

## Evidence

| Signal | Value |
| --- | --- |
| Words | 1771 |
| Sentences | 87 |
| Headings | 12 |
| CTA candidates | 5 |

## Do / Don't

- Do: write concise, outcome-first copy using the observed verbs and nouns.
- Do: keep CTAs short and action-led.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
