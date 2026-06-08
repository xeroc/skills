# Swiss Design — Extracted Component Patterns

Components extracted from the Swiss Design System showcase. These use the stone palette and accent color system. Adapt colors to your project's palette while keeping the structural patterns.

---

## Fixed Navigation with Backdrop Blur

```html
<nav
  class="fixed top-0 left-0 right-0 z-50 border-b border-stone-200 dark:border-stone-800 bg-stone-50/90 dark:bg-stone-950/90 backdrop-blur-sm"
>
  <div class="max-w-6xl mx-auto px-8 flex items-center justify-between h-14">
    <a
      href="/"
      class="text-xs tracking-widest uppercase font-medium text-stone-900 dark:text-stone-50"
    >
      Brand Name
    </a>
    <div
      class="hidden md:flex items-center gap-6 text-xs tracking-widest uppercase"
    >
      <a
        href="#section"
        class="text-stone-900/60 dark:text-stone-50/60 hover:text-stone-900 dark:hover:text-stone-50 transition-colors"
        >Section</a
      >
    </div>
    <div class="flex items-center gap-4">
      <button
        class="w-8 h-8 flex items-center justify-center border border-stone-300 dark:border-stone-700 hover:border-stone-500 dark:hover:border-stone-500 transition-colors"
        aria-label="Toggle dark mode"
      >
        <span class="dark:hidden text-xs text-stone-900">&#x25CB;</span>
        <span class="hidden dark:inline text-xs text-stone-50">&#x25CF;</span>
      </button>
    </div>
  </div>
</nav>
```

---

## Section Label (Numbered Header + Divider)

Used consistently across all Swiss sections. Provides numbered structure.

```html
<div class="flex items-center gap-4 mb-20">
  <span
    class="text-xs font-mono font-medium text-stone-900/60 dark:text-stone-50/60"
    >01</span
  >
  <span
    class="text-xs tracking-widest uppercase font-medium text-stone-900/80 dark:text-stone-50/80"
    >Section Name</span
  >
  <div class="flex-1 h-px bg-stone-300 dark:border-stone-700"></div>
</div>
```

---

## Pull Quote with Accent Bar

```html
<div class="flex gap-4">
  <div class="w-0.5 bg-[#C8102E] self-stretch shrink-0"></div>
  <div>
    <p
      class="text-2xl font-normal leading-snug tracking-tight text-stone-900 dark:text-stone-50"
    >
      "The will to order."
    </p>
    <span
      class="text-xs tracking-widest uppercase text-stone-900/50 dark:text-stone-50/50 mt-3 block"
      >Attribution</span
    >
  </div>
</div>
```

---

## Key Principles Card (Accent Top Bar)

```html
<div
  class="border-t-2 border-[#C8102E] pt-6 bg-stone-100 dark:bg-stone-900 p-6"
>
  <span
    class="text-xs tracking-widest uppercase text-stone-900/60 dark:text-stone-50/60 block mb-5"
    >Key principles</span
  >
  <ul class="space-y-3">
    <li
      class="text-base text-stone-900/80 dark:text-stone-50/80 flex items-start gap-2"
    >
      <span class="text-[#C8102E] mt-0.5 shrink-0">—</span>
      <span>Principle text</span>
    </li>
  </ul>
</div>
```

---

## Geometric Decorations

## Concentric Circles

```html
<div
  class="absolute -top-16 -right-16 w-64 h-64 rounded-full border border-stone-700 pointer-events-none"
></div>
<div
  class="absolute -top-8 -right-8 w-64 h-64 rounded-full border border-stone-700 pointer-events-none"
></div>
<div
  class="absolute top-4 right-4 w-64 h-64 rounded-full border border-stone-700 pointer-events-none"
></div>
```

## CSS Triangle

```html
<div
  class="absolute bottom-0 left-0 w-32 h-32 bg-[#003B8E]/30 pointer-events-none"
  style="clip-path: polygon(0 100%, 100% 100%, 0 0)"
></div>
```

## Large Background Numeral

```html
<div
  class="absolute top-0 right-0 text-[clamp(10rem,28vw,26rem)] font-light leading-none text-stone-900/5 dark:text-stone-50/5 select-none pointer-events-none translate-x-8"
>
  01
</div>
```

## Large Triangle (Full Section)

```html
<div
  class="absolute -top-24 -right-24 w-96 h-96 pointer-events-none opacity-10"
  style="clip-path: polygon(100% 0, 0 0, 100% 100%); background-color: #C8102E;"
></div>
```

## Circle (Bottom-left)

```html
<div
  class="absolute -bottom-16 -left-16 w-64 h-64 rounded-full border border-stone-700 pointer-events-none"
></div>
```

---

## Accent Color Block Card

```html
<div
  class="border border-stone-200 dark:border-stone-800 p-5 flex items-start gap-4"
>
  <div class="w-8 h-8 shrink-0 mt-0.5" style="background-color: #C8102E"></div>
  <div>
    <p class="text-sm font-medium text-stone-900 dark:text-stone-50">
      Swiss Red
    </p>
    <p class="text-xs text-stone-900/50 dark:text-stone-50/50 font-mono mt-0.5">
      #C8102E
    </p>
    <p
      class="text-sm text-stone-900/60 dark:text-stone-50/60 mt-2 leading-relaxed"
    >
      Bold and assertive.
    </p>
  </div>
</div>
```

---

## Hover Effect Card (with Geometric Accent)

```html
<a
  href="#"
  class="bg-stone-50 dark:bg-stone-950 p-8 flex flex-col gap-6 hover:bg-white dark:hover:bg-stone-900 transition-colors group relative overflow-hidden"
>
  <!-- Geometric accent: small circle top-right -->
  <div
    class="absolute top-4 right-4 w-12 h-12 rounded-full border-2 pointer-events-none opacity-20 group-hover:opacity-40 transition-opacity"
    style="border-color: #C8102E"
  ></div>
  <div class="flex items-start justify-between">
    <div class="w-10 h-10" style="background-color: #C8102E;"></div>
    <span
      class="text-sm font-mono font-medium text-stone-900/70 dark:text-stone-50/70"
      >1962</span
    >
  </div>
  <div>
    <div class="w-6 h-px mb-4" style="background-color: #C8102E"></div>
    <span
      class="text-xs tracking-widest uppercase font-medium text-stone-900/70 dark:text-stone-50/70 block mb-2"
      >Label</span
    >
    <h3
      class="text-xl font-medium text-stone-900 dark:text-stone-50 leading-snug"
    >
      Title
    </h3>
    <p
      class="text-sm text-stone-900/70 dark:text-stone-50/70 leading-relaxed mt-3 max-w-[32ch]"
    >
      Description text.
    </p>
  </div>
  <div
    class="mt-auto pt-4 border-t border-stone-200 dark:border-stone-800 flex items-center justify-between"
  >
    <span
      class="text-xs tracking-widest uppercase font-medium px-2 py-1"
      style="background-color: rgba(200,16,46,0.15); color: #C8102E"
      >Tag</span
    >
    <span
      class="text-stone-900/50 dark:text-stone-50/50 text-sm group-hover:text-stone-900 dark:group-hover:text-stone-50 transition-colors"
      >↗</span
    >
  </div>
</a>
```

---

## 1px Grid Gap Card Layout

```html
<div
  class="grid grid-cols-1 md:grid-cols-3 gap-px bg-stone-200 dark:bg-stone-800"
>
  <!-- Cards use bg-stone-50 dark:bg-stone-950 for the 1px gap effect -->
</div>
```

---

## Key-Value Metadata Row

```html
<div class="grid grid-cols-2 gap-4 mb-8">
  <div>
    <span
      class="text-xs tracking-widest uppercase text-stone-900/40 dark:text-stone-50/40 block mb-1"
      >Label</span
    >
    <span class="text-sm text-stone-900 dark:text-stone-50">Value</span>
  </div>
</div>
```

---

## Progress Bar (Inline)

```html
<div class="flex items-center justify-end gap-2">
  <div class="w-16 h-0.5 bg-stone-200 dark:bg-stone-800 relative">
    <div
      class="absolute left-0 top-0 h-full bg-[#C8102E]"
      style="width: 96%"
    ></div>
  </div>
  <span class="text-sm font-mono text-stone-900/60 dark:text-stone-50/60 w-6"
    >96</span
  >
</div>
```

---

## Featured Row Highlight

```html
<tr
  class="border-b border-stone-200 dark:border-stone-800 hover:bg-stone-100 dark:hover:bg-stone-900 transition-colors bg-[#C8102E]/5"
>
  <td class="py-4 pr-6 pl-4">
    <span class="text-stone-900 dark:text-stone-50 font-normal">Item name</span>
    <span
      class="ml-2 text-xs tracking-widest uppercase bg-[#C8102E]/10 text-[#C8102E] px-1.5 py-0.5"
      >Primary</span
    >
  </td>
</tr>
```

---

## List Item Row (App-style)

```html
<div
  class="border-t border-stone-200 dark:border-stone-800 py-4 flex items-center justify-between hover:bg-stone-50 dark:hover:bg-stone-900/50 px-2 -mx-2 transition-colors cursor-pointer"
>
  <div class="flex items-center gap-4">
    <div
      class="w-6 h-6 border border-stone-200 dark:border-stone-800 flex items-center justify-center"
    >
      <span class="text-[9px] font-mono text-stone-900/50 dark:text-stone-50/50"
        >Aa</span
      >
    </div>
    <span class="text-base text-stone-900 dark:text-stone-50">Item name</span>
  </div>
  <div class="flex items-center gap-8">
    <span class="text-sm text-stone-900/60 dark:text-stone-50/60"
      >Metadata</span
    >
    <span class="text-sm font-mono text-stone-900/50 dark:text-stone-50/50"
      >Year</span
    >
  </div>
</div>
```

---

## Grayscale Swatch Grid

```html
<div
  class="grid grid-cols-5 md:grid-cols-11 gap-px bg-stone-200 dark:bg-stone-800"
>
  <div
    class="aspect-square flex flex-col justify-end p-2"
    style="background-color: #fafaf9"
  >
    <span class="text-[10px] font-mono" style="color: #1c1917; opacity: 0.6"
      >50</span
    >
  </div>
  <!-- repeat for each scale -->
</div>
```

---

## Accent Opacity Strip

```html
<div class="space-y-1">
  <div class="h-10 flex items-center px-3 relative overflow-hidden">
    <div
      class="absolute inset-0"
      style="background-color: #C8102E; opacity: 1;"
    ></div>
    <span class="relative text-xs font-mono" style="color: white">100%</span>
  </div>
  <div class="h-10 flex items-center px-3 relative overflow-hidden">
    <div
      class="absolute inset-0"
      style="background-color: #C8102E; opacity: 0.6;"
    ></div>
    <span class="relative text-xs font-mono" style="color: white">60%</span>
  </div>
  <div class="h-10 flex items-center px-3 relative overflow-hidden">
    <div
      class="absolute inset-0"
      style="background-color: #C8102E; opacity: 0.2;"
    ></div>
    <span class="relative text-xs font-mono" style="color: #C8102E">20%</span>
  </div>
  <div class="h-10 flex items-center px-3 relative overflow-hidden">
    <div
      class="absolute inset-0"
      style="background-color: #C8102E; opacity: 0.1;"
    ></div>
    <span class="relative text-xs font-mono" style="color: #C8102E">10%</span>
  </div>
</div>
```

---

## Footer (Minimal)

```html
<footer class="border-t border-stone-200 dark:border-stone-800">
  <div
    class="max-w-6xl mx-auto px-8 py-16 flex flex-col md:flex-row items-start md:items-center justify-between gap-8"
  >
    <div>
      <span
        class="text-sm tracking-widest uppercase font-medium text-stone-900 dark:text-stone-50"
        >Brand Name</span
      >
      <p class="text-sm text-stone-900/50 dark:text-stone-50/50 mt-2">
        Tagline text
      </p>
    </div>
    <div class="flex items-center gap-8 flex-wrap">
      <a
        href="#"
        class="text-sm tracking-widest uppercase text-stone-900/50 dark:text-stone-50/50 hover:text-stone-900 dark:hover:text-stone-50 transition-colors"
      >
        Link ↗
      </a>
    </div>
  </div>
</footer>
```

---

## Dark Mode Toggle Script

```html
<script>
  // Apply stored preference immediately (no flash)
  (function () {
    var stored = localStorage.getItem("theme");
    var prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    if (stored === "dark" || (!stored && prefersDark)) {
      document.documentElement.classList.add("dark");
    }
  })();

  function toggleDark() {
    var html = document.documentElement;
    html.classList.toggle("dark");
    localStorage.setItem(
      "theme",
      html.classList.contains("dark") ? "dark" : "light",
    );
  }

  window
    .matchMedia("(prefers-color-scheme: dark)")
    .addEventListener("change", function (e) {
      if (!localStorage.getItem("theme")) {
        document.documentElement.classList.toggle("dark", e.matches);
      }
    });
</script>
```

## 18.2. Section Separators

Use subtle visual separators between sections:

```tsx
// Terminal-style comment separator
<div className="font-mono text-sm text-muted-foreground/30 select-none" aria-hidden="true">
  //
</div>

// Or a simple border
<div className="border-t border-border/50" />
```

## 18.3. Clean Card Layout

Use simple borders instead of shadows and gradients:

```tsx
// ✗ DON'T - too much visual noise
<div className="rounded-2xl shadow-lg border hover:shadow-xl hover:-translate-y-1 hover:border-primary/20">
  <div className="bg-gradient-to-br ...">
    Content
  </div>
</div>

// ✅ DO - clean and focused
<div className="border border-border/50 hover:border-primary/30 transition-all p-6">
  Content
</div>
```

## 18.4. Stats Section

Display key metrics prominently in the hero:

```tsx
const stats = [
  { label: "Metric 1", value: "100" },
  { label: "Metric 2", value: "99%" },
];

<div className="flex flex-col justify-center space-y-4">
  {stats.map((stat) => (
    <div key={stat.label} className="space-y-2">
      <div className="font-mono text-sm text-muted-foreground">
        {stat.label}
      </div>
      <div className="text-2xl font-bold">{stat.value}</div>
    </div>
  ))}
</div>;
```

## 18.5. Typography Hierarchy

Use consistent typography with `uppercase tracking-[0.12em]` for nav/labels:

```tsx
// Navigation and labels
<span className="text-xs uppercase tracking-[0.12em] text-muted-foreground">
  SECTION LABEL
</span>

// Headings
<h1 className="text-3xl font-bold tracking-tight">
  Main Heading
</h1>

// Body
<p className="text-muted-foreground leading-relaxed">
  Body text with comfortable reading width
</p>
```

## 19. Troubleshooting

## 19.1. HashRouter Not Working

Ensure you're using `HashRouter` (not `BrowserRouter`) in `src/main.tsx`:

```tsx
import { HashRouter } from "react-router-dom";
```

## 19.2. Tailwind Classes Not Working

Check that `src/globals.css` has the import:

```css
@import "tailwindcss";
```

And that `postcss.config.cjs` uses the correct plugin:

```javascript
module.exports = {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};
```

## 19.3. Theme Toggle Not Persisting

`ThemeToggle` component saves to `localStorage`. Check browser console for errors.

## 19.4. n8n Webhook Fails

Check that:

- `.env` file exists in project root (not `src/`)
- Variable name is `VITE_N8N_WEBHOOK_URL` (with `VITE_` prefix)
- Restart dev server after adding `.env`

## 19.5. GitHub Pages 404s

Ensure:

- `base: "./"` is set in `vite.config.ts`
- GitHub Pages source is set to **GitHub Actions** (not `gh-pages` branch)
- GitHub Actions workflow deploys `./dist` folder

## 19.6. "outline-none is deprecated" Warning

In Tailwind v4, use `outline-hidden` instead:

```tsx
<input className="focus:outline-hidden" />
```

## 19.7. Shadow Scale in Tailwind v4

Tailwind v4 provides: `shadow-xs`, `shadow-sm`, `shadow`, `shadow-md`, `shadow-lg`, `shadow-xl`, `shadow-2xl`.

## 20. Landing Page Section Templates

Reusable section components for building landing pages. Each section is self-contained and follows the ChainSquad dark-theme aesthetic. Sections are separated by `space-y-36` on the parent wrapper.

## 20.0. Page Wrapper Pattern

All sections live inside a single wrapper `<div>` with generous vertical spacing:

```tsx
export default function Home(): JSX.Element {
  return <div className="space-y-36">{/* ── Sections go here ── */}</div>;
}
```

## 20.1. Hero Section

**Use when:** Every landing page needs one. First thing visitors see. Sets the tone.

**Structure:** Gradient background blobs → headline with `gradient-text` accent → subtitle → CTA button row (primary + secondary).

```tsx
{
  /* ── Hero ── */
}
<section className="relative pt-24 pb-12 overflow-hidden">
  {/* Background glow blobs */}
  <div className="absolute inset-0 overflow-hidden pointer-events-none">
    <div className="absolute top-1/3 left-1/4 w-[700px] h-[700px] bg-primary/4 rounded-full blur-[140px]" />
    <div className="absolute bottom-0 right-1/4 w-[500px] h-[500px] bg-secondary/4 rounded-full blur-[120px]" />
  </div>
  <div className="relative max-w-4xl mx-auto text-center px-6">
    <h1 className="text-5xl md:text-7xl font-bold mb-6 leading-[1.06] tracking-tight">
      <span className="text-white">The REST API for</span>
      <br />
      <span className="gradient-text">Solana programs.</span>
    </h1>
    <p className="text-lg md:text-xl text-gray-400 mb-10 max-w-2xl mx-auto leading-relaxed">
      Upload your Anchor IDL. Get a production REST API, AI-ready docs, and an
      MCP server — in 30 seconds. No backend code, no SDK, no infrastructure.
    </p>
    <div className="flex flex-col sm:flex-row justify-center gap-4">
      <a href="#" className="btn-primary text-base px-8 py-4">
        Primary CTA
      </a>
      <Link to="/page" className="btn-secondary text-base px-8 py-4">
        Secondary CTA
      </Link>
    </div>
  </div>
</section>;
```

**Key patterns:**

- Two overlapping radial glow blobs (primary + secondary, 4% opacity, 120-140px blur)
- Headline: `text-5xl md:text-7xl font-bold leading-[1.06] tracking-tight`
- Accent word uses `gradient-text` class
- Two CTAs: primary (filled) + secondary (outlined/ghost)
- Responsive: stacked on mobile, row on `sm:`

**Required CSS (add to globals.css):**

```css
.gradient-text {
  background: linear-gradient(
    135deg,
    var(--color-primary),
    var(--color-secondary)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.75rem;
  font-weight: 600;
  background: var(--color-primary);
  color: var(--color-primary-foreground);
  transition: opacity 0.2s;
}
.btn-primary:hover {
  opacity: 0.9;
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.75rem;
  font-weight: 600;
  border: 1px solid var(--color-border);
  color: var(--color-foreground);
  transition: border-color 0.2s;
}
.btn-secondary:hover {
  border-color: var(--color-primary);
}
```

---

## 20.2. How It Works (Steps Section)

**Use when:** Explaining a multi-step process. Onboarding flows, product demos, getting-started guides.

**Structure:** Centered heading → horizontal connecting line → 4-column grid with numbered icon cards.

```tsx
{
  /* ── How It Works ── */
}
<section className="max-w-6xl mx-auto px-6">
  <div className="text-center mb-12">
    <h2 className="text-3xl md:text-4xl font-bold mb-4">
      <span className="text-white">How </span>
      <span className="gradient-text">It Works</span>
    </h2>
    <p className="text-gray-400 max-w-2xl mx-auto">
      From zero to production in four steps. No backend code, no devops.
    </p>
  </div>
  <div className="relative">
    {/* Horizontal connecting line (desktop only) */}
    <div className="hidden md:block absolute top-8 left-[calc(12.5%+2rem)] right-[calc(12.5%+2rem)] h-px bg-gradient-to-r from-primary/10 via-primary/40 to-primary/10 pointer-events-none" />
    <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
      {steps.map(({ num, title, desc, accent, path }) => (
        <div key={num} className="flex flex-col items-center text-center group">
          <div
            className={`relative w-16 h-16 rounded-2xl bg-surface-elevated border border-${accent}/25 flex items-center justify-center mb-5 z-10 group-hover:border-${accent}/60 group-hover:bg-${accent}/10 transition-all duration-300`}
          >
            <svg
              className={`w-7 h-7 text-${accent}`}
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={1.5}
                d={path}
              />
            </svg>
            <span
              className={`absolute -top-2 -right-2 w-5 h-5 rounded-full bg-${accent} text-dark-900 text-xs font-bold flex items-center justify-center`}
            >
              {num}
            </span>
          </div>
          <h4 className="font-bold text-white mb-2 text-sm">{title}</h4>
          <p className="text-xs text-gray-400 leading-relaxed">{desc}</p>
        </div>
      ))}
    </div>
  </div>
</section>;
```

**Data shape:**

```tsx
const steps = [
  {
    num: "1",
    title: "Step Title",
    desc: "One-line description of what happens at this step.",
    accent: "primary",
    path: "M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z",
  },
  // ... repeat for 2-4 steps
];
```

**Key patterns:**

- Steps data array drives the grid
- SVG icons via inline `path` (Heroicons outlines)
- Numbered badge: `absolute -top-2 -right-2` on the icon container
- Horizontal gradient line connects steps on desktop (`hidden md:block`)
- Last step uses `accent: 'secondary'` to draw attention to the final action

---

## 20.3. Sidebar Feature Showcase

**Use when:** Showcasing multiple related features that users should browse interactively. API capabilities, tool comparisons, feature deep-dives.

**Structure:** Left-aligned heading → two-column layout with sticky vertical nav (left) and feature content panel (right). Nav items switch content via `useState`.

```tsx
{
  /* ── Sidebar feature section ── */
}
<section className="max-w-6xl mx-auto px-6">
  <div className="mb-16 max-w-2xl">
    <h2 className="text-3xl md:text-4xl font-bold mb-5 leading-tight">
      <span className="text-white">An API platform built for </span>
      <span className="gradient-text">developers.</span>
    </h2>
    <p className="text-gray-400 leading-relaxed text-lg">
      Description of the feature category.
    </p>
  </div>

  <div className="grid md:grid-cols-[220px_1fr] gap-12 items-start">
    {/* Left — vertical nav */}
    <nav className="flex flex-col md:sticky md:top-24">
      {features.map((f) => (
        <button
          key={f.id}
          onClick={() => setActiveFeature(f)}
          className={`text-left px-4 py-3.5 rounded-xl text-sm font-medium transition-all duration-200 flex items-center gap-2.5 ${
            activeFeature.id === f.id
              ? "text-white bg-surface-card border border-white/8"
              : "text-gray-500 hover:text-gray-300 hover:bg-surface-elevated"
          }`}
        >
          <span
            className={`w-1.5 h-1.5 rounded-full flex-shrink-0 transition-colors ${
              activeFeature.id === f.id ? "bg-primary" : "bg-gray-700"
            }`}
          />
          {f.label}
        </button>
      ))}
    </nav>

    {/* Right — content */}
    <div className="space-y-7">
      <div>
        <h3 className="text-2xl font-bold text-white mb-3 leading-snug">
          {activeFeature.heading}
        </h3>
        <p className="text-gray-400 leading-relaxed">{activeFeature.desc}</p>
      </div>
      <div className="flex flex-wrap gap-2">
        {activeFeature.bullets.map((b) => (
          <span
            key={b}
            className="flex items-center gap-1.5 text-sm text-gray-300 bg-surface-elevated border border-white/5 rounded-lg px-3 py-1.5"
          >
            <span className="w-1.5 h-1.5 rounded-full bg-primary flex-shrink-0" />
            {b}
          </span>
        ))}
      </div>
      <div className="rounded-2xl overflow-hidden border border-white/5">
        <CodeBlock
          language={activeFeature.language}
          code={activeFeature.code}
        />
      </div>
    </div>
  </div>
</section>;
```

**Data shape:**

```tsx
const features = [
  {
    id: "feature-id",
    label: "Short Label",
    heading: "Feature headline.",
    desc: "Longer description of the feature.",
    bullets: ["Bullet 1", "Bullet 2", "Bullet 3"],
    language: "bash" as const,
    code: `$ curl example.com\n\n# Response\n{ "key": "value" }`,
  },
  // ... more features
];
```

**State:**

```tsx
const [activeFeature, setActiveFeature] = useState(features[0]);
```

**Key patterns:**

- Sticky nav: `md:sticky md:top-24` keeps nav visible while scrolling content
- Active indicator: small dot (`w-1.5 h-1.5 rounded-full`) changes color
- Pill badges for feature bullets (`bg-surface-elevated border border-white/5 rounded-lg`)
- Code block in a rounded card container (`rounded-2xl overflow-hidden border border-white/5`)
- Grid columns: `md:grid-cols-[220px_1fr]` — fixed sidebar + fluid content

---

## 20.4. Editorial Section (Copy + Visual, Standard)

**Use when:** Deep-dive into a single feature. Best for the most important capability that needs long-form copy with a code/visual companion. Product pages, technical features.

**Structure:** Two-column grid. Left: tag label → headline → body → checklist with icons → CTA link. Right: terminal-style code card with traffic lights.

```tsx
{
  /* ── Editorial Section (Standard) ── */
}
<section className="max-w-6xl mx-auto px-6">
  <div className="grid md:grid-cols-2 gap-16 md:gap-20 items-center">
    {/* Copy — left */}
    <div className="space-y-8">
      <p className="text-xs text-primary font-bold uppercase tracking-[0.15em]">
        Feature Label
      </p>
      <h2 className="text-3xl md:text-4xl font-bold leading-tight">
        <span className="text-white">
          Headline part one
          <br />
          from{" "}
        </span>
        <span className="gradient-text">accent phrase.</span>
      </h2>
      <p className="text-gray-400 leading-relaxed text-[15px]">
        Long-form description of the feature. Two to three sentences.
      </p>
      <ul className="space-y-5">
        {checklistItems.map(({ title, desc }) => (
          <li key={title} className="flex items-start gap-4">
            <div className="w-5 h-5 rounded-full border border-primary/40 bg-primary/10 flex items-center justify-center flex-shrink-0 mt-0.5">
              <svg
                className="w-3 h-3 text-primary"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2.5}
                  d="M5 13l4 4L19 7"
                />
              </svg>
            </div>
            <div>
              <p className="text-white text-sm font-semibold mb-0.5">{title}</p>
              <p className="text-gray-500 text-sm leading-relaxed">{desc}</p>
            </div>
          </li>
        ))}
      </ul>
      <Link
        to="/page"
        className="inline-flex items-center gap-2 text-sm text-primary font-medium group"
      >
        <span>Link text</span>
        <span className="transition-transform group-hover:translate-x-1">
          →
        </span>
      </Link>
    </div>

    {/* Visual — right (terminal card) */}
    <div className="rounded-2xl overflow-hidden border border-white/5 bg-surface-elevated">
      <div className="flex items-center gap-2 px-5 py-4 border-b border-white/5">
        <div className="flex gap-1.5">
          <div className="w-2.5 h-2.5 rounded-full bg-red-500/40" />
          <div className="w-2.5 h-2.5 rounded-full bg-yellow-500/40" />
          <div className="w-2.5 h-2.5 rounded-full bg-green-500/40" />
        </div>
        <span className="text-xs text-gray-600 font-mono ml-2">
          filename.sh
        </span>
      </div>
      <CodeBlock
        language="bash"
        copyable={false}
        code={`$ command here\n\n# Output\n{ "result": "value" }`}
      />
    </div>
  </div>
</section>;
```

**Key patterns:**

- Tag label: `text-xs font-bold uppercase tracking-[0.15em]` — colored with the section accent
- Checklist items with circle check icons (`border-primary/40 bg-primary/10`)
- Arrow CTA link with hover animation (`group-hover:translate-x-1`)
- Terminal card: traffic light dots (`bg-red-500/40`, `bg-yellow-500/40`, `bg-green-500/40`) + filename
- Column gap: `gap-16 md:gap-20` — generous breathing room

---

## 20.5. Editorial Section (Reversed: Visual + Copy)

**Use when:** Same as standard editorial but for the second feature. Alternating layout creates visual rhythm. Use for the second or third deep-dive on the same page.

**Structure:** Same two-column grid but columns swapped. Visual on left, copy on right. Uses `order-1`/`order-2` to stack correctly on mobile.

```tsx
{
  /* ── Editorial Section (Reversed) ── */
}
<section className="max-w-6xl mx-auto px-6">
  <div className="grid md:grid-cols-2 gap-16 md:gap-20 items-center">
    {/* Visual — left */}
    <div className="order-2 md:order-1 rounded-2xl overflow-hidden border border-white/5 bg-surface-elevated">
      <div className="flex items-center justify-between px-5 py-4 border-b border-white/5">
        <div className="flex items-center gap-2">
          <div className="flex gap-1.5">
            <div className="w-2.5 h-2.5 rounded-full bg-red-500/40" />
            <div className="w-2.5 h-2.5 rounded-full bg-yellow-500/40" />
            <div className="w-2.5 h-2.5 rounded-full bg-green-500/40" />
          </div>
          <span className="text-xs text-gray-600 font-mono ml-2">
            config.json
          </span>
        </div>
        <span className="text-[10px] bg-secondary/10 text-secondary border border-secondary/20 rounded px-2 py-0.5 font-medium">
          TAG
        </span>
      </div>
      <CodeBlock language="json" copyable={false} code={`{ "key": "value" }`} />
      {/* Optional: caption / callout strip below code */}
      <div className="border-t border-white/5 px-5 py-4 bg-surface/50 space-y-2">
        <p className="text-xs text-gray-500 italic">
          "Example prompt or caption text."
        </p>
        <div className="flex items-center gap-2">
          <div className="w-5 h-5 rounded-full bg-secondary/15 border border-secondary/30 flex items-center justify-center">
            <span className="text-secondary text-[8px] font-bold">AI</span>
          </div>
          <span className="text-xs text-secondary">Attribution label</span>
        </div>
      </div>
    </div>

    {/* Copy — right */}
    <div className="space-y-8 order-1 md:order-2">
      <p className="text-xs text-secondary font-bold uppercase tracking-[0.15em]">
        Feature Label
      </p>
      <h2 className="text-3xl md:text-4xl font-bold leading-tight">
        <span className="text-white">Headline </span>
        <span className="gradient-text">accent phrase.</span>
      </h2>
      <p className="text-gray-400 leading-relaxed text-[15px]">
        Description of the feature.
      </p>
      <ul className="space-y-4">
        {fnList.map(({ fn, desc }) => (
          <li key={fn} className="flex items-start gap-3">
            <code className="text-xs bg-surface-elevated border border-secondary/20 text-secondary px-2.5 py-1 rounded-lg font-mono flex-shrink-0 mt-0.5">
              {fn}
            </code>
            <p className="text-gray-500 text-sm leading-relaxed">{desc}</p>
          </li>
        ))}
      </ul>
      <Link
        to="/page"
        className="inline-flex items-center gap-2 text-sm text-secondary font-medium group"
      >
        <span>Link text</span>
        <span className="transition-transform group-hover:translate-x-1">
          →
        </span>
      </Link>
    </div>
  </div>
</section>;
```

**Variations from standard editorial:**

- `order-2 md:order-1` on visual, `order-1 md:order-2` on copy — correct mobile stacking
- Function list variant: inline `<code>` tags instead of checkmark list — better for API endpoints/tools
- Optional caption strip below code block with icon attribution
- Tag badge in terminal header (`bg-secondary/10 text-secondary`)

---

## 20.6. Editorial Section (Copy + Docs/Table Preview)

**Use when:** Showcasing documentation, API references, or structured data output. Use when the visual companion is a formatted document, not a terminal/code block.

**Structure:** Same two-column as standard editorial, but the right column is a docs preview with tables and formatted text instead of a code block.

```tsx
{
  /* ── Editorial Section (Docs Preview) ── */
}
<section className="max-w-6xl mx-auto px-6">
  <div className="grid md:grid-cols-2 gap-16 md:gap-20 items-center">
    {/* Copy — left */}
    <div className="space-y-8">
      <p className="text-xs text-primary font-bold uppercase tracking-[0.15em]">
        Documentation
      </p>
      <h2 className="text-3xl md:text-4xl font-bold leading-tight">
        <span className="text-white">Documentation that </span>
        <span className="gradient-text">writes itself.</span>
      </h2>
      <p className="text-gray-400 leading-relaxed text-[15px]">
        Description of the documentation feature.
      </p>
      <ul className="space-y-5">{/* Same checklist pattern as 20.4 */}</ul>
      <Link
        to="/page"
        className="inline-flex items-center gap-2 text-sm text-primary font-medium group"
      >
        <span>See examples</span>
        <span className="transition-transform group-hover:translate-x-1">
          →
        </span>
      </Link>
    </div>

    {/* Visual — docs preview */}
    <div className="rounded-2xl overflow-hidden border border-white/5 bg-surface-elevated">
      <div className="flex items-center gap-2 px-5 py-4 border-b border-white/5">
        <div className="flex gap-1.5">
          <div className="w-2.5 h-2.5 rounded-full bg-red-500/40" />
          <div className="w-2.5 h-2.5 rounded-full bg-yellow-500/40" />
          <div className="w-2.5 h-2.5 rounded-full bg-green-500/40" />
        </div>
        <span className="text-xs text-gray-600 font-mono ml-2">
          document.md
        </span>
      </div>
      <div className="p-6 space-y-5 font-mono text-xs">
        <div>
          <p className="text-primary font-bold text-sm"># heading</p>
          <p className="text-gray-500 mt-1.5 font-sans text-sm">
            Description paragraph.
          </p>
        </div>
        <div>
          <p className="text-gray-300 font-bold mb-2">## Table Section</p>
          <div className="rounded-lg overflow-hidden border border-white/5">
            <table className="w-full text-xs">
              <thead className="bg-surface">
                <tr>
                  <th className="text-left px-3 py-2 text-gray-500 font-medium">
                    Col A
                  </th>
                  <th className="text-left px-3 py-2 text-gray-500 font-medium">
                    Col B
                  </th>
                  <th className="text-left px-3 py-2 text-gray-500 font-medium">
                    Col C
                  </th>
                </tr>
              </thead>
              <tbody>
                {tableData.map((row) => (
                  <tr key={row.name} className="border-t border-white/5">
                    <td className="px-3 py-2 text-secondary">{row.name}</td>
                    <td className="px-3 py-2 text-primary/70">{row.type}</td>
                    <td className="px-3 py-2 text-gray-500">{row.desc}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
        <div>
          <p className="text-gray-300 font-bold mb-2">## Fields</p>
          <div className="bg-surface rounded-lg px-4 py-3 border border-white/5 flex items-center gap-2">
            <span className="text-secondary">fieldName</span>
            <span className="text-gray-700">·</span>
            <span className="text-primary/70">type</span>
            <span className="text-gray-600">— Description</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>;
```

**Key patterns:**

- Terminal header with filename (e.g., `document.md`)
- Inner content uses `font-mono text-xs` for code feel
- Table with dark styling: `bg-surface` header, `border-white/5` separators
- Inline field display: dot-separated format with colored segments

---

## 20.7. Social Proof Section

**Use when:** Building trust. Place after editorial sections but before the final CTA. Use testimonials, tweet embeds, or logo walls.

**Structure:** Centered heading → external component (TwitterWall, logo grid, testimonial cards).

```tsx
{
  /* ── Social Proof ── */
}
<div className="space-y-12">
  <div className="max-w-6xl mx-auto px-6 text-center">
    <h2 className="text-3xl md:text-4xl font-bold mb-4">
      <span className="text-white">Trusted by </span>
      <span className="gradient-text">builders</span>
    </h2>
    <p className="text-gray-500 max-w-xl mx-auto">
      Developers and teams trust us to handle the hard parts.
    </p>
  </div>
  {/* Replace with your social proof component */}
  <TwitterWall />
  {/* Or a logo grid: */}
  {/* <div className="grid grid-cols-2 md:grid-cols-4 gap-8 max-w-4xl mx-auto px-6">
    {logos.map(({ name, src }) => (
      <div key={name} className="flex items-center justify-center h-16 opacity-50 hover:opacity-100 transition-opacity">
        <img src={src} alt={name} className="max-h-12" />
      </div>
    ))}
  </div> */}
</div>;
```

**Key patterns:**

- Wrapper is `<div>` not `<section>` — lighter weight
- `space-y-12` for internal spacing between heading and social proof component
- Logo grid alternative with opacity hover effect (`opacity-50 hover:opacity-100`)

---

## 20.8. Final CTA Section

**Use when:** Every landing page needs one. Last section before the footer. Drives the primary conversion action.

**Structure:** Centered headline → subtitle → two CTA buttons (same pattern as hero).

```tsx
{
  /* ── Final CTA ── */
}
<section className="max-w-4xl mx-auto px-6 pb-8 text-center">
  <h2 className="text-4xl md:text-5xl font-bold leading-tight mb-6">
    <span className="text-white">Build without limits.</span>
    <br />
    <span className="gradient-text">What will you ship?</span>
  </h2>
  <p className="text-gray-400 max-w-lg mx-auto leading-relaxed mb-10">
    Call to action subtitle. One line about what happens next.
  </p>
  <div className="flex flex-col sm:flex-row justify-center gap-4">
    <a href="#" className="btn-primary text-base px-8 py-4">
      Primary CTA
    </a>
    <Link to="/page" className="btn-secondary text-base px-8 py-4">
      Secondary CTA
    </Link>
  </div>
</section>;
```

**Key patterns:**

- `max-w-4xl` (narrower than other sections — focuses attention)
- `pb-8` (bottom padding before footer)
- Same button pattern as hero for consistency
- Headline slightly smaller than hero: `text-4xl md:text-5xl` vs hero's `text-5xl md:text-7xl`

---
