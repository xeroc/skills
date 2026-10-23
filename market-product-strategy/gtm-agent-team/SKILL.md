---
name: gtm-agent-team
description: Build autonomous Python agent teams that automate go-to-market operations — signal collection, scoring, content drafting, and self-tuning reporting. Use when adapting external GTM playbooks for developer tools/protocols, building recurring GTM automation, or creating a "morning standup" system that finds and engages prospects on developer-native channels. Triggers on "GTM agent team", "autonomous outreach", "automated signal scanning", "go-to-market automation", "adapt GTM playbook", "prospector agent", "scanner agent", or when a user shares a GTM framework and wants it implemented.
metadata:
  hermes:
    tags: [agents, automation, go-to-market, python, cron, delegation]
    related_skills: [web-research, subagent-driven-development]
---

# GTM Agent Team

Build autonomous agent teams that automate go-to-market operations for developer tools and protocols. Each seat reads and writes to a shared memory store, runs on cron, and produces a "morning standup" the human reviews in 2 minutes.

## When to Use This Pattern

- Developer tools, SDKs, protocols, or APIs where the funnel is product-led (not sales-led)
- Bootstrap budget ($0 infrastructure, $5-20/month LLM tokens)
- Signals are on developer-native channels (GitHub, Twitter, Reddit, npm) not email/LinkedIn
- You found an external GTM playbook and want to adapt it

**One-shot vs. recurring:** If the job is a one-shot enrichment of N known items (CSV → researched notes) rather than a recurring autonomous system, use `web-research` (Mode B: bulk entity enrichment) instead — it fans batches through Hermes' own `delegate_task`.

## Critical Evaluation Framework

When a user shares an external GTM playbook/framework, evaluate it against the actual context BEFORE adopting:

1. **Channel fit**: Does the playbook assume email/LinkedIn? Developers don't respond to cold email. Replace with GitHub, Twitter, Reddit, Discord, npm.
2. **Funnel model**: Does it assume sales-led (email → demo → close)? Developer tools are product-led (discover → star repo → read docs → install SDK). Replace the funnel.
3. **Budget**: Does it assume $400/month tools (Overloop, etc.)? Bootstrap means $0 infrastructure. Use free APIs and CLI tools.
4. **Signals**: Does it track job postings and LinkedIn triggers? Replace with: project launches, technical questions, competitor usage, funding rounds.
5. **Seats**: Does it have a "researcher" for pre-call briefs? If there are no sales calls, replace with content generation and community monitoring.

**What usually transfers:** Shared memory architecture, two-tier scoring (LLM + heuristic), JSON-structured prompts, self-tuning weights, dry-run-by-default, cron-driven execution, "edit not operate" UX.

**What usually doesn't:** Channels, funnel model, budget assumptions, signal types, seat definitions.

## Architecture

```
gtm-team/
├── run.py                  # Morning standup orchestrator (cron entry point)
├── core/
│   ├── memory.py           # SQLite shared memory (single source of truth)
│   ├── models.py           # Data models (Signal, Account, Touch, ContentDraft, Weights)
│   ├── llm.py              # OpenAI-compatible LLM wrapper with heuristic fallback
│   └── adapters/           # Signal sources (github.py, twitter.py, reddit.py, npm.py)
├── team/
│   ├── scanner.py          # Seat 1: Signal collection + ICP judgment + response drafting
│   ├── content.py          # Seat 2: Content generation from top signals
│   └── reporter.py         # Seat 3: Stats, weight re-tuning, weekly report
├── prompts/                # LLM prompts as markdown files (judge, draft_*, report)
├── config/                 # ICP, sources, weights, team settings (YAML)
└── data/                   # SQLite DB + standup output
```

## Key Design Decisions

### 1. Shared SQLite Memory

One database, six tables: accounts, signals, touches, content, weights, outcomes. Every seat reads and writes through stable method names. No seat keeps its own notes.

Critical methods: `upsert_account()`, `add_signal()` (deduplicated), `get_unprocessed_signals()`, `mark_signal_processed()`, `log_touch()`, `get_last_touch()`, `days_since_last_touch()`, `add_content()`, `get_weights()` / `update_weights()`, `get_stats()`.

### 2. Two-Tier Scoring

Tier 1 (LLM): Send signal + ICP + account history to Claude/GPT at temperature 0. Get back `{score, why_now, play, rationale}`.

Tier 2 (heuristic fallback): Base 30-50 from bucket weight, +15 per keyword match (max +40), +10 competitor mention, +10 intent words. Always available, works offline.

Thresholds: `first_touch` >= 60, `follow_up` >= 40, below that = `skip`. The system saying "no" is part of the job.

### 3. Self-Tuning Weights

Every run, the reporter re-weights signal buckets by outcomes:
- Integration (SDK installed): 3x weight
- Meeting/reply: 2x / 1x
- Click: 0.3x
- Sent (no response): 0.1x

Normalized and floored at 5% so no bucket is suppressed. Only applied if max delta > 5% (prevents noise churn).

### 4. JSON-Structured Prompts

All prompts are plain markdown files with: ROLE, INPUT, RULES, OUTPUT (JSON only). The LLM returns JSON, parsed with fuzzy matching (handles code fences, extra text). Edit the files, don't touch the code.

### 5. Dry-Run Default

Nothing sends without `--no-dry-run`. Drafts are logged to memory, not published. Cron runs dry by default; the human approves before anything goes live.

### 6. Adapters With Offline Fallback

Every adapter (GitHub, Twitter, Reddit, npm) generates mock data when credentials are missing. The system runs end-to-end on first try with `python3 run.py --reset` — no API keys needed for initial testing.

## Signal Buckets for Developer Tools

| Bucket | What to watch | Example |
|--------|---------------|---------|
| `project_launch` | New project, hackathon entry, product launch | "Just launched our AI agent platform!" |
| `technical` | Developer asking how to solve X | "How do I implement recurring USDC payments?" |
| `competitor` | Using/integrating a competitor | "Helio's fees are eating into our margins" |
| `funding` | Raised a round or got a grant | "Closed our $2M seed round" |

## Free Adapter Stack

| Source | Tool | Auth | Notes |
|--------|------|------|-------|
| GitHub | `gh` CLI | `gh auth login` | Repo search, issue search, competitor tracking |
| Twitter | API v2 | Bearer token | Keyword search; expensive at scale |
| Reddit | Public JSON API | None | `https://reddit.com/r/{sub}/search.json` |
| npm | Registry API | None | Download stats, spike detection |

## Pitfalls

- **Don't use email/LinkedIn for developer outreach.** Developers ignore cold email. Use the channels they're already on.
- **Don't assume a sales-led funnel.** Developer tools convert through documentation, examples, and SDK quality, not sales calls.
- **Don't skip the heuristic fallback.** The LLM tier is better, but the heuristic tier lets the system work on day one with zero setup.
- **Calibrate scoring thresholds early.** If everything scores as "skip," lower thresholds or boost keyword/competitor/intent weights in the heuristic.
- **Don't generate content without guardrails.** Each content type needs explicit `must` and `never` rules in the prompt. Without them, the LLM produces generic marketing slop.
- **One content piece per type per run.** Prevents flooding the approval queue. The human's job is editorial, not bulk review.
- **7-day cooldown between touches on the same account.** Prevents spamming. Enforced in the scanner, not just the prompt.
- **Min-age window for follow-ups.** The sequencer should only chase accounts whose last touch is 3+ days old, not fresh ones.

## Build Sequence

1. **Phase 0**: Core modules (memory.py, models.py, llm.py) + config YAMLs + prompt markdown files
2. **Phase 1**: Adapters (github, twitter, reddit, npm) + scanner seat
3. **Phase 2**: Content seat (thread, blog, comparison generation)
4. **Phase 3**: Reporter seat (stats, weight tuning, weekly report) + run.py orchestrator
5. **Phase 4+**: Tracker (directory submissions), Community (Discord/Telegram), Delivery adapters (actually post content)

Test after Phase 3: `python3 run.py --reset` should produce a full standup with mock data.

## References

- `references/developer-protocol-gtm-adaptation.md` — Detailed comparison: what transfers from B2B SaaS GTM playbooks vs what needs replacing for developer tools
