# Component Reference Patterns

Reusable component patterns for playbooks.com-inspired landing pages.

## Theme Toggle

```tsx
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

**Usage**: Place in navigation bar, after logo/brand element.

## Header

```tsx
<header className="py-6">
  <div className="mx-auto flex w-full max-w-5xl flex-col gap-4 px-4 md:flex-row md:items-center md:justify-between">
    <a className="inline-flex text-primary" href="/">
      <span className="font-semibold text-xs uppercase tracking-[0.3em]">
        Brand
      </span>
    </a>
    <div className="flex w-full flex-col gap-4 md:w-auto md:flex-row md:items-center md:justify-end md:gap-6">
      <nav className="flex flex-wrap items-center gap-4 text-muted-foreground text-xs uppercase tracking-[0.12em]">
        <a className="transition-colors hover:text-foreground" href="/">
          Home
        </a>
        <a className="transition-colors hover:text-foreground" href="/about">
          About
        </a>
        <ThemeToggle />
        <div className="flex items-center gap-2">
          <span className="text-muted-foreground text-xs uppercase tracking-[0.12em] transition-colors">
            Status
          </span>
        </div>
      </nav>
    </div>
  </div>
</header>
```

**Key classes**:
- Container: `max-w-5xl` with `px-4`
- Layout: `flex-col` on mobile, `md:flex-row` on desktop
- Logo: `text-primary`, `uppercase tracking-[0.3em]`
- Navigation: `text-xs uppercase tracking-[0.12em]`

## Hero Section

```tsx
<section className="mx-auto max-w-5xl">
  <div className="grid gap-8 lg:grid-cols-[2fr_1fr] lg:gap-16">
    <div className="flex flex-col items-start gap-2 text-left">
      <h1 className="text-3xl font-bold leading-snug tracking-tighter md:text-4xl">
        Main heading
      </h1>
      <p className="text-xl text-muted-foreground">
        Subheading description
      </p>
      {/* Form or CTA */}
    </div>
    <div className="flex flex-col justify-center">
      {/* Sidebar content - badges, stack, etc. */}
    </div>
  </div>
</section>
```

**Layout**: 2/3 split on large screens (`lg:grid-cols-[2fr_1fr]`)

## Badge Component

```tsx
<span className="border-border bg-muted/20 text-muted-foreground px-3 py-1.5 text-sm border">
  Badge text
</span>
```

**Use cases**: Technology stack, features, tags, status indicators

## Section Divider

```tsx
<div className="font-mono text-sm text-muted-foreground/30 select-none" aria-hidden="true">
  //
</div>
```

**Purpose**: Visual separator between major sections

## Feature Card

```tsx
<div className="space-y-2">
  <div className="font-mono text-sm text-muted-foreground">01</div>
  <h3 className="font-medium">Feature Title</h3>
  <p className="text-sm text-muted-foreground">
    Feature description
  </p>
</div>
```

**Pattern**: Numbered items with mono numbers, sans headings

## Input Field

```tsx
<input
  type="email"
  placeholder="your@email.com"
  className="bg-input/30 border-input placeholder:text-muted-foreground/50 h-11 w-full border px-4 text-sm transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50"
/>
```

**Classes breakdown**:
- Background: `bg-input/30` (subtle)
- Border: `border-input` (muted)
- Height: `h-11` (44px)
- Text: `text-sm` (14px)
- Focus: `ring-1` on `ring-ring` color

## Buttons

### Primary Button
```tsx
<button className="bg-primary text-primary-foreground shadow-xs hover:bg-primary/90 inline-flex cursor-pointer items-center justify-center gap-2 whitespace-nowrap rounded-none font-medium text-sm outline-none transition-all focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 h-11 px-6">
  Button text
</button>
```

### Secondary/Outlined Button
```tsx
<button className="border bg-background shadow-xs hover:bg-accent hover:text-accent-foreground inline-flex cursor-pointer items-center justify-center gap-2 whitespace-nowrap rounded-none font-medium text-sm outline-none transition-all focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 h-11 px-6">
  Button text
</button>
```

**Key patterns**:
- `rounded-none` - No border radius
- `shadow-xs` - Subtle shadow
- `h-11` - Consistent height
- `px-6` - Consistent padding
- Focus states with `ring`

## FAQ Grid

```tsx
<section className="mx-auto max-w-5xl">
  <div className="mb-8 max-w-2xl space-y-3">
    <h2 className="text-xl font-semibold">Section heading</h2>
    <p className="text-muted-foreground">Section description</p>
  </div>
  <div className="grid gap-8 md:grid-cols-3">
    <div className="space-y-2">
      <div className="font-mono text-sm text-muted-foreground">01</div>
      <h3 className="font-medium">Question</h3>
      <div className="space-y-2 text-sm text-muted-foreground">
        <p>Answer paragraph 1</p>
        <p>Answer paragraph 2</p>
      </div>
    </div>
    {/* More cards */}
  </div>
</section>
```

**Layout**: 3 columns on tablet and up (`md:grid-cols-3`)

## Footer

```tsx
<footer className="container mx-auto mt-auto max-w-5xl px-4">
  <div className="flex items-center justify-between border-t border-border/50 py-6">
    <div className="flex items-center gap-4 font-mono text-xs text-muted-foreground">
      <span className="font-semibold uppercase tracking-[0.3em]">
        Brand
      </span>
      <div className="flex items-center gap-1">
        <a href="/privacy" className="transition-colors hover:text-foreground">
          Privacy
        </a>
        <span className="px-1">/</span>
        <a href="/terms" className="transition-colors hover:text-foreground">
          Terms
        </a>
      </div>
    </div>
    <div className="font-mono text-xs text-muted-foreground">
      © 2026 Brand
    </div>
  </div>
</footer>
```

**Key classes**:
- Border top: `border-t border-border/50`
- Text size: `text-xs` for footer elements
