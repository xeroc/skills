# Jujutsu (jj) Reference

`.jj/` present. The working copy IS the current change `@` — there is no
staging area; every pending change is already part of `@` and is snapshotted
on the next jj command.

## Agent safety (non-negotiable)

- Always `--no-pager`
- Always `-m` or `--stdin` for the message. NEVER run bare `jj describe` /
  `jj new` / `jj commit` — they open an editor and hang the session

## Gather Context

```bash
# What's in the working-copy change?
jj --no-pager status
jj --no-pager diff --stat

# Does @ already have a description? (empty output = undescribed)
jj --no-pager log -r @ --no-graph -T 'description'

# Recent commits for style reference
jj --no-pager log --limit 5
```

## Analyze

```bash
jj --no-pager diff
```

The diff covers the ENTIRE change `@` (not just this session's edits) — the
message must match all of it.

## Describe vs New

| State of `@`       | Action                                                 |
| ------------------ | ------------------------------------------------------ |
| empty (no changes) | nothing to commit — tell the user, stop                |
| no description     | `jj describe -m "<message>"` then `jj new`             |
| already described  | `jj describe -m "<message>"` (overwrite) then `jj new` |

`jj describe` REPLACES the description. New working-copy changes amend into
`@` automatically, so when `@` was already described the old message no
longer covers the diff — always regenerate the message from the full
`jj diff`, never append.

## Execute (on confirmation)

```bash
# multi-line message (quoted delimiter keeps $, backticks, ! verbatim):
jj --no-pager describe --stdin <<'EOF'
<type>(<scope>): <subject>

<body>

[Refs: <bean-id>]
EOF

# one-liner:
jj --no-pager describe -m "<message>"

jj --no-pager new   # seal the change, fresh working copy
```

If user says "1" or "option 1", use that option directly.

Skip the `jj new` when the user wants to keep amending the same change.

## Notes

- Colocated (`.jj/` + `.git/`): mutate only via jj — never `git add` /
  `git commit` (desyncs them). Read-only git (`log`, `status`) is fine.
- Git hooks (pre-commit) do NOT run under jj — the no-emoji rule from
  SKILL.md must be kept manually.
- Verify afterwards: `jj --no-pager log --limit 3`
