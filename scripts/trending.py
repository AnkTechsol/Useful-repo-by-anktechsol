#!/usr/bin/env python3
"""Pull github.com/trending (daily + weekly), keep AI/agent/automation repos,
and write a digest with licence check, plain description and a quick start.

Standard library only (Python 3.8+). Free: reads the public trending page and
the public GitHub REST API. No LLM is called; "how to" text is extracted from
each repo's own README. Hand-written guides in guides/ are linked when present.

  python3 scripts/trending.py
Outputs: data/trending.json, trending/latest.md, trending/archive/<date>.md
"""
import datetime as dt
import html
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_JSON = ROOT / "data" / "trending.json"
OUT_MD = ROOT / "trending" / "latest.md"
ARCHIVE = ROOT / "trending" / "archive"
GUIDES = ROOT / "guides"
TODAY = dt.datetime.utcnow().date()

PAGES = [("daily", "https://github.com/trending?since=daily"),
         ("weekly", "https://github.com/trending?since=weekly")]
KEYWORDS = re.compile(
    r"\b(agent|agents|agentic|claude|codex|mcp|skill|skills|llm|llms|ai|gpt|openai|anthropic|"
    r"gemini|cursor|copilot|prompt|automation|rag|assistant|chatbot|workflow|copilot|plugin)\b", re.I)
OSS = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "MPL-2.0", "GPL-2.0", "GPL-3.0",
       "AGPL-3.0", "LGPL-2.1", "LGPL-3.0", "Unlicense", "CC0-1.0", "0BSD"}
HEAD_RE = re.compile(r"^#{1,4}\s*(.*(install|quick\s*start|getting started|usage|setup).*)$", re.I | re.M)


def token():
    t = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if t:
        return t
    try:
        return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10).stdout.strip() or None
    except Exception:
        return None


def get(url, accept=None, tok=None):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 useful-repo-by-anktechsol")
    if accept:
        req.add_header("Accept", accept)
    if tok and "api.github.com" in url:
        req.add_header("Authorization", f"Bearer {tok}")
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read().decode("utf-8", "replace")


def clean(t):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", t or ""))).strip()


def parse_trending(page):
    items = []
    for a in re.findall(r'<article class="Box-row">(.*?)</article>', page, re.S):
        m = re.search(r'<h2[^>]*>.*?href="/([^"/]+/[^"/]+)"', a, re.S)
        if not m:
            continue
        desc = re.search(r'<p class="[^"]*color-fg-muted[^"]*">(.*?)</p>', a, re.S)
        lang = re.search(r'itemprop="programmingLanguage">(.*?)<', a, re.S)
        gain = re.search(r"([\d,]+)\s+stars?\s+(today|this week|this month)", a)
        items.append({
            "repo": m.group(1),
            "description": clean(desc.group(1)) if desc else "",
            "language": clean(lang.group(1)) if lang else "",
            "gained": int(gain.group(1).replace(",", "")) if gain else 0,
            "period": gain.group(2) if gain else "",
        })
    return items


def api(repo, tok):
    try:
        d = json.loads(get(f"https://api.github.com/repos/{repo}", "application/vnd.github+json", tok))
    except Exception:
        return None
    return {"stars": d.get("stargazers_count", 0), "license": (d.get("license") or {}).get("spdx_id") or "NONE",
            "pushed_at": d.get("pushed_at"), "archived": bool(d.get("archived")),
            "topics": d.get("topics", []), "homepage": d.get("homepage") or ""}


def readme(repo, tok):
    try:
        return get(f"https://api.github.com/repos/{repo}/readme", "application/vnd.github.raw", tok)
    except Exception:
        return ""


def summary(md):
    """First readable paragraph of a README."""
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    md = re.sub(r"<[^>]+>", "", md)
    for para in re.split(r"\n\s*\n", md):
        p = para.strip()
        if not p or p.startswith(("#", "!", "[!", "|", "```", "- ", "* ", ">", "[![")):
            continue
        p = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", p)
        p = re.sub(r"[*_`]", "", p)
        p = re.sub(r"\s+", " ", p)
        if len(p) > 60:
            return p[:300].rstrip() + ("..." if len(p) > 300 else "")
    return ""


def quickstart(md):
    """First code block under an install / quick start / usage heading (max 10 lines)."""
    for m in HEAD_RE.finditer(md):
        chunk = md[m.end(): m.end() + 3000]
        nxt = re.search(r"^#{1,4}\s", chunk, re.M)
        if nxt:
            chunk = chunk[: nxt.start()]
        code = re.search(r"```[\w-]*\n(.*?)```", chunk, re.S)
        if code:
            lines = [l.rstrip() for l in code.group(1).strip().splitlines()][:10]
            if lines:
                return "\n".join(lines)
    return ""


def relevant(item, meta):
    text = " ".join([item["repo"], item["description"], " ".join((meta or {}).get("topics", []))])
    return bool(KEYWORDS.search(text))


def guide_link(repo):
    f = GUIDES / (repo.replace("/", "--") + ".md")
    return f"guides/{f.name}" if f.exists() else ""


def main():
    tok = token()
    seen, rows = {}, []
    for period, url in PAGES:
        try:
            items = parse_trending(get(url))
        except Exception as e:
            print("could not read", url, e)
            continue
        print(f"{period}: {len(items)} repos on the page")
        for it in items:
            if it["repo"] in seen:
                seen[it["repo"]]["also"].append(f"+{it['gained']} {it['period']}")
                continue
            it["also"] = []
            seen[it["repo"]] = it
            rows.append(it)
    kept = []
    for it in rows:
        meta = api(it["repo"], tok)
        if not meta or meta["archived"] or not relevant(it, meta):
            continue
        md = readme(it["repo"], tok)
        it.update(meta)
        it["summary"] = it["description"] if len(it["description"]) >= 40 else (summary(md) or it["description"])
        it["spike"] = it["stars"] > 1000 and it["gained"] / max(it["stars"], 1) > 0.4
        it["quickstart"] = quickstart(md)
        it["open_source"] = meta["license"] in OSS
        it["guide"] = guide_link(it["repo"])
        kept.append(it)
    kept.sort(key=lambda x: (-int(x["open_source"]), -x["gained"]))
    OUT_JSON.write_text(json.dumps({"date": TODAY.isoformat(), "repos": kept}, indent=1) + "\n")

    lines = [f"# Trending for AI agents and tools: {TODAY.isoformat()}\n",
             "Auto-generated from [github.com/trending](https://github.com/trending) (daily and weekly), "
             "filtered for AI, agents, skills, MCP and automation. Open-source repos are listed first. "
             "Repos marked ⚠️ have no OSI-style licence or an unusual star spike, so check before using them. "
             "Quick-start snippets are auto-extracted from each README: read the README before running anything.\n"]
    if not kept:
        lines.append("_Could not read the trending page this run._")
    for it in kept:
        badge = "✅ open source" if it["open_source"] else f"⚠️ licence: {it['license']}"
        if it.get("spike"):
            badge += " · ⚠️ unusual star spike, verify before trusting"
        gain = f"+{it['gained']} stars {it['period']}".strip()
        extra = (", " + ", ".join(it["also"])) if it["also"] else ""
        lines += [f"## [{it['repo']}](https://github.com/{it['repo']})",
                  f"{badge} · {it['language'] or 'n/a'} · ★ {it['stars']:,} · {gain}{extra}\n",
                  f"**What it is:** {it['summary']}\n"]
        if it["guide"]:
            lines.append(f"**Full guide (use cases + how to):** [{it['guide']}]({it['guide']})\n")
        if it["quickstart"]:
            lines += ["**Quick start (from its README):**", "```", it["quickstart"], "```", ""]
        else:
            lines.append("**How to start:** open the repo and follow its README.\n")
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    text = "\n".join(lines) + "\n"
    OUT_MD.write_text(text)
    (ARCHIVE / f"{TODAY.isoformat()}.md").write_text(text)
    print(f"kept {len(kept)} relevant repos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
