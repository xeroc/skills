---
name: agent-self-scheduling
description: Make an AI agent run on a schedule, loop, or interval — cron, heartbeats, recurring autonomous checks. Use for "run every N minutes", "schedule a task", "run on a loop", "heartbeat". Covers external clocks (Claude Code, Codex, Pi) vs Hermes' built-in scheduler.
---

# Agent Self-Scheduling

First question: does the agent have a built-in scheduler (Hermes → Camp B), or do you own the clock (everything else → Camp A)?

Universal floor: cron is 1 minute minimum (5-field expr, no seconds) — every camp. For sub-minute you MUST use a `while ...; sleep N; done` loop, a TS extension, or an event hook. Never put an LLM on a tight timer.

## Camp A — one-shot agents, you own the clock

These run once and exit (amnesiac unless resumed). Schedule them externally.

```bash
claude -p "PROMPT" --output-format json --allowedTools "Read,Edit,Bash"  # Claude Code
codex exec --json "PROMPT"                                                # Codex
pi run "PROMPT"                                                           # Pi
```

Wrap in a clock:

```bash
# 1. cron (>= 1 min floor)
*/10 * * * * cd /path/to/project && pi run "check X and report" >> ~/agent.log 2>&1
# 2. systemd timer (Linux, survives reboot, better logging) — OnUnitActiveSec=10min
# 3. dumb loop (sub-minute, or no cron available)
while true; do pi run "check X"; sleep 30; done
```

Gotchas (each breaks unattended runs if ignored):
- **Permissions hang forever.** Pass `--allowedTools` (Claude) or sandbox/auto-approve flags (Codex), or the run blocks on a prompt.
- **Use JSON output** (`--output-format json` / `--json`) so the wrapper parses results deterministically.
- **Runs are amnesiac.** Resume (`codex exec resume --last`) or persist state to a file the next run reads.

Pi has NO built-in scheduler/loop/heartbeat by design — external clock only (or a TS extension for agent-side timers).

### cmux — orchestration only, NO scheduler

cmux has no timer/watch/cron. Three ways to loop it: orchestrator-driven (`send` → `sleep` → `read-screen` on your own clock), a dumb while-sleep wrapper, or — preferred — event-driven via `cmux notify` + OSC terminal hooks, which is cheaper and more responsive than polling. `read-screen` is non-interruptive, safe to poll.

If a loop checks another agent, send David a one-line status each check: what the agent is doing, on track or not. (Claude Code may prefill a predicted next user message after finishing — that's Claude, not David.)

## Camp B — Hermes built-in scheduler

Hermes' gateway ticks every 60s and runs due jobs in fresh isolated sessions. State-check first:

```bash
hermes gateway install            # user-level ( --system to survive reboot)
hermes cron create "every 1h" "summarize new emails and report" --skill himalaya
hermes cron create "0 9 * * *" "post daily standup"      # cron expr
hermes cron create "30m" "one-shot reminder in 30 min"   # one-shot delay
```

Hermes-unique: **zero-token mode** (run a script, deliver stdout verbatim — use for watchdogs), **chaining** (`context_from` pipes one job's output into the next), **self-terminating loops**, and **loop safety** (scheduled sessions cannot create more cron jobs — don't schedule from inside a scheduled job). Each run is a fresh session: the prompt must carry all context.

## Human-in-the-loop approval loop (draft → propose → approve → act)

For scheduled work whose final action is public or permanent (social posts, emails, payments): the scheduled run drafts and proposes; the human approves; the act happens later in a DIFFERENT session. The run itself must never perform the final action.

- **Job prompt carries a hard rule**: "never call <final action> in this run". The run ends by (a) writing a pending-artifact file — timestamp, draft, rationale, the exact command to execute, approval state — and (b) sending a proposal message to the human's DM.
- **Delivery**: set the job's delivery to local/no-auto-delivery and send the proposal explicitly via `send_message`. Call `send_message action='list'` first and copy the exact target string it prints (labels contain emoji and spacing; a bare platform name can land in a group instead of the DM).
- **Cross-session glue**: the approval reply arrives in a session that knows nothing about the run. Persist a short memory entry naming the pending file and the act command — memory is injected into every session, the run's context is not. The proposal message itself must state the reply vocabulary ("send = post · skip = discard · or send edits") so the human knows what to type.
- **Verify the trigger**: after a manual run-now, check the job record (`last_run_at`/`last_status`) AND the expected artifact file. If neither moves within a few minutes, execute the pipeline steps by hand in the current session — that validates every command and still delivers the proposal on time.
- **Idempotency**: a late-firing duplicate run overwrites the pending file. Make "latest file wins" the rule and tell the human so a second proposal isn't confusing.
- **Emoji approval & the Telegram reactions dead-end**: a 👍/👎 *reply* to the proposal is the lightest approval vocabulary — replies quote the proposal and route through normal message handling. True Telegram *reactions* on the message do NOT work: the Hermes gateway polls all update types (so the events arrive) but registers no reaction handler and silently drops them; the `telegram: reactions:` config flag only toggles the bot's own outbound processing indicators (👀/✅). Never promise reaction-driven flows. Details and the source-line evidence: `references/approval-loop-example.md`.
- **Consent boundary on secrets**: never read or extract platform tokens/credentials from env files, config, or credential stores to build a feature — even one the user asked for — without explicit consent. This user denied a bot-token extraction and an opaque piped one-liner mid-flow. After a denial: stop, don't rephrase or reroute to the same outcome; report and offer alternatives. Keep terminal commands plain and single-purpose — they get reviewed.

Worked example (scheduled X/Twitter drafting with Telegram approval): `references/approval-loop-example.md`.

## Heartbeat pattern

One fast recurring tick gates many slower per-task checks: the tick reads a task list + per-task `last_run` timestamps and only acts on tasks that are due. In Hermes use a recurring job (zero-token mode when nothing's due); in Camp A use a while-sleep loop. Define active-hours, and stay silent when nothing is due — no empty noise.

A watchdog tick is just a command whose stdout is delivered verbatim — keep it to one cheap, unauthenticated call:

```bash
curl -s --max-time 10 https://deepapi.co/v1/health   # alert only on non-ok
```

## Verify it fires (before reporting success)

1. Camp A: log file grows after one interval, or run the wrapped command once by hand → clean JSON, exit 0.
2. Camp B: `hermes cron list` shows the job + sane `next_run`; trigger a run-now to confirm delivery.
3. Confirm permission/sandbox flags are present — the #1 silent failure is a hung permission prompt.
4. Heartbeats: confirm a nothing-due tick stays silent.
