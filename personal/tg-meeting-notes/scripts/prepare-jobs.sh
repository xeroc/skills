#!/usr/bin/env bash
# prepare-jobs.sh <watermark-date YYYY-MM-DD> [job-count]
# Filters non-archived tg chats with activity AFTER the watermark, splits them into
# job files for extraction subagents, and writes the username lookup table.
# Requires: tg chats output cached at /tmp/tg_chats.json (run `tg chats > /tmp/tg_chats.json` first).
set -euo pipefail

WATERMARK="${1:?usage: prepare-jobs.sh <YYYY-MM-DD> [job-count]}"
JOBS="${2:-10}"
OUT=/tmp/tg_jobs
CHATS=/tmp/tg_chats.json

jq -r --arg wm "$WATERMARK" '
  [.[] | select(.archived == false and .last_message.date > $wm)]
  | sort_by(.last_message.date) | reverse
  | .[] | "\(.id)\t\(.type)\t\(.title | gsub("\t";" "))\t\(.last_message.date[0:10])\t\(.unread)"
' "$CHATS" > "$OUT/all.tsv"

total=$(wc -l < "$OUT/all.tsv")
[ "$total" -eq 0 ] && { echo "no chats active after $WATERMARK"; exit 0; }
rm -f "$OUT"/job_* "$OUT/usernames.tsv"
split -n "l/$JOBS" -d "$OUT/all.tsv" "$OUT/job_"

tg contacts | jq -r '.[] | select(.username != null) | "\(.id)\t@\(.username)"' > "$OUT/usernames.tsv"

echo "watermark=$WATERMARK chats=$total jobs=$JOBS"
wc -l "$OUT"/job_* | sed 's/^/  /'
