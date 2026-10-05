---
name: git-thread
---

---

name: git-changelog-thread
description: "Use when the user wants git commits turned into a public-facing Twitter/X thread — e.g. 'summarize these commits for Twitter', 'make a changelog thread', 'what should we announce from this release'. Reads commit history from the prompt context (a repo path, commit range, tag range, or pasted git log), extracts and categorizes the changes, then writes and posts back a ready-to-publish thread. Not for internal changelogs, release notes docs, or non-public audiences — those are a different deliverable."

---

## 1. Get the commits

Determine scope from what the user gave me, in this priority order:

1. An explicit commit range or tag range (`v1.2.0..v1.3.0`, `abc123..HEAD`).
2. A repo path/branch with no range → default to commits since the last tag; if no tags exist, default to the last 20 commits.
3. A pasted git log / commit list in the prompt → use it as-is, don't re-fetch.

Pull full commit data, not just subjects, so nothing gets miscategorized from a vague one-liner:

```
git log <range> --no-merges --pretty=format:'%h|%s|%b'
```

If the range is genuinely ambiguous (no repo, no range, no pasted log), ask one short clarifying question instead of guessing.

## 2. Extract

For each commit, capture: hash, subject line, and body (bodies often contain the real "why" that the subject line compresses away — use them for context, not for tweet text).

## 3. Categorize

Sort every commit into exactly one bucket. Use conventional-commit prefixes where present, and message content as fallback:

- **Major feature** — new capability, new product surface, breaking change, anything a user would notice unprompted. (`feat!`, `feat(...)` touching a core flow, "add", "introduce", "launch")
- **Minor feature** — small enhancement, quality-of-life addition, extends something that already existed. (`feat` that's incremental, "improve", "support for", "add option to")
- **Fix** — bug fixes that affected real usage. (`fix`)
- **Ignore — do not include in the thread**: `chore`, `ci`, `build`, `test`, `docs`, dependency bumps, refactors with no user-visible effect, formatting/lint commits, internal tooling, version bumps. If in doubt whether something is operational noise vs. a real fix, ask: "would a user notice this changed?" — no → ignore.

Drop anything that doesn't survive categorization. A thread with 3 real items beats one padded with noise.

## 4. Apply the rmslop skill

Apply the rmslop skill to whatever draft text comes out of this workflow before it's shown to the user.

## 5. Build the thread

Only major features, minor features, and fixes worth telling the public about make it in — skip anything too niche or technical for a general audience, even if it's a real change.

**Structure:**

- **Tweet 1 = the hook.** No "here's what's new" throat-clearing. Lead with the single most compelling change, a number, a question, or a before/after — something that stops the scroll. This tweet decides whether anyone reads tweet 2.
- One idea per tweet after that. Major features get their own tweet each; minor features and fixes can be grouped a few per tweet if there are many.
- Order by impact, not by commit order: biggest news first (right after the hook), fixes last.
- Last tweet = a close, not a fade-out: a one-line summary and a concrete CTA (try it, read the full changelog, reply with feedback — whatever fits; don't invent a link that wasn't given).

**Writing rules:**

- Every word earns its place — cut filler, cut hedging, cut "we're excited to announce."
- Active voice, concrete verbs, plain language over jargon. Translate technical commit-speak into what changed for the user, not how it was implemented.
- Emojis: used sparingly and only where they carry meaning (✅ for a fix, 🚀 for a launch, ⚡ for a speed win) — never one per line, never decorative.
- Keep each tweet comfortably under 280 characters so it never gets silently truncated.
- Number tweets (1/, 2/, 3/...) so the thread reads as one piece.
- No fabricated stats, dates, or links — only use what's actually in the commit data or was given by the user.

## 6. If there's too much to fit

If the real (non-ignored) changes don't fit a tight, engaging thread (roughly 5–9 tweets is the sweet spot; 25 is X's hard technical limit but engagement drops long before that), don't just cram everything in. Tell the user their options:

- **Cut, don't compress** — keep only the top 3–5 most public-interesting items; move the rest to a linked full changelog.
- **Split by theme** — one thread for major features, a separate lighter one for fixes/minor polish, posted on different days.
- **Go weekly/monthly digest** — batch smaller items into a recurring "this week's changes" thread instead of one giant release thread.
- **Pin a summary tweet** — one tweet with the full list as a quote-thread anchor, then expand only the top items into full tweets.

State which option would fit best given what was cut, rather than silently truncating.

## 7. Output

Respond with the finished thread directly in the chat, each tweet clearly numbered and separated, ready to copy. Don't create a file for this — it's meant to be read and copied, not archived.
