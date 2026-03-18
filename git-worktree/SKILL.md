---
name: git-worktree
description: This skill manages Git worktrees for isolated parallel development. It handles creating, listing, switching, and cleaning up worktrees with a simple interactive interface, following KISS principles.
---

## What are git worktrees?

**ELI5:** Normally, you can only work on one git branch at a time in a folder. Want to fix a bug while working on a feature? You have to stash changes, switch branches, then switch back. Git worktrees let you have multiple branches checked out at once in different folders - like having multiple copies of your project, each on a different branch.

**The Problem:** Everyone's using git worktrees wrong (or not at all):

- Constantly stashing/switching branches disrupts flow
- Running tests on main while working on features requires manual copying
- Reviewing PRs means stopping current work
- **Parallel AI agents on different branches?** Nearly impossible without worktrees

**Why people sleep on worktrees:** The DX is terrible. `git worktree add ../my-project-feature feature` is verbose, manual, and error-prone.

**Enter gtr:** Simple commands, AI tool integration, automatic setup, and built for modern parallel development workflows.

**Usage:**

```bash
# One-time setup (per repository)
git gtr config set gtr.editor.default nvim
git gtr config set gtr.ai.default opencode

# Daily workflow
git gtr new my-feature          # Create worktree folder: my-feature
git gtr new my-feature --editor # Create and open in editor
git gtr new my-feature --ai     # Create and start AI tool
git gtr new my-feature -e -a    # Create, open editor, then start AI
git gtr editor my-feature       # Open in nvim
git gtr ai my-feature           # Start opencode

# Run commands in worktree
git gtr run my-feature npm test # Run tests

# Navigate to worktree
gtr new my-feature --cd         # Create and cd (requires shell integration)
gtr cd                          # Interactive picker (requires fzf + shell integration)
gtr cd my-feature               # Requires shell integration (see below)
cd "$(git gtr go my-feature)"   # Alternative without shell integration

# List all worktrees
git gtr list

# Remove when done
git gtr rm my-feature

# Or remove all worktrees with merged PRs/MRs (requires gh or glab CLI)
git gtr clean --merged
```

## Why gtr?

While `git worktree` is powerful, it's verbose and manual. `git gtr` adds quality-of-life features for modern development:

| Task              | With `git worktree`                        | With `git gtr`                           |
| ----------------- | ------------------------------------------ | ---------------------------------------- |
| Create worktree   | `git worktree add ../repo-feature feature` | `git gtr new feature`                    |
| Create + open     | `git worktree add ... && cursor .`         | `git gtr new feature --editor`           |
| Open in editor    | `cd ../repo-feature && cursor .`           | `git gtr editor feature`                 |
| Start AI tool     | `cd ../repo-feature && claude`             | `git gtr ai feature`                     |
| Copy config files | Manual copy/paste                          | Auto-copy via `gtr.copy.include`         |
| Run build steps   | Manual `npm install && npm run build`      | Auto-run via `gtr.hook.postCreate`       |
| List worktrees    | `git worktree list` (shows paths)          | `git gtr list` (shows branches + status) |
| Clean up          | `git worktree remove ../repo-feature`      | `git gtr rm feature`                     |

**TL;DR:** `git gtr` wraps `git worktree` with quality-of-life features for modern development workflows (AI tools, editors, automation).

## Commands

Commands accept branch names to identify worktrees. Use `1` to reference the main repo.
Run `git gtr help` for full documentation.

### `git gtr new <branch> [options]`

Create a new git worktree. Folder is named after the branch.

```bash
git gtr new my-feature                                                                   # Creates folder: my-feature
git gtr new hotfix --from v1.2.3                                                         # Create from specific ref
git gtr new variant-1 --from-current                                                     # Create from current branch
git gtr new feature/auth                                                                 # Creates folder: feature-auth
git gtr new feature/implement-user-authentication-with-oauth2-integration --folder auth  # Custom folder name
git gtr new feature-auth --name backend --force                                          # Same branch, custom name
git gtr new my-feature --name descriptive-variant                                        # Optional: custom name without --force
```

**Options:**

- `--from <ref>`: Create from specific ref
- `--from-current`: Create from current branch (useful for parallel variant work)
- `--track <mode>`: Tracking mode (auto|remote|local|none)
- `--no-copy`: Skip file copying
- `--no-fetch`: Skip git fetch
- `--no-hooks`: Skip post-create hooks
- `--force`: Allow same branch in multiple worktrees (**requires --name or --folder**)
- `--name <suffix>`: Custom folder name suffix (optional, required with --force)
- `--folder <name>`: Custom folder name (replaces default, useful for long branch names)
- `--editor`, `-e`: Open in editor after creation
- `--ai`, `-a`: Start AI tool after creation
- `--yes`: Non-interactive mode

### `git gtr editor <branch> [--editor <name>]`

Open worktree in editor (uses `gtr.editor.default` or `--editor` flag).

```bash
git gtr editor my-feature                    # Uses configured editor
git gtr editor my-feature --editor vscode    # Override with vscode
```

### `git gtr ai <branch> [--ai <name>] [-- args...]`

Start AI coding tool (uses `gtr.ai.default` or `--ai` flag).

```bash
git gtr ai my-feature                      # Uses configured AI tool
git gtr ai my-feature --ai codex          # Override with different tool
git gtr ai my-feature -- --model gpt-4    # Pass arguments to tool
git gtr ai 1                              # Use AI in main repo
```

### `git gtr run <branch> <command...>`

Execute command in worktree directory.

```bash
git gtr run my-feature npm test             # Run tests
git gtr run my-feature npm run dev          # Start dev server
git gtr run feature-auth git status         # Run git commands
git gtr run 1 npm run build                 # Run in main repo
```

### `git gtr rm <branch>... [options]`

Remove worktree(s) by branch name.

```bash
git gtr rm my-feature                              # Remove one
git gtr rm feature-a feature-b                     # Remove multiple
git gtr rm my-feature --delete-branch --force      # Delete branch and force
```

**Options:** `--delete-branch`, `--force`, `--yes`

### `git gtr mv <old> <new> [--force] [--yes]`

Rename worktree directory and branch together. Aliases: `rename`

```bash
git gtr mv feature-wip feature-auth      # Rename worktree and branch
git gtr mv old-name new-name --force     # Force rename locked worktree
git gtr mv old-name new-name --yes       # Skip confirmation
```

**Options:** `--force`, `--yes`

**Note:** Only renames the local branch. Remote branch remains unchanged.

### `git gtr copy <target>... [options] [-- <pattern>...]`

Copy files from main repo to existing worktree(s). Useful for syncing env files after worktree creation.

```bash
git gtr copy my-feature                       # Uses gtr.copy.include patterns
git gtr copy my-feature -- ".env*"            # Explicit pattern
git gtr copy my-feature -- ".env*" "*.json"   # Multiple patterns
git gtr copy -a -- ".env*"                    # Copy to all worktrees
git gtr copy my-feature -n -- "**/.env*"      # Dry-run preview
```

**Options:**

- `-n, --dry-run`: Preview without copying
- `-a, --all`: Copy to all worktrees
- `--from <source>`: Copy from different worktree (default: main repo)

### `git gtr list [--porcelain]`

List all worktrees. Use `--porcelain` for machine-readable output.

### `git gtr config {get|set|add|unset|list} <key> [value] [--global]`

Manage configuration via git config.

```bash
git gtr config set gtr.editor.default cursor       # Set locally
git gtr config set gtr.ai.default claude --global  # Set globally
git gtr config get gtr.editor.default              # Get value
git gtr config list                                # List all gtr config
```

### `git gtr clean [options]`

Remove worktrees: clean up empty directories, or remove those with merged PRs/MRs.

```bash
git gtr clean                                  # Remove empty worktree directories and prune
git gtr clean --merged                         # Remove worktrees for merged PRs/MRs
git gtr clean --merged --dry-run               # Preview which worktrees would be removed
git gtr clean --merged --yes                   # Remove without confirmation prompts
```

**Options:**

- `--merged`: Remove worktrees whose branches have merged PRs/MRs (also deletes the branch)
- `--dry-run`, `-n`: Preview changes without removing
- `--yes`, `-y`: Non-interactive mode (skip confirmation prompts)

**Note:** The `--merged` mode auto-detects your hosting provider (GitHub or GitLab) from the `origin` remote URL and requires the corresponding CLI tool (`gh` or `glab`) to be installed and authenticated. For self-hosted instances, set the provider explicitly: `git gtr config set gtr.provider gitlab`.

### Other Commands

- `git gtr doctor` - Health check (verify git, editors, AI tools)
- `git gtr adapter` - List available editor & AI adapters
- `git gtr version` - Show version

## CRUCIAL: Remind the user to configure gtr

```bash
# Set your editor (antigravity, cursor, vscode, zed)
git gtr config set gtr.editor.default nvim

# Set your AI tool (aider, auggie, claude, codex, continue, copilot, cursor, gemini, opencode)
git gtr config set gtr.ai.default opencode

# Copy env files to new worktrees
git gtr config add gtr.copy.include "**/.env.example"

# Run setup after creating worktrees
git gtr config add gtr.hook.postCreate "npm install"

# Re-source environment after gtr cd or gtr new --cd (runs in current shell)
git gtr config add gtr.hook.postCd "source ./vars.sh"

# Disable color output (or use "always" to force it)
git gtr config set gtr.ui.color never
```
