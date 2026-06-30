---
name: commit
description: use when committing to a git repository. smart commit with bean context and conventional commit format
---

---

Generate a commit message based on staged changes and bean context.

## Step 1: Gather Context

```bash
# What's staged?
git diff --cached --stat
git diff --cached --name-only

# What branch are we on?
git branch --show-current

# Recent commits for style reference
git log --oneline -5

# Current bean context (if any in-progress)
beans list --status in-progress --json 2>/dev/null | head -5
```

## Step 2: Analyze Changes

Read the staged diff to understand what changed:

```bash
git diff --cached
```

Categorize the change:

- `feat` - new feature
- `fix` - bug fix
- `refactor` - code restructuring without behavior change
- `docs` - documentation only
- `test` - adding/fixing tests
- `chore` - maintenance, deps, config
- `perf` - performance improvement
- `style` - formatting, whitespace

If any files from ./beans/ are staged, use their content to provide context for
the commit message.

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

## Step 7: Execute (on confirmation)

Once user picks or provides message:

```bash
git commit -m "<message>"
```

If user says "1" or "option 1", use that option directly.

## Important Notes

- do NOT prefix the category in the subject line with an emoji. `pre-commit`
  will be automatically called and take care of this consistency!
