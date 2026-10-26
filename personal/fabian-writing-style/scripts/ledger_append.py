#!/usr/bin/env python3
"""Append an entry at the TOP of the cron-tweet-pipeline ledger.

Usage: python3 ledger_append.py ENTRY_FILE [LEDGER_PATH]

Inserts ENTRY_FILE's content (plus a blank line) before the ledger's first
`^## ` header, leaving the intro paragraph untouched, then prints the seam
for verification. Deterministic string insertion — no fuzzy patch anchors,
so none of the failure modes the ledger's own intro catalogues (header-
anchored inserts landing mid-bullet, "Found N matches" rejects on loosened
anchors, duplicated seam words). First try, clean seam (observed
2026-10-24T13:10).

Default LEDGER_PATH points at the fabian-writing-style skill's copy;
pass an explicit path if the skill moves or a sibling pipeline keeps its
ledger elsewhere. ENTRY_FILE should be a timestamped /tmp artifact —
sibling cron runs share /tmp.
"""
import os
import re
import sys

entry_path = sys.argv[1]
ledger = (sys.argv[2] if len(sys.argv) > 2 else os.path.expanduser(
    "~/.hermes/skills/personal/fabian-writing-style/references/cron-tweet-pipeline.md"))

entry = open(entry_path).read()
if not entry.endswith("\n\n"):
    entry = entry.rstrip("\n") + "\n\n"

text = open(ledger).read()
m = re.search(r"^## ", text, re.M)
if not m:
    sys.exit("no ## header found in ledger; aborting")

pos = m.start()
new = text[:pos] + entry + text[pos:]
open(ledger, "w").write(new)
print("inserted at char", pos)
seam = max(0, pos - 80)
print("--- seam (tail of new entry + next header) ---")
print(new[seam:seam + 400])
