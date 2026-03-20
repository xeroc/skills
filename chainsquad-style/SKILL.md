---
name: chainsquad-style
description: the unique style used by chainsquad.com's websites
---

# ChainSquad Style - Static Site Template

**Use when** creating a new static website with Vite + React that needs:

- HashRouter routing (for GitHub Pages)
- Tailwind CSS v4 styling (CSS-first configuration)
- Dark/light theme toggle
- Header/Footer separation from pages
- n8n webhook integration for forms
- TypeScript with strict config
- Static build for GitHub Pages hosting

## Stack

- **Build Tool**: Vite 6.x
- **Framework**: React 19.x with TypeScript
- **Routing**: react-router-dom v7.x (HashRouter)
- **Styling**: Tailwind CSS 4.x (CSS-first config, no tailwind.config.js!)
- **Icons**: lucide-react
- **Font**: Roboto Mono + Inter (via Google Fonts)

## Key Differences: Tailwind v3 → v4

| Feature        | Tailwind v3                           | Tailwind v4                                   |
| -------------- | ------------------------------------- | --------------------------------------------- |
| Config file    | `tailwind.config.js`                  | **No config file** - use `@theme` in CSS      |
| CSS import     | `@tailwind base/components/utilities` | `@import 'tailwindcss'`                       |
| Dark mode      | `darkMode: ['class']` in config       | `@custom-variant dark (&:is(.dark *))` in CSS |
| PostCSS plugin | `tailwindcss` + `autoprefixer`        | `@tailwindcss/postcss` only                   |
| Colors/theme   | `theme.extend` in JS                  | `@theme` block in CSS                         |
| `outline-none` | Removes outline                       | **Use `outline-hidden`**                      |
| `shadow-xs`    | Extra small shadow                    | **Use `shadow-2xs`**                          |

## Directory Structure

```
my-site/
├── .env                      # Environment vars (VITE_N8N_WEBHOOK_URL)
├── .gitignore
├── index.html                 # Entry point with #root div
├── package.json
├── postcss.config.cjs         # PostCSS with @tailwindcss/postcss
├── tsconfig.json
├── tsconfig.node.json
├── vite.config.ts             # Vite config with path alias, base: "./"
├── src/
│   ├── env.d.ts
│   ├── globals.css            # @import 'tailwindcss' + @theme + CSS vars
│   ├── main.tsx              # ReactDOM.createRoot + HashRouter
│   ├── App.tsx               # Routes + Header + Footer wrapper
│   ├── components/
│   │   ├── Header.tsx         # Nav with dropdown, theme toggle
│   │   ├── Footer.tsx         # Multi-column footer
│   │   └── ThemeToggle.tsx    # Dark/light switcher
│   ├── pages/
│   │   ├── Home.tsx           # Landing page
│   │   ├── Contact.tsx         # Contact form with n8n
│   │   └── ...
│   └── lib/
│       └── n8n.ts            # Webhook wrapper function
└── dist/                     # Build output (gitignored)
```

**NOTE**: No `tailwind.config.js` file exists in Tailwind v4!

## 1. Package.json

```json
{
  "name": "my-site",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "preview": "vite preview",
    "lint": "eslint ."
  },
  "dependencies": {
    "@tailwindcss/postcss": "^4.2.2",
    "lucide-react": "^0.564.0",
    "postcss": "^8.5.6",
    "react": "^19.2.4",
    "react-dom": "^19.2.4",
    "react-router-dom": "^7.13.1",
    "tailwindcss": "^4.2.2"
  },
  "devDependencies": {
    "@types/node": "25.2.3",
    "@types/react": "19.2.14",
    "@types/react-dom": "^19.2.3",
    "@vitejs/plugin-react": "^4.4.1",
    "typescript": "5.9.3",
    "vite": "^6.3.4",
    "vite-plugin-webfont-dl": "^3.12.0"
  }
}
```

**Changes from v3:**

- Removed `autoprefixer` (built into v4)
- Added `@tailwindcss/postcss`
- Updated `tailwindcss` to `^4.2.2`

## 2. Vite Config (vite.config.ts)

**Critical**: `base: "./"` for GitHub Pages static hosting.

```typescript
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";
import webfontDownload from "vite-plugin-webfont-dl";

export default defineConfig({
  plugins: [
    webfontDownload([
      "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap",
      "https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap",
    ]),
    react(),
  ],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  base: "./", // CRITICAL for GitHub Pages
  build: {
    outDir: "dist",
    sourcemap: false,
  },
});
```

## 3. PostCSS Config (postcss.config.cjs)

**IMPORTANT**: Use `@tailwindcss/postcss` (not `tailwindcss` + `autoprefixer`).

```javascript
module.exports = {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};
```

**Note**: File extension is `.cjs` for CommonJS compatibility.

## 4. Globals CSS (src/globals.css)

**This is the heart of Tailwind v4** - all configuration happens here via `@theme`.

```css
@import "tailwindcss";

@custom-variant dark (&:is(.dark *));

@theme {
  --color-border: hsl(var(--border));
  --color-input: hsl(var(--input));
  --color-ring: hsl(var(--ring));
  --color-background: hsl(var(--background));
  --color-foreground: hsl(var(--foreground));

  --color-primary: hsl(var(--primary));
  --color-primary-foreground: hsl(var(--primary-foreground));

  --color-secondary: hsl(var(--secondary));
  --color-secondary-foreground: hsl(var(--secondary-foreground));

  --color-destructive: hsl(var(--destructive));
  --color-destructive-foreground: hsl(var(--destructive-foreground));

  --color-muted: hsl(var(--muted));
  --color-muted-foreground: hsl(var(--muted-foreground));

  --color-accent: hsl(var(--accent));
  --color-accent-foreground: hsl(var(--accent-foreground));

  --color-popover: hsl(var(--popover));
  --color-popover-foreground: hsl(var(--popover-foreground));

  --color-card: hsl(var(--card));
  --color-card-foreground: hsl(var(--card-foreground));

  --radius-lg: var(--radius);
  --radius-md: calc(var(--radius) - 2px);
  --radius-sm: calc(var(--radius) - 4px);

  --font-sans: Roboto Mono, Inter, sans-serif;
  --font-mono: Roboto Mono, monospace;
}

/*
  The default border color has changed to `currentcolor` in Tailwind CSS v4,
  so we've added these compatibility styles to make sure everything still
  looks the same as it did with Tailwind CSS v3.

  If we ever want to remove these styles, we need to add an explicit border
  color utility to any element that depends on these defaults.
*/
@layer base {
  *,
  ::after,
  ::before,
  ::backdrop,
  ::file-selector-button {
    border-color: var(--color-gray-200, currentcolor);
  }
}

@layer base {
  :root {
    /* Light theme - Professional blue/slate palette */
    --background: 0 0% 100%;
    --foreground: 222.2 47.4% 11.2%;

    --card: 0 0% 100%;
    --card-foreground: 222.2 47.4% 11.2%;

    --popover: 0 0% 100%;
    --popover-foreground: 222.2 47.4% 11.2%;

    /* Primary - Professional blue */
    --primary: 221.2 83.2% 53.3%;
    --primary-foreground: 0 0% 100%;

    --secondary: 210 40% 96.1%;
    --secondary-foreground: 222.2 47.4% 11.2%;

    --muted: 210 40% 96.1%;
    --muted-foreground: 215.4 16.3% 46.9%;

    --accent: 210 40% 96.1%;
    --accent-foreground: 222.2 47.4% 11.2%;

    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 0 0% 100%;

    --border: 214.3 31.8% 91.4%;
    --input: 214.3 31.8% 91.4%;
    --ring: 221.2 83.2% 53.3%;

    --radius: 0.5rem;
  }

  .dark {
    /* Dark theme - Same professional blue but dark background */
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;

    --card: 222.2 84% 4.9%;
    --card-foreground: 210 40% 98%;

    --popover: 222.2 84% 4.9%;
    --popover-foreground: 210 40% 98%;

    --primary: 217.2 91.2% 59.8%;
    --primary-foreground: 210 40% 98%;

    --secondary: 217.2 32.6% 17.5%;
    --secondary-foreground: 210 40% 98%;

    --muted: 217.2 32.6% 17.5%;
    --muted-foreground: 215 20.2% 65.1%;

    --accent: 217.2 32.6% 17.5%;
    --accent-foreground: 210 40% 98%;

    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 210 40% 98%;

    --border: 217.2 32.6% 17.5%;
    --input: 217.2 32.6% 17.5%;
    --ring: 217.2 91.2% 59.8%;
  }
}

@layer base {
  * {
    @apply border-border;
  }
  body {
    @apply bg-background text-foreground;
  }
}
```

### Tailwind v4 CSS Syntax Breakdown

| Element      | Syntax                                         | Purpose                               |
| ------------ | ---------------------------------------------- | ------------------------------------- |
| Import       | `@import 'tailwindcss';`                       | Replaces `@tailwind` directives       |
| Dark mode    | `@custom-variant dark (&:is(.dark *));`        | Enables `.dark` class-based dark mode |
| Theme colors | `--color-primary: hsl(var(--primary));`        | Maps CSS var to Tailwind color        |
| Theme fonts  | `--font-sans: Roboto Mono, Inter, sans-serif;` | Defines font family                   |
| Theme radius | `--radius-lg: var(--radius);`                  | Defines border radius                 |

## 5. Entry Point (src/main.tsx)

Uses `HashRouter` for GitHub Pages compatibility.

```tsx
import React from "react";
import ReactDOM from "react-dom/client";
import { HashRouter } from "react-router-dom";
import App from "./App";
import "./globals.css";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <HashRouter>
      <App />
    </HashRouter>
  </React.StrictMode>,
);
```

## 6. App Component (src/App.tsx)

Wrapper that includes Header, Routes, and Footer.

```tsx
import { Routes, Route } from "react-router-dom";
import { Header } from "./components/Header";
import { Footer } from "./components/Footer";
import Home from "./pages/Home";
import Contact from "./pages/Contact";

export default function App() {
  return (
    <div className="min-h-screen bg-background antialiased font-sans">
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
      <Footer />
    </div>
  );
}
```

## 7. Header Component (src/components/Header.tsx)

Separated navigation with theme toggle and product dropdown.

```tsx
import { Link } from "react-router-dom";
import { ThemeToggle } from "./ThemeToggle";
import { ChevronDown } from "lucide-react";
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";

const navItems = [
  { label: "About", href: "about" },
  { label: "Services", href: "services" },
  { label: "Contact", href: "contact" },
];

const products = [
  {
    label: "Product 1",
    href: "/products/product1",
    description: "Description",
  },
  {
    label: "Product 2",
    href: "/products/product2",
    description: "Description",
  },
];

export function Header() {
  const navigate = useNavigate();
  const scrollToSection = (id: string) => {
    navigate("/");
    sessionStorage.setItem("scrollTo", id);
    document.getElementById(id)?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    const section = sessionStorage.getItem("scrollTo");
    if (section) {
      sessionStorage.removeItem("scrollTo");
      setTimeout(() => {
        document
          .getElementById(section)
          ?.scrollIntoView({ behavior: "smooth" });
      }, 100);
    }
  }, []);

  return (
    <header className="py-6">
      <div className="mx-auto flex w-full max-w-5xl flex-col gap-4 px-4 md:flex-row md:items-center md:justify-between">
        <Link className="inline-flex text-primary" to="/">
          <span className="font-semibold text-xs uppercase tracking-[0.3em]">
            YOUR BRAND
          </span>
        </Link>
        <div className="flex w-full flex-col gap-4 md:w-auto md:flex-row md:items-center md:justify-end md:gap-6">
          <nav className="flex flex-wrap items-center gap-4 text-muted-foreground text-xs uppercase tracking-[0.12em]">
            {navItems.map((item) => (
              <a
                key={item.href}
                className="transition-colors hover:text-foreground hover:cursor-pointer"
                onClick={() => scrollToSection(item.href)}
              >
                {item.label}
              </a>
            ))}
            <div className="relative group">
              <button className="flex items-center gap-1 transition-colors hover:text-foreground">
                PRODUCTS
                <ChevronDown className="h-3 w-3 transition-transform group-hover:rotate-180" />
              </button>
              <div className="absolute left-0 top-full pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all">
                <div className="bg-background border border-border shadow-lg min-w-48 py-2">
                  {products.map((product) => (
                    <Link
                      key={product.href}
                      to={product.href}
                      className="block px-4 py-2 hover:bg-muted/50 transition-colors"
                    >
                      <div className="text-xs uppercase tracking-[0.12em] text-foreground">
                        {product.label}
                      </div>
                      <div className="text-[10px] text-muted-foreground mt-0.5 normal-case tracking-normal">
                        {product.description}
                      </div>
                    </Link>
                  ))}
                </div>
              </div>
            </div>
            <ThemeToggle />
          </nav>
        </div>
      </div>
    </header>
  );
}
```

## 8. Footer Component (src/components/Footer.tsx)

Multi-column footer with links.

```tsx
import { Link } from "react-router-dom";
import { Code2 } from "lucide-react";

export function Footer() {
  return (
    <footer className="border-t border-border/50">
      <div className="container mx-auto max-w-6xl px-6 py-12">
        <div className="grid md:grid-cols-4 gap-8">
          <div>
            <div className="flex items-center gap-2 mb-4">
              <Code2 className="h-5 w-5 text-primary" />
              <span className="font-semibold uppercase tracking-[0.3em]">
                YOUR BRAND
              </span>
            </div>
            <p className="text-sm text-muted-foreground">
              Tagline or description goes here.
            </p>
          </div>
          <div>
            <div className="font-medium text-sm mb-4">Resources</div>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li>
                <a href="#" className="hover:text-foreground transition-colors">
                  GitHub Repository
                </a>
              </li>
            </ul>
          </div>
          <div>
            <div className="font-medium text-sm mb-4">Legal</div>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li>
                <Link
                  to="/privacy"
                  className="hover:text-foreground transition-colors"
                >
                  Privacy Policy
                </Link>
              </li>
              <li>
                <Link
                  to="/legal"
                  className="hover:text-foreground transition-colors"
                >
                  Legal Notice & Terms
                </Link>
              </li>
            </ul>
          </div>
        </div>
        <div className="text-center text-sm text-muted-foreground/60 mt-8">
          &copy; 2026 Your Company. Built with ❤️.
        </div>
      </div>
    </footer>
  );
}
```

## 9. Theme Toggle (src/components/ThemeToggle.tsx)

Dark/light mode switcher using Tailwind dark mode class.

```tsx
import { useEffect, useState } from "react";
import { Moon, Sun } from "lucide-react";

export function ThemeToggle() {
  const [theme, setTheme] = useState(() => {
    if (typeof window !== "undefined") {
      return localStorage.getItem("theme") || "light";
    }
    return "light";
  });

  useEffect(() => {
    const root = document.documentElement;
    if (theme === "dark") {
      root.classList.add("dark");
      localStorage.setItem("theme", "dark");
    } else {
      root.classList.remove("dark");
      localStorage.setItem("theme", "light");
    }
  }, [theme]);

  return (
    <button
      onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
      className="p-2 rounded-md hover:bg-muted transition-colors"
    >
      {theme === "dark" ? (
        <Sun className="h-4 w-4" />
      ) : (
        <Moon className="h-4 w-4" />
      )}
    </button>
  );
}
```

## 10. n8n Integration (src/lib/n8n.ts)

Wrapper function for form submissions via n8n webhooks.

```typescript
export async function addToWaitlist(args: Record<string, string>) {
  const n8nWebhookUrl = import.meta.env.VITE_N8N_WEBHOOK_URL;

  if (!n8nWebhookUrl) {
    throw new Error(
      "N8N webhook URL not configured. Please set VITE_N8N_WEBHOOK_URL environment variable.",
    );
  }

  try {
    const response = await fetch(n8nWebhookUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
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

## 11. Environment Variables (.env)

Create `.env` file in project root:

```env
VITE_N8N_WEBHOOK_URL=https://your-n8n-instance.com/webhook/your-webhook-path
```

**IMPORTANT**: Environment variables must start with `VITE_` prefix for Vite to expose them to client-side code.

## 12. TypeScript Config (tsconfig.json)

Strict TypeScript configuration.

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "isolatedModules": true,
    "moduleDetection": "force",
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true
  },
  "include": ["src"]
}
```

## 13. Example Page (src/pages/Home.tsx)

```tsx
export default function Home() {
  return (
    <main className="container mx-auto max-w-5xl px-6 py-12">
      <section id="about" className="mb-20">
        <h1 className="text-4xl font-bold tracking-tight mb-6">
          Welcome to Your Site
        </h1>
        <p className="text-lg text-muted-foreground mb-6">
          Your value proposition goes here.
        </p>
      </section>
      <section id="services" className="mb-20">
        <h2 className="text-3xl font-bold tracking-tight mb-6">Services</h2>
        <div className="grid md:grid-cols-2 gap-6">
          <div className="border border-border p-6 rounded-lg">
            <h3 className="text-xl font-semibold mb-3">Service 1</h3>
            <p className="text-muted-foreground">Description of service 1.</p>
          </div>
          <div className="border border-border p-6 rounded-lg">
            <h3 className="text-xl font-semibold mb-3">Service 2</h3>
            <p className="text-muted-foreground">Description of service 2.</p>
          </div>
        </div>
      </section>
    </main>
  );
}
```

## 14. GitHub Pages Deployment

### 14.1. Build Command

```bash
npm run build
```

### 14.2. GitHub Actions Workflow (.github/workflows/deploy.yml)

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"

      - name: Install dependencies
        run: npm ci

      - name: Build
        run: npm run build

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./dist

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### 14.3. GitHub Pages Settings

1. Go to repository **Settings** → **Pages**
2. Set **Source** to **GitHub Actions**

## 15. Common Patterns

### 15.1. Adding New Pages

1. Create page file in `src/pages/YourPage.tsx`
2. Add route in `src/App.tsx`:

```tsx
<Route path="/your-page" element={<YourPage />} />
```

### 15.2. Adding New Components

Create component in `src/components/YourComponent.tsx`, then import and use in pages.

### 15.3. Styling with Tailwind v4

Use utility classes. All colors use CSS variables for theming:

```tsx
<div className="bg-background text-foreground border-border">
  Primary color: <span className="text-primary">Text</span>
  Muted: <span className="text-muted-foreground">Text</span>
</div>
```

### 15.4. Dark Mode

Use `dark:` prefix for dark-mode-specific styles:

```tsx
<div className="bg-background dark:bg-card">Content</div>
```

Theme toggle handled by `ThemeToggle` component adding/removing `.dark` class on `<html>` element.

### 15.5. Tailwind v4 Class Name Changes

| v3 Class        | v4 Replacement   | Notes                             |
| --------------- | ---------------- | --------------------------------- |
| `outline-none`  | `outline-hidden` | Hides outline but keeps focusable |
| `shadow-xs`     | `shadow-2xs`     | Extra small shadow renamed        |
| `bg-opacity-50` | `bg-primary/50`  | Use opacity syntax directly       |

## 16. Quick Start

1. Scaffold new project:

```bash
npm create vite@latest my-site -- --template react-ts
cd my-site
npm install
```

2. Install dependencies:

```bash
npm install react-router-dom lucide-react @tailwindcss/postcss tailwindcss postcss vite-plugin-webfont-dl
npm install -D @types/node
```

3. Copy config files:
   - `vite.config.ts`
   - `postcss.config.cjs`
   - `tsconfig.json`
   - `src/globals.css`

4. Create directory structure:
   - `src/components/`
   - `src/pages/`
   - `src/lib/`

5. Copy component files:
   - `src/main.tsx`
   - `src/App.tsx`
   - `src/components/Header.tsx`
   - `src/components/Footer.tsx`
   - `src/components/ThemeToggle.tsx`
   - `src/lib/n8n.ts`

6. Create `.env` file with `VITE_N8N_WEBHOOK_URL`

7. Run dev server:

```bash
npm run dev
```

8. Build for production:

```bash
npm run build
```

## 17. Key Differences from Standard Vite + React

| Feature  | Standard                       | ChainSquad Style                                 |
| -------- | ------------------------------ | ------------------------------------------------ |
| Router   | BrowserRouter                  | **HashRouter** (for GitHub Pages)                |
| Tailwind | v3 or v4                       | **v4** (CSS-first config, no tailwind.config.js) |
| Config   | `tailwind.config.js`           | **No config file** - use `@theme` in CSS         |
| PostCSS  | `tailwindcss` + `autoprefixer` | **`@tailwindcss/postcss`** only                  |
| Theme    | Manual                         | Built-in dark/light with CSS vars                |
| Layout   | Inline components              | **Separated Header/Footer** in `src/components/` |
| Base URL | `/`                            | `"./"` for static hosting                        |
| Forms    | Native fetch                   | **n8n webhook** wrapper in `src/lib/n8n.ts`      |
| Build    | Standard                       | Static build for GitHub Pages                    |

## 18. Landing Page Best Practices

### 18.1. No Animations

Avoid `framer-motion` or similar animation libraries. Use CSS transitions for simple hover effects:

```tsx
// ✗ DON'T
<motion.div
  initial={{ opacity: 0, y: 30 }}
  whileInView={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.5 }}
>
  Content
</motion.div>

// ✅ DO
<div className="transition-colors hover:bg-muted">
  Content
</div>
```

**Why:**

- Performance: Animations add bundle size and runtime overhead
- Accessibility: Respects `prefers-reduced-motion`
- Maintainability: CSS transitions are easier to debug
- Conversion focus: Content should be the focus, not movement

### 18.2. Section Separators

Use subtle visual separators between sections:

```tsx
// Terminal-style comment separator
<div className="font-mono text-sm text-muted-foreground/30 select-none" aria-hidden="true">
  //
</div>

// Or a simple border
<div className="border-t border-border/50" />
```

### 18.3. Clean Card Layout

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

### 18.4. Stats Section

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

### 18.5. Typography Hierarchy

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

### 19.1. HashRouter Not Working

Ensure you're using `HashRouter` (not `BrowserRouter`) in `src/main.tsx`:

```tsx
import { HashRouter } from "react-router-dom";
```

### 19.2. Tailwind Classes Not Working

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

### 19.3. Theme Toggle Not Persisting

`ThemeToggle` component saves to `localStorage`. Check browser console for errors.

### 19.4. n8n Webhook Fails

Check that:

- `.env` file exists in project root (not `src/`)
- Variable name is `VITE_N8N_WEBHOOK_URL` (with `VITE_` prefix)
- Restart dev server after adding `.env`

### 19.5. GitHub Pages 404s

Ensure:

- `base: "./"` is set in `vite.config.ts`
- GitHub Pages source is set to **GitHub Actions** (not `gh-pages` branch)
- GitHub Actions workflow deploys `./dist` folder

### 19.6. "outline-none is deprecated" Warning

In Tailwind v4, use `outline-hidden` instead:

```tsx
// ❌ Wrong (v3)
<input className="focus:outline-none" />

// ✅ Correct (v4)
<input className="focus:outline-hidden" />
```

### 19.7. "shadow-xs is deprecated" Warning

In Tailwind v4, use `shadow-2xs` instead:

```tsx
// ❌ Wrong (v3)
<button className="shadow-xs" />

// ✅ Correct (v4)
<button className="shadow-2xs" />
```

## 20. Migration Guide: v3 → v4

If upgrading an existing project from Tailwind v3:

### Step 1: Update Dependencies

```bash
npm uninstall autoprefixer
npm install @tailwindcss/postcss@^4.2.2 tailwindcss@^4.2.2
```

### Step 2: Update PostCSS Config

Replace `postcss.config.js` with `postcss.config.cjs`:

```javascript
module.exports = {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};
```

### Step 3: Delete tailwind.config.js

```bash
rm tailwind.config.js
```

### Step 4: Update globals.css

Replace:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

With:

```css
@import "tailwindcss";

@custom-variant dark (&:is(.dark *));

@theme {
  /* Move all theme.extend colors here */
  --color-primary: hsl(var(--primary));
  --color-primary-foreground: hsl(var(--primary-foreground));
  /* ... etc */
}
```

### Step 5: Update Class Names

Find and replace:

- `outline-none` → `outline-hidden`
- `shadow-xs` → `shadow-2xs`

### Step 6: Test Build

```bash
npm run build
```

---

**Remember**: Tailwind v4 is CSS-first. No JavaScript config file needed!
