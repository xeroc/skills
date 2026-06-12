---
name: pitch-deck-builder
description: Construct investor pitch decks using the 6-act sales narrative structure (market forces, pain, vision, solution, proof, path). Use when building, restructuring, or reviewing pitch decks for pre-seed, seed, or angel rounds. Triggers on "pitch deck", "investor deck", "fundraising deck", "build pitch", "restructure pitch", "review pitch", "sales deck".
---

# Pitch Deck Builder

Construct investor pitch decks that tell a story, not list features.

## Core Framework: 6-Act Sales Narrative

Every pitch follows this structure. Every slide maps to one act.

| #   | Act           | Purpose           | Emotion    |
| --- | ------------- | ----------------- | ---------- |
| 1   | Market Forces | Why now           | Urgency    |
| 2   | Their Pain    | What's broken     | Empathy    |
| 3   | Future Vision | What it should be | Desire     |
| 4   | The Bridge    | How we get there  | Confidence |
| 5   | Proof Points  | Why believe us    | Trust      |
| 6   | Next Steps    | The path forward  | Action     |

**The flip test**: Read only the title sentences of each slide, in order. They should tell a complete story.

## Design Rules

- Max 10 slides
- One big sentence per slide title
- One big image or visual per slide
- Super simple words — no "revolutionizing", "disrupting", "platform"
- Don't specify the problem as a lack of solution — specify it as a real desire
- Don't use "The Problem" / "The Solution" as slide titles
- Max ~300 words total across all slide bodies
- Black background, white font, no branding fluff

## Workflow

```
Pitch Deck Progress:
- [ ] Step 1: Gather inputs
- [ ] Step 2: Nail the one-liner
- [ ] Step 3: Map the 6-act structure
- [ ] Step 4: Draft each slide
- [ ] Step 5: Run the flip test
- [ ] Step 6: Tighten to 300 words
- [ ] Step 7: Write speaker notes
```

### Step 1: Gather Inputs

Ask the founder for:

- **Product**: What does it do? (one paragraph max)
- **Audience**: Angel? VC? Crypto-native? Generalist?
- **Stage**: Pre-seed, seed, series A?
- **Raise**: How much and what for?
- **Traction**: Any metrics — users, revenue, payments, volume
- **Team**: Who are you? What have you shipped?
- **Differentiation**: What can't competitors do?
- **One-liner**: If they have one. If not, Step 2 creates it.

If any input is missing, ask. Don't guess.

### Step 2: Nail the One-Liner

Compress the startup into ≤5 words. Hierarchy:

1. Explicit — what it actually does
2. Non-ambiguous — no room for misinterpretation
3. Exciting — makes someone want to know more
4. Truthful — the right picture

Best format: "X for Y" maps to something people know.

Examples:

- "Self-driving money" (4 words — abstract but electric)
- "Tokenized dinosaur fossils" (3 words — specific, vivid)
- "Stripe for composable money" (4 words — X-for-Y)

Bad examples:

- "Co-pilot for e-commerce" (ambiguous — shopper or shop owner?)
- "The automation layer for stablecoins" (6 words, "the" wastes a slot)

### Step 3: Map the 6-Act Structure

For each act, define:

| Field         | What to Fill                                  |
| ------------- | --------------------------------------------- |
| Title         | One big sentence                              |
| Story         | The narrative beat (2-4 sentences)            |
| Visual        | What image/diagram supports it                |
| Speaker notes | What the founder says that isn't on the slide |

See [references/slide-templates.md](references/slide-templates.md) for per-act templates with examples.

**Act 1 — Market Forces**: What macro trend makes this inevitable? Use real numbers. Cite sources.

**Act 2 — Their Pain**: Not "there's no solution." Real pain. Pick 2-3 vivid vignettes from different segments — all pointing to the same root cause. The vignettes are people or organizations suffering _right now_.

**Act 3 — Future Vision**: "What if" framing. Resolve the vignettes from Act 2. Same segments, now unblocked. One shared mechanism. Don't reveal the product yet — reveal the possibility.

**Act 4 — The Bridge**: Now reveal the product. Core primitive in one diagram. Walk through with a single example, then show composability by swapping parts. Competition folded in here if needed — as a brief "why no one else does this" callout, not a full slide.

**Act 5 — Proof Points**: Traction metrics first (big numbers). Live integrations. Team credentials. If the product enables an ecosystem of businesses, list them as a grid — proof of platform value, not a roadmap.

**Act 6 — Next Steps**: The ask. Allocation table. 12-month arc with verifiable milestones. Close with the one-liner.

### Step 4: Draft Each Slide

For each slide:

1. Write the title sentence first
2. Write the story in ≤50 words
3. Specify the visual (don't create it — describe it)
4. Write speaker notes separately

### Step 5: Run the Flip Test

Read only the title sentences, slides 1 through 6 (or 10 if you have more). Do they tell a story?

Good flip test:

1. "$316B in stablecoins. Zero automation."
2. "Money that can't act on its own is money that can't scale."
3. "What if money could act within boundaries you set?"
4. "Tributary: the composable automation layer for self-driving money."
5. "Built. Live. The market is already building on it."
6. "Self-driving money starts now."

Bad flip test:

1. "Market Opportunity"
2. "The Problem"
3. "Our Vision"
4. "The Solution"
5. "Traction"
6. "The Ask"

If titles are generic labels instead of sentences, rewrite.

### Step 6: Tighten to 300 Words

Count total words across all slide bodies (not titles, not speaker notes). If >300, cut:

- Adjectives and adverbs first
- Then secondary points
- Then anything that repeats across slides

Every word must earn its place.

### Step 7: Write Speaker Notes

Speaker notes are what the founder says that isn't on the slide. They:

- Expand on the story beat
- Name-drop specifics (partners, competitors, ecosystem players)
- Handle anticipated questions
- Adapt to audience (technical vs. non-technical)

Speaker notes don't count toward the 300-word limit.

## Anti-Patterns

| Don't                                     | Do Instead                          |
| ----------------------------------------- | ----------------------------------- |
| "There's no solution for X"               | "People want to [specific desire]"  |
| List features                             | Tell a story with a protagonist     |
| Use buzzwords (revolutionary, disruptive) | Use plain language                  |
| Have 15 slides                            | Cut to 10. Then cut to 6.           |
| Dedicate a slide to competition           | Fold into solution or proof         |
| Apologize for raise amount                | State it cleanly, move on           |
| Put all detail on slides                  | Put detail in speaker notes         |
| Use "The Problem" as a title              | Use a sentence that states the pain |
| Show made-up projections                  | Show real traction, even if small   |

## Reference Files

- **[references/slide-templates.md](references/slide-templates.md)** — Per-act templates with real examples from the Tributary composable pitch
- **[references/sales-deck-structure.md](references/sales-deck-structure.md)** — Deep dive into the 6-act structure theory and why it works
- **[references/enabled-businesses.md](references/enabled-businesses.md)** — Business category grid for platform pitches (DCA, stop-loss, AI agents, inheritance, etc.)

## When to Use This Skill

- Building a pitch deck from scratch
- Restructuring an existing deck that isn't working
- Reviewing a deck and giving feedback
- Preparing for a specific investor meeting
- Writing a Pixar blurb for written submissions
- Adapting a deck for a different audience (angels vs. VC vs. hackathon judges)

## Pixar Blurb Template

For written submissions (YC, grant applications, email intros):

```
[Context — 1 sentence: the world state]. [Problem — 1 sentence: what's broken].
[Hero — 1 sentence: what we're building]. [Why you — 1 sentence: traction + team].
[Ask — 1 sentence: what we need].
```
