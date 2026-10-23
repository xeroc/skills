# Extraction Rules — Subagent Instruction Set

Hand this file verbatim (plus the job file path, existing-people list, and Fabian's
sender_id) to each extraction subagent. Replace `<WATERMARK>` where noted.

## Goal
Read recent Telegram conversations (non-archived chats, active after <WATERMARK>) and
persist the substantive ones into the Obsidian vault at `/home/xeroc/.obsidian` as
**meeting notes**, linking/creating **people notes**.

## Your job file
`/tmp/tg_jobs/job_NN` — TSV columns: `chat_id <TAB> type <TAB> title <TAB> last_active <TAB> unread`.
Process EVERY row. For each chat run (read-only, safe):

    tg read <chat_id> --last 50

If output errors, retry once. High-signal business chats (Tributary, riprap, ChainSquad,
MTNDAO, Superteam, Foundation) may use `--last 100`. Transient sqlite "database is locked"
errors resolve on retry.

**Fabian (the user) is sender_id 13109052** (@xeroc). Attribute his messages correctly.

## Telegram username lookup
`/tmp/tg_jobs/usernames.tsv` — TSV: `user_id <TAB> @username` (from contacts). User chats:
chat_id == user_id. Use for the `telegram:` frontmatter field of people notes.

## What is worth persisting (be selective — noise is the default)
CREATE a meeting note when a chat contains: decisions, commitments, action items,
deadlines/dates, money/contract terms, project status, contact-info exchanges, or
meaningful relationship beats (intros, referrals, offers).

SKIP (create nothing) when the chat is only: greetings/gm spam, engagement-farming,
bot/service notifications, broadcast channels without interaction, memes/links without
context, scam/spam. If in doubt, skip.

For group chats, only persist if there is a genuinely notable decision/event/status
involving Fabian or his projects (Tributary, riprap.xyz, ChainSquad, Tributary Foundation,
MTNDAO work, Superteam Germany). Generic community chatter → skip.

## Deliverable 1: Meeting notes
Create in `/home/xeroc/.obsidian/50-59.Time/52.Meetings/`, filename: `YYYY-MM-DD <Short Title>.md`
(date = the day the substantive exchange happened; spanning days → last substantive day).
Title pattern: `TG — <Person/Topic>`, e.g. `2026-09-17 TG — Billy attn.markets.md`.
Check for filename collisions first; never overwrite existing files.

Exact format (from `00-09.System/01.Templates/01.03 General/Meeting.md`, Templater resolved):

    ---
    date: YYYY-MM-DD
    type: meeting
    company: <company/project if evident, else empty>
    summary: "<one-line summary>"
    tags: [telegram]
    ---

    %% [[00-09.System/03.Navigation/03.11 MOCs/🗣 Meetings MOC]] %%

    ## 🧑‍🤝‍🧑 Attendees

    - [[Fabian Schuh]]
    - [[<Person>]] (only if a people file exists or you create it)

    ## 🕐 Agenda/Questions

    -

    ## 📝 Notes

    - (dense factual bullets; dates, numbers, links, quotes where load-bearing)

    ## 🗜️ Follow-Up Questions

    -

    ## 💥 Action points

    - [ ] <task> (owner)

Rules:
- English prose. Keep original German only in short quotes.
- Only `[[wikilink]]` files that exist. Everyone else: plain text name.
- `company:` only if evident from the chat. No fabrication — unsure name mapping →
  use the Telegram display name as plain text.
- Group chats: same format; attendees = Fabian + people with files; group name in title.

## Deliverable 2: People notes
Folder: `/home/xeroc/.obsidian/20-29.Business/21.People/`. Filename = real name
(`First Last.md`) if known; else cleaned display name (strip emojis and " | company"
suffixes → keep the distinctive part).

CREATE only when: substantive ongoing relationship (work, deal, collaboration, investor,
partner) AND no existing note. One-message cold pitches → no note (skip or meeting note only).

Exact format (from `00-09.System/01.Templates/01.03 General/People.md`, Templater resolved):

    ---
    company: <if evident, else empty>
    location:
    title: <e.g. "Founder, attn.markets" if evident>
    email:
    telegram: <@handle from usernames.tsv, else empty — NEVER quoted>
    x: <full URL https://x.com/handle if known, else empty — NEVER quoted>
    website:
    aliases: [<Telegram display name>]
    type: people
    ---

    %% [[00-09.System/03.Navigation/03.11 MOCs/👪 People MOC]] %%

    ## Notes

    - <who they are, relationship to Fabian, 1-3 dense bullets>

    ## Meetings

    ```dataview
    TABLE file.cday as Created, summary AS "Summary"
    FROM "50-59.Time/52.Meetings" where contains(file.outlinks, [[<FileTitle>]])
    SORT file.cday DESC
    ```

Replace `<FileTitle>` with the exact filename without `.md`. Keep the triple-backtick fence.

Frontmatter hygiene (a previous run got this wrong):
- One key per line; values unquoted; empty value = nothing after the colon.
- `telegram:` = `@handle`; `x:` = `https://x.com/handle` (existing-file convention).
- Frontmatter must open AND close with `---`.

riprap.xyz launch-boost contacts already live in
`20-29.Business/28.Other projects/28.08-Riprap/Breakpoint/boost-network.md` — no people notes.

## Hard constraints
- Do NOT modify any existing vault file. Only create new files in the two folders above.
- Do NOT touch: people-map.md, JDex, MOCs, daily notes, templates.
- Do NOT run tg write commands (move/archive/send). Reads only.
- Before writing a person file, re-check it doesn't already exist (another agent may have
  created it mid-run); if so, link it instead. If YOU notice the same display name clearly
  refers to two different humans, suffix disambiguation: `Name (Org).md`.
- If the same person appears in multiple of your chats, one person file, and fold the
  group-chat context into the most relevant meeting note (note it in your report).

## Report format (final message)
One line per chat: `<chat_id> <title> → SKIPPED (reason)` or `→ CREATED <filename>`
(+ `+ PERSON <filename>`). End with totals. Compact — it is all the parent sees.
