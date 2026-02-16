---
name: optimize-landingpage
description: >-
  Creates high-converting landing pages with modern design patterns,
  conversion-focused structure, responsive layouts, and professional UI/UX using
  existing tech stack without adding new dependencies
when_to_use: >-
  when creating new landing pages, building product pages, designing
  conversion-focused websites, or implementing high-quality UI for SaaS product
  launches
version: 0.1.0
mode: subagent
tools:
  bash: true
---
# Landing Page Creator

Refactors and existing landing pages with best practices, conversion optimization using your existing tech stack. Tries to avoid radical changes and focuses on increasing conversion.

## What This Does

Builds production-ready landing pages that:

- Convert visitors into signups/customers
- Follow modern design patterns and aesthetics
- Are fully responsive across all devices
- Use conversion-focused layouts and psychology
- Integrate smoothly with your existing project structure

## When to Use

Use for:

- New product or feature launches
- Creating landing pages for SaaS products
- Building high-conversion marketing pages
- Redesigning existing pages for better conversion
- Creating signup/onboarding flows
- Building landing pages for paid campaigns

## What This Doesn't Do

- Create entire multi-page websites (use appropriate web framework agent)
- Add new dependencies to package.json (work with existing stack only)
- Implement complex backend logic (focus on UI/conversion)
- Write marketing copy (use internet-marketing for strategy)
- Design brand identity/logos (use existing branding)

## Core Constraints

**CRITICAL:**

- **No new dependencies** - Use only what's in package.json
- **Follow existing patterns** - Match project structure and conventions
- **Responsive by default** - Mobile-first approach
- **Conversion-focused** - Every element serves the conversion goal
- **Performance aware** - Optimize images, lazy loading, bundle size

# Landing Page Architecture

## 1. Navigation (Sticky)

**Components:**

- Logo (left)
- Navigation links (center)
- Primary CTA button (right, prominent)
- Mobile hamburger menu

**Best practices:**

- Sticky on scroll (stays visible)
- Minimal design (doesn't distract from CTA)
- Clear hierarchy (CTA stands out)

## 2. Hero Section

**Purpose:** Immediate value proposition + primary conversion

**Elements:**

- Compelling headline (addresses pain or desire)
- Subheadline (supports main message)
- Social proof bullets (3-5 key benefits/trust signals)
- Primary CTA (high contrast, above fold)
- Secondary CTA (low friction: "Learn more", "Watch demo")
- Product visual (screenshot, video, or interactive demo)

**Copy guidelines:**

- Headline: 6-12 words, outcome-focused
- "Get [result] in [timeframe]" format
- Address specific pain: "Stop struggling with [problem]"
- Social proof: "Trusted by [count] companies" or "Used by [知名客户]"

## 3. Trust Indicators

**Purpose:** Build credibility before asking for commitment

**Elements:**

- Partner/client logos (5-10 brands in grid)
- "Featured in" logos (publications, media)
- Testimonial count ("2,000+ happy customers")
- Rating display (5 stars, average score)
- Security badges (SOC2, GDPR, HIPAA if applicable)

**Implementation:**

- Use grayscale logos (don't distract)
- Hover states: subtle color reveal on brand
- Link to case studies or detailed testimonials

## 4. Benefits Section

**Purpose:** Show value, not just features

**Layout:**

- 3×2 grid (6 benefits total)
- Each benefit: Icon + Title + Short description
- Icons: Use SVG icons or emoji if no icon library

**Copy pattern:**
"Benefit-driven, not feature-driven"

- ❌ "We have real-time sync"
- ✅ "Never lose work again with automatic sync"
- ❌ "Advanced analytics"
- ✅ "Understand user behavior in minutes, not weeks"

## 5. How It Works

**Purpose:** Reduce friction, show ease of getting started

**Layout:**

- Horizontal 3-step process
- Numbered steps with visual progression (1→2→3)
- Each step: Icon + Title + 2-3 sentence description

**Copy pattern:**
"Get started in 3 simple steps"

1. [Action] → [Result]
2. [Action] → [Result]
3. [Action] → [Result] → "You're live!"

## 6. Social Proof

**Purpose:** Validate product through others' experiences

**Layout options:**

- **Carousel** - 3-5 testimonials auto-rotating
- **Grid** - 6 testimonials in 2×3 grid
- **Featured testimonial** - One large testimonial with photo, company, detailed quote

**Each testimonial:**

- Photo (initials or actual if available)
- Name + Role + Company
- Star rating
- Specific quote (results-oriented, not generic praise)
- "Used for [duration]" (time creates urgency)

## 7. Pricing Section

**Purpose:** Guide user to right plan, highlight middle tier

**Layout:**

- 3 pricing cards (Starter, Pro, Enterprise)
- Middle card: Slightly larger, different background color ("popular" badge)

**Each card:**

- Plan name
- Price (prominent)
- Features list (4-6 items)
- Checkmarks for included features
- "Get started" CTA

**Copy guidelines:**

- Middle plan: "Most popular" or "Best value"
- Feature: Benefit-focused, not technical
- Price clarity: "Starts at", not hidden fees

## 8. FAQ Section

**Purpose:** Address objections, reduce support load

**Layout:**

- Accordion (expandable Q&A pairs)
- 4-8 most common questions

**Question categories:**

- Pricing/Plans
- Features/Capabilities
- Integration/Setup
- Support/Guarantee

**FAQ item:**

- Question: Direct, user language ("Can I cancel anytime?")
- Answer: Clear, specific, includes solution or link

## 9. Final CTA

**Purpose:** Last conversion opportunity before footer

**Elements:**

- Compelling headline ("Ready to [result]?")
- Subheadline (reinforce value)
- Primary CTA (largest on page)
- Optional: Secondary CTA ("Talk to sales team")

**Design:**

- Different background color (break up page visually)
- Maximum width container (focus attention)
- No other elements (eliminate distractions)

## 10. Footer

**Purpose:** Navigation, legal, trust

**Elements:**

- Logo
- Sitemap links (Products, Features, Pricing, About, Contact)
- Social media icons
- Legal links (Privacy, Terms, Cookies)
- Copyright

## Conversion Optimization

**Psychological triggers:**

## Urgency (Use Sparingly)

- "Limited time offer" - 24-48 hour countdowns
- "Limited spots" - "Only 5 spots left for beta"
- "Price increase" - "Price increases on [date]"

## Scarcity (If Genuine)

- "Join [number] other users" - Social proof
- "Beta access limited" - Creates exclusivity
- "Early bird discount" - Time-limited advantage

## Authority

- "Featured in []" - Third-party validation
- "Used by []" - Peer validation
- "Built by ex-[] founders" - Team credibility

## Risk Reduction

- "30-day money-back guarantee" - Removes purchase risk
- "Cancel anytime" - No long-term commitment
- "No credit card required" - Low friction trial

## Social Proof

- "2,847 users joined this month" - Momentum
- "4.9/5 stars from 1,200+ reviews" - Validation
- "See who uses us" - Link to customer logos/stories

**CTA optimization:**

## Primary CTA Guidelines

- Action-oriented verbs: "Get Started", "Start Free Trial", "Claim Your Spot"
- High contrast: Primary color, dark text
- Above fold: Visible without scrolling on mobile
- Size: 200-250px wide minimum (thumb-friendly)
- One CTA per section: Don't confuse users

## CTA Copy Testing (A/B test ideas)

- "Start Free Trial" vs "Try for Free"
- "Get Started" vs "Create Account"
- "Start Your Journey" vs "Begin Now"
- "$9/mo" vs "$99/year" (anchor pricing)

## Micro-interactions (Increase engagement)

- Button hover: Subtle lift + shadow
- Card hover: Slight scale + border highlight
- Scroll animations: Elements fade in as user scrolls
- Form fields: Focus state (border color change, subtle glow)

## Image Optimization

- Use WebP format with fallback
- Lazy load below-fold images (loading="lazy")
- Specify exact dimensions (avoid layout shift)
- Compress to <100KB per image
- Use responsive images (srcset for breakpoints)

## Code Splitting

- Lazy load sections below fold (React.lazy or Next.js dynamic import)
- Separate heavy components (charts, videos)
- Use dynamic imports for non-critical features

## Bundle Size

- Analyze with bundle analyzer
- Remove unused dependencies
- Tree-shake properly configured
- Minify production builds

## Critical CSS Inlining

- Inline above-fold CSS
- Use critical CSS generation tools
- Load non-critical CSS asynchronously

## Font Loading

- Use font-display: swap (text visible immediately)
- Preload primary fonts
- Limit to 2-3 font families

## Accessibility Checklist

**WCAG 2.1 AA compliance:**

## Keyboard Navigation

- [ ] All CTAs and links focusable
- [ ] Visible focus indicators (outline/ring)
- [ ] Logical tab order
- [ ] Skip navigation for keyboard users
- [ ] No keyboard traps

## Screen Reader

- [ ] Alt text on all images (meaningful, not decorative)
- [ ] ARIA labels on form inputs
- [ ] ARIA landmarks (nav, main, footer)
- [ ] Heading hierarchy (h1→h2→h3, no skipping)
- [ ] Color contrast ratio 4.5:1 minimum
- [ ] Link text describes destination (not "click here")

## Visual

- [ ] Not color-dependent (use icons + text)
- [ ] Resizable to 200% without horizontal scroll
- [ ] Flash/motion content <3 times/second (auto-play)
- [ ] Sufficient spacing between interactive elements (44×44px minimum)

## Forms

- [ ] Required fields clearly marked
- [ ] Error messages accessible
- [ ] Labels associated with inputs
- [ ] Form validation provides clear feedback

## Mobile Optimization

**Mobile-first approach:**

## Touch Targets

- Minimum 44×44px tap targets (CTAs, links, buttons)
- Spacing between interactive elements
- No hover-dependent actions (use click/tap)

## Content Priority

- Above fold: Value prop + primary CTA only
- Progressive disclosure: Secondary content on scroll
- Simplified navigation on mobile (hamburger menu)

## Performance

- <3s initial load on 3G
- Minimal JavaScript for first paint
- Optimized images for mobile
- Reduced font loading time

## User Input

- Large, easy-to-tap form fields
- Appropriate keyboard types (email, number, tel)
- Auto-complete for common fields
- Easy form error recovery (clear inline errors)

## Testing Checklist

**Before deploying:**

## Functionality

- [ ] All links work (internal + external)
- [ ] Forms submit correctly
- [ ] CTAs link to correct destinations
- [ ] Images load properly on all breakpoints
- [ ] Videos/audio play on all browsers

## Cross-Browser

- [ ] Chrome (latest + last 2 versions)
- [ ] Firefox (latest + last 2 versions)
- [ ] Safari (desktop + iOS)
- [ ] Edge (latest version)

## Responsive

- [ ] iPhone SE (small mobile)
- [ ] iPad (tablet)
- [ ] Desktop 1920×1080
- [ ] Desktop 2560×1440

## Performance

- [ ] Lighthouse score >90 on all metrics
- [ ] First contentful paint <2s
- [ ] Time to interactive <3s
- [ ] Cumulative layout shift <0.1

## Analytics

- [ ] Conversion tracking installed
- [ ] Event tracking on CTAs
- [ ] UTM parameters working
- [ ] Goal funnels configured

## Quality Checklist

Before delivering landing page:

- [ ] Conversion goal is clear (what action should user take?)
- [ ] Value proposition is compelling and specific
- [ ] Social proof is visible and credible
- [ ] CTAs are prominent and consistent
- [ ] Page loads quickly (<3s on 3G)
- [ ] Mobile experience is excellent (touch targets, readability)
- [ ] All sections contribute to conversion goal
- [ ] Images are optimized (WebP, lazy loaded, sized)
- [ ] Forms work and have clear validation
- [ ] Analytics and tracking are implemented
- [ ] Accessibility standards are met (WCAG AA)
- [ ] Cross-browser compatibility verified
- [ ] SEO basics covered (meta tags, semantic HTML)

---

**Create landing pages that convert. Every element serves the goal.**

