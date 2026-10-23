---
name: reactbits-finder
description: Resolve the right ReactBits component for any UI context by searching the official reactbits.dev catalog over free plain-text endpoints. Use when picking, finding, recommending, or installing an animation, text effect, background, micro-interaction, or interactive component from reactbits.dev — no MCP server, no API key, no cost.
---

# ReactBits Finder

Answer "which ReactBits component fits here?" from UI context, using only free endpoints.

## Why this works free

reactbits.dev publishes its full free catalog as one plain-text file: **https://reactbits.dev/llms.txt** (~95 KB, maintained by the author, written for agents). Every free component appears as one line with name, page URL, one-line description, and CLI identifier:

```
- [Decrypted Text](https://www.reactbits.dev/text-animations/decrypted-text): Hacker-style decryption cycling random glyphs until resolving to real text. CLI: `DecryptedText`.
```

The paid MCP wraps this same data. You never need it.

## Workflow

### 1. Fetch the catalog (once per session)

Read the URL with your fetch/read tool, or cache for repeated greps:

```bash
curl -s https://reactbits.dev/llms.txt > /tmp/reactbits-llms.txt
# fallback if rate-limited (same file, GitHub mirror):
curl -s https://raw.githubusercontent.com/DavidHDev/react-bits/main/public/llms.txt > /tmp/reactbits-llms.txt
```

### 2. Classify the context

Pick one of five categories by what the user is animating:

| User is animating…            | Catalog section      |
| ----------------------------- | -------------------- |
| a heading / word / phrase     | `## Text Animations` |
| a page or section backdrop    | `## Backgrounds`     |
| a card, menu, carousel, nav   | `## Components`      |
| a button, toggle, input, loader | `## Micro`         |
| entrance/exit/cursor/scroll feel itself | `## Animations` |

### 3. Grep candidates

Extract keyword stems from the user's context (mood nouns, verbs, surface type) and grep 2–3 passes, case-insensitive:

```bash
grep -iE 'decrypt|scramble|glitch|terminal' /tmp/reactbits-llms.txt | grep -v 'pro\.reactbits\.dev'
```

Each hit line is self-contained: name + URL + description + CLI id. Grep across all sections if the category is uncertain — the description disambiguates. The catalog also lists paid React Bits Pro entries inline; the `grep -v` filter above excludes them (drop it only when Pro is acceptable).

### 4. Rank the shortlist (cap at 3–5)

- **Dependency weight** — prefer lower unless the user explicitly wants 3D/shader: none/CSS < `gsap`/`motion` < `three`/`ogl`/WebGPU.
- **Trigger fit** — mount vs scroll vs hover vs cursor-follow. Don't pick cursor-chasers for touch-only surfaces, scroll effects for non-scrolling views.
- **Motion-safety flag** — many components loop continuously or ignore `prefers-reduced-motion`. Flag any pick that does.

### 5. Deliver

Per pick, output: **name — why it fits (one line tying back to the user's context words) — deps — page URL — install command.**

## Getting the code (free)

Install via CLI (registry endpoint, `LANG` = `JS|TS`, `STYLE` = `CSS|TW`):

```bash
npx shadcn@latest add https://reactbits.dev/r/<PascalName>-<LANG>-<STYLE>
# or
npx jsrepo@latest add https://reactbits.dev/r/<PascalName>-<LANG>-<STYLE>
```

Or fetch raw source (variant roots, all on `main`):

| Variant   | Path                                                          | Ext   |
| --------- | ------------------------------------------------------------- | ----- |
| JS + CSS  | `src/content/<Category>/<Name>/<Name>.jsx`                    | `.jsx` |
| JS + TW   | `src/tailwind/<Category>/<Name>/<Name>.jsx`                   | `.jsx` |
| TS + CSS  | `src/ts-default/<Category>/<Name>/<Name>.tsx`                 | `.tsx` |
| TS + TW   | `src/ts-tailwind/<Category>/<Name>/<Name>.tsx`                | `.tsx` |

Full URL pattern: `https://raw.githubusercontent.com/DavidHDev/react-bits/main/<variantRoot>/<Category>/<Name>/<Name>.<ext>`
Category dirs: `TextAnimations`, `Animations`, `Components`, `Micro`, `Backgrounds`.

After fetching source, check what it imports and install those deps:

```bash
grep -E "^import" <source-file>   # then install any of gsap / motion / three / ogl found
```

## Context → keyword starter table

When the user's words are vague, seed greps from here — the live catalog is always the source of truth; component names drift, this table only seeds keywords:

| Context                            | grep terms                           | known strong picks                          |
| ---------------------------------- | ------------------------------------ | ------------------------------------------- |
| hacker / terminal / techy reveal   | `decrypt`, `glitch`, `scramble`      | DecryptedText, GlitchText, ScrambledText    |
| elegant heading entrance           | `split`, `blur`, `reveal`, `stroke`  | SplitText, ScrollReveal, StrokeText         |
| numbers / stats emphasis           | `count`, `counter`                   | CountUp, Counter                            |
| calm hero backdrop                 | `aurora`, `silk`, `waves`, `grain`   | Aurora, Silk, Waves                         |
| bold hero backdrop                 | `liquid`, `chrome`, `plasma`         | LiquidChrome, Plasma, Particles             |
| scroll storytelling                | `scroll`                             | ScrollFloat, ScrollVelocity, ScrollExpand   |
| playful cursor feel                | `cursor`, `trail`, `spark`           | ClickSpark, ImageTrail, BlobCursor          |
| card hover depth                   | `tilt`, `glare`, `spotlight`, `glass`| TiltedCard, GlareHover, SpotlightCard       |
| loading / progress states          | `loader`, `progress`, `gauge`        | LatticeLoader, Stepper, SloshGauge          |
| luxury / reflective sheen          | `shine`, `metallic`, `holo`          | ShinyText, MetallicPaint, HoloCard          |

## Failure modes

- **llms.txt unreachable** → use the raw.githubusercontent mirror.
- **Grep returns nothing** → the user's metaphor is nonstandard. Dump one whole section and pick by description: `sed -n '/## Text Animations/,/## Animations/p' /tmp/reactbits-llms.txt`.
- **Registry URL 404s** → fetch the raw source instead. CLI ids are the PascalCase component name; page URLs are kebab-case.
- **User says "free only"** → everything on reactbits.dev is free (MIT + Commons Clause — free to use commercially, just don't resell the library). React Bits **Pro** (pro.reactbits.dev) is paid; its catalog is machine-readable at `reactbits.dev/pro-manifest.json` but the code is not free — don't recommend Pro components when the constraint is free.
