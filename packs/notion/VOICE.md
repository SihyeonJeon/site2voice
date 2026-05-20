# VOICE.md

Source: `https://www.notion.com/`

Use this file to keep AI-generated pages, docs, and UI copy aligned with the observed website voice.

## Voice Summary

- Overall tone: **balanced, action-oriented, technical, trust-forward**.
- Sentence shape: about **14.8 words** per sentence.
- Main vocabulary: `work`, `notion`, `agents`, `enterprise`, `knowledge`, `search`, `custom`, `own`, `over`, `tools`, `automate`, `answers`.
- Common CTAs: `See what’s new →`, `Request a demo`, `Get Notion free`, `See pricing plans →`, `Explore more →`.
- Navigation labels: `Notion Your AI workspace`, `Notion Calendar`, `Notion Mail`, `Notion AI AI tools for work`, `Agents Automate busywork`, `Enterprise Search Find answers instantly`, `Knowledge Base Centralize your knowledge`, `Docs Simple and powerful`, `Projects Manage any project`, `Connections Connect your apps`.

## Style Fingerprint

- Heading shape: about **2.7 words** per heading.
- Paragraph rhythm: about **9 words** per paragraph sample.
- CTA shape: about **3 words** per CTA.
- CTA verbs: `see`, `request`, `get`, `explore`.
- Lexical variety: **0.402** type-token ratio.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Reuse the observed vocabulary, but do not copy full marketing paragraphs.
- Keep headings specific; avoid generic labels like `Powerful features` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Output Contract

- Keep average sentence length between **11.1 and 18.5 words**.
- Keep headings near **2.7 words**; avoid generic one-word section labels unless the source uses them.
- Keep paragraph blocks near **9.0 words**.
- Keep CTAs near **3.0 words** and start them with: `see`, `request`, `get`, `explore`.
- Use at least **4** of these terms where natural: `work`, `notion`, `agents`, `enterprise`, `knowledge`, `search`, `custom`, `own`, `over`, `tools`, `automate`, `answers`.
- Keep the first screen structure close to: specific headline, short proof/value sentence, one or two action CTAs.
- If writing a candidate file, run:
  `site2voice bench https://www.notion.com/ path/to/candidate.md --strict`
- Revise until overall >= **75**, copy safety >= **85**, and claim safety >= **75**.

## Evidence

| Signal | Value |
| --- | --- |
| Words | 635 |
| Sentences | 43 |
| Headings | 12 |
| CTA candidates | 5 |

## Do / Don't

- Do: write concise, outcome-first copy using the observed verbs and nouns.
- Do: keep CTAs short and action-led.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
