# Digital Footprint Audit Checklist

Run this BEFORE building entity signals. The audit determines what exists,
what's missing, and whether any existing entity data belongs to a DIFFERENT
person with the same name.

## 1. Wikidata Search (CRITICAL — do this first)

Search for the person's name on Wikidata. If a Q-item exists, verify it is
the RIGHT person:

```bash
curl -s "https://www.wikidata.org/w/api.php?action=wbsearchentities&search=FIRSTNAME%20LASTNAME&language=en&format=json&limit=10" | python3 -c "
import json, sys
d = json.load(sys.stdin)
for r in d.get('search', []):
    print(f\"{r['id']}: {r.get('label','')} — {r.get('description','')}\")"
```

If a Q-item exists, fetch its full data and check:
- Occupation (P106) — does it match?
- Date of birth (P569) — does it match?
- Description — is it the same person?

If it's a different person, DO NOT edit that item. Create a new one with a
disambiguating description (e.g., "German blockchain engineer" vs "German physician").

## 2. Domain Availability

Check if firstname-lastname.com is available. This is the ideal domain for
entity signals.

```bash
whois FIRSTNAME-LASTNAME.com | grep -iE "No match|NOT FOUND|Creation Date"
```

Also check .dev, .io, .de (for German persons).

## 3. Existing Profiles

Check each platform for an existing profile and note the URL slug/handle:

- **X/Twitter**: What's the handle? What does the bio say? What location?
- **GitHub**: What's the username? Bio? Location? Profile photo?
- **LinkedIn**: What's the URL slug? Headline? Location?
- **Crunchbase**: Does a profile exist?
- **Google Scholar**: Any publications indexed?
- **Amazon Author**: If they've published books, is there an author page?

## 4. Academic/Professional Records

- **DBLP**: Search for publications
  ```bash
  curl -s "https://dblp.org/search/author/api?q=FIRSTNAME+LASTNAME&format=json"
  ```
- **University**: If they have a PhD, is the thesis indexed by the university library?
- **GND (German National Library)**: For German persons. Use lobid.org API
  (the direct DNB portal API returns 404 for some endpoints).
  ```bash
  # Search by name (use lobid.org, NOT portal.dnb.de)
  curl -s 'https://lobid.org/gnd/search?q=preferredName%3A%22LASTNAME%2C+FIRSTNAME%22&format=json&size=10'

  # Check a specific GND ID
  curl -s "https://lobid.org/gnd/ID/about" | python3 -c "
  import json, sys
  d = json.load(sys.stdin)
  # Check: professionOrOccupation, dateOfBirth, academicDegree, affiliation
  "
  ```
  CRITICAL: Verify the GND entry is the right person. Common names have
  multiple entries with different professions and birth dates.

## 5. Independent Press Coverage

This is the most important gap to identify. Count:
- Tier-1 press (NYT, WSJ, Reuters) — extremely hard to get
- Tier-2 press (Forbes, industry-specific like CoinDesk/Decrypt for crypto)
- Tier-3 press (smaller outlets, blogs, interviews)
- Hackathon listings, conference talks, podcast appearances

Each independent mention can serve as a P854 reference URL on Wikidata.
Without at least 2-3, the Knowledge Panel may not instantiate.

## 6. Current Website Schema

If the person already has a website, check for existing JSON-LD:
```bash
curl -s "https://SITE.com/" | grep -o 'application/ld+json'
```

## 7. Summary Table

After the audit, produce a table:

| Item | Status | URL/Value | Notes |
|------|--------|-----------|-------|
| Personal domain | Available/Owned | | |
| Wikidata item | None/Wrong person/Correct | Q-number | |
| Website schema | None/Partial/Complete | | |
| Commons image | None/Exists | | |
| LinkedIn | Exists/Needs update | URL | |
| X/Twitter | Exists/Needs update | handle | |
| GitHub | Exists/Needs update | username | |
| Crunchbase | None/Exists | URL | |
| Press coverage | Count + tiers | | |
| Consistency | Aligned/Gaps | | |

This table becomes the gap analysis that drives the action plan.
