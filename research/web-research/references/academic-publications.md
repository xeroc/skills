# Academic Publications as Knowledge Panel Signals

Academic publications are equivalent or stronger than press coverage for
Google's Knowledge Graph. They carry DOIs, are indexed by IEEE Xplore / ACM /
DBLP / Google Scholar, and are independently verifiable. A person with 5+
indexed papers and a published PhD thesis has a stronger notability signal
than someone with 2-3 industry blog posts.

## Why Academic Publications Are Strong Signals

- Google indexes IEEE Xplore, DBLP, Semantic Scholar, and Google Scholar heavily
- DOIs are persistent, verifiable identifiers (unlike URLs that rot)
- ISBNs for theses/books are catalogued in national libraries (DNB, LoC)
- Citation networks create a web of independent references to the person
- Academic databases have high domain authority — Google trusts them

## Audit: Finding Existing Academic Footprint

### DBLP (computer science / IT)
```bash
# Search for author
curl -s "https://dblp.org/search/author/api?q=FIRSTNAME+LASTNAME&format=json" | python3 -c "
import json, sys
d = json.load(sys.stdin)
for h in d.get('result',{}).get('hits',{}).get('hit',[]):
    info = h.get('info',{})
    print(f'  pid={info.get(\"url\",\"\").split(\"/\")[-1] if \"/pid/\" in info.get(\"url\",\"\") else \"\"}')
    print(f'  name={info.get(\"author\",{}).get(\"text\",\"\") if isinstance(info.get(\"author\"),dict) else info.get(\"author\",\"\")}')
"

# Search for publications
curl -s "https://dblp.org/search/publ/api?q=FIRSTNAME+LASTNAME&format=json&h=20" | python3 -c "
import json, sys
d = json.load(sys.stdin)
for h in d.get('result',{}).get('hits',{}).get('hit',[]):
    info = h.get('info',{})
    print(f'  [{info.get(\"year\",\"?\")}] {info.get(\"title\",\"?\")} ({info.get(\"venue\",\"?\")})')
"
```

If a DBLP pid exists, add it to JSON-LD sameAs as `https://dblp.org/pid/XX/XXXXX`
and to Wikidata as P8034.

### GND / lobid.org (German National Library authority file)
For German persons, the GND (Gemeinsame Normdatei) is the authority file.
CRITICAL: use lobid.org API, NOT the direct DNB portal API (which returns 404
for some endpoints).

```bash
# Search GND for a person by name
curl -s 'https://lobid.org/gnd/search?q=preferredName%3A%22LASTNAME%2C+FIRSTNAME%22&format=json&size=10'

# Check a specific GND ID
curl -s "https://lobid.org/gnd/ID/about" | python3 -c "
import json, sys
d = json.load(sys.stdin)
# Look for: professionOrOccupation, biographicalOrHistoricalInformation,
# dateOfBirth, academicDegree, affiliation
"
```

IMPORTANT: Verify the GND entry matches the right person. Common names have
multiple GND entries. Check: profession, date of birth, biographical info,
academic degree, and affiliation. Example: "Schuh, Fabian" GND 1232022373 is
a physician from Heidelberg (Dr. med., diss. 2024), NOT the blockchain engineer.

### Google Books / ISBN lookup
```bash
curl -s "https://www.googleapis.com/books/v1/volumes?q=isbn:ISBN_NUMBER" | python3 -c "
import json, sys
d = json.load(sys.stdin)
items = d.get('items', [])
if items:
    info = items[0].get('volumeInfo', {})
    print(f'Title: {info.get(\"title\")}')
    print(f'Authors: {info.get(\"authors\",[])}')
"
```

Note: Not all ISBNs are in Google Books. German theses from Shaker Verlag
may not appear. The ISBN is still valid for Wikidata/schema regardless.

## Creating Wikidata Q-Items for Publications

### For a PhD thesis / book (has ISBN)
Create a Q-item:
- Label: full thesis title
- Description: "YEAR doctoral thesis, UNIVERSITY"
- P31 instance of -> doctoral thesis (Q187685)
- P50 author -> person Q-item
- P123 publisher -> publisher Q-item (or string)
- P957 ISBN-13 -> the ISBN
- P407 language of work -> English (Q1860) or German (Q188)
- P577 publication date -> YYYY-MM
- P854 reference URL -> university library catalogue or Google Books

### For a conference/journal paper (has DOI)
Create a Q-item:
- Label: paper title
- Description: "YEAR scientific paper, VENUE"
- P31 instance of -> scientific article (Q13442814)
- P50 author -> person Q-item (add all co-authors as separate Q-items or strings)
- P356 DOI -> the DOI string (e.g., "10.1109/ISCCSP.2014.6877916")
- P1433 published in -> conference/journal Q-item (search Wikidata for the venue)
- P577 publication date -> YYYY-MM
- P854 reference URL -> IEEE Xplore / ACM / publisher page

### For a best paper award
Add to the paper's Q-item:
- P166 award received -> best paper award (or specific award Q-item)
This is a strong notability signal.

### Linking back to the person item
On the person's Wikidata Q-item, add:
- P800 notable work -> paper/thesis Q-item (as a Q-item reference, NOT a string)

Priority order for Q-item creation (if many publications exist):
1. PhD thesis (strongest -- published book with ISBN)
2. Papers with explicit DOIs
3. Best paper award winners
4. Papers at prestigious venues (GLOBECOM, ICNC, etc.)
5. Remaining papers

## Google Scholar Profile

1. Go to https://scholar.google.com -> sign in
2. "My Profile" -> search for papers by title
3. Add all publications -- verify correct author match (common names = multiple
   profiles in the database)
4. Set affiliation, research interests
5. Make profile PUBLIC
6. Copy the profile URL -- it goes into:
   - JSON-LD sameAs array
   - Wikidata P1960 (Google Scholar ID)

## ORCID Registration

1. Go to https://orcid.org/register (free)
2. Add education (university, degree, year)
3. Add employment
4. Import publications by DOI (Crossref integration)
5. Copy the ORCID iD (format: 0000-0000-0000-0000) -- it goes into:
   - JSON-LD sameAs array
   - Wikidata P8035 (ORCID iD)

## Academic Wikidata Identifiers (add to person item)

| Property | Value | Reference |
|----------|-------|-----------|
| P8034 DBLP author ID | pid path (e.g., 87/11471) | https://dblp.org/pid/XX/XXXXX |
| P1960 Google Scholar ID | user ID from profile URL | Scholar profile URL |
| P8035 ORCID iD | 0000-0000-0000-0000 | ORCID profile URL |
| P512 academic degree | Doctor of Engineering Q-item | Thesis ISBN or university record |

## Schema.org: Thesis as Book Entity

Add a Book entity to the JSON-LD @graph for the PhD thesis:

```json
{
  "@type": "Book",
  "@id": "https://SITE.com/#thesis",
  "name": "THESIS TITLE",
  "isbn": "ISBN_NUMBER",
  "description": "PhD thesis. SERIES NAME, Volume N.",
  "datePublished": "YEAR",
  "inLanguage": "en",
  "publisher": {"@type": "Organization", "name": "PUBLISHER"},
  "author": [{"@type": "Person", "@id": "https://SITE.com/#you"}]
}
```

## Impact on Timeline

Academic publications remove the "need press first" bottleneck:
- Without publications: 8-12 weeks, may fail on notability
- With 5+ publications: 6-10 weeks, notability gap is closed
- Publications + press: fastest path (4-8 weeks)

The academic track record is verifiable NOW -- no waiting for press pitches,
no dependency on journalist response times.
