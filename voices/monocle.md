# VOICE.md

Source: `https://monocle.com/`

Use this file to keep AI-generated pages, docs, and UI copy aligned with the observed website voice.

## Voice Summary

- Overall tone: **explanatory, action-oriented**.
- Sentence shape: about **66.9 words** per sentence.
- Main vocabulary: `monocle`, `min`, `city`, `design`, `guides`, `read`, `affairs`, `radio`, `new`, `travel`, `shop`, `fashion`.
- Common CTAs: `see all`, `See all Monocle events and collaborations`, `Contact Us`, `Get in touch`, `Sign in`, `Buy a subscription`, `Sign out`.
- Navigation labels: `Skip to main content`, `Subscribe`, `British Pound (GBP)`, `Euro (EUR)`, `US Dollar (USD)`, `Australian Dollar (AUD)`, `Swiss Franc (CHF)`, `Magazine`, `Radio`, `Shop`.

## Style Fingerprint

- Heading shape: about **8.2 words** per heading.
- Paragraph rhythm: about **7 words** per paragraph sample.
- CTA shape: about **2.9 words** per CTA.
- CTA verbs: `see`, `contact`, `get`, `sign`, `buy`.
- Lexical variety: **0.29** type-token ratio.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Reuse the observed vocabulary, but do not copy full marketing paragraphs.
- Keep headings specific; avoid generic labels like `Powerful features` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Output Contract

- Keep average sentence length between **50.2 and 83.6 words**.
- Keep headings near **8.2 words**; avoid generic one-word section labels unless the source uses them.
- Keep paragraph blocks near **7.0 words**.
- Keep CTAs near **2.9 words** and start them with: `see`, `contact`, `get`, `sign`, `buy`.
- Use at least **4** of these terms where natural: `monocle`, `min`, `city`, `design`, `guides`, `read`, `affairs`, `radio`, `new`, `travel`, `shop`, `fashion`.
- Keep the first screen structure close to: specific headline, short proof/value sentence, one or two action CTAs.
- If writing a candidate file, run:
  `site2voice bench https://monocle.com/ path/to/candidate.md --strict`
- Revise until overall >= **75**, copy safety >= **85**, and claim safety >= **75**.

## Evidence

| Signal | Value |
| --- | --- |
| Words | 2675 |
| Sentences | 40 |
| Headings | 12 |
| CTA candidates | 7 |

## Do / Don't

- Do: write concise, outcome-first copy using the observed verbs and nouns.
- Do: keep CTAs short and action-led.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
