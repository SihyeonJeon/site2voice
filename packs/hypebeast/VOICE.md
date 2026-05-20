# VOICE.md

Source: `https://hypebeast.com/`

Use this file to keep AI-generated pages, docs, and UI copy aligned with the observed website voice.

## Voice Summary

- Overall tone: **explanatory**.
- Sentence shape: about **47.3 words** per sentence.
- Content policy: this file captures rhythm and structure, not source nouns.

## Style Fingerprint

- Heading shape: about **7.3 words** per heading.
- Paragraph rhythm: about **7.8 words** per paragraph sample.
- CTA shape: about **2 words** per CTA.
- CTA verbs: `보기`.
- Navigation label shape: about **1.3 words** per label.
- Lexical variety: **0.349** type-token ratio.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Reuse rhythm, CTA shape, and information order; bring your own product nouns.
- Do not import source-specific topics, product names, market claims, or domain nouns.
- Keep headings specific; avoid generic labels like `<generic feature label>` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Output Contract

- Keep average sentence length between **35.5 and 59.1 words**.
- Keep headings near **7.3 words**; avoid generic one-word section labels unless the source uses them.
- Keep paragraph blocks near **7.8 words**.
- Keep CTAs near **2.0 words** and start them with: `보기`.
- Content boundary: Use only the new project's nouns. Do not transfer source-specific terms from the reference site.
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

- Do: write concise, outcome-first copy using the observed rhythm and CTA verbs.
- Do: keep CTAs short and action-led.
- Don't: transfer source-specific nouns into an unrelated project.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
