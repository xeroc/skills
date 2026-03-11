---
name: reddit-launcher
description: "Create and post product/article launch posts across Reddit subreddits with platform-specific content. Use when launching a product, SaaS, tool, or article on Reddit communities. Generates subreddit-optimized posts following best practices from launch-playbook: problem-first approach, authentic tone, no hype, platform-specific formats. Supports 32 startup/dev subreddits with batch posting safeguards (max 3 posts per batch with user confirmation)."
---

# Reddit Launcher

You generate and post product/article launch content for Reddit subreddits. Each subreddit has unique expectations - you must adapt content to fit platform culture while maintaining core message.

## Core Principles (From Launch Playbook)

- **Problem-first**: Lead with pain point you solve, not product features
- **Authentic tone**: No hype, no marketing speak, no "game-changer" language
- **Technical depth**: For dev-focused subs, show you understand the tech
- **Behind-the-scenes**: Share development story, why you built it
- **Value over features**: Explain benefits, not feature lists
- **Ask for feedback**, never "upvotes" or "support"

## Step 1: Product Brief (Required)

Before generating posts, collect product information:

### Essential Questions

1. What does it do? (one sentence)
2. Who is it for? (target audience)
3. What's the primary pain point solved?
4. What stage? (MVP, beta, launched, established)
5. Is it free/paid/freemium?

### Universal Copy Blocks

Generate these from brief:

**Tagline variants:**

- 60 chars: For subs with short title limits
- 100 chars: Most directories
- Full sentence: Detailed listings

**Description blocks:**

- Short: 1-2 sentences (previews)
- Medium: 1 paragraph (directory pages)
- Long: 3-5 paragraphs with bullets (comprehensive)

**Story elements:**

- Hook: Pain point + curiosity
- Journey: Why/when you built it
- Solution: How it solves the problem
- Proof: Screenshots, metrics, user feedback
- CTA: Try it out / feedback welcome

## Step 2: Load Subreddit Reference

Check [references/subreddit-formats.md](references/subreddit-formats.md) for detailed guidance on each subreddit's posting format, rules, and expectations.

Each subreddit file includes:

- Posting format requirements (self post vs link post)
- Title patterns and length limits
- Flair/tag requirements
- Community rules and restrictions
- Example successful posts
- Timing recommendations

## Step 3: Generate Subreddit-Specific Posts

For each target subreddit:

1. **Load subreddit reference** from `references/subreddit-formats.md`
2. **Adapt universal copy** to subreddit requirements
3. **Apply format rules** (length, flair, self vs link)
4. **Include subreddit-specific elements** (tags, technical details, proof)
5. **Follow posting best practices** from [references/best-practices.md](references/best-practices.md)

### Title Adaptation Examples

**General startup subs** (r/SideProject, r/entrepreneur):

- "Built a SaaS that automates X for Y"
- "Tired of X? I built a solution"

**Dev-focused subs** (r/webdev, r/chrome_extensions):

- "Open source tool for [specific use case]"
- "[Tool name]: CLI tool that does X in 30s"

**Show & tell subs** (r/Imadethis, r/showmeyoursaaa):

- "I built [product] to solve [problem]"
- "After 6 months of side projects, finally launched"

**Critique subs** (r/roastmystartup):

- "Be brutal: My SaaS solves X. Is there product-market fit?"
- "First-time founder here. Roast my approach to [niche]"

## Step 4: Batch Posting Safeguards

**Critical Rule**: Never post to more than 3 subreddits without user confirmation.

### Posting Flow

```
For each batch of 3 subreddits:
1. Generate 3 platform-specific posts
2. Show user: Posts to create + subreddit list
3. Ask: "Ready to post these 3? (y/n)"
4. If user confirms: Use Reddit MCP tools to post
5. If user declines: Ask what to modify
6. Repeat for next batch
```

### Batch Progress Tracking

Track posted subreddits:

- Date posted
- Post URL
- Engagement (upvotes, comments)
- Notes

## Step 5: Post-Launch Engagement

After posting:

### Immediate Actions (First 24 hours)

- **Reply to every comment** within 1-2 hours
- **Thank genuine feedback** specifically
- **Answer questions** with detail, not brief responses
- **Share updates** if users suggest features
- **DM engaged users** (if appropriate) for deeper feedback

### Monitor for Patterns

- **Which subs performed best?** (upvotes, comments, quality feedback)
- **What title hooks worked?** (curiosity, pain points, numbers)
- **What questions came up repeatedly?** (address in post updates)
- **Any subreddit-specific issues?** (mod removal, downvote patterns)

### Engagement Templates

Use these when replying:

**For positive feedback:**

- "Thanks! That's actually a great point. We added that to our roadmap."

**For feature requests:**

- "Love this idea - would you mind sharing your use case? Helps us prioritize."

**For criticism:**

- "Fair point. We struggled with X because [reason]. Open to alternatives - any suggestions?"

**For questions:**

- "Great question. Here's how that works internally: [brief technical explanation]"

## Step 6: Common Mistakes to Avoid

### Title Mistakes

- **Vague titles**: "Check out my new tool" (no context)
- **Hype words**: "Revolutionary", "game-changer", "groundbreaking"
- **Self-promotion tone**: "I'm selling a product that..."
- **Wrong format**: Subreddit has specific title requirements (e.g., "Show HN:")

### Content Mistakes

- **Feature lists**: "Does X, Y, Z, A, B..." (boring, doesn't show understanding)
- **No pain point**: Starting with "I built a tool" instead of "Tired of X?"
- **Too generic**: "Helps you work faster" (too vague)
- **Salesy language**: "Limited time offer", "Don't miss out"

### Engagement Mistakes

- **Asking for upvotes**: "Please upvote if you like it" (breaks Reddit etiquette)
- **Defensive responses**: Getting defensive when criticized
- **Ghost posting**: Posting and never responding to comments
- **Copy-pasting**: Same post across multiple subs without adaptation

### Timing Mistakes

- **Wrong timezone**: Posting when target audience is asleep
- **Bad day**: Subreddit has active days/times (some are dead on weekends)
- **Spam frequency**: Too many posts in short time window

## Step 7: When to Use This Skill

Trigger this skill when:

- Launching a new product/SaaS/tool
- Posting an article for feedback
- Submitting to r/SideProject, r/Imadethis, r/showmeyoursaaa
- Sharing on r/entrepreneur, r/startups, r/indiehackers
- Launching on r/webdev, r/chrome_extensions, r/androidapps
- Seeking growth/marketing feedback on r/growthhacking, r/seo, r/askmarketing
- Posting to r/productivityapps, r/selfhosted, r/internetisbeautiful

**Do NOT use for:**

- General Reddit browsing (no post creation needed)
- Non-product discussions
- News sharing (different format)
- Questions about Reddit itself

## Quick Reference

| Subreddit           | Focus            | Key Format                      | Best Day               |
| ------------------- | ---------------- | ------------------------------- | ---------------------- |
| r/SideProject       | Side projects    | "I built X to solve Y"          | Weekday 8 AM-12 PM PST |
| r/Imadethis         | Show & tell      | "I made [product]" story format | Weekday 8 AM-12 PM PST |
| r/showmeyoursaaa    | SaaS showcase    | Feature-focused, proof included | Weekday 8 AM-12 PM PST |
| r/roastmystartup    | Critique         | "Roast my [X]" invite feedback  | Weekday 8 AM-12 PM PST |
| r/webdev            | Dev tools        | Technical depth required        | Weekday 9 AM-5 PM PST  |
| r/chrome_extensions | Extensions       | Extension-specific features     | Weekday 9 AM-5 PM PST  |
| r/entrepreneur      | Founders         | Journey + metrics included      | Weekday 8 AM-12 PM PST |
| r/startups          | Startup launches | Business model focus            | Weekday 8 AM-12 PM PST |
| r/indiehackers      | Indie projects   | Revenue/traffic numbers         | Weekday 8 AM-12 PM PST |
| r/saas              | SaaS products    | MRR, churn, metrics             | Weekday 8 AM-12 PM PST |

For complete subreddit reference, see [references/subreddit-formats.md](references/subreddit-formats.md).
