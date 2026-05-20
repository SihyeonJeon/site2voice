# VOICE.md

Source: `https://linear.app/`

Use this file to keep AI-generated pages, docs, and UI copy aligned with the observed website voice.

## Voice Summary

- Overall tone: **balanced, action-oriented, technical**.
- Sentence shape: about **12.9 words** per sentence.
- Main vocabulary: `linear`, `product`, `teams`, `agents`, `app`, `agent`, `just`, `contact`, `plan`, `work`, `will`, `customers`.
- Common CTAs: `Contact`, `Sign up`, `3.0 Build →`, `Get started`, `Contact sales`, `Download`, `Build`, `Contact us`.
- Navigation labels: `Skip to content →`, `Customers`, `Pricing`, `Now`, `Contact`, `Docs`, `Open app`, `Log in`, `Sign up`, `1.0 Intake →`.

## Style Fingerprint

- Heading shape: about **7.2 words** per heading.
- Paragraph rhythm: about **16.1 words** per paragraph sample.
- CTA shape: about **1.5 words** per CTA.
- CTA verbs: `contact`, `sign`, `build`, `get`, `download`.
- Lexical variety: **0.399** type-token ratio.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Reuse the observed vocabulary, but do not copy full marketing paragraphs.
- Keep headings specific; avoid generic labels like `Powerful features` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Output Contract

- Keep average sentence length between **9.7 and 16.1 words**.
- Keep headings near **7.2 words**; avoid generic one-word section labels unless the source uses them.
- Keep paragraph blocks near **16.1 words**.
- Keep CTAs near **1.5 words** and start them with: `contact`, `sign`, `build`, `get`, `download`.
- Use at least **4** of these terms where natural: `linear`, `product`, `teams`, `agents`, `app`, `agent`, `just`, `contact`, `plan`, `work`, `will`, `customers`.
- Keep the first screen structure close to: specific headline, short proof/value sentence, one or two action CTAs.
- If writing a candidate file, run:
  `site2voice bench https://linear.app/ path/to/candidate.md --strict`
- Revise until overall >= **75**, copy safety >= **85**, and claim safety >= **75**.

## Evidence

| Signal | Value |
| --- | --- |
| Words | 797 |
| Sentences | 62 |
| Headings | 12 |
| CTA candidates | 8 |

## Do / Don't

- Do: write concise, outcome-first copy using the observed verbs and nouns.
- Do: keep CTAs short and action-led.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
