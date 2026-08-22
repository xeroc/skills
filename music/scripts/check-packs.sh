#!/usr/bin/env bash
# Health check for T2 packs referenced by SAMPLE-CATALOG.md.
# Usage: scripts/check-packs.sh — prints PASS/FAIL per pack; nonzero exit if any FAIL.
set -u
PACKS=(
  "tidalcycles/Dirt-Samples main"
  "Bubobubobubobubo/Dough-Amen main"
  "yaxu/clean-breaks main"
  "eddyflux/crate main"
  "salsicha/capoeira_strudel main"
  "sonidosingapura/rochormatic main"
  "terrorhank/samples main"
  "RikyBac15/samples main"
  "kaiye10/strudelSamples main"
)
fail=0
for entry in "${PACKS[@]}"; do
  repo=${entry% *}; branch=${entry#* }
  url="https://raw.githubusercontent.com/$repo/$branch/strudel.json"
  keys=$(curl -sL --max-time 15 "$url" | jq -r 'del(._base) | keys | length' 2>/dev/null)
  if [ "${keys:-0}" -gt 0 ] 2>/dev/null; then
    echo "PASS $repo ($keys sounds)"
  else
    echo "FAIL $repo — strudel.json unreachable or empty ($url)"
    fail=1
  fi
done
exit $fail
