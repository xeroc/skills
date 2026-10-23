---
name: obsidian-memory-pipeline
description: Three-tier memory pipeline using Obsidian vault as persistent memory backend. Routes content to the right tier, manages memory promotion, creates daily notes, and maintains vault hygiene.
version: 1.0
---

# Obsidian Memory Pipeline

Three-tier memory system connecting Hermes hot memory to Obsidian vault for persistent long-term context.

## Vault Location

Root: `~/.obsidian/`
JD structure with `00-09.System/` through `80-89.Attachments/`

## Tier System

### Tier 1 — Hot Memory (injected every turn)
- `~/.hermes/memories/MEMORY.md` — procedural knowledge, quirks, active facts
- `~/.hermes/memories/USER.md` — user profile, vault lookup map
- Max ~2,200 chars combined. When MEMORY.md hits ~67% (~1,500 chars), promote stable entries.

### Tier 2 — Vault Living Files (on-demand)
- `~/.obsidian/00-09.System/04.Context/now.md` — current operations, active projects
- `~/.obsidian/00-09.System/04.Context/04.14 preferences.md` — communication style, delivery rules
- `~/.obsidian/00-09.System/04.Context/04.15 environment.md` — hardware, services, known issues
- `~/.obsidian/00-09.System/09.Maps/people-map.md` — plain-text contact index
- `~/.obsidian/00-09.System/09.Maps/project-map.md` — plain-text project index

### Tier 3 — Daily Notes (searchable timeline)
- `~/.obsidian/50-59.Time/51.Journal/YYYY-MM-DD.md`
- Append-only. Sections: Tasks, Schedule, Log, Wins, Context.

## Content Routing

When user says "log it" or "save it":

1. **Operational events** (meetings, calls, decisions) → daily note `## Log`
   Format: `- HH:MM — description`
2. **System issues/fixes** → `50-59.Time/54.Issues/` (use Issue template from `01.Templates/`)
3. **Incidents** → `50-59.Time/53.Incidents/` (use Incident template from `01.Templates/`)
4. **New person** → `20-29.Business/21.People/` (use People template from `01.Templates/`)
5. **New meeting** → `50-59.Time/52.Meetings/` (use Meeting template from `01.Templates/`)
6. **New company** → `20-29.Business/20.Companies/` (use Company template from `01.Templates/`)
7. **Learned corrections/preferences** → Hot memory (or `04.14 preferences.md` if stable)
8. **Recurring workflows** → Save as Hermes skill in `~/.hermes/skills/`
9. **Unknown** → `70-79.Capture/71.Inbox/`

## Memory Promotion (Tier 1 → Tier 2)

When MEMORY.md hits ~1,500 chars:

1. Identify entries that are stable (won't change soon): environment configs, operational patterns, known failures
2. Move each to the appropriate vault living file:
   - Technical/setup facts → `04.15 environment.md`
   - Preference/communication facts → `04.14 preferences.md`
   - Project/operational facts → `now.md`
3. Replace the MEMORY.md entry with a one-line vault pointer if needed
4. Keep ephemeral entries (active bugs, recent corrections) in MEMORY.md

## Daily Note Procedure

When creating a daily note:

1. Check if `~/.obsidian/50-59.Time/51.Journal/YYYY-MM-DD.md` already exists
2. If not, use the Daily Notes template structure:
   ```markdown
   ---
   date: YYYY-MM-DD
   type: daily
   tags: [daily]
   ---
   ## Tasks
   ## Schedule
   ## Log
   ## Wins
   ## Context
   ```
3. If exists, append to the Log section
4. Use wiki-links: `[[20-29.Business/21.People/Name]]`

## Vault Search

- `qmd` indexes the vault as `obsidian-main-vault`
- Use `search_files` with `path=~/.obsidian/` for direct grep
- JDex at `00-09.System/00.00 JDex.md` is the master ID index

## Templates

All templates at `~/.obsidian/00-09.System/01.Templates/`:

| Template | Creates in |
|----------|-----------|
| `Daily Notes.md` | `50-59.Time/51.Journal/` |
| `Meeting.md` | `50-59.Time/52.Meetings/` |
| `People.md` | `20-29.Business/21.People/` |
| `Company.md` | `20-29.Business/20.Companies/` |
| `Issue.md` | `50-59.Time/54.Issues/` |
| `Incident.md` | `50-59.Time/53.Incidents/` |
| `Project.md` | `20-29.Business/` |

When creating programmatically (without Templater), use the JD folder paths and adapt frontmatter manually.

## Pitfalls

- Templates reference pre-JD paths like `/Extras/People/` — always use JD paths when creating programmatically
- Legacy emoji-based folders still exist; JD paths are canonical
- Track A identity files (`05.Identity/`) are read-only unless user explicitly asks
- Daily notes are append-only — never remove content
- Always register new JD IDs in `00.00 JDex.md` before creating files
- Hetzner blocks automated requests — avoid scraping
- Git sync runs at 10:00 UTC via `~/.local/bin/sync-obsidian.sh`; changes before then are local only
