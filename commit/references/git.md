# Git Reference

Plain git repository (no `.jj/`). Stage-and-commit flow.

## Gather Context

```bash
# What's staged?
git diff --cached --stat
git diff --cached --name-only

# What branch are we on?
git branch --show-current

# Recent commits for style reference
git log --oneline -5
```

## Analyze

```bash
git diff --cached
```

## Execute (on confirmation)

```bash
# multi-line message (quoted delimiter keeps $, backticks, ! verbatim):
git commit -F - <<'EOF'
<type>(<scope>): <subject>

<body>

[Refs: <bean-id>]
EOF

# one-liner:
git commit -m "<message>"
```

If user says "1" or "option 1", use that option directly.

## Notes

- `pre-commit` hooks run automatically on `git commit` and take care of
  consistency (e.g. emoji prefixes) — never add emoji yourself.
