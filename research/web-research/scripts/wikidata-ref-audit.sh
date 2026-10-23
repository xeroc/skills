#!/usr/bin/env bash
# Wikidata Reference Audit
# Verifies that every statement on a Wikidata item has at least one reference.
# Usage: ./wikidata-ref-audit.sh Q123456789
# Any line showing "MISSING REF" needs a P854 reference URL added.

set -euo pipefail

Q_ID="${1:?Usage: $0 Q123456789}"

echo "Auditing Wikidata item: $Q_ID"
echo "================================"

curl -s "https://www.wikidata.org/wiki/Special:EntityData/${Q_ID}.json" | \
python3 -c "
import json, sys

data = json.load(sys.stdin)
entities = data.get('entities', {})
entity = entities.get('${Q_ID}', list(entities.values())[0]) if '${Q_ID}' in entities else list(entities.values())[0]

claims = entity.get('claims', {})
total = 0
unreferenced = 0

for prop, vals in sorted(claims.items()):
    for v in vals:
        total += 1
        refs = len(v.get('references', []))
        if refs == 0:
            unreferenced += 1
            status = '*** MISSING REF ***'
        else:
            status = 'ok'
        print(f'  {prop}: refs={refs}  {status}')

print()
print(f'Total statements: {total}')
print(f'Referenced: {total - unreferenced}')
print(f'Unreferenced: {unreferenced}')
if unreferenced > 0:
    print()
    print('WARNING: Unreferenced statements are deletion bait.')
    print('Add P854 (reference URL) + P813 (retrieved date) to each.')
    sys.exit(1)
else:
    print('All statements referenced.')
"
