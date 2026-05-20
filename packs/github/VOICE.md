# VOICE.md

Source: `https://github.com/`

Use this file to keep AI-generated pages, docs, and UI copy aligned with the observed website voice.

## Voice Summary

- Overall tone: **explanatory, action-oriented, technical, trust-forward**.
- Sentence shape: about **40.7 words** per sentence.
- Main vocabulary: `github`, `code`, `security`, `copilot`, `view`, `explore`, `support`, `features`, `customer`, `platform`, `manage`, `community`.
- Common CTAs: `Sign in`, `Create saved search`, `Sign up`, `Sign up for GitHub`, `Try GitHub Copilot`, `Explore GitHub Copilot`, `Explore GitHub Actions`, `Explore GitHub Codespaces`.
- Navigation labels: `Skip to content`, `Sign in`, `GitHub Models Manage and compare prompts`, `MCP Registry New Integrate external tools`, `Actions Automate any workflow`, `Codespaces Instant dev environments`, `Issues Plan and track work`, `Code Review Manage code changes`, `Why GitHub`, `Documentation`.

## Style Fingerprint

- Heading shape: about **5.3 words** per heading.
- Paragraph rhythm: about **12.4 words** per paragraph sample.
- CTA shape: about **3.2 words** per CTA.
- CTA verbs: `sign`, `create`, `try`, `explore`, `learn`.
- Lexical variety: **0.26** type-token ratio.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Reuse the observed vocabulary, but do not copy full marketing paragraphs.
- Keep headings specific; avoid generic labels like `Powerful features` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Output Contract

- Keep average sentence length between **30.5 and 50.9 words**.
- Keep headings near **5.3 words**; avoid generic one-word section labels unless the source uses them.
- Keep paragraph blocks near **12.4 words**.
- Keep CTAs near **3.2 words** and start them with: `sign`, `create`, `try`, `explore`, `learn`.
- Use at least **4** of these terms where natural: `github`, `code`, `security`, `copilot`, `view`, `explore`, `support`, `features`, `customer`, `platform`, `manage`, `community`.
- Keep the first screen structure close to: specific headline, short proof/value sentence, one or two action CTAs.
- If writing a candidate file, run:
  `site2voice bench https://github.com/ path/to/candidate.md --strict`
- Revise until overall >= **75**, copy safety >= **85**, and claim safety >= **75**.

## Evidence

| Signal | Value |
| --- | --- |
| Words | 1628 |
| Sentences | 40 |
| Headings | 12 |
| CTA candidates | 12 |

## Do / Don't

- Do: write concise, outcome-first copy using the observed verbs and nouns.
- Do: keep CTAs short and action-led.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
