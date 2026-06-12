# Slide Templates (Per Act)

Real templates with the Tributary composable pitch as worked example. Replace content for your product.

## Act 1: Market Forces

### Template

```
Title: [Big number / stark contrast]. [Gap statement.]
Story: [Trend with real number]. [What's missing]. [Validation signal].
Visual: [Contrast image — big number vs. gap]
Speaker notes: [Lead with the number, not the explanation. Name-drop validation.]
```

### Worked Example (Tributary)

```
Title: $316B in stablecoins. Zero automation.
Story: Stablecoins won. $316B market cap. Solana holds $15.2B with $4.6B DeFi TVL.
       But stablecoins solved moving money. They didn't solve composing money.
       The Solana Foundation confirmed this gap — they shipped their own delegation
       primitive, co-developed with Helius, Dynamic, Mesh. The market validated the
       thesis before Tributary raised a single dollar.
Visual: Large "$316B" with "zero automation" underneath.
Speaker notes: Lead with "$316B" and the gap. SF validation is your strongest signal.
```

### What to Avoid

- Don't dump all market stats. One number that hits.
- Don't mention your product yet.
- Don't use "the market is expected to grow to $X by 2030" — that's a projection, not a fact.

---

## Act 2: Their Pain

### Template

```
Title: [Root cause stated as a sentence, not a label.]
Story: [Vignette 1: specific org + specific situation + consequence].
       [Vignette 2: different segment + same root cause].
       [Vignette 3: different segment + same root cause].
       [Connecting thread: what all three share].
Visual: [Vignette illustrations or repeated signing dialog]
Speaker notes: [Pick the vignette that matches the audience. Explain the pattern.]
```

### Worked Example (Tributary)

```
Title: Money that can't act on its own is money that can't scale.
Story: A DAO with $50M treasury. Market moves at 2am. Someone needs to wake up,
       check prices, sign a rebalancing transaction. Every time. Or the portfolio drifts.

       An AI agent that needs compute. It can't pay for API calls without your private
       key. Hand over full access — or the agent can't function.

       A trader who wants to DCA. Every Monday: open the DEX, connect wallet, approve,
       swap, sign. Every. Single. Week.

       Every financial automation in TradFi is impossible on-chain without custody.
Visual: Three vignette illustrations — DAO dashboard, AI agent stuck, calendar reminders.
Speaker notes: For crypto angels, lead with AI agent. For finance angels, lead with DAO.
```

### What to Avoid

- Don't say "there's no solution for X" — that's a lack of solution.
- Don't be abstract — specific vignettes beat general statements.
- Don't mention your product yet.

---

## Act 3: Future Vision

### Template

```
Title: What if [desired state]?
Story: What if [vignette 1 resolved]?
       What if [vignette 2 resolved]?
       What if [vignette 3 resolved]?
       [One shared mechanism]. [Safety guarantee].
Visual: [Clean flow diagram or "approve once" visual]
Speaker notes: [Match to Act 2 vignettes for A→B story. Don't reveal product yet.]
```

### Worked Example (Tributary)

```
Title: What if money could act within boundaries you set?
Story: What if a DAO could rebalance automatically — only when the oracle confirms
       a 5% drift, only within approved parameters, non-custodial the whole time?
       What if an AI agent could pay for compute within a $50/day budget — no private
       keys, no custody, just scoped authority you approved once?
       What if investing $200 into SOL every Monday just happened?
       One approval. Rules you define. Money moves within your boundaries.
       Non-custodial. Always.
Visual: User sets rules → money acts → boundaries enforced.
Speaker notes: "What if" is deliberate. Make them imagine before you reveal how.
```

### What to Avoid

- Don't reveal the product name or mechanism yet.
- Don't list features.
- Don't use "our platform enables..." — use "what if..."

---

## Act 4: The Bridge

### Template

```
Title: [Product name]: [one-line description using the one-liner].
Story: [Core primitive as diagram or formula].
       Walk through one example.
       Show composability by swapping parts.
       [3-5 differentiators as bullets — what makes this actually work].
       [Fold in competition as "why no one else does this"].
Visual: [Core primitive diagram]
Speaker notes: [Walk through with example, then swap parts. Handle competition question.]
```

### Worked Example (Tributary)

```
Title: Tributary: the composable automation layer for self-driving money.
Story: WHEN (condition) → PULL (amount) → ROUTE (to any on-chain program)

       Walk through: WHEN weekly → PULL $100 → ROUTE swap to SOL.
       Swap parts: replace 'weekly' with 'when price drops 5%' and 'swap' with 'stake'.
       Same primitive. Different product.

       What makes this work:
       - Non-custodial: token delegation, never custody
       - Conditional execution: validation CPI gates
       - Composable routing: any whitelisted DeFi protocol
       - Output-based fees: earn on result, not input
       - Instruction-level security: byte-range validation

       No one has built composable pull payments with conditional execution
       and arbitrary forward routing on Solana. This is new.
Visual: WHEN→PULL→ROUTE diagram.
Speaker notes: If asked about SF: they're the road, we're the logistics network.
```

### What to Avoid

- Don't list every feature — show one example, then composability.
- Don't dedicate a separate competition slide — fold it in as a callout.
- Don't go deep on technical implementation — that's speaker notes.

---

## Act 5: Proof Points

### Template

```
Title: [Traction signal]. [Market signal].
Story: [Big metric 1]. [Big metric 2]. [All organic, zero marketing].
       [Production systems count]. [Security verification].
       [Integration list — names + what they build].
       [Ecosystem enablement grid if platform — 6-10 categories].
       [Team — condensed to one punch line].
Visual: [Left: big metrics. Right: category grid. Bottom: team punch.]
Speaker notes: [Lead with strongest metric. Ecosystem grid = platform proof, not roadmap.]
```

### Worked Example (Tributary)

```
Title: Built. Live. The market is already building on it.
Story: 4,000+ payments. $12,000+ transferred. Zero marketing.
       9 production systems. Ottersec verified, >95% coverage.
       Integrations: Allowly, Contribute, Yumi Finance, Polycode, Orquestra.

       [Grid of 14 enabled business categories — DCA, stop-loss, AI agents, etc.]

       Each composition = new product. Each product flows through Tributary.
       Each flow earns protocol fees.

       Fabian Schuh, Dr.-Ing. PhD. 10+ years blockchain. 4 exits.
       26+ shipped projects. One founder. Zero funding.
Visual: Metrics + grid + team punch.
Speaker notes: "4,000 payments, zero marketing" hits harder than any projection.
```

### What to Avoid

- Don't lead with team — lead with traction.
- Don't show projections — show real numbers, even if small.
- Don't explain every integration — name them, move on.

---

## Act 6: Next Steps

### Template

```
Title: [One-liner repeated as action statement].
Story: Raising [amount] [stage].
       [Allocation table — 3-4 rows].
       [12-month arc — 4 milestones with success signals].
       [Closing: the foundation exists. Next step is X.]
Visual: [Timeline bar + allocation pie]
Speaker notes: [State amount cleanly. Milestones are verifiable. Close with one-liner.]
```

### Worked Example (Tributary)

```
Title: Self-driving money starts now.
Story: Raising <$250K pre-seed.
       30% security audit. 27% composable layer. 27% growth. 16% ops.
       Month 3: audit complete. Month 6: composable live.
       Month 9: 15+ integrations. Month 12: seed raise on real metrics.
       The protocol is built. The market is validated.
       The next step is composable, programmable, self-driving money.
Visual: Timeline + allocation.
Speaker notes: Don't apologize for the amount. Close with the one-liner. Let it land.
```

### What to Avoid

- Don't say "we're flexible" — state a range.
- Don't show detailed financial models.
- Don't forget the closing line — it's the last thing they hear.

---

## Closing Line

Two sentences. The first acknowledges what changed. The second is what you do.

Example:

> Stablecoins made money internet-native.
> Tributary makes it self-driving.
