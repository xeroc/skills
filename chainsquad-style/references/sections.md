# Swiss Design — Section Layout Patterns

Full section patterns extracted from the Swiss Design System showcase. Each section is self-contained with the section label, grid, and content.

---

## Poster Section (Dark + Light Side by Side)

Two-column poster layout — dark full-bleed poster on the left, light form-style poster on the right.

```html
<section id="poster" class="border-b border-stone-200 dark:border-stone-800">
  <div class="max-w-6xl mx-auto px-8 py-32">
    <!-- Section label -->
    <div class="flex items-center gap-4 mb-20">
      <span
        class="text-xs font-mono font-medium text-stone-900/60 dark:text-stone-50/60"
        >03</span
      >
      <span
        class="text-xs tracking-widest uppercase font-medium text-stone-900/80 dark:text-stone-50/80"
        >Poster</span
      >
      <div class="flex-1 h-px bg-stone-300 dark:bg-stone-700"></div>
    </div>

    <div class="grid grid-cols-12 gap-8">
      <!-- Dark poster -->
      <div
        class="col-span-12 md:col-span-7 bg-stone-950 dark:bg-stone-900 p-12 relative overflow-hidden min-h-[480px] flex flex-col justify-between"
      >
        <div>
          <div class="flex items-center gap-3 mb-12">
            <div class="w-6 h-px bg-[#003B8E]"></div>
            <span class="text-xs tracking-widest uppercase text-stone-50/60"
              >Subtitle</span
            >
          </div>
          <h2
            class="text-5xl md:text-7xl font-normal tracking-tight text-stone-50 leading-none"
          >
            Title<br />Lines
          </h2>
        </div>
        <div class="relative z-10">
          <div class="w-full h-px bg-stone-700 mb-6"></div>
          <div class="flex items-end justify-between">
            <p class="text-sm text-stone-50/70 leading-relaxed max-w-[28ch]">
              Description.
            </p>
            <div class="text-right">
              <div class="w-8 h-8 bg-[#003B8E] mb-2"></div>
              <span class="text-xs tracking-widest uppercase text-stone-50/40"
                >Label</span
              >
            </div>
          </div>
        </div>
      </div>

      <!-- Light poster -->
      <div
        class="col-span-12 md:col-span-5 bg-stone-100 dark:bg-stone-900 p-10 relative overflow-hidden min-h-[480px] flex flex-col justify-between border border-stone-200 dark:border-stone-800"
      >
        <div class="absolute top-0 left-0 w-full h-1 bg-[#C8102E]"></div>
        <div>
          <span
            class="text-xs tracking-widest uppercase text-stone-900/60 dark:text-stone-50/60"
            >Subtitle</span
          >
          <h2
            class="text-4xl md:text-5xl font-normal tracking-tight text-stone-900 dark:text-stone-50 leading-tight mt-6"
          >
            Title
          </h2>
          <p
            class="text-base leading-relaxed text-stone-900/70 dark:text-stone-50/70 mt-6 max-w-[32ch]"
          >
            Description.
          </p>
        </div>
        <div>
          <div class="grid grid-cols-2 gap-4 mb-8">
            <div>
              <span
                class="text-xs tracking-widest uppercase text-stone-900/40 dark:text-stone-50/40 block mb-1"
                >Date</span
              >
              <span class="text-sm text-stone-900 dark:text-stone-50"
                >Value</span
              >
            </div>
          </div>
          <button
            class="w-full py-3 bg-[#C8102E] text-white text-xs tracking-widest uppercase hover:bg-[#C8102E]/90 transition-colors"
          >
            CTA Button
          </button>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## Data Table Section

Full-width table with accent color sidebar and inline progress bars.

```html
<section id="data" class="border-b border-stone-200 dark:border-stone-800">
  <div class="max-w-6xl mx-auto px-8 py-32">
    <!-- Section label -->
    <div class="flex items-center gap-4 mb-20">
      <span
        class="text-xs font-mono font-medium text-stone-900/60 dark:text-stone-50/60"
        >04</span
      >
      <span
        class="text-xs tracking-widest uppercase font-medium text-stone-900/80 dark:text-stone-50/80"
        >Data</span
      >
      <div class="flex-1 h-px bg-stone-300 dark:bg-stone-700"></div>
    </div>

    <div class="grid grid-cols-12 gap-8">
      <div class="col-span-12 md:col-span-8">
        <h2
          class="text-3xl md:text-4xl font-normal tracking-tight text-stone-900 dark:text-stone-50 mb-3"
        >
          Table Title
        </h2>
        <p
          class="text-base text-stone-900/70 dark:text-stone-50/70 mb-12 max-w-[52ch]"
        >
          Description.
        </p>

        <table class="w-full text-sm">
          <thead>
            <tr
              class="border-t-2 border-stone-900 dark:border-stone-50 border-b border-b-stone-200 dark:border-b-stone-800"
            >
              <th
                class="text-left text-xs tracking-widest uppercase text-stone-900/60 dark:text-stone-50/60 font-medium py-3 pr-6 pl-4"
              >
                Column A
              </th>
              <th
                class="text-left text-xs tracking-widest uppercase text-stone-900/60 dark:text-stone-50/60 font-medium py-3 pr-6"
              >
                Column B
              </th>
              <th
                class="text-right text-xs tracking-widest uppercase text-stone-900/60 dark:text-stone-50/60 font-medium py-3 pr-4"
              >
                Score
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              class="border-b border-stone-200 dark:border-stone-800 hover:bg-stone-100 dark:hover:bg-stone-900 transition-colors"
            >
              <td class="py-4 pr-6 pl-4 text-stone-900 dark:text-stone-50">
                Row value
              </td>
              <td class="py-4 pr-6 text-stone-900/70 dark:text-stone-50/70">
                Metadata
              </td>
              <td class="py-4 pr-4 text-right">
                <div class="flex items-center justify-end gap-2">
                  <div
                    class="w-16 h-0.5 bg-stone-200 dark:bg-stone-800 relative"
                  >
                    <div
                      class="absolute left-0 top-0 h-full bg-[#C8102E]"
                      style="width: 80%"
                    ></div>
                  </div>
                  <span
                    class="text-sm font-mono text-stone-900/60 dark:text-stone-50/60 w-6"
                    >80</span
                  >
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Sidebar: accent color blocks -->
      <div class="col-span-12 md:col-span-4 flex flex-col gap-4">
        <div
          class="border border-stone-200 dark:border-stone-800 p-5 flex items-start gap-4"
        >
          <div
            class="w-8 h-8 shrink-0 mt-0.5"
            style="background-color: #C8102E"
          ></div>
          <div>
            <p class="text-sm font-medium text-stone-900 dark:text-stone-50">
              Color Name
            </p>
            <p
              class="text-xs text-stone-900/50 dark:text-stone-50/50 font-mono mt-0.5"
            >
              #C8102E
            </p>
            <p
              class="text-sm text-stone-900/60 dark:text-stone-50/60 mt-2 leading-relaxed"
            >
              Description.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## App Chrome Section

Sidebar + content layout mockup with traffic-light dots and breadcrumb.

```html
<section id="app" class="border-b border-stone-200 dark:border-stone-800">
  <div class="max-w-6xl mx-auto px-8 py-32">
    <!-- Section label -->
    <div class="flex items-center gap-4 mb-20">
      <span
        class="text-xs font-mono font-medium text-stone-900/60 dark:text-stone-50/60"
        >06</span
      >
      <span
        class="text-xs tracking-widest uppercase font-medium text-stone-900/80 dark:text-stone-50/80"
        >App</span
      >
      <div class="flex-1 h-px bg-stone-300 dark:bg-stone-700"></div>
    </div>

    <div class="border border-stone-200 dark:border-stone-800 overflow-hidden">
      <!-- App top bar -->
      <div
        class="border-b border-stone-200 dark:border-stone-800 bg-stone-100 dark:bg-stone-900 px-6 py-3 flex items-center justify-between"
      >
        <div class="flex items-center gap-6">
          <span
            class="text-sm font-medium tracking-widest uppercase text-stone-900 dark:text-stone-50"
            >App Name</span
          >
          <span class="text-sm text-stone-900/50 dark:text-stone-50/50"
            >Subtitle</span
          >
        </div>
        <div class="flex items-center gap-2">
          <span
            class="w-2 h-2 rounded-full bg-stone-300 dark:bg-stone-700"
          ></span>
          <span
            class="w-2 h-2 rounded-full bg-stone-300 dark:bg-stone-700"
          ></span>
          <span class="w-2 h-2 rounded-full bg-[#C8102E]"></span>
        </div>
      </div>

      <div class="flex">
        <!-- Sidebar -->
        <div
          class="w-48 border-r border-stone-200 dark:border-stone-800 bg-stone-50 dark:bg-stone-950 p-6 min-h-72 shrink-0"
        >
          <span
            class="text-xs tracking-widest uppercase text-stone-900/50 dark:text-stone-50/50 block mb-4"
            >Menu Group</span
          >
          <ul class="space-y-0.5">
            <li>
              <a
                href="#"
                class="flex items-center justify-between py-2 px-2 text-sm text-[#C8102E] bg-[#C8102E]/5"
              >
                <span>Active Item</span>
                <span class="font-mono text-xs text-[#C8102E]/70">34</span>
              </a>
            </li>
            <li>
              <a
                href="#"
                class="flex items-center justify-between py-2 px-2 text-sm text-stone-900/60 dark:text-stone-50/60 hover:text-stone-900 dark:hover:text-stone-50 hover:bg-stone-100 dark:hover:bg-stone-900 transition-colors"
              >
                <span>Inactive Item</span>
                <span
                  class="font-mono text-xs text-stone-900/40 dark:text-stone-50/40"
                  >22</span
                >
              </a>
            </li>
          </ul>
        </div>

        <!-- Main content -->
        <div class="flex-1 p-8">
          <!-- Breadcrumb -->
          <div
            class="flex items-center gap-2 text-sm text-stone-900/50 dark:text-stone-50/50 mb-6"
          >
            <span>Parent</span>
            <span>/</span>
            <span class="text-stone-900 dark:text-stone-50">Current</span>
          </div>
          <div class="flex items-start justify-between mb-8">
            <div>
              <h3
                class="text-2xl font-normal text-stone-900 dark:text-stone-50"
              >
                Page Title
              </h3>
              <p class="text-sm text-stone-900/60 dark:text-stone-50/60 mt-1">
                34 items
              </p>
            </div>
            <button
              class="px-4 py-2 bg-[#C8102E] text-white text-xs tracking-widest uppercase hover:bg-[#C8102E]/90 transition-colors"
            >
              Action
            </button>
          </div>
          <!-- Content list -->
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## Form Section (Swiss Style)

Two-column: metadata on left, form card on right.

```html
<section
  id="form"
  class="border-b border-stone-200 dark:border-stone-800 bg-stone-100 dark:bg-stone-900"
>
  <div class="max-w-6xl mx-auto px-8 py-32">
    <!-- Section label -->
    <div class="flex items-center gap-4 mb-20">
      <span
        class="text-xs font-mono font-medium text-stone-900/60 dark:text-stone-50/60"
        >09</span
      >
      <span
        class="text-xs tracking-widest uppercase font-medium text-stone-900/80 dark:text-stone-50/80"
        >Form</span
      >
      <div class="flex-1 h-px bg-stone-200 dark:bg-stone-800"></div>
    </div>

    <div class="grid grid-cols-12 gap-8">
      <!-- Left: metadata -->
      <div class="col-span-12 md:col-span-5">
        <div class="w-6 h-px bg-[#F0B429] mb-8"></div>
        <h2
          class="text-3xl md:text-4xl font-normal tracking-tight text-stone-900 dark:text-stone-50 mb-4"
        >
          Form Title
        </h2>
        <p
          class="text-base leading-relaxed text-stone-900/60 dark:text-stone-50/60 max-w-[36ch]"
        >
          Description.
        </p>
        <div class="mt-12 space-y-4">
          <div
            class="flex gap-4 border-t border-stone-200 dark:border-stone-800 pt-4"
          >
            <span
              class="text-xs tracking-widest uppercase text-stone-900/50 dark:text-stone-50/50 w-20 shrink-0 pt-0.5"
              >Label</span
            >
            <span class="text-sm text-stone-900/80 dark:text-stone-50/80"
              >Value</span
            >
          </div>
        </div>
      </div>

      <!-- Right: form card -->
      <div class="col-span-12 md:col-span-6 md:col-start-7">
        <form
          class="space-y-6 bg-stone-50 dark:bg-stone-950 border border-stone-200 dark:border-stone-800 p-8"
          onsubmit="return false"
        >
          <div class="grid grid-cols-2 gap-4">
            <div class="flex flex-col gap-2">
              <label
                class="text-xs tracking-widest uppercase text-stone-900/60 dark:text-stone-50/60 font-medium"
                >First name</label
              >
              <input
                type="text"
                class="border border-stone-300 dark:border-stone-700 bg-transparent text-stone-900 dark:text-stone-50 text-base px-4 py-3 outline-none focus:border-stone-900 dark:focus:border-stone-50 placeholder:text-stone-900/30 dark:placeholder:text-stone-50/30 transition-colors"
                placeholder="First"
              />
            </div>
            <div class="flex flex-col gap-2">
              <label
                class="text-xs tracking-widest uppercase text-stone-900/60 dark:text-stone-50/60 font-medium"
                >Last name</label
              >
              <input
                type="text"
                class="border border-stone-300 dark:border-stone-700 bg-transparent text-stone-900 dark:text-stone-50 text-base px-4 py-3 outline-none focus:border-stone-900 dark:focus:border-stone-50 placeholder:text-stone-900/30 dark:placeholder:text-stone-50/30 transition-colors"
                placeholder="Last"
              />
            </div>
          </div>
          <div class="flex flex-col gap-2">
            <label
              class="text-xs tracking-widest uppercase text-stone-900/60 dark:text-stone-50/60 font-medium"
              >Email address</label
            >
            <input
              type="email"
              class="border border-stone-300 dark:border-stone-700 bg-transparent text-stone-900 dark:text-stone-50 text-base px-4 py-3 outline-none focus:border-stone-900 dark:focus:border-stone-50 placeholder:text-stone-900/30 dark:placeholder:text-stone-50/30 transition-colors"
              placeholder="email@example.com"
            />
          </div>
          <div class="flex flex-col gap-2">
            <label
              class="text-xs tracking-widest uppercase text-stone-900/60 dark:text-stone-50/60 font-medium"
              >Option</label
            >
            <select
              class="border border-stone-300 dark:border-stone-700 bg-stone-50 dark:bg-stone-950 text-stone-900 dark:text-stone-50 text-base px-4 py-3 outline-none focus:border-stone-900 dark:focus:border-stone-50 appearance-none"
            >
              <option>Option 1</option>
              <option>Option 2</option>
            </select>
          </div>
          <div class="flex flex-col gap-2">
            <label
              class="text-xs tracking-widest uppercase text-stone-900/60 dark:text-stone-50/60 font-medium"
              >Message (optional)</label
            >
            <textarea
              rows="3"
              class="border border-stone-300 dark:border-stone-700 bg-transparent text-stone-900 dark:text-stone-50 text-base px-4 py-3 outline-none focus:border-stone-900 dark:focus:border-stone-50 resize-none transition-colors placeholder:text-stone-900/30 dark:placeholder:text-stone-50/30"
              placeholder="Additional info..."
            ></textarea>
          </div>
          <label class="flex items-start gap-3 cursor-pointer">
            <input
              type="checkbox"
              class="mt-0.5 w-4 h-4 border border-stone-400 dark:border-stone-600 accent-[#F0B429]"
            />
            <span
              class="text-sm text-stone-900/60 dark:text-stone-50/60 leading-relaxed"
              >I agree to the terms.</span
            >
          </label>
          <button
            type="submit"
            class="w-full py-4 bg-[#F0B429] text-stone-900 text-xs tracking-widest uppercase font-medium hover:bg-[#F0B429]/90 transition-colors"
          >
            Submit
          </button>
        </form>
      </div>
    </div>
  </div>
</section>
```

---

## Color Palette Section

Grayscale swatch grid + accent palette with opacity strips.

```html
<section id="color" class="border-b border-stone-200 dark:border-stone-800">
  <div class="max-w-6xl mx-auto px-8 py-32">
    <!-- Section label -->
    <div class="flex items-center gap-4 mb-20">
      <span
        class="text-xs font-mono font-medium text-stone-900/60 dark:text-stone-50/60"
        >08</span
      >
      <span
        class="text-xs tracking-widest uppercase font-medium text-stone-900/80 dark:text-stone-50/80"
        >Color</span
      >
      <div class="flex-1 h-px bg-stone-300 dark:bg-stone-700"></div>
    </div>

    <!-- Grayscale swatches -->
    <div class="mb-20">
      <h3
        class="text-sm font-medium tracking-widest uppercase text-stone-900/80 dark:text-stone-50/80 mb-8"
      >
        Grayscale
      </h3>
      <div
        class="grid grid-cols-5 md:grid-cols-11 gap-px bg-stone-200 dark:bg-stone-800"
      >
        <!-- Each swatch: aspect-square with scale number -->
      </div>
    </div>

    <!-- Accent palette x opacity -->
    <div class="mb-20">
      <h3
        class="text-sm font-medium tracking-widest uppercase text-stone-900/80 dark:text-stone-50/80 mb-8"
      >
        Accent palette × opacity
      </h3>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
        <!-- Each accent: name + opacity strips -->
      </div>
    </div>

    <!-- Opacity rule callout -->
    <div class="bg-stone-900 p-8 border-l-2 border-stone-600">
      <h3 class="text-lg font-medium text-stone-50 mb-3">The opacity rule</h3>
      <p class="text-base leading-relaxed text-stone-50/70 max-w-[60ch]">
        To make text less dominant, reduce opacity — never change the hue.
      </p>
    </div>
  </div>
</section>
```

---

## Responsive Section (Dark)

Breakpoint table + code examples in a 2x2 grid + gotchas.

```html
<section
  id="responsive"
  class="border-b border-stone-200 dark:border-stone-800 bg-stone-900 dark:bg-stone-950 text-stone-50 relative overflow-hidden"
>
  <div
    class="max-w-6xl mx-auto px-4 md:px-8 py-16 md:py-24 lg:py-32 relative z-10"
  >
    <!-- Section label -->
    <div class="flex items-center gap-4 mb-16 md:mb-20">
      <span class="text-xs font-mono font-medium text-stone-50/60">10</span>
      <span
        class="text-xs tracking-widest uppercase font-medium text-stone-50/80"
        >Responsive</span
      >
      <div class="flex-1 h-px bg-stone-700"></div>
    </div>

    <!-- Breakpoint table -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-16 mb-16 md:mb-24">
      <div>
        <h2
          class="text-3xl md:text-4xl lg:text-5xl font-medium tracking-tight leading-tight text-stone-50 mb-6"
        >
          Mobile first.<br />Always.
        </h2>
        <p class="text-lg leading-relaxed text-stone-50/80 max-w-[52ch]">
          Description.
        </p>
      </div>
      <div class="space-y-4">
        <!-- Breakpoint rows -->
        <div class="flex items-start gap-4 border-t border-stone-800 pt-4">
          <div class="shrink-0 w-12">
            <code class="font-mono text-xs text-[#C8102E]">md:</code>
          </div>
          <div class="shrink-0 w-16">
            <span class="font-mono text-xs text-stone-50/40">768px+</span>
          </div>
          <div>
            <span class="text-sm font-medium text-stone-50 block">Tablet</span>
            <span class="text-sm text-stone-50/60">Multi-column</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Code examples (2x2 grid with 1px gap) -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-px bg-stone-800">
      <div class="bg-stone-900 dark:bg-stone-950 p-6 md:p-8">
        <span
          class="text-xs tracking-widest uppercase text-stone-50/40 block mb-4"
          >Pattern name</span
        >
        <pre
          class="font-mono text-sm text-stone-50/80 leading-relaxed overflow-x-auto"
        ><code>code here</code></pre>
      </div>
    </div>

    <!-- Gotchas row -->
    <div
      class="mt-8 md:mt-12 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-px bg-stone-800"
    >
      <div class="bg-stone-900 dark:bg-stone-950 p-6">
        <p class="text-sm font-medium text-stone-50 mb-4 leading-snug">
          Rule text
        </p>
        <div class="space-y-2">
          <div class="flex items-start gap-2">
            <span class="text-stone-50/30 text-xs mt-0.5 shrink-0">✗</span>
            <code class="font-mono text-xs text-stone-50/40">bad example</code>
          </div>
          <div class="flex items-start gap-2">
            <span class="text-[#C8102E] text-xs mt-0.5 shrink-0">✓</span>
            <code class="font-mono text-xs text-stone-50/70">good example</code>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## Hero Section (Swiss Style)

Full-height hero with background numeral and vertical label column.

```html
<section
  id="hero"
  class="relative min-h-screen flex items-center overflow-hidden border-b border-stone-200 dark:border-stone-800"
>
  <!-- Large background numeral -->
  <div
    class="absolute top-0 right-0 text-[clamp(10rem,28vw,26rem)] font-light leading-none text-stone-900/5 dark:text-stone-50/5 select-none pointer-events-none translate-x-8"
  >
    01
  </div>

  <div
    class="max-w-6xl mx-auto px-8 py-40 relative z-10 grid grid-cols-12 gap-8 w-full"
  >
    <div class="col-span-12 md:col-span-8">
      <span
        class="text-sm tracking-widest uppercase font-medium text-stone-900/80 dark:text-stone-50/80"
        >Subtitle</span
      >
      <div class="w-8 h-px bg-[#C8102E] mt-6 mb-10"></div>
      <h1
        class="text-6xl md:text-8xl font-medium tracking-tight leading-none text-stone-900 dark:text-stone-50"
      >
        Headline<br />Lines<br />Here.
      </h1>
      <p
        class="text-xl leading-relaxed text-stone-900/80 dark:text-stone-50/80 mt-10 max-w-[52ch]"
      >
        Body text description.
      </p>
      <div class="mt-12 flex flex-col sm:flex-row items-start gap-4">
        <div
          class="bg-stone-900 dark:bg-stone-50 text-stone-50 dark:text-stone-900 px-6 py-3 font-mono text-sm select-all"
        >
          command here
        </div>
        <a
          href="#"
          class="px-6 py-3 border border-stone-400 dark:border-stone-600 text-stone-900/80 dark:text-stone-50/80 text-sm tracking-wide hover:border-stone-900 dark:hover:border-stone-50 transition-colors"
        >
          Link Text ↗
        </a>
      </div>
    </div>

    <!-- Column of vertical labels -->
    <div class="hidden md:flex col-span-4 flex-col justify-end gap-6 pb-4">
      <div
        class="flex items-center gap-3 border-t border-stone-300 dark:border-stone-700 pt-4"
      >
        <span
          class="text-xs text-stone-900/60 dark:text-stone-50/60 font-mono font-medium"
          >01</span
        >
        <span
          class="text-xs tracking-widest uppercase font-medium text-stone-900/80 dark:text-stone-50/80"
          >Feature label</span
        >
      </div>
    </div>
  </div>
</section>
```

---

## Editorial Section (Swiss Style)

Essay + sidebar with pull quote, principles card, and two-schools card.

```html
<section id="editorial" class="border-b border-stone-200 dark:border-stone-800">
  <!-- Thin accent bar across the top -->
  <div class="h-1 bg-[#C8102E]"></div>

  <div class="max-w-6xl mx-auto px-4 md:px-8 py-24 md:py-32">
    <!-- Section label -->
    <div class="flex items-center gap-4 mb-20">
      <span
        class="text-xs font-mono font-medium text-stone-900/60 dark:text-stone-50/60"
        >02</span
      >
      <span
        class="text-xs tracking-widest uppercase font-medium text-stone-900/80 dark:text-stone-50/80"
        >Editorial</span
      >
      <div class="flex-1 h-px bg-stone-300 dark:bg-stone-700"></div>
    </div>

    <div class="grid grid-cols-12 gap-8">
      <!-- Main essay column -->
      <div class="col-span-12 md:col-span-7 relative">
        <!-- Accent rectangle in the left margin -->
        <div
          class="absolute -left-8 top-2 w-1 h-16 bg-[#C8102E] hidden md:block"
        ></div>

        <h2
          class="text-4xl md:text-5xl font-normal tracking-tight text-stone-900 dark:text-stone-50 leading-tight mb-10"
        >
          Heading text here.
        </h2>
        <p
          class="text-lg leading-relaxed text-stone-900 dark:text-stone-50 max-w-[60ch] mb-6"
        >
          Primary body text at full opacity.
        </p>
        <p
          class="text-lg leading-relaxed text-stone-900/70 dark:text-stone-50/70 max-w-[60ch] mb-6"
        >
          Secondary body text at 70% opacity.
        </p>
        <p
          class="text-lg leading-relaxed text-stone-900/60 dark:text-stone-50/60 max-w-[60ch]"
        >
          Tertiary body text at 60% opacity.
        </p>
        <div
          class="mt-10 pt-10 border-t border-stone-200 dark:border-stone-800"
        >
          <span
            class="text-sm tracking-widest uppercase text-stone-900/50 dark:text-stone-50/50"
            >— Attribution, <em>Source</em>, Year</span
          >
        </div>
      </div>

      <!-- Right column -->
      <div class="col-span-12 md:col-span-4 md:col-start-9 flex flex-col gap-8">
        <!-- Pull quote with left accent bar -->
        <!-- Key principles card with accent top bar -->
        <!-- Two-schools card with accent top bar -->
      </div>
    </div>
  </div>
</section>
```

---

## Masonry Image Grid (Inspiration Page)

```html
<div class="columns-1 sm:columns-2 lg:columns-3 gap-8 space-y-8">
  <div class="break-inside-avoid">
    <a href="#" class="group block">
      <div
        class="overflow-hidden bg-stone-100 dark:bg-stone-900 border border-stone-200 dark:border-stone-800"
      >
        <img
          src="image.jpg"
          alt=""
          loading="lazy"
          class="w-full block group-hover:opacity-90 transition-opacity duration-200"
        />
      </div>
      <div class="mt-4 pb-8 border-b border-stone-200 dark:border-stone-800">
        <h3
          class="text-sm font-medium text-stone-900 dark:text-stone-50 leading-snug group-hover:text-[#C8102E] transition-colors"
        >
          Title
        </h3>
        <span class="text-xs text-stone-900/40 dark:text-stone-50/40 block mb-1"
          >Attribution</span
        >
        <div class="flex items-center gap-3">
          <span
            class="text-xs font-mono text-stone-900/50 dark:text-stone-50/50"
            >Year</span
          >
          <span
            class="text-xs tracking-widest uppercase font-medium px-1.5 py-0.5 bg-stone-100 dark:bg-stone-900 text-stone-900/60 dark:text-stone-50/60"
            >Category</span
          >
        </div>
      </div>
    </a>
  </div>
</div>
```

---

## Category Filter Buttons

```html
<div
  class="flex items-center gap-2 flex-wrap mb-16 border-t border-stone-200 dark:border-stone-800 pt-8"
>
  <a
    href="#"
    class="px-4 py-2 text-xs tracking-widest uppercase font-medium border border-stone-300 dark:border-stone-700 text-stone-900/70 dark:text-stone-50/70 hover:bg-stone-900 hover:text-stone-50 dark:hover:bg-stone-50 dark:hover:text-stone-900 transition-colors"
  >
    Category
  </a>
</div>
```
