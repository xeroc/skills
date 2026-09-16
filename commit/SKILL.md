---
name: commit
description: use when committing to a git or jujutsu (jj) repository. smart commit with bean context and conventional commit format. detects plain git vs jj (.jj) and follows the matching workflow
---

Generate a commit message based on pending changes and bean context. Message
construction is identical for git and jj — only context gathering and the
final execution differ.

## Step 1: Detect VCS & Gather Context

Check the repo root for a `.jj/` directory:

- `.jj/` present (even if colocated with `.git/`) → follow
  [references/jj.md](references/jj.md) — gather context with `jj` and never
  run mutating git commands
- only `.git/` → follow [references/git.md](references/git.md)

The reference file provides the exact commands for the pending diff, current
branch/change, recent commit style, and how to execute the commit (for jj:
when to use `jj describe` vs `jj new`).

Additionally check current bean context (both VCSs):

```bash
beans list --status in-progress --json 2>/dev/null | head -5
```

## Step 2: Analyze Changes

Read the pending diff (staged changes for git; working-copy change `@` for
jj — see the reference file for the command) and categorize the change:

- `feat` - new feature
- `fix` - bug fix
- `refactor` - code restructuring without behavior change
- `docs` - documentation only
- `test` - adding/fixing tests
- `chore` - maintenance, deps, config
- `perf` - performance improvement
- `style` - formatting, whitespace

If any files from ./beans/ are part of the change, use their content to
provide context for the commit message.

## Step 3: Identify Scope

From the changed files, determine scope:

- Single component/module → use that name
- Multiple related files → use parent directory/feature name
- Broad changes → omit scope

## Step 4: Check for Bean Reference

If there's an in-progress bean related to this work, include it:

```
feat(auth): add session refresh logic

Implements automatic token refresh before expiry.

Refs: <bean-id>
```

## Step 5: Generate Commit Message

Format:

```
<type>(<scope>): <short description>

<body - what and why, not how>

[Refs: <bean-id>]
```

Rules:

- Subject line ≤ 72 chars
- Imperative mood ("add" not "added")
- No period at end of subject
- Body explains WHY, not just WHAT
- Reference bean if applicable

### Example commit message

```
feat(auth): implement proactive JWT token refresh mechanism

- Add refresh check to auth middleware
- Create background refresh scheduler
- Handle refresh failures gracefully

Refs: <bean-id>
```

## Step 6: Execute (on confirmation)

Once the user picks or provides a message, execute with the VCS-specific
command from the reference file (git.md / jj.md).

If user says "1" or "option 1", use that option directly.

## Important Notes

- do NOT prefix the category in the subject line with an emoji — this applies
  to git and jj alike (plain git: `pre-commit` enforces it automatically;
  under jj hooks don't run, so keep it manually)
