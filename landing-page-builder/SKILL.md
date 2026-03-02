---
name: landing-page-builder
description: Build modern landing pages with dark/light theme toggle, Roboto Mono typography, and Solana-inspired color scheme. Use when you need to create a sleek, minimalist landing page with playbooks.com-inspired design patterns, gradient accents, and smooth transitions.
---

# Landing Page Builder

Build modern, high-conversion landing pages with a dark/light toggle, Roboto Mono typography, and Solana color scheme. This skill provides the complete design system and component patterns used to create the Vyne landing page.

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

### 6. Gradient Background (Optional)

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
   - Optional motion with framer-motion

3. Review and adjust as needed

## Implementation Notes

### Font Strategy

Remove all `font-mono` classes from components. Let the default font stack handle typography uniformly. This keeps code clean and allows global font changes.

### Responsive Breakpoints

- **Mobile (< md)**: Stacked layout
- **Tablet (md-lg)**: Grid with 2 columns
- **Desktop (lg)**: Full layout with max-width containers

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

## Example Output

See the Vyne landing page for a complete implementation of this design system:

- Dark/light toggle in header
- Roboto Mono everywhere
- Solana purple/teal gradients
- Playbooks.com-inspired grid layouts
- Section dividers with `//`
- No border radius on buttons
