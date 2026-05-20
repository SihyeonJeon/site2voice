# VOICE.md

Source: `https://www.anthropic.com/`

Use this file to keep AI-generated pages, docs, and UI copy aligned with the observed website voice.

## Voice Summary

- Overall tone: **explanatory, technical, trust-forward**.
- Sentence shape: about **34.3 words** per sentence.
- Main vocabulary: `claude`, `anthropic`, `security`, `policy`, `code`, `log`, `responsible`, `download`, `app`, `constitution`, `scaling`, `compliance`.
- Common CTAs: `Try Claude`, `Contact sales`, `Download app`.
- Navigation labels: `Skip to main content`, `Skip to footer`, `Research`, `Economic Futures`, `Claude's Constitution`, `Transparency`, `Responsible Scaling Policy`, `Security and compliance`, `Anthropic Academy`, `Tutorials`.

## Style Fingerprint

- Heading shape: about **5.2 words** per heading.
- Paragraph rhythm: about **14.8 words** per paragraph sample.
- CTA shape: about **2 words** per CTA.
- CTA verbs: `try`, `contact`, `download`.
- Lexical variety: **0.233** type-token ratio.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Reuse the observed vocabulary, but do not copy full marketing paragraphs.
- Keep headings specific; avoid generic labels like `Powerful features` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Evidence

| Signal | Value |
| --- | --- |
| Words | 1064 |
| Sentences | 31 |
| Headings | 12 |
| CTA candidates | 3 |

## Do / Don't

- Do: write concise, outcome-first copy using the observed verbs and nouns.
- Do: keep CTAs short and action-led.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
