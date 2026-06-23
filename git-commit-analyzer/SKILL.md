---
name: git-commit-analyzer
description: Use when analyzing git commits between two references and producing a summary article of all changes
tags:
  - git
  - analysis
  - documentation
  - changelog
---

# git-commit-analyzer

Use when you need to analyze a range of git commits and produce a human-readable summary article of all changes between two points (commits, tags, or branches).

## When to Use

- Generating changelogs from commit history
- Creating "what changed" documentation for releases
- Reviewing code changes over a specific time period
- Preparing release notes from git history

## What It Does

1. Collects all commits between two git references (A and B)
2. For each commit, extracts:
   - Commit hash, author, timestamp
   - Full commit message
   - Files changed with diff statistics
   - Detailed diff content
3. Formats summaries for all commits
4. Calls `blog-writer` skill to produce a polished article

## Inputs

- `commit_a`: Starting commit reference (hash, tag, branch)
- `commit_b`: Ending commit reference (hash, tag, branch)
- `title`: (optional) Article title, defaults to "What Changed"
- `include_diff`: (optional) Whether to include full diffs, defaults to false

## Usage

```typescript
await skills_use({
  name: "git-commit-analyzer",
  context: "Analyze commits from v1.0.0 to v2.0.0 and create release notes",
});
```

Or trigger via slash command if configured.

## Implementation

```bash
# Get commit range
commits=$(git rev-list --reverse ${commit_a}..${commit_b})

# For each commit, collect details
for commit in $commits; do
  git show --stat --format=fuller $commit
  git show $commit --format=""
done

# Generate structured output for blog-writer
```

## Output Format

The skill produces structured data for blog-writer:

```markdown
## Commit Summary: [hash]

**Author**: [name] <[email]>
**Date**: [date]
**Message**: [commit message]

**Files Changed**: [N]
```

[FULL_DIFF_CONTENT]

```

---
```

## Examples

**Analyze releases:**

```
commit_a: v1.5.0
commit_b: v2.0.0
title: Release 2.0.0 Changelog
```

**Review feature branch:**

```
commit_a: main
commit_b: feature/new-api
title: API Changes Review
```

**Audit security fixes:**

```
commit_a: v1.2.0
commit_b: v1.2.5
include_diff: true
```

## Large-Diff Thematic Analysis (alternative workflow)

For large commit ranges (20+ commits, many files), per-commit iteration produces noisy, repetitive output. Use this grouped approach instead.

### Workflow

1. **Commit overview**: `git log --oneline A..B -- <path>` — get the commit list and count at a glance
2. **File-level stat**: `git diff --stat A..B -- <path>` — see which files changed and by how much
3. **Grouped file diffs**: Run targeted `git diff A..B -- <file1> <file2> ...` in parallel batches, grouping files by concern area (e.g., instructions/, controllers/, state/, math/, config/). For diffs over ~500 lines, pipe through `head -N` on first read, then re-read specific sections if needed.
4. **Thematic synthesis**: Categorize findings into themes (branding, fee changes, safety rails, new features, refactors, bugfixes). For each theme, note what changed, why (from commit messages or code comments), and the behavioral impact.

### Output format

```markdown
# <Component> Changes since <ref>

N commits, M files, ~X lines changed. One-line summary.

## 1. Theme Name
- Bullet points of specific changes
- File references where relevant

## 2. Theme Name
...

## N. Minor / Cleanup
- Gas optimizations, logging changes, etc.

---
**Summary:** One paragraph capturing the arc of changes.
```

### When to use this vs per-commit

| Scenario | Use |
|---|---|
| Release notes, changelogs, blog articles | Per-commit workflow (original) |
| "What changed in this directory since X?" | Thematic workflow (this section) |
| Code review for a specific PR (1-10 commits) | Per-commit workflow (original) |
| Large fork/modification audit (20+ commits) | Thematic workflow (this section) |

### Pitfalls

- Don't skip the `--stat` step — it reveals which files deserve deep reads vs skimming
- For diffs over 800 lines in a single file, read in sections (offset/limit or `head`/`tail`) rather than dumping the whole thing
- Commit messages in forks often contain the *rationale* for changes (e.g., "Mash: we trust the oracle fully") — mine these for the "why" in the report
- Group parallel `git diff` calls by concern area to keep the analysis organized from the start

## Notes

- Requires git repository with accessible commit history
- Large commit ranges may produce lengthy articles
- Use `include_diff: true` for detailed technical reviews
- Commits are processed in chronological order (oldest first)
- For path-scoped analysis, append `-- <path>` to all git commands
