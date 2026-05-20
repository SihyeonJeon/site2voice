# VOICE.md

Source: `https://hypebeast.com/`

Use this file to keep AI-generated pages, docs, and UI copy aligned with the observed website voice.

## Voice Summary

- Overall tone: **explanatory**.
- Sentence shape: about **47.3 words** per sentence.
- Main vocabulary: `브랜드`, `댓글들`, `컬렉션`, `디자인`, `라이프스타일`, `hypebeast`, `한국어`, `버튼을`, `클릭합니다`, `페이지를`, `아래의`, `hypebae`.
- Common CTAs: `더 보기`.
- Navigation labels: `Hypebeast`, `Hypebae`, `Hypemaps`, `HBX`, `회원 가입`, `로그인`, `한국어`, `Deutsch`, `English`, `Filipino`.

## Style Fingerprint

- Heading shape: about **7.3 words** per heading.
- Paragraph rhythm: about **7.8 words** per paragraph sample.
- CTA shape: about **2 words** per CTA.
- CTA verbs: `더`.
- Lexical variety: **0.349** type-token ratio.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Reuse the observed vocabulary, but do not copy full marketing paragraphs.
- Keep headings specific; avoid generic labels like `Powerful features` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Output Contract

- Keep average sentence length between **35.5 and 59.1 words**.
- Keep headings near **7.3 words**; avoid generic one-word section labels unless the source uses them.
- Keep paragraph blocks near **7.8 words**.
- Keep CTAs near **2.0 words** and start them with: `더`.
- Use at least **4** of these terms where natural: `브랜드`, `댓글들`, `컬렉션`, `디자인`, `라이프스타일`, `hypebeast`, `한국어`, `버튼을`, `클릭합니다`, `페이지를`, `아래의`, `hypebae`.
- Keep the first screen structure close to: specific headline, short proof/value sentence, one or two action CTAs.
- If writing a candidate file, run:
  `site2voice bench https://hypebeast.com/ path/to/candidate.md --strict`
- Revise until overall >= **75**, copy safety >= **85**, and claim safety >= **75**.

## Evidence

| Signal | Value |
| --- | --- |
| Words | 993 |
| Sentences | 21 |
| Headings | 12 |
| CTA candidates | 1 |

## Do / Don't

- Do: write concise, outcome-first copy using the observed verbs and nouns.
- Do: keep CTAs short and action-led.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
