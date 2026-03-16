---
name: landing-page-builder
description: Build modern landing pages with dark/light theme toggle, Roboto Mono typography, and Solana-inspired color scheme. Use when you need to create a sleek, minimalist landing page with playbooks.com-inspired design patterns, gradient accents, busy terminal cards, and smooth transitions.
---

# Landing Page Builder

Build modern, high-conversion landing pages with a dark/light toggle, Roboto Mono typography, and Solana color scheme. This skill provides the complete design system and component patterns used to create a modern landing page.

## Quick Start

Create a new Next.js project with Tailwind CSS:

```bash
npx create-next-app@latest my-landing --typescript --tailwind --eslint
cd my-landing
npm install lucide-react framer-motion clsx tailwind-merge
```

Copy the design system files from this skill's reference directory.

## Design System

### Color Palette (Solana-inspired)

```css
/* Primary accent colors */
--primary: 267 100% 65%; /* Solana purple #9945FF */
--primary-foreground: 210 40% 98%;

/* Background and foreground */
--background: 222.2 84% 4.9%; /* Nearly black */
--foreground: 210 40% 98%; /* Nearly white */

/* Muted colors */
--muted: 217.2 32.6% 17.5%;
--muted-foreground: 215 20.2% 65.1%;
```

### Typography (Roboto Mono Everywhere)

```javascript
// layout.tsx
import { Inter, Roboto_Mono } from "next/font/google";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });
const robotoMono = Roboto_Mono({
  subsets: ["latin"],
  variable: "--font-roboto-mono",
  weight: ["400", "500", "700"],
});
```

```javascript
// tailwind.config.js
fontFamily: {
  sans: [
    "var(--font-roboto-mono)",
    "var(--font-inter)",
    "-apple-system",
    "BlinkMacSystemFont",
    "Segoe UI",
    "sans-serif",
  ],
  mono: ["var(--font-roboto-mono)", "Roboto Mono", "monospace"],
}
```

### Design Patterns (playbooks.com-inspired)

- **Max-width containers**: `max-w-5xl` (1280px)
- **No border radius**: Buttons use `rounded-none`
- **Tight tracking**: Uppercase uses `tracking-[0.12em]` and `tracking-[0.3em]`
- **Muted colors**: Low opacity for subtle elements
- **Section dividers**: `//` mono separators between sections
- **Grid layouts**: 2/3-1/3 hero split, 3-column feature grids
- **Small fonts**: Navigation uses `text-xs`, body uses `text-sm`

## Core Components

### 1. Dark/Light Toggle with Sun/Moon

```typescript
"use client";

import { useState, useEffect } from "react";
import { Sun, Moon } from "lucide-react";

export function ThemeToggle() {
  const [isDark, setIsDark] = useState(true);

  useEffect(() => {
    const saved = localStorage.getItem("theme");
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    const shouldBeDark = saved === "dark" || (!saved && prefersDark);
    setIsDark(shouldBeDark);
    document.documentElement.classList.toggle("dark", shouldBeDark);
  }, []);

  const toggleTheme = () => {
    const newDark = !isDark;
    setIsDark(newDark);
    localStorage.setItem("theme", newDark ? "dark" : "light");
    document.documentElement.classList.toggle("dark", newDark);
  };

  return (
    <button
      onClick={toggleTheme}
      className="p-1 rounded-none hover:bg-accent hover:text-accent-foreground transition-colors"
      aria-label="Toggle theme"
    >
      {isDark ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
    </button>
  );
}
```

### 2. Hero Section

```tsx
<section className="mx-auto max-w-5xl">
  <div className="grid gap-8 lg:grid-cols-[2fr_1fr] lg:gap-16">
    <div className="flex flex-col items-start gap-2 text-left">
      <h1 className="text-3xl font-bold leading-snug tracking-tighter md:text-4xl">
        Main heading with
        <span className="bg-gradient-to-r from-[#9945FF] to-[#14F195] bg-clip-text text-transparent">
          gradient accent
        </span>
      </h1>
      <p className="text-xl text-muted-foreground">Subheading description</p>
    </div>
    <div className="flex flex-col justify-center">{/* Sidebar content */}</div>
  </div>
</section>
```

### 3. Form Styling

```tsx
<input
  type="email"
  className="bg-input/30 border-input placeholder:text-muted-foreground/50 h-11 w-full border px-4 text-sm transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50"
/>

<button
  type="submit"
  className="bg-primary text-primary-foreground shadow-xs hover:bg-primary/90 inline-flex cursor-pointer items-center justify-center gap-2 whitespace-nowrap rounded-none font-medium text-sm outline-none transition-all focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 h-11 px-6"
>
  Button text
</button>
```

### 4. Section Dividers

```tsx
<div
  className="font-mono text-sm text-muted-foreground/30 select-none"
  aria-hidden="true"
>
  //
</div>
```

### 5. Feature Cards

```tsx
<div className="space-y-2">
  <div className="font-mono text-sm text-muted-foreground">01</div>
  <h3 className="font-medium">Feature Title</h3>
  <p className="text-sm text-muted-foreground">Feature description</p>
</div>
```

### 6. Busy Terminal Cards (Git Diff/Code Style)

Create "busy" cards that show activity, terminal output, or git diffs. Use these to make landing pages feel alive and active.

**Git Diff Card Pattern:**

```tsx
<div className="bg-card border-border rounded-lg border p-4 space-y-3">
  <div className="flex items-center gap-2">
    <span className="text-muted-foreground">$</span>
    <span className="text-foreground">replicas connect update-changelog</span>
  </div>

  <div className="flex items-center gap-3">
    <span className="text-sm text-muted-foreground">feat/analytics</span>
    <div className="flex gap-2">
      <span className="text-green-500 text-sm">+</span>
      <span className="text-foreground text-sm">1247</span>
      <span className="text-red-500 text-sm">-</span>
      <span className="text-foreground text-sm">89</span>
    </div>
  </div>

  <button className="bg-muted hover:bg-muted/80 text-muted-foreground text-xs px-3 py-1.5 rounded transition-colors">
    Copy command
  </button>
</div>
```

**Terminal Activity Grid:**

```tsx
<div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
  {[
    {
      cmd: "replicas connect fix-auth-race",
      branch: "fix/auth-middleware",
      add: 12,
      del: 456,
    },
    {
      cmd: "replicas connect refactor-ml-jobs",
      branch: "refactor/data-processing",
      add: 3412,
      del: 2178,
    },
    {
      cmd: "replicas connect revamp-ui",
      branch: "feat/dark-mode",
      add: 834,
      del: 45,
    },
  ].map((item) => (
    <div
      key={item.cmd}
      className="bg-card border-border rounded-lg border p-4 space-y-3"
    >
      <div className="flex items-center gap-2">
        <span className="text-muted-foreground">$</span>
        <span className="text-foreground text-sm">{item.cmd}</span>
      </div>

      <div className="flex items-center gap-3">
        <span className="text-xs text-muted-foreground">{item.branch}</span>
        <div className="flex gap-2">
          <span className="text-green-500 text-xs">+</span>
          <span className="text-foreground text-xs">{item.add}</span>
          <span className="text-red-500 text-xs">-</span>
          <span className="text-foreground text-xs">{item.del}</span>
        </div>
      </div>

      <button className="bg-muted hover:bg-muted/80 text-muted-foreground text-xs px-3 py-1.5 rounded transition-colors">
        Copy command
      </button>
    </div>
  ))}
</div>
```

**Busy Terminal Animation (Optional):**

```tsx
import { motion } from "framer-motion";

<motion.div
  initial={{ opacity: 0, y: 10 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.3, delay: index * 0.05 }}
  className="bg-card border-border rounded-lg border p-4"
>
  {/* Card content */}
</motion.div>;
```

**Color Tokens for Git Diffs:**

```css
--git-add: 34 197% 39%; /* Green */
--git-delete: 0 84% 60%; /* Red */
--git-modify: 253 95% 53%; /* Yellow/Orange */
```

### 7. Gradient Background (Optional)

```css
.gradient-bg {
  background: radial-gradient(
    ellipse 80% 50% at 50% -20%,
    rgba(153, 69, 255, 0.15),
    transparent
  );
}
```

## Usage Pattern

When you need to create a landing page:

1. Tell Claude: "Build me a landing page for [company/product] with [description]"
2. Claude will use this skill to generate:
   - Complete page structure
   - Dark/light toggle implementation
   - Roboto Mono typography
   - Solana color scheme
   - Playbooks.com-inspired layout
   - Busy terminal/git-diff cards (for dev tools, CLI products)
   - Optional motion with framer-motion

3. Review and adjust as needed

## Implementation Notes

### Font Strategy

Remove all `font-mono` classes from components. Let the default font stack handle typography uniformly. This keeps code clean and allows global font changes.

### Responsive Breakpoints

- **Mobile (< md)**: Stacked layout
- **Tablet (md-lg)**: Grid with 2 columns
- **Desktop (lg)**: Full layout with max-width containers

### Busy Card Motion Guidelines

**Stagger animations for grid entries:**

```tsx
{
  items.map((item, index) => (
    <motion.div
      key={item.id}
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{
        duration: 0.3,
        delay: index * 0.05, // Stagger each card
        ease: "easeOut",
      }}
    >
      {/* Card content */}
    </motion.div>
  ));
}
```

**Hover lift effect:**

```tsx
<motion.div
  whileHover={{ y: -4, boxShadow: "0 10px 30px -10px rgba(153, 69, 255, 0.3)" }}
  transition={{ duration: 0.2 }}
>
  {/* Card content */}
</motion.div>
```

**Loading skeleton for busy cards:**

```tsx
<div className="animate-pulse space-y-3">
  <div className="h-4 w-3/4 bg-muted rounded"></div>
  <div className="h-8 w-full bg-muted rounded"></div>
  <div className="h-4 w-1/2 bg-muted rounded"></div>
</div>
```

### Button States

```tsx
// Primary action button
<button className="bg-primary text-primary-foreground hover:bg-primary/90">

// Secondary/outlined button
<button className="border bg-background hover:bg-accent hover:text-accent-foreground">

// Disabled state
<button disabled className="opacity-50 disabled:cursor-not-allowed">
```

## Variations

### Busy Cards for Dev Products

**When to use:** CLI tools, developer platforms, version control, API documentation, terminal-based products.

**Patterns:**

1. **Terminal Activity Grid** (replicas.dev style):
   - Multiple cards showing concurrent activity
   - Git diff stats with green/red colors
   - Command prompts with `$` prefix
   - Copy buttons for reuse

2. **Code Snippet Cards**:
   - Syntax-highlighted code blocks
   - File path indicators
   - Line numbers
   - Language badges (TS, JS, Go, etc.)

3. **Process Flow Cards**:
   - Step-by-step execution visualization
   - Checkmark `✓` animations
   - Progress indicators
   - Terminal output sections

### Gradient Accents

The Solana gradient works best for:

- Headline text: `bg-gradient-to-r from-[#9945FF] to-[#14F195] bg-clip-text text-transparent`
- Button backgrounds: `bg-gradient-to-r from-[#9945FF] to-[#14F195]`
- Icon containers: `bg-gradient-to-br from-[#9945FF] to-[#14F195]`

### Content Sections

Common landing page sections:

1. **Hero**: Value proposition + email capture
2. **Features**: 3-column grid with numbered items
3. **FAQ**: Grid of Q&A pairs
4. **Footer**: Links, copyright, optional CTA

### Badge Components

```tsx
<span className="border-border bg-muted/20 text-muted-foreground px-3 py-1.5 text-sm border">
  Badge text
</span>
```

### Waitlist or contact form

A separate n8n endpoint that accepts JSON blobs. Use this lib:

```typescript
export async function addToWaitlist(args: Record<string, string>) {
  const n8nWebhookUrl = process.env.NEXT_PUBLIC_N8N_WEBHOOK_URL;

  if (!n8nWebhookUrl) {
    throw new Error(
      "N8N webhook URL not configured. Please set NEXT_PUBLIC_N8N_WEBHOOK_URL environment variable.",
    );
  }

  try {
    const response = await fetch(n8nWebhookUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        ...args,
        timestamp: new Date().toISOString(),
      }),
    });

    if (!response.ok) {
      throw new Error(`N8N webhook failed: ${response.statusText}`);
    }

    await response.json();
  } catch (error) {
    console.error("Failed to add to waitlist:", error);
    throw error;
  }
}
```

## Common Pitfalls

- **Don't mix font classes**: Keep typography consistent - remove `font-mono` explicit classes
- **Don't add border-radius**: Use `rounded-none` for buttons to match design system
- **Don't hardcode theme**: Use toggle with localStorage persistence
- **Don't over-use gradients**: Subtle radial gradient only for background, inline for specific elements
- **Don't overuse busy cards**: Limit to 6-9 visible cards at once. More causes visual fatigue
- **Don't animate everything**: Only animate entry (initial load) and hover states. Continuous animations distract
- **Don't ignore performance**: Lazy-load busy card grids beyond viewport. Use `loading="lazy"` on images

## Example Output

See to the landing page for a complete implementation of this design system:

- Dark/light toggle in header
- Roboto Mono everywhere
- Solana purple/teal gradients
- Playbooks.com-inspired grid layouts
- Section dividers with `//`
- No border radius on buttons

For busy terminal card patterns, see replicas.dev or moltbay.com for reference implementations.

For busy terminal card patterns, see replicas.dev or moltbay.com for reference implementations.
