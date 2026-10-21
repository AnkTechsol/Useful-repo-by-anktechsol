#!/usr/bin/env python3
"""Validate data/repos.json and the gap-filler plugins. Standard library only.

Run from the repo root:  python3 scripts/validate.py   (exit code 1 on errors)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FORBIDDEN = [r"OPENAI_API_KEY", r"ANTHROPIC_API_KEY", r"GEMINI_API_KEY", r"GROQ_API_KEY",
             r"ELEVENLABS", r"\bapi[_ -]?key\b", r"\bpaid plan\b", r"\bcreate an account\b"]
TYPES = {"skill", "plugin", "mcp", "app", "cli", "tool", "list"}
errors = []


def err(msg):
    errors.append(msg)


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            a, b = line.split(":", 1)
            out[a.strip()] = b.strip()
    return out


def check_repos():
    data = json.loads((ROOT / "data" / "repos.json").read_text())
    cats = {c["id"] for c in data["categories"]}
    seen = set()
    for item in data["repos"]:
        r = item.get("repo", "")
        if not re.fullmatch(r"[\w.-]+/[\w.-]+", r):
            err(f"bad repo slug: {r!r}")
        if r.lower() in seen:
            err(f"duplicate repo: {r}")
        seen.add(r.lower())
        if item.get("category") not in cats:
            err(f"{r}: unknown category {item.get('category')!r}")
        if not item.get("why"):
            err(f"{r}: missing 'why'")
        if item.get("type") not in TYPES:
            err(f"{r}: type must be one of {sorted(TYPES)}")
    return len(data["repos"])


def check_plugins():
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
    for p in market["plugins"]:
        d = ROOT / p["source"]
        if not (d / ".claude-plugin" / "plugin.json").exists():
            err(f"{p['name']}: missing plugin.json")
    n = 0
    for md in sorted((ROOT / "plugins").glob("*/skills/*/SKILL.md")):
        n += 1
        rel = md.relative_to(ROOT)
        text = md.read_text()
        fm = frontmatter(text)
        if not fm:
            err(f"{rel}: missing frontmatter")
            continue
        if fm.get("name") != md.parent.name:
            err(f"{rel}: name must equal folder name")
        if not fm.get("description") or len(fm["description"]) > 1024:
            err(f"{rel}: description missing or too long")
        if "## Guardrails" not in text:
            err(f"{rel}: missing '## Guardrails'")
        for pat in FORBIDDEN:
            if re.search(pat, text, re.I):
                err(f"{rel}: forbidden paid/key dependency pattern {pat}")
    for py in (ROOT / "plugins").rglob("*.py"):
        s = py.read_text()
        for bad in ("import requests", "urllib", "import socket", "http.client", "subprocess"):
            if bad in s:
                err(f"{py.relative_to(ROOT)}: skill scripts must be offline, stdlib only ({bad})")
    return n


def check_guides():
    need = ["## What it is", "## Who it's for", "## Use cases", "## How to set up", "## Watch out"]
    n = 0
    for g in sorted((ROOT / "guides").glob("*.md")):
        if g.name.startswith("_"):
            continue
        n += 1
        t = g.read_text()
        for h in need:
            if h not in t:
                err(f"guides/{g.name}: missing section '{h}'")
        if "Setup level:" not in t:
            err(f"guides/{g.name}: missing 'Setup level:' line")
    return n


def main():
    nr, ns = check_repos(), check_plugins()
    check_guides()
    print(f"Checked {nr} listed repos and {ns} gap-filler skills.")
    for e in errors:
        print("ERROR", e)
    print("OK" if not errors else f"{len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
