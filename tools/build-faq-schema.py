#!/usr/bin/env python3
"""Rebuild the FAQPage JSON-LD from what the page actually says.

Google requires FAQPage structured data to match visible content. Hand-written
schema drifts the moment someone edits the copy, so this derives it instead.

Sources, both in index.html:
  1. <dl class="short">  -> <dt>question</dt><dd>answer</dd>
  2. <div class="q">     -> <b>question</b><p>answer</p>

Run after editing either block:  python3 tools/build-faq-schema.py
Verifies by default; pass --write to apply.
"""
import json, re, sys, html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE = ROOT / "index.html"
BASE = "https://palworks.github.io/openfullpage-site/"

def text(fragment: str) -> str:
    """Strip tags, unescape entities, collapse whitespace."""
    t = re.sub(r"<[^>]+>", "", fragment)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()

def extract(src: str):
    pairs = []
    short = re.search(r'<dl class="short">(.*?)</dl>', src, re.S)
    if short:
        for dt, dd in re.findall(r"<dt>(.*?)</dt>\s*<dd>(.*?)</dd>", short.group(1), re.S):
            pairs.append((text(dt), text(dd)))
    for q, a in re.findall(r'<div class="q"><b>(.*?)</b><p>(.*?)</p></div>', src, re.S):
        pairs.append((text(q), text(a)))
    seen, out = set(), []
    for q, a in pairs:
        if q.lower() in seen:
            continue
        seen.add(q.lower())
        out.append((q, a))
    return out

def main() -> int:
    src = PAGE.read_text(encoding="utf-8")
    pairs = extract(src)
    if not pairs:
        print("ERROR: found no question and answer pairs", file=sys.stderr)
        return 2

    node = {
        "@type": "FAQPage",
        "@id": BASE + "#faq",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in pairs
        ],
    }

    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', src, re.S)
    graph = json.loads(m.group(1))
    current = [n for n in graph["@graph"] if n.get("@type") == "FAQPage"]

    if current and current[0] == node:
        print(f"FAQ schema is in sync ({len(pairs)} questions)")
        return 0

    if "--write" not in sys.argv:
        print(f"FAQ schema is STALE. Page has {len(pairs)} questions, "
              f"schema has {len(current[0]['mainEntity']) if current else 0}.")
        print("Re-run with --write to update.")
        return 1

    graph["@graph"] = [n for n in graph["@graph"] if n.get("@type") != "FAQPage"] + [node]
    block = ('<script type="application/ld+json">\n'
             + json.dumps(graph, indent=2) + "\n</script>\n")
    PAGE.write_text(
        re.sub(r'<script type="application/ld\+json">.*?</script>\n', block, src, flags=re.S),
        encoding="utf-8")
    print(f"FAQ schema rewritten from the page: {len(pairs)} questions")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
