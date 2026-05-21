# SITE.md

`SITE.md` is a reference-only page-structure profile for AI agents.

Use it when the task is not only "write in this tone", but "build a page that
has the right information architecture, section rhythm, and conversion path."

It is not a substitute for `DESIGN.md`. If both files are present, `DESIGN.md`
owns colors, typography, spacing, layout grid, components, motion, and imagery
style. `SITE.md` owns page structure only.

## What It Captures

- page archetype;
- information density;
- conversion pressure;
- navigation model;
- section order;
- section jobs;
- section-level copy recipes;
- content boundaries and anti-patterns.

## What It Does Not Capture

- colors;
- typography;
- screenshots;
- logos;
- component styling;
- source headings;
- raw CTAs;
- source vocabulary;
- product catalogs, pricing, or market claims.

## Domain Firewall

`SITE.md` must not make the new product inherit the reference site's business
category. The new project brief owns:

- product category;
- audience;
- domain nouns;
- examples;
- offer;
- proof;
- claims;
- imagery subject matter.

For cross-domain work, use the reference only for structure. A retail reference
can shape the pacing of an education website, but the output must stay
educational in nouns, proof, examples, and CTAs.

## Use

```bash
curl -L https://raw.githubusercontent.com/SihyeonJeon/site2voice/main/sites/stripe.md -o SITE.md
curl -L https://raw.githubusercontent.com/SihyeonJeon/site2voice/main/voices/stripe.md -o VOICE.md
```

Then give both files to your agent:

```text
Use @SITE.md for page structure and @VOICE.md for copy rhythm. Bring our own product nouns, facts, and claims.
```

## Why Numbers Exist

The public Markdown files are designed around structure and writing behavior,
not word-count mimicry. Numeric ranges remain in the measurement section and
JSON files only as drift checks for benchmarking. They help reject copy that
becomes too long, too generic, or too far from the reference rhythm.

## Schema

The machine-readable form is `site2voice.site.v1` and is documented in
[`schemas/site.schema.json`](../schemas/site.schema.json).
