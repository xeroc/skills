---
name: tg-meeting-notes
description: Harvest substantive content from Fabian's Telegram (via the `tg` CLI) into the Obsidian vault at ~/.obsidian as meeting notes and people notes, incrementally via a watermark date. Use when the user says "sync/harvest/extract Telegram", "create meeting notes from Telegram/chats", "update meeting notes from TG", "tg prime + extract", or asks to persist Telegram conversations worth keeping. Also covers updating the extraction watermark state file and the vault people map.
---

# Telegram → Vault Meeting Notes

Incremental pipeline: read recent non-archived Telegram chats → create Meeting.md /
People.md notes in the vault → update people-map → advance the watermark.

## State file (read FIRST, update LAST)

`~/.obsidian/00-09.System/04.Context/04.11 Current State/tg-extraction.md`

Contains `last_completed_run: <YYYY-MM-DD>` plus per-run history. Next run processes
only chats whose last message date is **> last_completed_run**.

## Workflow

1. **Watermark**: read the state file. Default baseline if missing: today minus ~9 months
   (one Breakpoint cycle); confirm with the user before a cold full sweep.
2. **Inventory**: `tg prime`, then `tg chats > /tmp/tg_chats.json`. Filter:
   `archived == false` AND `last_message.date > <watermark>`. Sort by date desc.
3. **Prepare jobs**: run `scripts/prepare-jobs.sh <watermark-date> [job-count]` — emits
   `/tmp/tg_jobs/job_NN` (TSV: id, type, title, last_active, unread) and
   `/tmp/tg_jobs/usernames.tsv` (user_id → @username from `tg contacts`).
4. **Dispatch subagents** (max 10, one per job file, single `tasks[]` batch). Each gets:
   - full pointer to `references/extraction-rules.md` (the complete instruction set —
     templates, selection criteria, report format)
   - its job file path
   - the current list of existing people notes (from `ls ~/.obsidian/20-29.Business/21.People/`)
   - Fabian's sender_id: **13109052** (@xeroc)
5. **Verify** (parent, after all agents finish):
   - Python bytewise wikilink check over all files in `52.Meetings/` + `21.People/`
     (resolve `[[X]]` against full rel path OR basename, NFC-normalized). Unresolved links
     in files created this run = bug; in pre-2026 files = pre-existing, leave them.
   - Name-collision check: two agents can create the same first-name person file for two
     different humans (happened with "Steve": crypto-payments vs Triton). For every person
     file created this run, grep the new meeting notes that link it and confirm the context
     is one consistent person; if conflated, split into `Name (Org).md` and relink.
   - Frontmatter lint on new people files: keys company/location/title/email/telegram/x/
     website/aliases/type present; `telegram:` bare `@handle`; `x:` full `https://x.com/handle`
     URL (vault convention); NO quoted values; one key per line. Fix line-based, never with
     a `\s*` regex that can span newlines.
6. **Update people map**: merge new people into the Business Contacts table in
   `~/.obsidian/00-09.System/09.Maps/09.11 Maps & Indexes/people-map.md` (keep alphabetical,
   bump `updated` + footer date). Skip rows already present.
7. **Advance watermark**: append a run row to the state file's history table and set
   `last_completed_run:` to today (the date of the newest message read, i.e. today's run date).

## Hard rules

- `tg` reads are safe; NEVER run tg write commands (move/archive/send) — the tg skill
  requires explicit human confirmation for those.
- Subagents create NEW files only, in `50-59.Time/52.Meetings/` and `20-29.Business/21.People/`.
  They must not modify any existing vault file.
- The vault is a git repo: if the parent accidentally modifies pre-existing files
  (e.g. a botched lint), `git diff` to prove the change is yours, then `git checkout --` it.
  Never revert the user's own uncommitted edits.
- riprap launch-boost contacts (first-name/handle-only) stay in
  `20-29.Business/28.Other projects/28.08-Riprap/Breakpoint/boost-network.md` — no people notes.
- Read enough messages per chat to cover back to the watermark (`--last 50` default,
  `--last 100` for high-signal business chats; transient sqlite "database is locked"
  errors from `tg read` resolve on retry — serialize reads if they repeat).
