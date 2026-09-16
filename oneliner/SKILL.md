---
name: oneliner
description: Craft the 3-5 word one-liner for a startup or product — the "timeline pitch" that makes a scrolling stranger instantly understand and care. Use when a founder needs to compress what their product does into a few plain English words: "give me a one-liner for my startup", "compress my pitch", "3-5 word pitch", "elevator pitch", "review/critique these one-liners", or when writing bio lines, demo-day intros, or launch-post openers. Runs a grilling interview first so the founder explains what the product really does and how it works, then generates multiple candidates across eight angles (analogue, descriptive, problem-first, solution-first, outcome-first, audience-first, mechanism-first, stakes-first) and scores them on clarity, excitement, and truthfulness.
---

# Startup One-Liner

The one-liner answers "what is this?" in 3-5 plain English words, understandable by someone reading on a phone in an Uber with bad reception. It is a timeline pitch, not an elevator pitch: the reader is scrolling, owes you nothing, and each word is a risk of losing them. It earns the right to be read further — nothing more.

## Workflow

1. **Grill the founder first.** Load the `grilling` skill and run its interview process before writing a single candidate. Goal: the user explains what the product REALLY does and how it works, through context — not marketing copy. Cover: the mechanics under the hood, who it's for, the novel twist, the pain it kills, and how far the truth stretches (which users, how often — does the headline claim actually hold for the main use case?). Mechanics matter because truthful claims derive from them: Hobba can only fairly claim "negative interest loans" because their yield-farm cross-subsidy made it true for 90%+ of users, 95% of the time.
   - One question at a time, wait for each answer (grilling's rule). Include a recommended answer with every question.
   - If facts are discoverable (website, repo, docs, deck), look them up instead of asking. The product decisions are the founder's — put those to them.
   - Do not proceed until you can explain the product's mechanism yourself in two plain sentences.
2. **Generate candidates: 2-4 per angle, all eight angles below.** Every candidate must pass the hard rules.
3. **Score and recommend.** Present all candidates in a table grouped by angle with word counts, then apply the tests in priority order (non-ambiguous → exciting → truthful), name a winner and a runner-up. The winner is almost always analogue or descriptive — say so plainly when it is.

## Hard rules (non-negotiable)

- **Max 5 words.** Very rarely more. Even Bitcoin compresses to "digital gold" and Solana to "move money globally for cents".
- **Mother test.** Use the exact words your mother would use explaining your startup to her friends over coffee. "He helps people in Venezuela own dollars" — never "he's revolutionizing tradfi".
- **Banned buzzwords:** revolutionary, disruptive, redefining, "the future of", and friends.
- **Banned abstract metaphors:** legos, building blocks, layer, glue. No "legos for intellectual property", no "glue between apps and smart contracts".

## Anatomy — evaluate in this priority order

1. **Non-ambiguous.** The 10-reader test: 10 different people read it, all visualize the same product. "Copilot for eCommerce" fails (shopping assistant? merchant copilot? support agent? supply chain?). "Reddit for agents" passes — everyone knows exactly what it is and for whom. If they can't visualize it, they can't get excited, which is why this beats excitement.
2. **Exciting.** Provokes a feeling — curiosity, wtf, delight. "Tokenized dinosaurs" makes you go wait, what? A boring-but-clear line still beats an exciting-but-vague one.
3. **Truthful.** Paints the right picture; does NOT require 100% literal truth. If the main use case genuinely delivers, the claim is fair — details come later. SP3ND's "shop anything online with stablecoins" is fine at ~80% of shops.

## The eight angles

Generate 2-4 candidates for EACH angle. Two are workhorses; six rarely win but always generate them so the founder can compare and steal fragments.

### Workhorses

- **Analogue** — known anchor + your novelty. "Polymarket on Twitch streams". The anchor can be a product or a whole category: "Prediction markets on Twitch streams". The anchor must be universally known — "prime broker for Solana loans" fails only because few people know what a prime broker is.
- **Descriptive** — imperative verb + object + context. Action-coded and direct. "Launch tokens without seeding liquidity" (Pump), "Move money globally for cents" (Solana), "Shop anything online with stablecoins" (SP3ND).

### Rarely win — still generate

These lead with something other than the product itself, so they usually lose the non-ambiguity test. Worked on Hobba (overcollateralized loans whose interest is paid by yield-farming part of the collateral):

- **Problem-first** — leads with the pain: "Stop paying interest on loans"
- **Solution-first** — leads with the artifact/system: "Interest-free borrowing protocol"
- **Outcome-first** — leads with what changes for the user: "Your loans repay themselves"
- **Audience-first** — leads with who it's for: "Loans for BTC long-term holders"
- **Mechanism-first** — leads with how it works: "Farm yield pays your interest"
- **Stakes-first** — leads with what's at risk: "Inflation is eating your savings"

## Worked examples

Good:

| One-liner | Words | Why |
|---|---|---|
| Reddit for agents | 3 | one visual, zero jargon, instantly exciting |
| Tokenized dinosaurs | 2 | pure wtf-curiosity |
| Negative interest loans on Solana | 5 | Hobba — unambiguous, exciting, true for the main use case |
| Shop anything online with stablecoins | 5 | plain, truthful enough (~80% of shops) |

Bad:

| One-liner | Why it fails |
|---|---|
| Copilot for eCommerce | 10 readers, 10 different products |
| Loans that work for you | sales lingo; says nothing about what it is |
| Prime broker for loans on Solana | jargon anchor nobody knows |
| Self repaying loans | 10 readers, 10 meanings (self-liquidating? refinancing? autopay?) |
| Legos for intellectual property | banned abstract metaphor |

Note: Hobba shipped "negative interest loans on Solana" over three alternatives that each failed a test — ambiguity, jargon, or marketing smell. Compression is a skill worth the grind; clarity of the line reflects clarity of thinking.

## Output format

After the grilling interview, deliver:

1. One-line summary of your understanding of the product mechanism (founder corrects if wrong)
2. Candidates table: angle | one-liner | word count — all eight angles, 2-4 each
3. Verdict: apply non-ambiguous → exciting → truthful to the strongest few, kill the failures with one line of reasoning each
4. Winner + runner-up, with the one test each survives best
