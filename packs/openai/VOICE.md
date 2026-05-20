# VOICE.md

Source: `https://openai.com/`

Use this file to keep AI-generated pages, docs, and UI copy aligned with the observed website voice.

## Voice Summary

- Overall tone: **explanatory, action-oriented, technical**.
- Sentence shape: about **46.2 words** per sentence.
- Main vocabulary: `new`, `opens`, `window`, `research`, `product`, `chatgpt`, `may`, `gpt-5`, `business`, `min`, `read`, `safety`.
- Common CTAs: `Try ChatGPT (opens in a new window)`, `Download`, `Explore ChatGPT (opens in a new window)`, `Download (opens in a new window)`, `Contact Sales`.
- Navigation labels: `Skip to main content`, `Research`, `Business`, `Developers`, `Company`, `Foundation (opens in a new window)`, `Talk with ChatGPT`, `API Platform`, `Stories`, `Introducing GPT-5.5 Product 18 min read`.

## Style Fingerprint

- Heading shape: about **2.4 words** per heading.
- Paragraph rhythm: about **2.2 words** per paragraph sample.
- CTA shape: about **4.6 words** per CTA.
- CTA verbs: `try`, `download`, `explore`, `contact`.
- Lexical variety: **0.301** type-token ratio.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Reuse the observed vocabulary, but do not copy full marketing paragraphs.
- Keep headings specific; avoid generic labels like `Powerful features` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Evidence

| Signal | Value |
| --- | --- |
| Words | 554 |
| Sentences | 12 |
| Headings | 5 |
| CTA candidates | 5 |

## Do / Don't

- Do: write concise, outcome-first copy using the observed verbs and nouns.
- Do: keep CTAs short and action-led.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
