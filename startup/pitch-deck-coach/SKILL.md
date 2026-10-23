---
name: cm-pitch-deck-coach
description: Audit, structure, and rewrite startup pitch decks for VC, angel, seed, and bridge rounds. Diagnoses round stage, applies the canonical 10-slide structure, rewrites weak slides, fixes TAM/SAM/SOM math, sharpens hooks, and flags red flags investors reject decks for. Use when asked to review a pitch deck, build a fundraising deck, fix a problem slide, write a hook, calculate TAM, prep for a VC meeting, polish a seed/Series A deck, or rewrite a one-liner. Triggers on "pitch deck", "investor deck", "fundraising deck", "VC meeting", "seed round", "Series A", "pre-seed", "angel investor", "TAM SAM SOM", "investor hook", "problem slide", "traction slide", "demo day", "YC deck", "accelerator deck", "deck review", "deck audit".
metadata:
  tags: ["fundraising", "pitch-deck", "startups", "venture-capital", "founders", "seed", "series-a", "accelerator", "storytelling", "investor-relations"]
---

# Pitch Deck Coach

Audit, restructure, and rewrite startup pitch decks for venture capital, angel, seed, bridge, and Series A rounds. Acts as an experienced operator-investor reviewing your deck the way a partner at a fund would: brutally honest about what works, specific about what to cut, and prescriptive about how to rewrite it.

## Usage

Invoke this skill when you have a pitch deck (or are building one) and need it to actually raise money instead of getting polite "keep us posted" replies.

**Basic invocation:**
> Review my pitch deck — I'm raising a $1.5M seed
> Help me write the problem slide for a B2B SaaS pitching $4M Series A
> My TAM math says $400B — investors keep pushing back, fix it
> Write a hook slide for a vertical AI agent for property managers

**With context:**
> Here's the current deck [paste content], we have $18K MRR and 4 logos
> We've raised $500K pre-seed, now raising $3M seed at $15M cap, no lead yet
> We're applying to YC W27, our deck has to work as a 1-min read

The agent diagnoses round stage, audits each slide, rewrites weak ones, and produces a structured optimization report.

## How It Works

### Step 1: Round-Stage Diagnosis

Before touching any slide, the agent identifies what stage you are actually at — because the same slide that wins a pre-seed check kills a Series A meeting.

| Stage | Check Size | What Investors Want | What to Omit |
|-------|-----------|--------------------|--------------|
| **Pre-seed** ($250K–$1.5M) | Founder + insight + wedge | Story, why-you, why-now, prototype or design partners | Detailed financials, 5-yr projections, full org chart |
| **Seed** ($1.5M–$5M) | Early product + early signal | MRR/users curve, retention cohort, GTM motion, ICP clarity | Bottom-up TAM beyond 3 years, hypothetical pricing tiers |
| **Bridge** (extension) | Survival + concrete plan | What changed, milestones to next round, burn discipline | Vision-heavy slides, "we pivoted" framed as success |
| **Series A** ($5M–$15M) | Repeatable GTM + unit economics | Net dollar retention, payback period, scalable channel, hiring plan | Founder origin story (move to appendix), competitive deep dives |
| **Series B+** | Scale efficiency | LTV/CAC by cohort, magic number, segment expansion | Anything that smells "we're still figuring it out" |

The agent asks one question if unclear: **"What stage are you raising and how much?"** Everything downstream depends on this.

### Step 2: The 10-Slide Canonical Structure

Most fundable decks compress to 10 slides. Anything longer is a comprehension tax. The agent maps your deck to this skeleton and flags what is missing or bloated.

```
1.  Hook            One sentence. Company + what you do + the surprising part.
2.  Problem         One persona, one quantified pain, one moment.
3.  Solution        How the product solves it — screenshot or 3-step demo.
4.  Why Now         Tailwind that makes this inevitable in 2026, not 2019.
5.  Market          TAM/SAM/SOM with bottom-up math.
6.  Traction        Proof — calibrated to stage.
7.  Business Model  How you make money — unit economics, not just "$X/month".
8.  Competition     Why you win, not just who exists.
9.  Team            Why this team, this problem, now.
10. Ask + Vision    Round size, runway, milestones — and the 10-year horizon.
```

**What each slide MUST contain:**

| Slide | Mandatory Elements | Killers (cut these) |
|-------|--------------------|---------------------|
| Hook | Company name, one-line, the "huh, interesting" hook | Logos, mission statement, awards |
| Problem | Specific persona, quantified pain, frequency or cost | "X is broken", "people struggle with Y" |
| Solution | Visual of product, 3-step user journey, before/after | Feature checklist, technical architecture diagrams |
| Why Now | Concrete shift (regulation, behavior, tech unlock, cost curve) | "AI is hot", "post-pandemic" |
| Market | TAM/SAM/SOM with sources, bottom-up calc visible | "$200B market" with no derivation |
| Traction | Curve up-and-to-the-right, named logos or metrics | Vanity metrics (signups, registered users without engagement) |
| Business Model | Pricing, ACV, gross margin, CAC/LTV directionally | "We'll figure out monetization later" |
| Competition | Honest map, credible "why we win" wedge | "We have no competition" |
| Team | Why-this-team proof, prior outcomes, domain reps | Job titles only, generic advisor lists |
| Ask | $ amount, runway months, 3 milestones, optional cap hint | Open-ended "we're raising" without a number |

### Step 3: Hook Slide — The One Sentence

The hook is the single sentence that determines whether the deck gets read. It belongs in slide 1, the email subject line, and the first 30 seconds of any meeting.

**Formula that works:**

```
[Company] is [category] for [specific persona] — [the surprising mechanism or wedge].
```

**Examples:**

```
WEAK:  "Acme is an AI-powered platform that helps businesses streamline operations."
       (No persona. No mechanism. Could be 10,000 companies.)

STRONG: "Acme is QuickBooks for solo property managers — we plug into their bank
        and file Schedule E in 90 seconds at tax time."
       (Persona: solo property managers. Mechanism: bank plug-in + Schedule E.
        Surprising: 90 seconds at tax time.)
```

The agent rewrites the hook until a non-expert can repeat it correctly after one read.

### Step 4: Problem Slide — Persona, Pain, Moment

The mistake on 80% of decks: framing the problem as a category ("X is hard") instead of a moment in a real person's day.

**Required ingredients:**

1. **One specific persona** — not "businesses", not "consumers". Name the title, company size, segment.
2. **One quantified pain** — hours wasted, dollars leaked, error rate, churn caused.
3. **One moment** — the trigger event when the pain hits. This makes it visceral.

```
WEAK:  "Property managers struggle to manage tenant communications efficiently."

STRONG: "A solo property manager with 12 doors fields 47 tenant texts per week.
        At tax time, they spend 22 hours reconciling rent, expenses, and 1099s
        across 4 spreadsheets. 31% miss the IRS deadline and pay penalties."
```

The strong version is concrete enough that an investor can picture the person and verify the math.

### Step 5: Market Sizing — Bottom-Up TAM/SAM/SOM

Top-down TAM ("$200B market, we just need 1%") is the single most common credibility-killer. Investors discount it instantly.

**Bottom-up formula:**

```
Number of target customers x Annual contract value = TAM
Number reachable via your GTM x ACV = SAM
Number you realistically capture in 3-5 years x ACV = SOM
```

**Example — vertical SaaS for solo property managers:**

```
TAM: 11M U.S. landlords with 1-50 doors x $600 ACV = $6.6B
SAM: 2.4M with property mgmt software (TurboTenant, Avail data) x $600 = $1.4B
SOM: 1% of SAM in year 5 (24,000 customers) x $600 = $14.4M ARR

Sources: U.S. Census 2024 rental owner survey; TurboTenant 2025 pricing benchmark.
```

This shows three things investors check: **the market is real, your wedge is reachable, and you can be a venture-scale outcome.** A $14.4M Y5 ARR with healthy growth implies $50M+ ARR exit-trajectory — fundable.

### Step 6: Traction — Calibrated to Stage

Different stages, different proof. Putting Series A traction expectations on a pre-seed deck wastes slides; putting pre-seed signals on a seed deck looks weak.

| Stage | What Counts as Traction |
|-------|------------------------|
| **Pre-seed** | Working prototype, design partners (named), waitlist with engagement, 3-5 LOIs from real ICPs, founder-market fit story |
| **Seed** | $5K–$50K MRR, week-over-week or month-over-month growth rate, 30-day retention curve, 3+ paying customers in target segment |
| **Bridge** | New milestone hit since last round (revenue 3x, new channel proven, key hire), updated burn, runway clarity |
| **Series A** | $1M+ ARR, net dollar retention >110%, payback period <18 months, repeatable GTM channel with CAC math, gross margin >70% (SaaS) |
| **Series B+** | Magic number >0.7, multi-segment expansion proof, ARR growth >2x with improving burn multiple |

**Traction slide must show:**
- A curve (line chart) of the primary metric — not a screenshot of Stripe
- The growth rate written as a number ("32% MoM for the last 4 months")
- One retention or efficiency proof point underneath the curve
- Named logos if B2B (with permission), or named cohorts if B2C

```
WEAK:  "We have over 10,000 signups and growing."
       (No engagement, no revenue, no time period.)

STRONG: "$28K MRR in March 2026, up from $4K in December 2025 — 47% MoM growth.
        Day-30 retention: 64%. 9 paying customers, 3 expansions. Top customer
        Brookfield Residential, $1,200/mo, signed 3-yr LOI for portfolio rollout."
```

### Step 7: Business Model — Concrete Unit Economics

"SaaS at $99/month" is not a business model. The agent forces concrete numbers, even directional ones.

**Required disclosures (be approximate, not vague):**

- **Pricing**: per-seat, per-unit, usage-based, tier structure
- **ACV**: average contract value, both today and at maturity
- **Gross margin**: COGS breakdown for SaaS, take rate for marketplaces
- **CAC**: how you acquire, what it costs (or hypothesis if pre-revenue)
- **LTV / Payback**: directional, with method ("3.2x LTV/CAC, 11-month payback at current churn")

```
WEAK:  "We charge $50/month per user."

STRONG: "$49/month per landlord, +$2/door overage. ACV today $720, target $1,400
        at maturity (premium tier). Gross margin 84% (Stripe + Plaid + infra).
        CAC $180 via SEO + accountant referrals. Payback 5 months, LTV/CAC 4.1x
        on observed 38-month median tenure of solo PMs."
```

### Step 8: Competition — Three Approaches, Each With a Use Case

There are three workable competition slide formats. The agent picks the right one based on your category.

| Format | When to Use | Pitfall |
|--------|-------------|---------|
| **2x2 quadrant** | When you can credibly own a corner that no one else does | Don't put yourself top-right with everyone bottom-left — investors see it as a tell |
| **Feature matrix** | Crowded category where buyers compare on capability | Becomes a feature-checklist arms race; reviewers spot when you cherry-pick features |
| **Why-we-win narrative** | Categories where the wedge is structural (distribution, data moat, founder-market fit) not feature-level | Requires real conviction — sounds hand-wavy if you don't have a concrete wedge |

**Critical rule: never claim "we have no competition."** If the problem is real, someone is solving it — even if poorly, even if it's a spreadsheet. Saying "no competition" tells investors either (a) the problem isn't real, or (b) you haven't done the work. Always name 2-4 alternatives, including the status quo (Excel, manual labor, doing nothing).

### Step 9: Team Slide — Proof, Not Titles

Investors scan team slides for: **why this team, why this problem, why now.** Titles alone do nothing.

**What to include:**

- Domain reps: "Built X at Y for Z years" — relevant to the problem
- Prior outcomes: exits, scale, unique credentials (PhD if technical moat, GTM leader if sales-driven)
- Founder-market fit: lived experience with the customer or domain
- Key gaps acknowledged honestly (with a hire plan)

```
WEAK:  "Jane Doe — CEO. Former product manager at Google.
        John Smith — CTO. Stanford CS."

STRONG: "Jane Doe (CEO) — Spent 4 years as a solo property manager with 18 doors;
        sold portfolio in 2024 to start Acme. Built the original spreadsheet
        the product replaces.
        John Smith (CTO) — Built tax automation engine at Pilot.com (1M+ returns
        filed). 3 years inside the IRS Schedule E processing pipeline."
```

The strong version answers: *why these two, why this problem, why now they would win it.*

### Step 10: Ask Slide — Concrete, Not Open-Ended

The ask slide closes the deck. Vagueness here ("we're raising a round") signals you don't know your own plan.

**Required:**

- Round size in dollars
- Months of runway it buys
- 3 milestones it gets you to (each tied to next round criteria)
- Optional terms hint (cap, lead status, current commits)

```
WEAK:  "We're raising a seed round to scale the team and grow the product."

STRONG: "Raising $2.5M seed — 18 months runway. Target post-round milestones:
         (1) $100K MRR with <5% logo churn,
         (2) Repeatable SEO + accountant referral channel at <$200 CAC,
         (3) Texas + Florida market saturation as proof of geographic playbook.
         $15M post-money cap, $800K committed from [Lead Fund], room for $1.7M."
```

### Step 11: Appendix vs Main Deck

The main deck is 10 slides. Everything else goes in the appendix — accessible if the investor asks, invisible if they don't.

**Move to appendix:**

- Detailed financial projections (5-yr P&L, headcount plan)
- Cohort retention deep-dive
- Technical architecture diagrams
- Customer testimonial collage
- Competitive feature matrix (full version)
- Founder bios in long form
- Press, awards, pilot case studies
- Cap table summary

**Rule of thumb:** if a slide answers a question only some investors will ask, it goes in the appendix. If every investor will ask it, it stays in the main deck.

### Step 12: Common Red Flags (Auto-Reject Triggers)

The agent scans for the patterns that get decks rejected before slide 5:

| Red Flag | What Investors See | Fix |
|----------|---------------------|-----|
| **Top-down TAM** ("$200B market, we need 1%") | Founder hasn't done the math | Replace with bottom-up calc |
| **"No real competition"** | Founder is naive or problem isn't real | Name 3-4 alternatives, including status quo |
| **Hockey-stick projections** with no base | Reverse-engineered to a target | Show realistic curve with stated assumptions |
| **Vanity metrics** (signups, downloads, page views) | Avoiding the real numbers | Replace with revenue, retention, or engaged usage |
| **Feature-list product slide** | Solution looking for a problem | Replace with one-sentence outcome + screenshot |
| **Generic problem** ("X is hard") | No customer truth | Rewrite with persona + quantified pain + moment |
| **"We're like Uber for X"** without explaining the Uber-mechanic | Lazy positioning | Spell out the actual mechanism |
| **5+ co-founders, all CEOs** | Governance disaster | Restructure team slide, name single CEO |
| **No ask, no terms, no use-of-funds** | Founder isn't ready to raise | Add concrete ask slide |
| **Tiny ARR, gigantic valuation hint** | Mismatched expectations | Drop the cap signal or fix the round size |

### Step 13: Format Choice — Tool & Delivery

The right tool depends on whether the deck is **cold-sent** (read alone, no founder present) or **in-meeting** (presented live).

| Tool | Best For | Tradeoffs |
|------|----------|-----------|
| **Google Slides** | Universal compatibility, easy collab | Looks generic without design effort |
| **Pitch.com** | Beautifully default-designed, analytics on opens | Some investors auto-skip pitch.com links as "deck shop" output |
| **Notion** | Detail-heavy data rooms, internal docs | Wrong format for cold-send — feels unfinished |
| **Figma / Keynote** | Highest visual polish, custom design | Slower to update, lock-in to designer |
| **PDF (always)** | Cold-sends, attaching to emails | Mandatory — never send a Google Slides link cold |

**Embed vs PDF for cold-sends:**

- **PDF**: default for cold outreach. Investors live in inboxes, not browsers. PDF opens on phone, attaches forwardably, prints cleanly. Always under 8 MB.
- **Embedded link** (DocSend, Pitch.com): only when (a) you want analytics on who opened what, (b) the introduction is warm and the investor expects it. Don't gate cold-sends behind email walls — friction kills meetings.

### Step 14: Pre-Meeting Deck vs In-Meeting Deck

These are **two different decks**, not one. The agent helps build both versions.

**Pre-meeting deck (cold-send / forwarded):**

- Designed to be read alone, no narrator
- More text per slide — every slide must stand on its own
- Includes appendix accessible from main flow
- 10–12 slides max
- Hook slide does heavy lifting, since you may have 30 seconds before it gets closed

**In-meeting deck (live presentation):**

- Designed to be shown while you talk
- Less text, more visuals — you are the narrator, slides are backup
- Tighter sequence (8–10 slides), no appendix shown unless asked
- Each slide has one clear takeaway you can land in 60–90 seconds
- Demo slot replaces some text-heavy slides (live product or video)

**Common mistake:** founders use the cold-send deck in meetings, then read every word aloud while the investor reads ahead. This is a confidence-killer. Build both versions.

## Worked Examples

### Example 1: Weak Problem Slide → Rewritten

**WEAK (original deck):**

```
Slide 2 — The Problem

- Small business owners struggle with bookkeeping
- Existing tools are expensive and complicated
- 60% of small businesses fail within 5 years
- There has to be a better way
```

**Why it fails:**
- "Small business owners" is too broad — investor cannot picture one
- "Struggle with bookkeeping" is a category, not a moment
- The 60% failure stat is unrelated to bookkeeping (correlation/causation gap)
- "There has to be a better way" is a tell that the founder hasn't talked to enough customers

**REWRITTEN (strong):**

```
Slide 2 — The Problem

Solo e-commerce sellers on Shopify spend Sunday nights reconciling
3 platforms (Shopify, Stripe, USPS) into one spreadsheet to figure
out if last week was profitable.

  - 4.2 hours per week, every week (interviewed 47 sellers)
  - 38% have NEVER calculated true per-SKU margin
  - 71% miss quarterly tax estimates because they can't separate
    inventory cost from revenue in time

The moment: it's 11pm Sunday, they have 200 SKUs, and they need
to decide what to reorder for next week without knowing margin.
```

**Why it works:**
- Specific persona (solo Shopify sellers, not "small businesses")
- Quantified pain (4.2 hours, 38%, 71%) with sourced research
- The moment (11pm Sunday, 200 SKUs, reorder decision) is visceral
- Implies the wedge: this is not generic accounting — it's a per-SKU margin tool tied to reorder timing

### Example 2: Weak Traction Slide → Rewritten

**WEAK (original deck):**

```
Slide 6 — Traction

  - 12,000 users on the waitlist
  - Featured in TechCrunch
  - Strong product-market fit signals
  - Growing fast every week
```

**Why it fails:**
- Waitlist isn't traction — engagement is. 12K signups with 0% conversion is worse than 200 paying users.
- "Featured in TechCrunch" is press, not customer demand
- "Strong PMF signals" with no metric is hand-waving
- "Growing fast" with no rate is the deck equivalent of "trust me bro"

**REWRITTEN (strong):**

```
Slide 6 — Traction (March 2026)

  Revenue:        $34K MRR  (up from $6K in Nov 2025 — 41% MoM, 5 months)
  Customers:      114 paying ($299 ACV avg)
  Retention:      Day-90 logo retention 87%
                  Net dollar retention 118% (expansion via add-ons)
  Top cohort:     Nov 2025 cohort — 91% still active, $42 NDR uplift

  [Line chart: MRR Nov '25 -> Mar '26, climbing from $6K to $34K]

  Channel breakdown:
    SEO ("shopify margin calculator"):    62% of new logos
    Accountant referrals:                  28%
    Founder-led outbound:                  10%

  CAC blended: $94. Payback: 3.4 months.
```

**Why it works:**
- Real revenue, not waitlist
- Specific growth rate over a stated time window
- Retention numbers — both logo and net dollar
- Channel attribution shows GTM is repeatable, not luck
- CAC + payback shows unit economics already work

This is exactly enough for a seed lead to write a term sheet.

## Output

The agent produces:

- **Round-stage diagnosis**: which stage the deck should target and what level of proof is required
- **Slide-by-slide audit**: each slide rated (strong / acceptable / rewrite-required) with specific notes
- **Rewritten slides**: full replacement copy for any slide flagged as weak
- **Hook iterations**: 3-5 candidate one-liners, ranked
- **TAM/SAM/SOM rebuild**: bottom-up math with cited sources
- **Red-flag report**: list of auto-reject triggers found, with fixes
- **Two-deck plan**: separate pre-meeting and in-meeting versions if the founder will pitch live
- **Format recommendation**: tool + delivery format for the founder's specific context

## Common Scenarios

### "Investors keep saying 'too early' — what's wrong with my deck?"
The agent diagnoses round-stage mismatch — usually the deck is positioned for seed but the proof is pre-seed (or vice versa). Repositions the narrative to the stage the proof actually supports.

### "We have a 25-slide deck and meetings stall around slide 12"
Compress to 10. The agent identifies the load-bearing slides, moves the rest to appendix, and rewrites transitions so the story holds without the cut content.

### "I need a hook for cold outreach to VCs"
The agent generates 5 candidate hooks following the Company + persona + mechanism formula, ranked by specificity and stickiness.

### "My TAM slide keeps getting pushed back"
The agent rebuilds it bottom-up with named sources, ICPs counted, and ACV grounded in your actual pricing.

### "I'm prepping for YC / Techstars / On Deck demo day — different rules?"
Demo days are a unique format: 60-90 seconds, hook-heavy, traction front-loaded, no Q&A. The agent restructures into a demo-day cut with one-breath narrative.

### "I need to send a deck cold today, no warm intro"
The agent prioritizes the hook slide, the problem slide, and the traction slide — the three any investor reads before deciding whether to keep going. Format: PDF, under 6 MB, hook in subject line.

## Tips for Best Results

- Share the actual deck (paste content, attach PDF, or describe each slide) — vague descriptions produce vague feedback
- State the round explicitly: stage, target raise, current commits, target close date
- Share the most recent investor objections you've heard verbatim — they reveal which slides are failing
- If pre-revenue, share design partner names and LOI status — pre-seed traction is mostly social proof
- If post-revenue, share MRR, growth rate, and retention by cohort — seed traction is mostly numbers
- Mention which investors you're targeting (tier-1 generalists, vertical specialists, angels, accelerators) — different audiences require different framing

## When NOT to use

This skill is specifically for **fundraising decks aimed at external investors**. Do not use for:

- **Operational decks**: internal strategy, all-hands, board updates (different audience, different content)
- **Sales decks**: customer-facing pitches optimized for closing deals, not raising capital
- **Internal investor updates**: post-funding monthly/quarterly reports — those follow a different template (KPIs, asks, lowlights, highlights)
- **Hiring decks**: candidate-facing pitches about company mission and equity — overlap exists but the optimization function is different
- **Partnership / BD decks**: pitching potential partners requires mutual-value framing, not investment-return framing
- **Corporate pitch competitions** with rigid templates — follow the prescribed format instead
- **Grant applications**: government and foundation grants follow structured forms, not narrative decks

For these cases, use the appropriate domain-specific tool or template — not a fundraising-deck framework.
