# Developer-Protocol GTM Adaptation

What transfers and what doesn't when adapting B2B SaaS GTM playbooks for developer tools, SDKs, and protocols.

## Source Playbook Pattern (B2B SaaS)

The "GTM team on Claude Code" pattern assumes:
- 5 seats: prospector, researcher, sequencer, recoverer, reporter
- Channels: email (Overloop AI), LinkedIn
- Signals: job postings, social engagement, company changes, funding
- Funnel: cold email → demo → close
- Budget: ~$400/month (Overloop + tokens)
- Schedule: 8am cron, Slack standup
- Memory: SQLite shared per-account records

## What Transfers (Architecture)

| Element | Why it works |
|---------|-------------|
| SQLite shared memory | One source of truth across seats — universal pattern |
| Two-tier scoring (LLM + heuristic) | Heuristic fallback enables day-one operation without API keys |
| JSON-structured prompts (ROLE/INPUT/RULES/OUTPUT) | Separates judgment from code; editable by non-engineers |
| Self-tuning weights | System improves without code changes; outcome-driven |
| Dry-run by default | Safe iteration; nothing sends without explicit approval |
| Cron-driven "morning standup" | Human reviews in 2 minutes; edits instead of operates |
| Signal buckets (4 types) | Concept transfers; the specific bucket definitions change |
| 7-day cooldown between touches | Universal anti-spam measure |

## What Must Be Replaced (Business Logic)

| Element | B2B SaaS Original | Developer Tool Replacement |
|---------|-------------------|---------------------------|
| Channels | Email, LinkedIn | GitHub, Twitter, Reddit, npm, Discord |
| Signal: job postings | Role opens/reposts | Repo created, hackathon entry |
| Signal: social | LinkedIn engagement | Twitter: "how do I..." questions |
| Signal: company | Stack changes | Competitor SDK download spikes |
| Signal: funding | Round/acquisition | Same (developers care about funded projects) |
| Funnel | Email → demo → close | Discover → star repo → docs → SDK install |
| Prospector seat | Watches job boards, LinkedIn | Scanner: GitHub search, Reddit, npm |
| Sequencer seat | Email follow-up cadences | Content: Twitter threads, blog posts |
| Researcher seat | Pre-call briefs | (Drop or replace with community monitoring) |
| Recoverer seat | No-show email recovery | (Drop — no calendar-based funnel) |
| Reporter seat | Sales pipeline metrics | Developer funnel metrics (integrations, not meetings) |
| Budget | $400/mo (Overloop + tokens) | $0 infrastructure, $5-20/mo tokens |
| Delivery | Overloop/Slack integration | Terminal, Telegram, or file output |

## Why Email/LinkedIn Fails for Developers

1. Developers don't check LinkedIn regularly
2. Cold email to developers gets filtered, ignored, or resent as mockery
3. Developers discover tools through: GitHub trending, Twitter/X, Reddit (r/programming, r/webdev, language-specific subs), Hacker News, Discord/Telegram communities, package managers
4. Developer trust is built through code quality, documentation, and technical depth — not sales sequences
5. A developer who stars your repo is 100x more qualified than someone who opened a cold email

## ICP Adaptation

B2B SaaS ICP typically defines:
- Company size, revenue, industry
- Job title (Head of RevOps, VP Engineering)
- Buying signals (budget cycles, org changes)

Developer tool ICP should define:
- Project type (dApp, CLI, API, protocol)
- Technical stack (language, framework, chain)
- Pain point (what they're building that your tool solves)
- Competitor usage (who they currently use)
- Keywords (for heuristic signal matching)

## Scoring Adaptation

B2B SaaS scoring values:
- Meeting booked = highest outcome
- Reply = medium
- Email opened = low

Developer tool scoring values:
- SDK installed / repo integrated = highest outcome
- Star/fork/watch = medium-high
- Reply/comment/question = medium
- Click/visit = low
- Message sent (no response) = baseline

## Content Adaptation

B2B SaaS content:
- Personalized cold emails (3-5 sentences)
- Follow-up sequences (4 touches over a week)
- LinkedIn connection requests

Developer tool content:
- Twitter threads (technical, with code examples)
- Blog posts (how-to guides, architectural comparisons)
- Reddit comments (genuine, helpful, non-promotional)
- GitHub issues/PRs (contributing to their project, mentioning your tool naturally)
- Documentation improvements

The key difference: developer content must have technical substance. A generic "saw you're working on X, have you tried Y?" without deep technical context will damage credibility.
