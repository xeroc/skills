# Worked example: scheduled tweet drafting with human approval

Tributary pipeline (live since 2026-10-12): twice-daily drafts for the
@tributaryso X account, proposed to Fabian's Telegram DM, posted only on
explicit approval.

## Job configuration

- cronjob name `tributary-tweet-pipeline`, schedule `0 8,15 * * *`
  (08:00/15:00 local), deliver `local` (no auto-delivery).
- attached skills: `tributary`, `fabian-writing-style`,
  `simplified-technical-english` (user asked for a "simple-engineering"
  skill; this is the closest existing match — confirm substitution with
  the user).
- toolsets: terminal + file + messaging (send_message).

## Run steps (each scheduled session)

1. `x2llm prime`, then `x2llm search "recurring payments solana lang:en" --limit 15`
   (fallback query: streaming/subscriptions/payroll + solana). Extract themes,
   questions, misconceptions; ignore engagement bait.
2. Read `/home/xeroc/Tributary/tributary/PROJECT.md` (first ~150 lines) —
   current project reality beats old marketing claims. Never promise
   non-live features.
3. Draft ONE tweet ≤280 chars in Fabian's measured register
   (fabian-writing-style): project account = "we/it" voice, no hashtags,
   blank-line beats, numbers over adjectives, flat ending, ".." closer,
   max one emoji.
4. Overwrite `~/.hermes/tributary_pending_tweet.md`: ISO timestamp,
   `TWEET:` + exact text, `RATIONALE:`, `POST:` + exact command, approval
   state. Previous unapproved draft = discarded (say so in the proposal).
5. `send_message action='list'`, then send to the DM target containing
   "Fabian Schuh" and "(dm)". Message <120 words: draft in a quote block,
   one line why, then "Reply: send = post as @tributaryso · skip =
   discard · or send edits."
6. Hard rule: the scheduled run NEVER calls `x2llm post`/`x2llm like`.

## Approval session (different from the run)

Triggered by Fabian's Telegram reply ("send", "skip", or edits). The
session learns the procedure from the memory entry + pending file:

1. Read `~/.hermes/tributary_pending_tweet.md` (latest file wins).
2. "send" → run the `POST:` line verbatim: `x2llm -u tributaryso post "<text>"`.
   Edits → apply, re-confirm once, then post.
3. HTTP 226 "looks automated" → retry once, then offer manual paste.
   Auth errors (401/403, transaction-id expired) → ask for a fresh HAR
   capture + `x2llm import`.
4. "skip" → delete/annotate the pending file, no post.

## Multi-pipeline variant (live since 2026-10-13)

Same pattern, three parallel jobs — no shared state except memory:

- Accounts: @tributaryso (repo ~/Tributary/tributary), @riprapxyz
  (repo ~/Accord/riprap), @xer0c promoting Accord (repo ~/Accord/accord).
- Schedules staggered so proposals never pile up: 08:00/08:30/09:00 and
  15:00/15:30/16:00. One proposal in the DM at a time.
- One pending file per pipeline: `~/.hermes/{tributary,riprap,accord}_pending_tweet.md`.
- Per-pipeline approval keywords — "send tributary" / "send riprap" /
  "send accord" — because several pending files coexist and a bare
  "send" is ambiguous. Emoji reply without a quote → freshest pending
  file wins (compare timestamps).
- Reply-opportunity mode: the search step also hunts recent tweets worth
  REPLYING to (someone asking for exactly what the product does,
  complaining about the gap it fills). A proposal may be a reply: pending
  file records `REPLY_TO:` id + author, and the `POST:` command gains
  `--reply-to ID`. Reply etiquette per fabian-writing-style: match the
  parent's register, under 2 lines unless technical, pitch only when the
  parent is literally asking for what the product does.
- Project-specific constraints travel in the job prompt, sourced from
  each repo's PROJECT.md (e.g. riprap's two-layer messaging law; accord's
  "arbitration oracle, never 'decentralized court'/`trustless`" honesty
  rule). The cron prompt is the only context a fresh session gets — bake
  such rules into it, don't assume the skill carries them.

## Telegram reactions investigation (2026-10-12/13)

User asked to approve via emoji reaction ON the proposal message.
Findings from the gateway source
(`env/lib/python3.14/site-packages/gateway/platforms/telegram.py`):

- The bot polls `allowed_updates=Update.ALL_TYPES` → reaction events DO
  arrive at the gateway.
- Registered handlers: TEXT / COMMAND / LOCATION / MEDIA message handlers
  plus one `CallbackQueryHandler` (~line 1583). NO `MessageReactionHandler`
  → reaction updates are silently discarded. No session ever sees them.
- `config.yaml → telegram: reactions: false` is unrelated to incoming
  reactions. It toggles the bot's own OUTBOUND processing indicators
  (👀 while processing, final reaction on completion — `_set_reaction` /
  `_clear_reactions`, ~lines 5784-5860).
- Adopted workaround: emoji as REPLY TEXT (👍 = post, 👎 = discard).
  Travels the normal message route, quotes the proposal for routing, zero
  gateway changes. Proposal footer: "Reply 👍 = post · 👎 = discard · or
  reply with edits."
- Real reaction support would mean patching site-packages (register a
  MessageReactionHandler that injects "user reacted X to message Y" into
  the session) + gateway restart + re-applying after every hermes update.
  Offered with trade-offs; user deferred.
- Buttons: the CallbackQueryHandler exists (button presses ARE handled),
  but `send_message` is text-only — no keyboard attachment. Inline URL
  buttons (t.me deep-links prefilling "send riprap") were scoped but
  sending keyboards still requires the raw Bot API + bot token.
- `send_message` returns `chat_id` + `message_id`: if exact
  message→pipeline mapping is ever needed, record `TG_MSG_ID:` in the
  pending file. Quoted replies made it unnecessary here.

## Pitfalls seen in the wild

- Manual `cronjob action='run'` returned success but never registered
  (`last_run_at` stayed null, no artifact after ~3 min). Fix: ran the
  pipeline by hand in-session. Also warned the user a late duplicate run
  might fire and overwrite the pending file — latest file wins. (The
  delayed trigger DID fire ~1h later and produced a second proposal —
  the warning mattered.)
- `x2llm search "from:tributaryso"` returns empty (sparse project
  account not indexed by search). Not an error: fall back to the measured
  @xer0c register with project-account person swap. Never retry.
- Memory was at 98% capacity — adding the cross-session glue entry
  required compacting an existing entry first. Check usage before relying
  on memory for handoff. Multi-pipeline glue entry must name ALL pending
  files + approval keywords compactly.
- The scheduled run only proposes — the one time the full loop closed
  (draft → DM → approval → post → file annotated with tweet id), it did
  so entirely without the originating session. Verify posted tweets by id
  before reporting success; pending-file annotations are self-reports.
