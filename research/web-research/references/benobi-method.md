# Benobi.one Method — Validated Execution Reference

Source: benobi.one/posts/google-knowledge-panel-guide/ (June 2026)
Case: Ben Sigman, entrepreneur and author. Panel appeared ~73 days from first
schema commit, ~38 days from full Wikidata + Commons image completion.

## Validated Timeline

| Date | Event |
|------|-------|
| Apr 12 | First JSON-LD schema deployed |
| Apr 13 | Wikidata item created, schema refactored to @graph |
| Apr 14 | llms.txt deployed |
| May 7 | City consistency fix + Wikidata Q-URL in sameAs |
| May 16 | **Wikimedia Commons image + P18 added** (the unlock) |
| ~Jun 23 | **Knowledge Panel went live** |

Key insight: Wikidata item existed since Apr 13 but panel didn't appear until
P18 was set on May 16 (~5 weeks later).

## JSON-LD Schema Extras (beyond basic Person)

These additions shipped on benobi.one and may have helped:

```json
"gender": "Male",
"nationality": {"@type": "Country", "name": "United States"},
"homeLocation": {
  "@type": "Place",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Santa Monica",
    "addressRegion": "CA",
    "addressCountry": "US"
  }
},
"alumniOf": {
  "@type": "CollegeOrUniversity",
  "name": "University of California, Los Angeles",
  "sameAs": "https://www.wikidata.org/wiki/Q174710"
}
```

For affiliations, use OrganizationRole with roleName instead of plain Organization:

```json
"affiliation": [{
  "@type": "OrganizationRole",
  "roleName": "Founder & CEO",
  "memberOf": {
    "@type": "Organization",
    "name": "Your Company",
    "url": "https://yourcompany.com/",
    "founder": {"@id": "https://yoursite.com/#you"}
  }
}]
```

## Wikidata Properties That Mattered

| Property | Purpose | Notes |
|----------|---------|-------|
| P31 | instance of → human (Q5) | Required |
| P21 | sex or gender | |
| P106 | occupation (can add multiple) | Use specific Q-items |
| P800 | notable work → Q-items (not strings) | Create work Q-items first |
| P18 | image → Commons filename | **Highest impact. The unlock.** |
| P551 | residence → city Q-item | Must match JSON-LD homeLocation |
| P856 | official website | Bidirectional bridge with JSON-LD sameAs |
| P735 | given name Q-item | |
| P734 | family name Q-item | |
| P69 | educated at → university Q-item | Add P582 end-time with graduation year |
| P512 | academic degree | |
| P2002 | X username | Just the handle, no @ |
| P2037 | GitHub username | Just the handle |
| P6634 | LinkedIn personal profile ID | The slug from the URL |
| P2963 | Goodreads author ID | Numeric part only |
| P2003 | Instagram username | Just the handle |
| P2397 | YouTube channel ID | UCxxxx portion |

## What Didn't Work

### Wikipedia Article via Articles for Creation
Submitted May 16, declined May 18. Two reasons:
1. Notability/sources — most sources mentioned the subject but weren't ABOUT
   them. Wikipedia's WP:GNG demands "significant coverage."
2. LLM-detection flag — article had LLM drafting tells. Once flagged, harder
   to push through even if rewritten.

Lesson: Don't draft Wikipedia articles with LLMs. Don't submit until you have
at least one source that is ABOUT the person. Wait 2-3 months between declines.

### Organization Q-items Without Press
Deferred for companies without independent press. Wikidata items for orgs
without press get nominated for deletion fast. Wait until each org has at
least one independent article.

## Cross-Platform Consistency Requirements

Match across ALL of these:
- Your site schema (homeLocation, jobTitle, description)
- Wikidata (P551 residence, P106 occupation)
- LinkedIn (headline, location, about)
- X/Twitter (bio, location)
- Crunchbase
- Amazon Author Central (if applicable)
- about.me or similar

## Post-Deploy CDN Sequence (Critical)

After deploying schema changes:
1. Push to git (parent + submodule if Hugo/Pages)
2. Purge Cloudflare: Dashboard → Caching → Configuration → Purge Everything
3. Verify: `curl -sI -A "Googlebot" "https://site.com/?v=$(date +%s)" | grep -iE "^age:|cf-cache"`
4. If Age > 600, purge is needed
5. Re-verify: 5 fetches, all should be Age < 30
6. Search Console → URL Inspection → TEST LIVE URL → REQUEST INDEXING

## Validation Workflow (After Changes)

1. Schema.org Validator (https://validator.schema.org/) — 0 errors, 0 warnings
2. Google Rich Results Test (https://search.google.com/test/rich-results) —
   Person and WebSite won't appear here (expected). SoftwareApplication and
   Book will if present.
3. Cache-bust: append `?v=N` to force fresh re-fetch
4. Search Console → URL Inspection → Request Indexing

## What "Complete" Looks Like

- JSON-LD @graph: Person + WebSite (optionally Books, SoftwareApplications),
  all linked via @id
- Person sameAs includes Wikidata Q-URL
- Wikidata Q-item: 10+ properties, every statement P854-referenced
- P18 (image) set from Wikimedia Commons
- P551 (residence) matches homeLocation in JSON-LD
- Identifiers in Wikidata: all relevant profile IDs
- llms.txt at site root
- robots.txt with sitemap reference
- Schema.org validator: 0 errors, 0 warnings
- Search Console: sitemap submitted, indexing requested
- Cross-platform consistency across all profiles
- At least 2 independent press pieces
