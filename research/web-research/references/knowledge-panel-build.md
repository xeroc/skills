# Google Knowledge Panel Builder (Mode C playbook)

Full playbook for Mode C — entity visibility build — of the `web-research`
skill. A Knowledge Panel is the info box Google shows on the right side when
you search for a notable entity. You don't apply for one — you give Google the
right signals and it instantiates one from its Knowledge Graph.

Routing within this skill: Mode C BUILDS entity signals (schema markup,
Wikidata, Commons, cross-platform consistency). For one-shot research about a
person/org without building anything — a research brief (Mode A) or bulk
entity enrichment notes (Mode B) — use those modes instead.

## The 5-Step Recipe

1. **Schema markup** — JSON-LD `Person` (or `Organization`) on a website you control
2. **Wikidata Q-item** — every claim referenced to an independent source
3. **Wikimedia Commons image** — upload headshot, add P18 to Wikidata (the unlock)
4. **Cross-platform consistency** — same name, city, title, bio everywhere
5. **Wait** — 5-10 weeks from all-signals-complete to panel

## Critical Principles

### Every Wikidata statement needs a P854 reference URL
Unreferenced claims get nominated for deletion within days. Editors patrol the
New Items queue. This is the #1 reason Wikidata items fail. Every P31, P106,
P800, P69, P551, identifier — each needs at least one `reference URL (P854)`
plus `retrieved (P813) = today`.

### P18 (image) is the single highest-impact step
In the reference case (benobi.one), the panel did not appear until P18 was set.
Google waits for a definitive, declarative image source before instantiating.
Upload to Wikimedia Commons under CC-BY-SA 4.0, then add P18 with the filename.

### Wikipedia is NOT required
The reference case achieved a panel without a Wikipedia article. The Wikipedia
AfC was actually declined. Do not block on Wikipedia.

### Cross-platform consistency is non-negotiable
Same city. Same title. Same bio. Google cross-references LinkedIn, X, GitHub,
Crunchbase, Amazon Author, about.me. One inconsistency weakens the signal.

### Independent press is the strongest lever — but academic publications are equivalent
One tier-2 press piece (Forbes-level, or industry-specific like CoinDesk/Decrypt
for crypto) outweighs everything else. Hackathon listings, conference talks,
and podcasts all count as secondary signals.

For anyone with academic publications (PhD thesis, journal/conference papers),
those are ALREADY independent, DOI-indexed, verifiable sources. Google's
Knowledge Graph trusts IEEE Xplore, DBLP, and Google Scholar heavily. A person
with 5+ IEEE-indexed papers and a published PhD thesis has a stronger notability
signal than someone with 2-3 crypto blog posts. See
`references/academic-publications.md` for the full academic publication strategy.

## Workflow

### Phase 0: Digital Footprint Audit
Before building, audit what exists. See `references/digital-footprint-audit.md`
for the full checklist. Key checks:
- Wikidata search for the person's name (CRITICAL: verify any existing Q-item
  is actually the right person — same names are common)
- Domain availability (prefer firstname-lastname.com)
- Existing profiles: LinkedIn, GitHub, X, Crunchbase, Google Scholar
- Independent press coverage count and quality

### Phase 1: Personal Website + Schema
- Deploy a minimal site with JSON-LD `Person` schema using `@graph` with `@id`
- Site title and og:site_name must be the person's name
- Create /about page (primary reference URL for Wikidata)
- Deploy /llms.txt and robots.txt with sitemap
- Set up Google Search Console, submit sitemap, request indexing
- See `templates/person-schema.json` for ready-to-adapt JSON-LD template
- Validate at https://validator.schema.org/ — 0 errors, 0 warnings

### Phase 2: Wikidata Entry
- Warm up account: 5-10 small edits to existing items before creating own
- Create item with proper label, description (for disambiguation), aliases
- Add core statements: P31, P21, P106, P27, P735, P734, P551, P69, P856, P512
- Add identifiers: P2002 (X), P2037 (GitHub), P6634 (LinkedIn)
- If academic: add P8034 (DBLP), P1960 (Google Scholar), P8035 (ORCID)
- Add notable work (P800) as Q-items for prominent projects OR academic papers
  independent references — otherwise deletion bait)
- For academic publications: create Q-items for thesis (with ISBN) and key
  papers (with DOIs). These are the strongest possible P800 notable work items
  because they carry verifiable identifiers. See
  `references/academic-publications.md`.
- Add P854 reference URL to EVERY statement + P813 retrieved date
- Run `scripts/wikidata-ref-audit.sh` to verify all statements are referenced

### Phase 3: Wikimedia Commons Image (THE UNLOCK)
- Upload professional headshot to Wikimedia Commons
- License: CC-BY-SA 4.0
- Descriptive filename: `Firstname Lastname headshot YYYY.jpg`
- Add P18 to Wikidata item pointing to the Commons filename
- Use the same photo across website, LinkedIn, X, GitHub

### Phase 4: Cross-Platform Consistency
Pick canonical values and use them EVERYWHERE:
- Name (full name, not handle)
- Title (e.g., "Blockchain Engineer & Entrepreneur")
- City (pick ONE — do not mix nearby cities)
- Bio (one canonical short version)

Update: LinkedIn, X/Twitter, GitHub, Crunchbase, Amazon Author (if applicable).
Then update schema sameAs to include all profile URLs + Wikidata Q-URL.

### Phase 5: Notability Signals (Press + Academic)
Two paths to notability — press OR academic. Both work. Academic is faster if
the person already has publications.

**Press path**: Target outlets by industry. Pitch specific angles tied to
current projects. See `references/benobi-method.md` for validated pitch angles
and timing.

**Academic path**: If the person has publications, create a Google Scholar
profile (P1960), register an ORCID iD (P8035), add DBLP author ID (P8034),
and create Wikidata Q-items for key papers/thesis with DOIs as references.
See `references/academic-publications.md` for the full workflow.

### Phase 6: Wait and Monitor
- Search the person's name on Google (incognito) weekly
- Expected: 5-10 weeks from all-signals-complete
- If no panel after 12 weeks: check Wikidata item is alive, schema validates,
  press coverage exists, cross-platform data is consistent
- When panel appears: claim it, screenshot immediately

## CDN Gotcha
After deploying schema changes, purge all CDN caches (Cloudflare, Fastly, etc.).
Googlebot may hit a stale edge and index old schema. This silently kills
Knowledge Graph signal propagation. Always:
1. Deploy schema
2. Purge CDN (Cloudflare → Caching → Purge Everything)
3. Verify with `curl -sI -A "Googlebot" https://site.com/` — check Age header
4. Then request indexing in Search Console

## Timing Benchmarks
- From zero (no schema): ~10 weeks
- From all-signals-complete (schema + Wikidata + Commons + consistency): ~5 weeks
- Faster with: Wikipedia article, tier-1 press, existing Knowledge Graph entity
- Slower with: below-tier-3 press, cross-platform gaps, Wikidata deletion flag

## Pitfalls
- **Wrong Wikidata item**: Always verify an existing Q-item is the right person.
  Search by name, then check occupation, birth date, and description. Common
  names have multiple Wikidata entries — using the wrong one merges identities.
- **Unreferenced Wikidata statements**: Deletion within days. Every statement
  needs P854 + P813.
- **Org Q-items without press**: Creating Wikidata items for companies/projects
  without independent press coverage is deletion bait. Wait until each org has
  at least one independent article.
- **LLM-drafted Wikipedia articles**: AfC reviewers are trained to spot LLM
  tells (citation-dense compound sentences, stilted tone). Draft in your own
  voice. Use LLM only to review for policy violations.
- **Inconsistent city**: Schema says "Erlangen", Wikidata says "Buckenhof",
  LinkedIn says "Bavaria". Pick ONE canonical city. Google reads all of them.
- **CDN stale edge**: Googlebot indexes stale schema. Purge after every deploy.
- **Schema sameAs missing Wikidata Q-URL**: The bidirectional bridge (Wikidata
  Q-URL in JSON-LD sameAs AND site URL in Wikidata P856) is essential.

## Reference Files
- `references/benobi-method.md` — Validated execution log, timeline, JSON-LD
  extras, additional Wikidata properties, and pitfalls from benobi.one (2026)
- `references/digital-footprint-audit.md` — Step-by-step audit checklist for
  researching a person's existing digital footprint before building signals
- `references/academic-publications.md` — How to leverage academic papers,
  PhD theses, DBLP, Google Scholar, and ORCID as Knowledge Panel signals
- `templates/person-schema.json` — Ready-to-adapt JSON-LD Person @graph template
- `scripts/wikidata-ref-audit.sh` — Verify every Wikidata statement has a reference
