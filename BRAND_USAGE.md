# Brand Usage

`site2voice` generates reference-only copy profiles from publicly visible
website text. It is built to help AI agents write less generic copy while
avoiding source prose, source nouns, and unsupported claims.

## What The Public Profiles Are

- Derived measurements of writing behavior: sentence rhythm, heading shape, CTA
  verb shape, paragraph rhythm, information order, and benchmark gates.
- Plain Markdown context files for AI coding and writing agents.
- Nominative references to public pages used for measurement.

## What They Are Not

- Official brand guidelines.
- Endorsements, partnerships, sponsorships, or affiliations.
- Permission to use trademarks, logos, screenshots, trade dress, proprietary
  product names, customer claims, or regulated claims.
- A license to impersonate a company, publication, person, or product.
- A collection of reusable source paragraphs or brand copy.

## Source Boundaries

Public `VOICE.md` files are generated without source paragraph samples, source
nouns, raw CTA labels, navigation labels, screenshots, logos, or brand assets.
They intentionally tell agents to bring new project nouns and avoid transferring
reference-specific topics, product names, market claims, and domain language.

`voice.json` files in the public packs are redacted for the same reason. They
retain derived metrics and the output contract, but omit raw source text arrays.

## User Responsibilities

When using a `VOICE.md` file:

- Use it as a writing contract, not as brand approval.
- Use only product names, claims, examples, and domain nouns that belong to your
  project or that you otherwise have rights to use.
- Do not present generated output as official copy from the reference source.
- Do not use the reference source's logo, screenshots, proprietary assets, or
  protected brand identity unless you have independent permission.
- Run `site2voice bench` when possible to check copy safety and claim safety.

## Takedown And Corrections

If a profile appears to include protected source copy, misleading affiliation
language, or an unsafe brand reference, open an issue with the affected file and
the specific concern. The preferred fix is to remove or further generalize the
affected profile rather than preserve questionable material.
