# Contributing

Useful contributions:

- better deterministic voice metrics;
- fixtures that are synthetic and safe to redistribute;
- docs for agent workflows;
- adapters for common public page structures;
- benchmark cases that catch copying or invented claims.

Run before opening a PR:

```bash
make test
make bench-ci
python3 -m compileall -q src tests
git diff --check
```

Please do not commit generated outputs from third-party sites unless they only
contain derived metrics and no source prose.

