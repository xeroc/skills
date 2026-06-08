---
name: twitter-thread
description: "Build Twitter/X posts and threads engineered for algorithmic distribution. Applies a systems-level model of the X feed (Phoenix transformer, engagement heads, weighted scoring) to craft hooks, structure threads, and design engagement loops. Use when writing tweets, threads, X Articles, or any content for X/Twitter. Triggers on: 'twitter thread', 'tweet', 'X post', 'write a thread', 'hook', 'twitter post', 'engagement', 'twitter strategy', 'viral tweet', 'write a tweet'."
---

# Twitter/X Content Engineering

The X feed ranks on predicted engagement probability, not content quality. Phoenix (Grok-derived transformer) scores each post against multiple engagement heads (favorite, reply, repost, quote, bookmark, profile click, dwell, follow-author, plus negative heads like block/report). A weighted scorer collapses these into a single relevance number.

**Job one**: maximize emotion density per token in the first line. Feeling first, facts second. If line one doesn't trigger OMG, LOL, or WTF, the rest doesn't matter.

## Hook Engineering

Write 20 first lines, ship the best one. Hooks are compression functions — squeeze max "stop scrolling and feel something" into the smallest window.

### Hook Levers

| Lever           | Mechanism                                                    | Example Pattern                                                         |
| --------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------- |
| **Curious**     | Information gap. Outcome without recipe.                     | "Here's what this got in 90 days and the exact framing"                 |
| **Superiority** | Insider data. Makes reader feel smart for sharing.           | Breakdowns, takes, data others don't have                               |
| **Belonging**   | Us vs. them. Tribe identity.                                 | "Two types of [X]" — clean in-group signal                              |
| **Challenged**  | Cognitive dissonance. Spiky truth.                           | "Your behavior doesn't match the story you tell about yourself"         |
| **Provoke**     | Tempered rage-bait. Mad enough to reply, not block.          | Knob, not a setting. Blocks/reports are heaviest negative heads         |
| **Validate**    | Names something they already felt. Vindication or gut punch. | "You're not stuck because of [tactic], you're stuck because of [truth]" |

Contrast: "Our API now supports serverless Functions" = information. "We just built AWS Lambda with a browser built-in." = hook. Same story, one interrupts a thumb.

## Format Selection

Pick one format per post. Don't mix.

- **Sub-280 one-liner**: High variance. Fun but rarely builds new audience without existing distribution. Good for reps and tone practice.
- **Long single post (Show more)**: The fold is a filter — expand = intent signal. Put your second-best line right below the fold. Expander gets immediate dopamine.
- **Thread**: Best for "save and come back" teaching, step-by-step sequences, long stories. Each numbered post should be screenshot-able on its own. Use less unless strong video attached — threads compete on density with Articles.
- **X Article**: Distribution cheat code right now. Over-indexes for reach. Write title first — if title alone doesn't compel a save, article is wasted. Best frame: come up with title, backfill article after.
- **Video/Image**: Treat as launch assets. Crisp visual proof. Quality bar: "would I put this in a pitch deck." Post less, keep bar high. Don't post noise for cadence.

## Engagement Stack

Likes are cheap. Design for (in order of signal strength):

1. **Replies + author replies back** — real back-and-forth, not emoji. Strongest pattern.
2. **Quote posts** — redistribution with commentary.
3. **Bookmarks** — "save for later" signals depth.
4. **Profile visits** — curiosity about author.
5. **Show more expands** — paid to read.

## Tactics

- **First 30 minutes**: Be in the thread like a standup. Reply, clarify. Not spam.
- **Link placement**: Put outbound link in first reply, not root post.
- **Boost others**: Want distribution on someone's post? Bookmark + real comment. Trains your graph.
- **Self-quote next day**: Quote your own banger with a new frame. Second pass at distribution without writing from zero. Especially good for Articles and long posts that under-timed.
- **Negative head ceiling**: Blocks and reports are the heaviest negative signals. Provoke is a knob, not a toggle.

## Workflow

When writing a thread or post:

1. **Define the emotional target** — which hook lever? Pick one.
2. **Write 20 first lines** — select the one with highest emotion density.
3. **Choose format** — match format to content type (teaching → thread, reference → article, launch → video/image).
4. **Structure the body** — each piece should standalone as screenshot-able.
5. **Design engagement loop** — end with something reply-worthy. Be present first 30 min.
6. **Ship deliberately** — this is engineering, not lottery.

Hook > format > engagement loop. Nailing one without the others is doomed from the start.
