# CI Usage

Use `site2voice bench` as a regression test for AI-written copy.

```bash
site2voice bench https://example.com docs/new-homepage.md --strict
```

`--strict` applies the default gates:

- overall score >= 75;
- copy safety >= 85;
- claim safety >= 75.

For custom thresholds:

```bash
site2voice bench https://example.com docs/new-homepage.md \
  --fail-under 80 \
  --min-copy-safety 90 \
  --min-claim-safety 90
```

Exit codes:

| Code | Meaning |
| --- | --- |
| 0 | Command succeeded and gates passed. |
| 1 | Input, fetch, parse, or write error. |
| 2 | Benchmark ran, but one or more gates failed. |

## GitHub Actions

```yaml
name: voice

on:
  pull_request:

jobs:
  copy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v6
        with:
          python-version: "3.13"
      - run: python -m pip install site2voice
      - run: site2voice bench https://example.com docs/homepage-copy.md --strict
```

