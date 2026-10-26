#!/usr/bin/env python3
"""Render x2llm search JSON as compact rows: id | @author | ts | f=likes | text.

Usage: python3 render_search.py FILE [FILE ...]

Every tweet-pipeline run needs one of these; writing it ad hoc in /tmp each
time wastes a call and invites the quoting/authorshape bugs (a naive
`author.get("screen_name")` crashes — x2llm search returns `author` as a
STRING, verified 2026-10-24T13:10). Handles: error documents ({"error": ...}
printed as ERROR), tweets-as-list or {"tweets": [...]}, string or dict
author, likes under `likes`/`favorite_count`, text under
`text`/`full_text`. Rows truncate at 190 chars; newlines flatten to " / ".
A parse failure in one file does not kill the batch.
"""
import json
import sys


def get(d, *keys, default=None):
    cur = d
    for k in keys:
        if not isinstance(cur, dict):
            return default
        cur = cur.get(k)
    return cur if cur is not None else default


def render(path):
    print("=" * 12, path)
    try:
        doc = json.load(open(path))
    except Exception as e:
        print("PARSE FAIL:", e)
        return
    if isinstance(doc, dict) and "error" in doc:
        print("ERROR:", doc["error"])
        return
    tweets = doc.get("tweets") if isinstance(doc, dict) else doc
    if not isinstance(tweets, list):
        print("unexpected shape:", type(doc).__name__,
              list(doc.keys()) if isinstance(doc, dict) else "")
        return
    for t in tweets:
        a = t.get("author") or t.get("user") or {}
        if isinstance(a, str):
            u = a
        else:
            u = (a.get("screen_name") or a.get("screenName")
                 or get(a, "core", "user_results", "result", "legacy",
                        "screen_name") or "?")
        ts = str(t.get("created_at") or t.get("createdAt") or "")[:16]
        fav = t.get("likes", t.get("favorite_count", "?"))
        txt = str(t.get("text") or t.get("full_text") or "")
        txt = txt.replace("\n", " / ")
        if len(txt) > 190:
            txt = txt[:190] + "..."
        print(f"{t.get('id', '?')} | @{u} | {ts} | f={fav} | {txt}")
    print(f"-- {len(tweets)} rows")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        render(p)
