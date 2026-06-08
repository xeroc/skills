---
name: seo-optimizer
---

## ✅ Programmatic SEO Tasks (to automate in your skill)

### 1. Set up meta tags on every page (title, description, OG image)

**How to automate:**

- Use a template engine (e.g., Jinja2 for Python, EJS for Node) or CMS hooks.
- Maintain a JSON/YAML config mapping each route to:
  - `title`
  - `description`
  - `og_image` (URL)
  - `og_type` (default `website`, `article` for blogs)
- Render tags in `<head>` dynamically.

**Example Python (Flask):**

```python
def generate_meta_tags(page_key):
    meta = meta_config.get(page_key, {})
    return f"""
    <title>{meta.get('title')}</title>
    <meta name="description" content="{meta.get('description')}">
    <meta property="og:title" content="{meta.get('title')}">
    <meta property="og:description" content="{meta.get('description')}">
    <meta property="og:image" content="{meta.get('og_image')}">
    """
```

**Validation:**  
Script should crawl all local routes and check that no page is missing `title`, `description`, `og:image`.

---

### 2. Add SoftwareApplication + FAQ schema (structured data)

**How to automate:**

- Inject JSON-LD script into `<body>` or `<head>`.
- Use a schema generator library (`schema-dorg` in Python, `jsonld` in Node).
- For FAQ: pull Q&A pairs from a CMS or markdown frontmatter.

**Example (SoftwareApplication + FAQ combined):**

```python
software_schema = {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Your App",
    "applicationCategory": "BusinessApplication",
    "offers": {...},
    "mainEntity": {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "Q1", "acceptedAnswer": {"@type": "Answer", "text": "A1"}}
        ]
    }
}
```

**Automated check:**  
Run a JSON-LD validator against each page’s rendered HTML.

---

### 3. Verify site in Google Search Console

**Automate via API (recommended):**

- Use Google Search Console API with OAuth 2.0.
- Automatically add property (URL-prefix or domain).
- Trigger ownership verification using DNS or HTML file upload (programmatically place `google[hash].html` in `.well-known/`).

**Sample script logic (Python):**

```python
from google.oauth2 import service_account
from googleapiclient.discovery import build

credentials = service_account.Credentials.from_service_account_file('key.json')
gsc = build('searchconsole', 'v1', credentials=credentials)
gsc.webmasters().sites().add(siteUrl='https://example.com/').execute()
```

---

### 4. Submit sitemap.xml to GSC

**Automate via API:**

- After generating `sitemap.xml` dynamically (using a crawler of your routes), call:

```python
gsc.sitemaps().submit(
    siteUrl='https://example.com/',
    feedpath='https://example.com/sitemap.xml'
).execute()
```

- Verify submission status via `gsc.sitemaps().list()`.

---

### 5. Manually request indexing for 5 core pages — **cannot fully automate** (Google requires user action), but you can

- Build a CLI tool that opens each URL in Chrome with `?force_indexing=1` and logs the need to click “Request Indexing” in GSC Inspector.
- Or use the **Indexing API** (only for job postings or livestream videos — not general pages).

**Better approach:**  
Let human handle this manually (see Manual section).

---

### 6. Set up Bing Webmaster Tools (import from GSC)

**Automate:**

- Bing API supports site import from GSC.
- Use OAuth and call:

```http
POST https://ssl.bing.com/webmaster/api.svc/json/AddSiteFromGoogleSearchConsole?apikey=YOUR_API_KEY
```

- Body contains GSC site URL and auth token.

---

### 7. Cross-link from existing property to new site

**Automate (partially):**

- Crawl existing site for pages with high authority (using your own crawler or ScreamingFrog CLI).
- Auto-insert a contextual link to the new site where relevant using regex/template matching.
- **Caution:** Manual review advised for quality — but can be batched if you control both CMSs.

---

### 8. Check robots.txt — nothing blocking crawlers

**Automate:**

```python
import requests
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.parse(requests.get('https://example.com/robots.txt').text)
disallowed = [rule.path for rule in rp.default_entry.line_groups if rule.allowance == False]
```

Fail if `/` or `/*` is disallowed for `Googlebot` or `*`.

---

### 9. Check all core pages are being indexed in GSC

**Automate via GSC API:**

```python
for url in core_pages:
    status = gsc.urlInspection().index().inspect(
        body={'inspectionUrl': url, 'siteUrl': 'https://example.com/'}
    ).execute()
    if status['inspectionResult']['indexStatus'] != 'INDEXED':
        alert(url)
```

---

### 10. Check canonical tags on all key pages

**Automate:**

- Crawl each page → extract `<link rel="canonical" href="...">`.
- Compare with expected canonical URL (from config).
- Fail if:
  - Missing canonical
  - Canonical points to different domain
  - Canonical is not absolute URL

---

### 11. Add alt text to all images

**Automate (two-step):**

- Crawl all images missing `alt=""` or `alt` attribute.
- Use an AI model (BLIP, GPT-4V, or local ML) to generate alt text.
- Auto-patch HTML or CMS content via API.

**Example:**

```bash
python -c "from auto_alt import fix_missing_alts; fix_missing_alts('https://example.com')"
```

---

### 12. Add `noindex` to login, dashboard, onboarding pages

**Automate:**

- For each specified route (`/login`, `/dashboard`, `/onboarding/*`), inject:

```html
<meta name="robots" content="noindex, nofollow" />
```

- Use middleware or server-side render check:

```python
if request.path.startswith(('/login', '/dashboard', '/onboarding')):
    response.headers['X-Robots-Tag'] = 'noindex, nofollow'
```

---

## 🧑‍💻 Manual SEO Tasks (for human execution)

| Task                                                 | Why manual                                                | How to check                                                          |
| ---------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------- |
| **Request indexing for 5 core pages**                | Google requires manual click in GSC Inspector.            | Human goes to GSC → URL Inspection → “Request Indexing”.              |
| **Check page speed & Core Web Vitals**               | Lab data + field data; requires interpretation.           | Run each core page through `pagespeed.web.dev`. Record LCP, CLS, FID. |
| **Confirm Core Web Vitals: LCP < 2.5s, CLS minimal** | Automated tools give scores, but real UX judgment needed. | Use Lighthouse in Chrome DevTools. Retest after fixes.                |
| **Cross-link quality review**                        | Automated linking can look spammy.                        | Manually review 3–5 cross-links for relevance.                        |
| **Verify Bing import from GSC**                      | UI confirmation step.                                     | Log into Bing Webmaster Tools → Settings → Import.                    |
| **Alt text quality check**                           | AI can generate, but human ensures accuracy/context.      | Spot-check 10% of images.                                             |

---

## 🧠 Final Skill Integration

Your skill’s CLI could run:

```bash
seo-automate --all
```

Which internally runs:

1. Meta tag validation
2. Schema injection + validation
3. GSC site addition + sitemap submit
4. Bing import via API
5. robots.txt & canonical checks
6. noindex for auth pages
7. Alt text auto-generation

Then output:

```
✅ Automated tasks complete.
📋 Manual tasks required:
 - Request indexing for: /pricing, /features, /signup, /demo, /docs
 - Run pagespeed.web.dev on those 5 URLs
 - Check cross-links from old-site.com to new-site.com
```
