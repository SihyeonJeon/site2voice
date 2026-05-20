# VOICE.md

Source: `https://vercel.com/`

Use this file to keep AI-generated pages, docs, and UI copy aligned with the observed website voice.

## Voice Summary

- Overall tone: **explanatory, action-oriented, technical, trust-forward**.
- Sentence shape: about **34.5 words** per sentence.
- Content policy: this file captures rhythm and structure, not source nouns.

## Style Fingerprint

- Heading shape: about **2.6 words** per heading.
- Paragraph rhythm: about **4.5 words** per paragraph sample.
- CTA shape: about **3.9 words** per CTA.
- CTA verbs: `build`, `see`, `join`, `sign`, `get`, `start`, `learn`.
- Navigation label shape: about **4.6 words** per label.
- Lexical variety: **0.171** type-token ratio.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Reuse rhythm, CTA shape, and information order; bring your own product nouns.
- Do not import source-specific topics, product names, market claims, or domain nouns.
- Keep headings specific; avoid generic labels like `<generic feature label>` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Output Contract

- Keep average sentence length between **25.9 and 43.1 words**.
- Keep headings near **2.6 words**; avoid generic one-word section labels unless the source uses them.
- Keep paragraph blocks near **4.5 words**.
- Keep CTAs near **3.9 words** and start them with: `build`, `see`, `join`, `sign`, `get`, `start`, `learn`.
- Content boundary: Use only the new project's nouns. Do not transfer source-specific terms from the reference site.
- Keep the first screen structure close to: specific headline, short proof/value sentence, one or two action CTAs.
- If writing a candidate file, run:
  `site2voice bench https://vercel.com/ path/to/candidate.md --strict`
- Revise until overall >= **75**, copy safety >= **85**, and claim safety >= **75**.

## Evidence

| Signal | Value |
| --- | --- |
| Words | 2033 |
| Sentences | 59 |
| Headings | 12 |
| CTA candidates | 11 |

## Do / Don't

- Do: write concise, outcome-first copy using the observed rhythm and CTA verbs.
- Do: keep CTAs short and action-led.
- Don't: transfer source-specific nouns into an unrelated project.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
