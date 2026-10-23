---
name: chaoscraft-tributary-context
description: "Project context for Fabian's active projects — Tributary, ChaosCraft, Allowly, Polycode. Use when working on these projects, researching competitors, or making decisions about them."
version: 1.0.0
triggers:
  - working on Tributary
  - working on ChaosCraft
  - working on Allowly
  - working on Polycode
  - tributary.so
  - chaoscraft.dev
  - allowly.app
---

# Fabian's Active Projects

## Tributary
- **What:** Non-custodial Solana payment protocol — automated recurring payments via token delegation
- **URL:** tributary.so
- **Program ID:** TRibg8W8zmPHQqWtyAD1rEBRXEdyU13Mu6qX1Sg42tJ
- **Repo:** ~/projects/Tributary/tributary/
- **Payment models:** Subscription, Milestone (escrow), Pay-as-you-go
- **Next phase:** Composable pull payments (CPI to whitelisted programs like Meteora DLMM, Jupiter swaps) + Lighthouse integration for programmable execution conditions
- **Architecture decision:** Composable policies should be a separate account type (not a new PolicyType variant) — follows Solana Foundation subscriptions pattern of separate typed accounts with common headers
- **Solana Foundation subscriptions reference:** subscriptions/ directory in repo, uses Pinocchio+Codama, Program ID De1egAFMkMWZSN5rvYXRj9CAdheBamobVNubTsi9avR44
- **x402:** HTTP 402 Payment Required implementation for web micropayments
- **Key docs:** PROJECT.md, METEORA.md, "Composable Pull Payments on Solana.md", AGENTS.md
- **Key insight:** C-SPL (Confidential SPL) could add privacy layer (from Breakpoint conference insight)

## ChaosCraft
- **What:** AI agent platform + 3D galaxy visualization of GitHub PR activity
- **URLs:** chaoscraft.dev (main), app.chaoscraft.dev (app interface)
- **Repos:** 
  - github.com/chainsquad/chaoscraft (frontend/visualization)
  - github.com/xeroc/chaoscraft (backend)
  - github.com/xeroc/polycode (AI agent framework, internal name "polycode")
- **Stack:** Next.js + Three.js for 3D galaxy, custom backend, GitHub OAuth
- **Features:** Galaxy stars = merged PRs, color-coded by file type, brightness by recency, size by impact. Forge component for feature building. Stripe payments integration.
- **DB:** better-sqlite3 with WAL mode

## Allowly
- **What:** Pay-as-you-go payment model for AI agents using Tributary on Solana
- **URL:** allowly.app
- **Repo:** github.com/xeroc/allowly
- **Submitted to:** Superteam Open Innovation Track (Feb 2026)

## Polycode
- **What:** AI agent framework powering ChaosCraft
- **Repo:** github.com/xeroc/polycode

## Tributary Fundraising

### Investor Database
- **Location:** `~/.obsidian/20-29.Business/27.Tributary/27.15 Fundraising/`
- **Subdirectories:** `VC/`, `Angel/`, `iGaming/`, `Strategic/`
- **Source:** `Fundraising/source.cvs` (134 entries, parsed to `/tmp/vc_entries.json`)
- **Profile count:** ~131 .md files with YAML frontmatter
- **Template:** See `templates/investor-profile.md` in this skill

### Top Priority Investors (highest Solana + DeFi fit)
1. Colosseum — Solana's primary accelerator/fund (CRITICAL)
2. Big Brain Holdings — Solana-native, pre-seed/seed (contact: Kasey)
3. Electric Capital — Solana investor, developer ecosystem expertise
4. Delphi Digital — deep Solana/DeFi research + investing
5. Nascent — Solana-native, first-check investor
6. Greenfield Capital — Berlin-based, Solana ecosystem (geographic match)
7. a16z Crypto — largest crypto fund, Solana presence
8. Standard Crypto — crypto-native, Solana/DeFi
9. North Island Ventures — Solana ecosystem
10. Propel VC — Solana ecosystem, pre-seed/seed

### Batch File Creation Technique
When creating many structured files from CSV/JSON data (50+), use `execute_code` with `hermes_tools.write_file` in batches of ~15 entries per call. This is faster and more reliable than `delegate_task` subagents for mechanical file generation tasks. Parse source data to JSON first, then loop through entries building frontmatter + markdown content per item.

## ChainSquad GmbH Infrastructure
- **n8n:** n8n.chainsquad.com (workflow automation, Twitter posting)
- **MetaMCP:** metamcp.chainsquad.com (Reddit, HN, Fetch tools)
- **GitHub org:** chainsquad
- **Telegram group:** -1003734601939
