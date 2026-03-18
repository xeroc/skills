---
name: chainsquad-style
description: the unique style used by chainsquad.com's websites
---

# ChainSquad Style - Static Site Template

**Use when** creating a new static website with Vite + React that needs:

- HashRouter routing (for GitHub Pages)
- Tailwind CSS v3 styling
- Dark/light theme toggle
- Header/Footer separation from pages
- n8n webhook integration for forms
- TypeScript with strict config
- Static build for GitHub Pages hosting

## Stack

- **Build Tool**: Vite 6.x
- **Framework**: React 19.x with TypeScript
- **Routing**: react-router-dom v7.x (HashRouter)
- **Styling**: Tailwind CSS 3.x (NOT v4!)
- **Icons**: lucide-react
- **Font**: Roboto Mono + Inter (via Google Fonts)

## Directory Structure

```
my-site/
├── .env                      # Environment vars (VITE_N8N_WEBHOOK_URL)
├── .gitignore
├── index.html                 # Entry point with #root div
├── package.json
├── postcss.config.js
├── tailwind.config.js         # Tailwind 3 config with HSL vars
├── tsconfig.json
├── tsconfig.node.json
├── vite.config.ts             # Vite config with path alias, base: "./"
├── src/
│   ├── env.d.ts
│   ├── globals.css            # Tailwind directives + CSS vars for theming
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
    "autoprefixer": "^10.4.24",
    "lucide-react": "^0.564.0",
    "postcss": "^8.5.6",
    "react": "^19.2.4",
    "react-dom": "^19.2.4",
    "react-router-dom": "^7.13.1",
    "tailwindcss": "^3.4.19"
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

## 3. Tailwind Config (tailwind.config.js)

**IMPORTANT**: Tailwind 3 syntax (NOT v4 - v4 uses different config format).

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ["class"],
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
      fontFamily: {
        sans: ["Roboto Mono", "Inter", "sans-serif"],
        mono: ["Roboto Mono", "monospace"],
      },
    },
  },
  plugins: [],
};
```

## 4. Globals CSS (src/globals.css)

Tailwind 3 directives + CSS variables for theming.

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    /* Light theme - Professional blue/slate palette */
    --background: 0 0% 100%;
    --foreground: 222.2 47.4% 11.2%;
    --card: 0 0% 100%;
    --card-foreground: 222.2 47.4% 11.2%;
    --popover: 0 0% 100%;
    --popover-foreground: 222.2 47.4% 11.2%;
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
        {/* Add more routes here */}
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

## 13. PostCSS Config (postcss.config.js)

Required for Tailwind CSS processing.

```javascript
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
```

## 14. Example Page (src/pages/Home.tsx)

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

## 15. GitHub Pages Deployment

### 15.1. Build Command

```bash
npm run build
```

This creates `dist/` folder with static files.

### 15.2. GitHub Actions Workflow (.github/workflows/deploy.yml)

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

### 15.3. GitHub Pages Settings

1. Go to repository **Settings** → **Pages**
2. Set **Source** to **GitHub Actions**

## 16. Common Patterns

### 16.1. Adding New Pages

1. Create page file in `src/pages/YourPage.tsx`
2. Add route in `src/App.tsx`:

```tsx
<Route path="/your-page" element={<YourPage />} />
```

### 16.2. Adding New Components

Create component in `src/components/YourComponent.tsx`, then import and use in pages.

### 16.3. Styling with Tailwind

Use utility classes from Tailwind 3. All colors use CSS variables for theming:

```tsx
<div className="bg-background text-foreground border-border">
  Primary color: <span className="text-primary">Text</span>
  Muted: <span className="text-muted-foreground">Text</span>
</div>
```

### 16.4. Dark Mode

Use `dark:` prefix for dark-mode-specific styles:

```tsx
<div className="bg-background dark:bg-card">Content</div>
```

Theme toggle handled by `ThemeToggle` component adding/removing `.dark` class on `<html>` element.

## 17. Quick Start

1. Scaffold new project:

```bash
npm create vite@latest my-site -- --template react-ts
cd my-site
npm install
```

1. Install dependencies:

```bash
npm install react-router-dom lucide-react tailwindcss postcss autoprefixer vite-plugin-webfont-dl
npm install -D @types/node
```

1. Copy config files:
   - `vite.config.ts`
   - `tailwind.config.js`
   - `postcss.config.js`
   - `tsconfig.json`
   - `src/globals.css`

2. Create directory structure:
   - `src/components/`
   - `src/pages/`
   - `src/lib/`

3. Copy component files:
   - `src/main.tsx`
   - `src/App.tsx`
   - `src/components/Header.tsx`
   - `src/components/Footer.tsx`
   - `src/components/ThemeToggle.tsx`
   - `src/lib/n8n.ts`

4. Create `.env` file with `VITE_N8N_WEBHOOK_URL`

5. Run dev server:

```bash
npm run dev
```

1. Build for production:

```bash
npm run build
```

## 18. Key Differences from Standard Vite + React

| Feature  | Standard          | ChainSquad Style                                 |
| -------- | ----------------- | ------------------------------------------------ |
| Router   | BrowserRouter     | **HashRouter** (for GitHub Pages)                |
| Tailwind | v4 or v3          | **v3 only** (v4 uses different config)           |
| Theme    | Manual            | Built-in dark/light with CSS vars                |
| Layout   | Inline components | **Separated Header/Footer** in `src/components/` |
| Base URL | `/`               | `"./"` for static hosting                        |
| Forms    | Native fetch      | **n8n webhook** wrapper in `src/lib/n8n.ts`      |
| Build    | Standard          | Static build for GitHub Pages                    |

## 19. Troubleshooting

### 19.1. HashRouter Not Working

Ensure you're using `HashRouter` (not `BrowserRouter`) in `src/main.tsx`:

```tsx
import { HashRouter } from "react-router-dom";
```

### 19.2. Tailwind Classes Not Working

Check that `src/globals.css` has Tailwind directives:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Ensure `tailwind.config.js` has correct `content` paths.

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
