# VOICE.md

Source: `https://www.eyesmag.com/about`

Use this file to keep AI-generated pages, docs, and UI copy aligned with the observed website voice.

## Voice Summary

- Overall tone: **balanced**.
- Sentence shape: about **12.8 words** per sentence.
- Main vocabulary: `eyesmag`, `회사소개`, `fashion`, `info`, `com`, `아이즈매거진`, `라이프스타일`, `매거진입니다`, `매력적인`, `정보를`, `선별하고`, `데스크톱`.
- Common CTAs: `Profile download`.
- Navigation labels: `샵`, `회사소개`, `info@eyesmag.com`, `Profile download`, `윤리강령`, `고충처리인`, `개인정보처리방침`, `홈`.

## Style Fingerprint

- Heading shape: about **1 words** per heading.
- Paragraph rhythm: about **16.2 words** per paragraph sample.
- CTA shape: about **2 words** per CTA.
- CTA verbs: `profile`.
- Lexical variety: **0.246** type-token ratio.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Reuse the observed vocabulary, but do not copy full marketing paragraphs.
- Keep headings specific; avoid generic labels like `Powerful features` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Output Contract

- Keep average sentence length between **9.6 and 16.0 words**.
- Keep headings near **1.0 words**; avoid generic one-word section labels unless the source uses them.
- Keep paragraph blocks near **16.2 words**.
- Keep CTAs near **2.0 words** and start them with: `profile`.
- Use at least **4** of these terms where natural: `eyesmag`, `회사소개`, `fashion`, `info`, `com`, `아이즈매거진`, `라이프스타일`, `매거진입니다`, `매력적인`, `정보를`, `선별하고`, `데스크톱`.
- Keep the first screen structure close to: specific headline, short proof/value sentence, one or two action CTAs.
- If writing a candidate file, run:
  `site2voice bench https://www.eyesmag.com/about path/to/candidate.md --strict`
- Revise until overall >= **75**, copy safety >= **85**, and claim safety >= **75**.

## Evidence

| Signal | Value |
| --- | --- |
| Words | 769 |
| Sentences | 60 |
| Headings | 1 |
| CTA candidates | 1 |

## Do / Don't

- Do: write concise, outcome-first copy using the observed verbs and nouns.
- Do: keep CTAs short and action-led.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
