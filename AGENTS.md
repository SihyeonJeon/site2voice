# AGENTS.md

Use this project as a small, dependency-free CLI. Keep new features focused on
agent copy context, deterministic voice profiling, and benchmark gates.

Before finishing code changes:

```bash
make test
make bench-ci
python3 -m compileall -q src tests
git diff --check
```

Do not add an LLM dependency for core profiling. Prefer deterministic metrics
and fixtures that do not redistribute third-party prose.

