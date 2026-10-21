#!/usr/bin/env python3
"""Refresh live GitHub stats and regenerate README sections and NEW.md.

Standard library only (Python 3.8+). Free: uses the public GitHub REST API.
  python3 scripts/update.py            # fetch stats, rewrite README + NEW.md
  python3 scripts/update.py --offline  # rebuild from data/stats.json, no network

Auth (optional, raises the rate limit): GITHUB_TOKEN env var, else `gh auth token`.
Rules enforced automatically (see RULES.md): repos with no OSI-style licence,
archived or missing repos go to the "Excluded" table, never the main lists.
"""
import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
REPOS = DATA / "repos.json"
STATS = DATA / "stats.json"
ADDED = DATA / "added.json"
README = ROOT / "README.md"
NEW_MD = ROOT / "NEW.md"

OSS_LICENSES = {
    "MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "MPL-2.0",
    "GPL-2.0", "GPL-3.0", "AGPL-3.0", "LGPL-2.1", "LGPL-3.0", "Unlicense", "CC0-1.0", "0BSD",
    "GPL-2.0-only", "GPL-3.0-only", "AGPL-3.0-only", "GPL-3.0-or-later", "AGPL-3.0-or-later",
}
STALE_DAYS = 270
NEW_DAYS = 14
TODAY = dt.datetime.utcnow().date()


def token():
    t = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if t:
        return t
    try:
        out = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10)
        return out.stdout.strip() or None
    except Exception:
        return None


def fetch(repo, tok):
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "useful-repo-by-anktechsol")
    if tok:
        req.add_header("Authorization", f"Bearer {tok}")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        return {"status": "not-found" if e.code == 404 else f"http-{e.code}"}
    except Exception as e:  # network problems
        return {"status": "error", "error": str(e)[:80]}
    lic = (d.get("license") or {}).get("spdx_id") or "NONE"
    return {
        "status": "ok",
        "full_name": d.get("full_name"),
        "stars": d.get("stargazers_count", 0),
        "license": lic,
        "pushed_at": d.get("pushed_at"),
        "archived": bool(d.get("archived")),
        "language": d.get("language"),
        "description": d.get("description") or "",
    }


def load(path, default):
    return json.loads(path.read_text()) if path.exists() else default


def refresh(repos, old, tok):
    stats = {}
    for item in repos:
        r = item["repo"]
        new = fetch(r, tok)
        prev = old.get(r, {})
        if new.get("status") != "ok":
            # keep last good data if the network hiccuped
            stats[r] = prev if prev.get("status") == "ok" else new
            continue
        new["stars_prev"] = prev.get("stars", new["stars"])
        new["prev_fetched"] = prev.get("fetched")
        new["fetched"] = TODAY.isoformat()
        stats[r] = new
        print(f"ok  {r}  {new['stars']}  {new['license']}")
    return stats


def classify(s):
    """Return (listed, reason)."""
    if s.get("status") != "ok":
        return False, f"unavailable ({s.get('status', 'no data')})"
    if s.get("archived"):
        return False, "archived"
    if s.get("license") not in OSS_LICENSES:
        return False, f"licence not OSI-style ({s.get('license')})"
    return True, ""


def days_since(iso):
    if not iso:
        return None
    return (TODAY - dt.datetime.strptime(iso[:10], "%Y-%m-%d").date()).days


def k(n):
    return f"{n/1000:.1f}k" if n >= 1000 else str(n)


def esc(t):
    return (t or "").replace("|", "\\|").replace("\n", " ")


def slug(title):
    return re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")


def row(item, s):
    d = s["stars"] - s.get("stars_prev", s["stars"])
    delta = f" (+{d})" if d > 0 else ""
    age = days_since(s.get("pushed_at"))
    pushed = s["pushed_at"][:10] if s.get("pushed_at") else "?"
    flag = " ⚠️ stale" if age is not None and age > STALE_DAYS else ""
    note = esc(item.get("note", ""))
    install = f"`{esc(item['install'])}`" if item.get("install") else ""
    extra = "; ".join(x for x in (install, note) if x)
    name = item["repo"]
    return (f"| [{name}](https://github.com/{name}) | {esc(item['why'])} | {item.get('type','')} "
            f"| {k(s['stars'])}{delta} | {s['license']} | {pushed}{flag} | {extra} |")


def build_lists(data, stats):
    cats = data["categories"]
    by_cat = {c["id"]: [] for c in cats}
    excluded = []
    for item in data["repos"]:
        s = stats.get(item["repo"], {"status": "no-data"})
        ok, why = classify(s)
        if ok:
            by_cat[item["category"]].append((item, s))
        else:
            excluded.append((item, why))
    out = []
    for c in cats:
        entries = sorted(by_cat[c["id"]], key=lambda x: -x[1]["stars"])
        if not entries:
            continue
        out.append(f"### {c['title']}\n\nDM keyword: `{c['keyword']}`\n")
        out.append("| Repo | What it does | Type | Stars | Licence | Last push | Notes |")
        out.append("|---|---|---|---|---|---|---|")
        out += [row(i, s) for i, s in entries]
        out.append("")
    if excluded:
        out.append("### Excluded automatically (does not meet the free and open-source rule)\n")
        out.append("| Repo | Reason |")
        out.append("|---|---|")
        out += [f"| [{i['repo']}](https://github.com/{i['repo']}) | {why} |" for i, why in excluded]
        out.append("")
    return "\n".join(out)


def build_index(data, stats):
    lines = ["| Comment this | Go to |", "|---|---|"]
    seen = {}
    for c in data["categories"]:
        seen.setdefault(c["keyword"], []).append(c["title"])
    for kw, titles in seen.items():
        links = ", ".join(f"[{t}](#{slug(t)})" for t in titles)
        lines.append(f"| `{kw}` | {links} |")
    return "\n".join(lines)


def build_trending(data, stats):
    items = []
    for item in data["repos"]:
        s = stats.get(item["repo"])
        if s and classify(s)[0]:
            items.append((s["stars"] - s.get("stars_prev", s["stars"]), item, s))
    items.sort(key=lambda x: -x[0])
    top = [x for x in items if x[0] > 0][:10]
    if not top:
        return "_Growth appears after the second weekly update._"
    lines = ["| Repo | New stars since last update | Total stars |", "|---|---|---|"]
    for d, item, s in top:
        lines.append(f"| [{item['repo']}](https://github.com/{item['repo']}) | +{d} | {k(s['stars'])} |")
    return "\n".join(lines)


def update_added(data):
    first_run = not ADDED.exists()
    added = load(ADDED, {})
    changed = False
    for item in data["repos"]:
        if item["repo"] not in added:
            # first import is marked "seed" so only later additions show up as NEW
            added[item["repo"]] = "seed" if first_run else TODAY.isoformat()
            changed = True
    if changed:
        ADDED.write_text(json.dumps(dict(sorted(added.items())), indent=2) + "\n")
    return added


def build_new(data, stats, added):
    cutoff = TODAY - dt.timedelta(days=NEW_DAYS)
    recent = []
    for item in data["repos"]:
        if added[item["repo"]] == "seed":
            continue
        d = dt.datetime.strptime(added[item["repo"]], "%Y-%m-%d").date()
        s = stats.get(item["repo"])
        if d >= cutoff and s and classify(s)[0]:
            recent.append((d, item, s))
    recent.sort(key=lambda x: (x[0], x[2]["stars"]), reverse=True)
    cats = {c["id"]: c for c in data["categories"]}
    card = ["# New additions (video cards)\n",
            f"Repos added in the last {NEW_DAYS} days. Each card has the facts for a motion-graphics video. "
            "Auto-generated by `scripts/update.py`.\n"]
    short = []
    if not recent:
        card.append("_Nothing new in this window._\n")
    for d, item, s in recent:
        c = cats[item["category"]]
        card += [
            f"## {item['repo']}",
            f"- **Added:** {d}",
            f"- **One line:** {item['why']}",
            f"- **Category / DM keyword:** {c['title']} / `{c['keyword']}`",
            f"- **Stars:** {k(s['stars'])}  |  **Licence:** {s['license']}  |  **Last push:** {(s.get('pushed_at') or '?')[:10]}",
            f"- **Type:** {item.get('type','')}",
            f"- **Install:** {item.get('install') or 'see the repo README'}",
            f"- **Caution:** {item.get('note') or 'read the SKILL.md or code before installing'}",
            "- **Video beats:** hook (the pain) / what it does / 10-second demo / how to get it (comment the keyword)",
            "",
        ]
        short.append(f"- **{item['repo']}**: {item['why']} ({d})")
    NEW_MD.write_text("\n".join(card))
    return "\n".join(short) if short else "_Nothing new this fortnight._"


def splice(text, name, body):
    pat = re.compile(rf"(<!-- BEGIN:{name} -->)(.*?)(<!-- END:{name} -->)", re.S)
    if not pat.search(text):
        raise SystemExit(f"README.md is missing markers for {name}")
    return pat.sub(lambda m: f"{m.group(1)}\n{body}\n{m.group(3)}", text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    data = json.loads(REPOS.read_text())
    old = load(STATS, {})
    if args.offline:
        stats = old
    else:
        stats = refresh(data["repos"], old, token())
        STATS.write_text(json.dumps(stats, indent=1, sort_keys=True) + "\n")
    added = update_added(data)
    text = README.read_text()
    text = splice(text, "INDEX", build_index(data, stats))
    text = splice(text, "NEW", build_new(data, stats, added))
    text = splice(text, "TRENDING", build_trending(data, stats))
    text = splice(text, "LIST", build_lists(data, stats))
    text = splice(text, "UPDATED", f"Last updated: {TODAY.isoformat()} (UTC). Star counts are live from the GitHub API.")
    README.write_text(text)
    listed = sum(1 for i in data["repos"] if classify(stats.get(i["repo"], {}))[0])
    print(f"done: {listed}/{len(data['repos'])} listed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
