---
name: setup-pre-commit
description: This skill sets up industry-standard pre-commit hooks using the **pre-commit** framework (Python-based) instead of Husky.
---

# Setup Pre-Commit Hooks

## Overview

This skill sets up industry-standard pre-commit hooks using the **pre-commit** framework (Python-based) instead of Husky. This is more flexible, supports multiple languages (Python, Rust, TypeScript, etc.), and is the recommended approach for modern monorepos.

## What This Sets Up

- **pre-commit** framework with best-practice hooks
- **Language-specific hooks** (TypeScript/JavaScript, Python, Rust, etc.)
- **Monorepo-aware** paths (apps/, packages/, etc.)
- **Formatting, linting, type checking, and testing** on commit
- **Security scanning** (secrets, credentials, etc.)

## Step 1: Detect Repository Structure

First, analyze the repo to determine:

- **Monorepo structure**: Check for `apps/`, `packages/`, `services/`, etc.
- **Languages used**: Check for `package.json` (TS/JS), `pyproject.toml`/`requirements.txt` (Python), `Cargo.toml` (Rust), `go.mod` (Go), etc.
- **Package manager**: Detect npm/pnpm/yarn/bun, pip/uv/poetry, cargo, etc.

## Step 2: Install pre-commit

```bash
# Install pre-commit (Python-based)
pip install pre-commit

# Or via package manager
brew install pre-commit  # macOS
apt install pre-commit   # Ubuntu/Debian

# Or install in the repo (if using Python)
uv add --dev pre-commit  # with uv
poetry add --dev pre-commit  # with poetry
```

## Step 3: Create `.pre-commit-config.yaml`

This is the main configuration file. Here's a comprehensive template for a modern monorepo:

```yaml
# .pre-commit-config.yaml
repos:
  # ===== GENERAL HOOKS =====
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
        args: ["--maxkb=1000"]
      - id: check-merge-conflict
      - id: detect-private-key
      - id: check-case-conflict
      - id: check-symlinks
      - id: check-json
      - id: check-toml

  # ===== SECURITY =====
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.2
    hooks:
      - id: gitleaks
        args: ["--verbose"]

  # ===== TYPESCRIPT/JAVASCRIPT =====
  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: v3.1.0
    hooks:
      - id: prettier
        files: \.(js|jsx|ts|tsx|json|css|scss|md|yaml|yml)$
        additional_dependencies: ["prettier@3.1.0"]

  - repo: local
    hooks:
      - id: typescript-typecheck
        name: TypeScript Type Check
        entry: npm run typecheck
        language: system
        files: \.(ts|tsx)$
        pass_filenames: false
        stages: [pre-commit]

      - id: eslint
        name: ESLint
        entry: npm run lint
        language: system
        files: \.(js|jsx|ts|tsx)$
        pass_filenames: false
        stages: [pre-commit]

      # Monorepo-specific: Run tests for changed packages
      - id: test-changed
        name: Test Changed Packages
        entry: |
          bash -c '
            CHANGED_PACKAGES=$(git diff --cached --name-only | grep -E "^(apps|packages)/" | cut -d/ -f1-2 | sort -u)
            if [ -n "$CHANGED_PACKAGES" ]; then
              for pkg in $CHANGED_PACKAGES; do
                if [ -f "$pkg/package.json" ]; then
                  echo "Running tests for $pkg"
                  (cd "$pkg" && npm test)
                fi
              done
            fi
          '
        language: system
        pass_filenames: false
        stages: [pre-commit]

  # ===== PYTHON =====
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.6
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
        files: \.py$
      - id: ruff-format
        files: \.py$

  - repo: https://github.com/RobertCraigie/pyright-python
    rev: v1.1.345
    hooks:
      - id: pyright
        files: \.py$
        additional_dependencies: [pydantic, pytest]

  # ===== RUST =====
  - repo: https://github.com/doublify/pre-commit-rust
    rev: v1.0
    hooks:
      - id: fmt
        files: \.rs$
      - id: clippy
        files: \.rs$
        args: [--, -D, warnings]

  # ===== GO =====
  - repo: https://github.com/golangci/golangci-lint
    rev: v1.55.2
    hooks:
      - id: golangci-lint
        files: \.go$
        args: [--fix]

  # ===== MARKDOWN =====
  - repo: https://github.com/igorshubovych/markdownlint-cli
    rev: v0.38.0
    hooks:
      - id: markdownlint
        files: \.md$
        args: [--fix]

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: trailing-whitespace
        exclude_types:
          - javascript
          - ts
      - id: check-executables-have-shebangs

  - repo: https://github.com/ljnsn/cz-conventional-gitmoji
    rev: v0.7.0
    hooks:
      - id: conventional-gitmoji

  - repo: local
    hooks:
      #     - id: no-repeated-whitespace
      #       name: No repeated spaces
      #       entry: '\S+\s{2,}'
      #       language: pygrep
      #       types: [text]
      #       exclude_types: [javascript, ts]
      #
      #     - id: no-bracket-links
      #       name: "Brackets should not be inside links [[link]](url) -> [[link](url)]"
      #       entry: '\]\]\('
      #       language: pygrep
      #       types: [markdown]
      #
      - id: no-http
        name: URLs must use HTTPS
        entry: "http:"
        language: pygrep
        types_or: [markdown, yaml]
        exclude: |
          (?x)^(
              .pre-commit-config.yaml|
              pnpm-lock.yaml
          )$

  ######################################
  # docs and other markdown files
  ######################################
  - repo: https://github.com/igorshubovych/markdownlint-cli
    rev: v0.45.0
    hooks:
      - id: markdownlint
        files: ".*.md"
        # MD013: line too long
        # MD033: no inline HTML
        # MD041: first line in a file should be a top-level heading
        args: [--fix, --disable, MD013, MD033, MD041, MD046, MD040, "--"]

  ######################################
  # frontend project
  ######################################
  - repo: https://github.com/pre-commit/mirrors-eslint
    rev: v9.37.0
    hooks:
      - id: eslint
        types: [file]
        args: [--fix, --config, app/eslint.config.js]
        files: ^app/.*\.(js|ts|tsx)$
        additional_dependencies:
          - eslint
          - eslint-plugin-react
          - typescript-eslint

  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: v4.0.0-alpha.8
    hooks:
      - id: prettier
        args: [--config, app/.prettierrc, --write] # edit files in-place
        files: ^app/.*
        additional_dependencies:
          - prettier
          - prettier-plugin-react
          - react

  # Contract project
  - repo: https://github.com/doublify/pre-commit-rust
    rev: v1.0
    hooks:
      - id: fmt
        files: ^programs/.*/.*.rs
        args: [--manifest-path=programs/tributary/Cargo.toml, --check, --]
      - id: cargo-check
        files: ^programs/
        args: [--manifest-path=programs/tributary/Cargo.toml, --]
```

## Step 4: Create Package-Specific Configs

### For TypeScript/JavaScript Monorepo

```json
// .prettierrc (root level)
{
  "useTabs": false,
  "tabWidth": 2,
  "printWidth": 100,
  "singleQuote": true,
  "trailingComma": "all",
  "semi": true,
  "arrowParens": "always"
}
```

```json
// .eslintrc.json (root level for monorepo)
{
  "root": true,
  "extends": ["eslint:recommended", "plugin:@typescript-eslint/recommended"],
  "parser": "@typescript-eslint/parser",
  "plugins": ["@typescript-eslint"],
  "ignorePatterns": ["dist", "build", "node_modules"]
}
```

### For Python

```toml
# pyproject.toml
[tool.ruff]
target-version = "py311"
line-length = 100

[tool.ruff.format]
quote-style = "single"
indent-style = "space"

[tool.pyright]
pythonVersion = "3.11"
typeCheckingMode = "strict"
```

### For Rust

```toml
# Cargo.toml (workspace root)
[workspace]
members = ["apps/*", "packages/*"]

[workspace.dependencies]
# ... shared dependencies
```

### All Repos

EVERY repo needs the follow pre-commit hooks:

```

```

- repo: <https://github.com/ljnsn/cz-conventional-gitmoji>
  rev: v0.7.0
  hooks:
  - id: conventional-gitmoji

## Step 5: Install the Git Hooks

```bash
# Install the hooks
pre-commit install

# (Optional) Install pre-push hooks
pre-commit install --hook-type pre-push

# Run against all files initially
pre-commit run --all-files
```

## Step 6: Add CI Integration

Create a GitHub Action workflow:

```yaml
# .github/workflows/pre-commit.yml
name: Pre-commit

on:
  pull_request:
  push:
    branches: [main]

jobs:
  pre-commit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - uses: pre-commit/action@v3.0.0
        with:
          extra_args: --all-files
```

## Step 7: Configuration for Monorepo-Specific Paths

If your monorepo has specific structures, add path-based configurations:

```yaml
# .pre-commit-config.yaml (add path exclusions)
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
        exclude: |
          (?x)^(
            apps/legacy/.*|
            packages/deprecated/.*
          )$
```

## Step 8: Testing the Setup

1. Stage some files:

   ```bash
   git add .
   ```

2. Test the hooks manually:

   ```bash
   pre-commit run
   ```

3. Make a test commit:

   ```bash
   git commit -m "chore: add pre-commit hooks"
   ```

## Migration from Husky

If the repo already has Husky:

1. Remove Husky dependencies:

   ```bash
   npm uninstall husky lint-staged
   ```

2. Remove `.husky/` directory

3. Follow the steps above to set up pre-commit

## Advanced: Custom Hooks

Add project-specific checks:

```yaml
# .pre-commit-config.yaml
- repo: local
  hooks:
    - id: check-commit-message
      name: Check Commit Message
      entry: ./.githooks/commit-msg-check.sh
      language: script
      stages: [commit-msg]

    - id: package-json-sort
      name: Sort package.json
      entry: npx sort-package-json
      language: system
      files: package\.json$
      pass_filenames: false
```

## Best Practices

1. **Keep hooks fast**: Run slow checks (type checking, tests) only on changed files
2. **Use caching**: Enable pre-commit caching for faster runs
3. **CI compatibility**: Run `pre-commit run --all-files` in CI
4. **Language-specific configs**: Keep configs in their respective directories
5. **Documentation**: Add `.pre-commit-config.yaml` comment explaining hooks

## Troubleshooting

| Issue                   | Solution                                                      |
| ----------------------- | ------------------------------------------------------------- |
| Hook not running        | Run `pre-commit install` again                                |
| Python version mismatch | Specify `default_language_version` in config                  |
| Files not matching      | Check `files:` regex patterns                                 |
| Too slow                | Use `stages: [pre-commit]` and local hooks for specific files |

## Commit Message

After setup, commit with:

```
chore: add pre-commit hooks

- Configured pre-commit framework with best-practice hooks
- Added language-specific formatters and linters
- Set up monorepo-aware path configurations
- Added security scanning (gitleaks)
- Configured CI workflow
```

---

This setup provides a robust, multi-language pre-commit system that scales well with monorepo growth and ensures code quality across all packages.
