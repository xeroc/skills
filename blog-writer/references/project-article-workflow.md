# Project Article Workflow (Fabian-Style)

For writing investor-facing or community-facing articles about a specific project that draw on internal vault research + external web research.

## Workflow

1. **Read the project context** -- PROJECT.md, technical specs (e.g., METEORA.md, SWAPWHENPRICE.md). These are dense and technical. You need them for accuracy but the article must be non-technical.
2. **Read use-case files** from the vault's use-case directory. Filter by status field in YAML frontmatter. Note: status values include emoji prefixes (e.g., `status: "🔍research"`, `status: "💭 ideation"`). Pick the 4-6 most compelling ones.
3. **Delegate web research** to a subagent for market data, competitor analysis, statistics. Give specific topics. The subagent returns bullet points with sources.
4. **Synthesize and write** using fabian-writing-style. The article structure that works:
   - Open with a paradox or misconception (push vs pull payments)
   - Define terms before diving in
   - Build argument incrementally (problem → existing solution → new capability → what it unlocks)
   - Use concrete examples, not abstractions
   - Each use case gets 2-3 paragraphs -- enough to spark imagination, not enough to bore
   - Close with "Room for Innovation" -- Fabian's signature section naming what's still unbuilt
5. **The funding ask** -- if the article targets investors, frame it as: foundation done, specification written, what's missing is the audit/trust layer.

## Key Principle

Technical specs go into the article as *explained concepts*, not as code or jargon. "CPI into Meteora DLMM" becomes "the protocol claims your tokens and swaps them through the DEX automatically." The reader understands the what and why; the how is described in plain language.

## Research Data Points (Composable Pull Payments, June 2026)

Market data gathered for the Tributary composable pull payments article:

- Global subscription/recurring billing market: ~$15B (2023), projected $55-60B by 2030 (CAGR ~18-20%)
- ACH (pull-based): $76.7T in payment value in the US in 2023
- SEPA Direct Debit (EU): €3.5+ trillion annually
- AI agent economy: projected $50-70B by 2030 (CAGR ~40-45%)
- Solana: ~400ms block time, <$0.001/tx, ~2000-5000+ non-vote TPS
- Solana CPI: up to 4 levels of nesting, synchronous, atomic (all-or-nothing)
- Meteora DLMM: top-5 Solana DEX, ~$200-400M TVL
- Solana program audit costs: $15K-$80K (standard), $75K-$250K (complex protocol)

Refresh these numbers before reusing in future articles.
