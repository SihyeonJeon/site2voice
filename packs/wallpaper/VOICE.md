# VOICE.md

Source: `https://www.wallpaper.com/`

Use this file to keep AI-generated pages, docs, and UI copy aligned with the observed website voice.

## Voice Summary

- Overall tone: **explanatory**.
- Sentence shape: about **68.3 words** per sentence.
- Main vocabulary: `may`, `published`, `new`, `last`, `design`, `updated`, `wallpaper`, `travel`, `tianna`, `williams`, `this`, `summer`.
- Common CTAs: `Sign up to our newsletter Newsletter`, `Contact Future's experts`.
- Navigation labels: `Wallpaper*`, `Architecture`, `Design & interiors`, `Art & Culture`, `Watches & Jewellery`, `Fashion & Beauty`, `Technology`, `Transportation`, `Travel`, `Entertaining`.

## Style Fingerprint

- Heading shape: about **1.5 words** per heading.
- Paragraph rhythm: about **16.2 words** per paragraph sample.
- CTA shape: about **4.5 words** per CTA.
- CTA verbs: `sign`, `contact`.
- Lexical variety: **0.23** type-token ratio.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Reuse the observed vocabulary, but do not copy full marketing paragraphs.
- Keep headings specific; avoid generic labels like `Powerful features` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Output Contract

- Keep average sentence length between **51.2 and 85.4 words**.
- Keep headings near **1.5 words**; avoid generic one-word section labels unless the source uses them.
- Keep paragraph blocks near **16.2 words**.
- Keep CTAs near **4.5 words** and start them with: `sign`, `contact`.
- Use at least **4** of these terms where natural: `may`, `published`, `new`, `last`, `design`, `updated`, `wallpaper`, `travel`, `tianna`, `williams`, `this`, `summer`.
- Keep the first screen structure close to: specific headline, short proof/value sentence, one or two action CTAs.
- If writing a candidate file, run:
  `site2voice bench https://www.wallpaper.com/ path/to/candidate.md --strict`
- Revise until overall >= **75**, copy safety >= **85**, and claim safety >= **75**.

## Evidence

| Signal | Value |
| --- | --- |
| Words | 2050 |
| Sentences | 30 |
| Headings | 12 |
| CTA candidates | 2 |

## Do / Don't

- Do: write concise, outcome-first copy using the observed verbs and nouns.
- Do: keep CTAs short and action-led.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
