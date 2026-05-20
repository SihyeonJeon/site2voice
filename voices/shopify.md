# VOICE.md

Source: `https://www.shopify.com/`

Use this file to keep AI-generated pages, docs, and UI copy aligned with the observed website voice.

## Voice Summary

- Overall tone: **explanatory**.
- Sentence shape: about **22.1 words** per sentence.
- Main vocabulary: `english`, `shopify`, `espa`, `fran`, `ais`, `sidekick`, `상거래`, `com`, `deutsch`, `에이전트`, `dev`, `shop`.
- Common CTAs: `플랜 보기`, `Shopify 지원 센터`.
- Navigation labels: `콘텐츠로 건너뛰기`, `Sidekick 상거래에 최적화된 AI 어시스턴트를 만나보세요.`, `웹사이트 빌더`, `테마`, `도메인`, `고객 계정`, `Sidekick`, `온라인`, `AI 채팅`, `POS(Point of Sale)`.

## Style Fingerprint

- Heading shape: about **4.4 words** per heading.
- Paragraph rhythm: about **4.2 words** per paragraph sample.
- CTA shape: about **2.5 words** per CTA.
- CTA verbs: `플랜`, `shopify`.
- Lexical variety: **0.293** type-token ratio.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Reuse the observed vocabulary, but do not copy full marketing paragraphs.
- Keep headings specific; avoid generic labels like `Powerful features` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Output Contract

- Keep average sentence length between **16.6 and 27.6 words**.
- Keep headings near **4.4 words**; avoid generic one-word section labels unless the source uses them.
- Keep paragraph blocks near **4.2 words**.
- Keep CTAs near **2.5 words** and start them with: `플랜`, `shopify`.
- Use at least **4** of these terms where natural: `english`, `shopify`, `espa`, `fran`, `ais`, `sidekick`, `상거래`, `com`, `deutsch`, `에이전트`, `dev`, `shop`.
- Keep the first screen structure close to: specific headline, short proof/value sentence, one or two action CTAs.
- If writing a candidate file, run:
  `site2voice bench https://www.shopify.com/ path/to/candidate.md --strict`
- Revise until overall >= **75**, copy safety >= **85**, and claim safety >= **75**.

## Evidence

| Signal | Value |
| --- | --- |
| Words | 1699 |
| Sentences | 77 |
| Headings | 12 |
| CTA candidates | 2 |

## Do / Don't

- Do: write concise, outcome-first copy using the observed verbs and nouns.
- Do: keep CTAs short and action-led.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
