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

## Tailwind v4 Essentials

| Feature        | Implementation                                                 |
| -------------- | -------------------------------------------------------------- |
| Config file    | **No config file** — use `@theme` in CSS                       |
| CSS import     | `@import 'tailwindcss'`                                        |
| Dark mode      | `@custom-variant dark (&:is(.dark *))` in CSS                  |
| PostCSS plugin | `@tailwindcss/postcss` only (no autoprefixer needed)           |
| Colors/theme   | `@theme` block in CSS                                          |
| `outline-none` | **Use `outline-hidden`** (accessibility-safe invisible)        |
| Default shadow | `shadow-xs` (smallest), `shadow-sm`, `shadow`, `shadow-md` ... |

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

**Notes:**

- `@tailwindcss/postcss` replaces the old `tailwindcss` PostCSS plugin + `autoprefixer`
- `tailwindcss` v4 includes built-in imports and vendor prefixing

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
  Tailwind CSS v4 changed the default border color to `currentcolor`.
  This sets a consistent default border color across all elements.
  Remove these styles if you prefer to specify border colors explicitly.
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

### Tailwind v4 CSS Syntax

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

### 15.5. Tailwind v4 Key Class Names

| Class            | Notes                                    |
| ---------------- | ---------------------------------------- |
| `outline-hidden` | Hides outline but keeps focusable (a11y) |
| `shadow-xs`      | Smallest shadow                          |
| `bg-primary/50`  | Opacity modifier syntax for colors       |

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
| Tailwind | Default setup                  | **v4** (CSS-first config, no tailwind.config.js) |
| Config   | `tailwind.config.js`           | **No config file** — use `@theme` in CSS         |
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
<input className="focus:outline-hidden" />
```

### 19.7. Shadow Scale in Tailwind v4

Tailwind v4 provides: `shadow-xs`, `shadow-sm`, `shadow`, `shadow-md`, `shadow-lg`, `shadow-xl`, `shadow-2xl`.

## 20. Landing Page Section Templates

Reusable section components for building landing pages. Each section is self-contained and follows the ChainSquad dark-theme aesthetic. Sections are separated by `space-y-36` on the parent wrapper.

### 20.0. Page Wrapper Pattern

All sections live inside a single wrapper `<div>` with generous vertical spacing:

```tsx
export default function Home(): JSX.Element {
  return <div className="space-y-36">{/* ── Sections go here ── */}</div>;
}
```

### 20.1. Hero Section

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

### 20.2. How It Works (Steps Section)

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

### 20.3. Sidebar Feature Showcase

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

### 20.4. Editorial Section (Copy + Visual, Standard)

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

### 20.5. Editorial Section (Reversed: Visual + Copy)

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

### 20.6. Editorial Section (Copy + Docs/Table Preview)

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

### 20.7. Social Proof Section

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

### 20.8. Final CTA Section

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

### 20.9. Section Selection Guide

| Section                       | Purpose                                | Position on Page             | Count     |
| ----------------------------- | -------------------------------------- | ---------------------------- | --------- |
| **Hero** (20.1)               | First impression, main value prop      | 1st                          | Exactly 1 |
| **How It Works** (20.2)       | Process explanation, onboarding        | After Hero                   | 0-1       |
| **Sidebar Features** (20.3)   | Multiple related features, interactive | After How It Works           | 0-1       |
| **Editorial Standard** (20.4) | Primary feature deep-dive              | After Sidebar Features       | 1-3       |
| **Editorial Reversed** (20.5) | Secondary feature (alternating layout) | Alternating with Standard    | As needed |
| **Editorial Docs** (20.6)     | Documentation/API reference showcase   | Mixed with other editorials  | 0-1       |
| **Social Proof** (20.7)       | Trust building, testimonials           | After editorials, before CTA | 0-1       |
| **Final CTA** (20.8)          | Last conversion push                   | Last section before footer   | Exactly 1 |

**Recommended page order:**

```
Hero → How It Works → Sidebar Features → Editorial A → Editorial B (reversed) → Editorial C (docs) → Social Proof → Final CTA
```

**Minimum viable landing page:**

```
Hero → Editorial A → Final CTA
```

---

**Remember**: Tailwind v4 is CSS-first. No JavaScript config file needed. Use `@theme` in CSS for all customization.
