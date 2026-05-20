# VOICE.md

Source: `https://www.figma.com/`

Use this file to keep AI-generated pages, docs, and UI copy aligned with the observed website voice.

## Voice Summary

- Overall tone: **explanatory, action-oriented, technical**.
- Sentence shape: about **57.2 words** per sentence.
- Main vocabulary: `figma`, `design`, `explore`, `code`, `make`, `prompt`, `anything`, `tools`, `sites`, `imagine`, `product`, `started`.
- Common CTAs: `AI Explore all Figma AI features`, `See all solutions`, `Events Learn best practices at virtual events`, `See all`, `Contact sales`, `Get started`, `Get started for free`, `Build`.
- Navigation labels: `Skip to main content`, `Dev Mode Translate designs into code`, `FigJam Collaborate with a digital whiteboard`, `Figma Slides Co-create presentations`, `AI Explore all Figma AI features`, `Design systems`, `Prototyping`, `UX design`, `Web design`, `Wireframing`.

## Style Fingerprint

- Heading shape: about **4.8 words** per heading.
- Paragraph rhythm: about **3.2 words** per paragraph sample.
- CTA shape: about **3.2 words** per CTA.
- CTA verbs: `ai`, `see`, `events`, `contact`, `get`, `build`, `explore`.
- Lexical variety: **0.227** type-token ratio.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Reuse the observed vocabulary, but do not copy full marketing paragraphs.
- Keep headings specific; avoid generic labels like `Powerful features` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Output Contract

- Keep average sentence length between **42.9 and 71.5 words**.
- Keep headings near **4.8 words**; avoid generic one-word section labels unless the source uses them.
- Keep paragraph blocks near **3.2 words**.
- Keep CTAs near **3.2 words** and start them with: `ai`, `see`, `events`, `contact`, `get`, `build`, `explore`.
- Use at least **4** of these terms where natural: `figma`, `design`, `explore`, `code`, `make`, `prompt`, `anything`, `tools`, `sites`, `imagine`, `product`, `started`.
- Keep the first screen structure close to: specific headline, short proof/value sentence, one or two action CTAs.
- If writing a candidate file, run:
  `site2voice bench https://www.figma.com/ path/to/candidate.md --strict`
- Revise until overall >= **75**, copy safety >= **85**, and claim safety >= **75**.

## Evidence

| Signal | Value |
| --- | --- |
| Words | 1544 |
| Sentences | 27 |
| Headings | 12 |
| CTA candidates | 12 |

## Do / Don't

- Do: write concise, outcome-first copy using the observed verbs and nouns.
- Do: keep CTAs short and action-led.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
