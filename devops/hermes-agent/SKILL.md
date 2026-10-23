---
name: hermes-agent
description: >
  Hermes Agent CLI configuration, skills management, and tooling reference.
  Load this skill whenever the user asks about configuring, setting up,
  installing, enabling, disabling, modifying, or troubleshooting Hermes Agent
  itself — its CLI, config, models, providers, tools, skills, voice, gateway,
  plugins, or any feature.
triggers:
  - hermes config
  - hermes setup
  - hermes skills
  - hermes tools
  - install skill
  - enable skill
  - hermes cli
  - configure hermes
  - hermes-agent
  - update hermes
  - hermes doctor
---

# Hermes Agent CLI Reference

## Skills Management

### Available Subcommands

```
hermes skills {browse,search,install,inspect,list,check,update,audit,uninstall,reset,publish,snapshot,tap,config}
```

**PITFALL:** There is NO `reload` or `enable` subcommand. If the user asks to
"reload skills" or "enable a skill", the correct actions are:

| User asks | Correct command |
|---|---|
| "reload skills" | `hermes skills update` |
| "enable a skill" | Skills are auto-enabled when installed; just `hermes skills install <name>` |
| "list my skills" | `hermes skills list` |
| "find a skill" | `hermes skills search <term>` |
| "browse available" | `hermes skills browse` |

### Installing Skills

```bash
hermes skills install <name-or-identifier>
```

- Interactive confirmation required (y/N prompt). Pipe `yes` or `echo "y"` to automate.
- Security scan runs automatically; skills are quarantined to `.hub/quarantine/` before approval.
- Installed skills land in `~/.hermes/skills/<name>/`.

### Third-Party Taps

```bash
hermes skills tap add <owner/repo>
```

- Adds a GitHub repo as a skill source.
- Tap config stored at `~/.hermes/skills/.hub/taps.json`.
- After adding a tap, skills from that repo become discoverable via `search` and `browse`.

### Searching and Browsing

```bash
hermes skills search <term>     # Search across ALL sources (official, skills.sh, clawhub, taps)
hermes skills browse            # Paginated list of all available skills
hermes skills inspect <id>      # Preview a skill before installing
```

### Updating and Auditing

```bash
hermes skills update            # Check for updates to installed skills
hermes skills check             # Health check
hermes skills audit             # Security audit installed skills
```

## General CLI

### Key Commands

```
hermes config      # Interactive configuration (requires TTY, not pipeable)
hermes setup       # First-time setup wizard
hermes doctor      # Diagnose common issues
hermes status      # Show current configuration and status
hermes tools       # Manage toolsets
hermes update      # Update Hermes itself
hermes --version   # Show version
```

### Session Management

```
hermes chat                    # Start interactive chat
hermes -z "prompt"             # One-shot prompt
hermes --resume <session>      # Resume a session
hermes --continue [name]       # Continue last session
hermes sessions                # List sessions
```

### Cron Jobs

```
hermes cron                    # Manage scheduled jobs
```

## Configuration

Config is interactive (`hermes config` requires a TTY). For non-interactive
setup, edit config files directly:

- Main config: `~/.hermes/config.yaml` (or `.json`)
- Skills directory: `~/.hermes/skills/`
- Tap registry: `~/.hermes/skills/.hub/taps.json`

## Pitfalls

1. **`hermes skills config` is not pipeable.** It requires an interactive terminal.
   Use `hermes config` from the user's terminal directly, or edit config files.
2. **`hermes skills install` prompts for confirmation.** When running from a
   subagent or script, pipe `echo "y"` to stdin.
3. **Skill names from taps may differ from what the user expects.** After adding
   a tap, run `hermes skills search` to discover the actual skill names before
   attempting install.
4. **Skills are auto-enabled after install.** There is no separate enable/disable step.
