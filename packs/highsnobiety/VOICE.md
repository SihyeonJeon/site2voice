# VOICE.md

Source: `https://www.highsnobiety.com/`

Use this file to keep AI-generated pages, docs, and UI copy aligned with the observed website voice.

## Voice Summary

- Overall tone: **explanatory**.
- Sentence shape: about **22.3 words** per sentence.
- Main vocabulary: `culture`, `style`, `highsnobiety`, `beauty`, `brands`, `sneakers`, `now`, `this`, `spring`, `issue`, `sable`, `yong`.
- Common CTAs: `Get our App`, `See All`, `Contact`.
- Navigation labels: `Highsnobiety`, `Latest`, `Shopping`, `Style`, `Sneakers`, `Culture`, `Beauty`, `SPRING ‘26 ISSUE`, `Drop Calendar`, `Magazines`.

## Style Fingerprint

- Heading shape: about **9.2 words** per heading.
- Paragraph rhythm: about **21 words** per paragraph sample.
- CTA shape: about **2 words** per CTA.
- CTA verbs: `get`, `see`, `contact`.
- Lexical variety: **0.355** type-token ratio.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Reuse the observed vocabulary, but do not copy full marketing paragraphs.
- Keep headings specific; avoid generic labels like `Powerful features` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Output Contract

- Keep average sentence length between **16.7 and 27.9 words**.
- Keep headings near **9.2 words**; avoid generic one-word section labels unless the source uses them.
- Keep paragraph blocks near **21.0 words**.
- Keep CTAs near **2.0 words** and start them with: `get`, `see`, `contact`.
- Use at least **4** of these terms where natural: `culture`, `style`, `highsnobiety`, `beauty`, `brands`, `sneakers`, `now`, `this`, `spring`, `issue`, `sable`, `yong`.
- Keep the first screen structure close to: specific headline, short proof/value sentence, one or two action CTAs.
- If writing a candidate file, run:
  `site2voice bench https://www.highsnobiety.com/ path/to/candidate.md --strict`
- Revise until overall >= **75**, copy safety >= **85**, and claim safety >= **75**.

## Evidence

| Signal | Value |
| --- | --- |
| Words | 1716 |
| Sentences | 77 |
| Headings | 12 |
| CTA candidates | 3 |

## Do / Don't

- Do: write concise, outcome-first copy using the observed verbs and nouns.
- Do: keep CTAs short and action-led.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
