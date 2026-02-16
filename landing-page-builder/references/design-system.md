# Landing Page Design System Reference

Complete design tokens and configuration for building playbooks.com-inspired landing pages.

## Color System (CSS Variables)

### Dark Mode
```css
:root {
  --background: 222.2 84% 4.9%;
  --foreground: 210 40% 98%;
  --card: 222.2 84% 4.9%;
  --card-foreground: 210 40% 98%;
  --popover: 222.2 84% 4.9%;
  --popover-foreground: 210 40% 98%;
  --primary: 221.2 83.2% 53.3%;
  --primary-foreground: 210 40% 98%;
  --secondary: 210 40% 96.1%;
  --secondary-foreground: 222.2 47.4% 11.2%;
  --muted: 210 40% 96.1%;
  --muted-foreground: 215.4 16.3% 46.9%;
  --accent: 210 40% 96.1%;
  --accent-foreground: 222.2 47.4% 11.2%;
  --destructive: 0 84.2% 60.2%;
  --destructive-foreground: 210 40% 98%;
  --border: 214.3 31.8% 91.4%;
  --input: 214.3 31.8% 91.4%;
  --ring: 221.2 83.2% 53.3%;
  --radius: 0.5rem;
}

.dark {
  --background: 222.2 84% 4.9%;
  --foreground: 210 40% 98%;
  --card: 222.2 84% 4.9%;
  --card-foreground: 210 40% 98%;
  --popover: 222.2 84% 4.9%;
  --popover-foreground: 210 40% 98%;
  --primary: 267 100% 65%; /* Solana purple */
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
  --ring: 267 100% 65%;
}
```

## Tailwind Configuration

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
        solana: {
          purple: "#9945FF",
          teal: "#14F195",
          gradient: "linear-gradient(135deg, #9945FF 0%, #14F195 100%)",
          dark: "linear-gradient(135deg, #7B3FE8 0%, #0FBE78 100%)",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
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
      },
      keyframes: {
        "accordion-down": {
          from: { height: "0" },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: "0" },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
      },
    },
  },
  plugins: [],
};
```

## Font Configuration

```typescript
// layout.tsx
import type { Metadata } from "next";
import "./globals.css";
import { Inter, Roboto_Mono } from "next/font/google";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });
const robotoMono = Roboto_Mono({
  subsets: ["latin"],
  variable: "--font-roboto-mono",
  weight: ["400", "500", "700"],
});

export const metadata: Metadata = {
  title: "Vyne - Program Your Payments",
  description: "A new way to move value. Built for AI agent economy.",
  keywords: "AI payments, agent commerce, subscriptions, micropayments, Solana payments, Tributary, Web3 payments",
  openGraph: {
    title: "Vyne - Program Your Payments",
    description: "Unified payment platform for AI agent economy. Built on Tributary protocol.",
    url: "https://vyne.so",
    siteName: "Vyne",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={`${inter.variable} ${robotoMono.variable}`}>
      <body className="antialiased">{children}</body>
    </html>
  );
}
```

## CSS Utilities

### Gradient Background
```css
.gradient-bg {
  background: radial-gradient(
    ellipse 80% 50% at 50% -20%,
    rgba(153, 69, 255, 0.15),
    transparent
  );
}
```

## Design Tokens

### Spacing
- Container padding: `py-8` (32px vertical)
- Section gap: `space-y-12` (48px vertical)
- Grid gap: `gap-8` (32px)
- Hero gap (large screens): `lg:gap-16` (64px)

### Typography Scale
- Navigation/labels: `text-xs` (12px)
- Body text: `text-sm` (14px)
- Section headers: `text-xl` (20px)
- Main heading (mobile): `text-3xl` (30px)
- Main heading (desktop): `md:text-4xl` (36px)

### Opacity Levels
- Muted foreground: `text-muted-foreground/30` (30% opacity)
- Badge backgrounds: `bg-muted/20` (20% opacity)
- Input backgrounds: `bg-input/30` (30% opacity)
- Placeholder text: `text-muted-foreground/50` (50% opacity)

### Layout Dimensions
- Max width: `max-w-5xl` (1280px)
- Button height: `h-11` (44px)
- Button padding: `px-6` (24px horizontal)
- Badge padding: `px-3 py-1.5` (12px horizontal, 6px vertical)

### Transitions
- Color transitions: `transition-colors`
- Hover effects: `hover:bg-accent`, `hover:text-foreground`
- Focus states: `focus-visible:ring-1`, `focus-visible:ring-[3px]`
