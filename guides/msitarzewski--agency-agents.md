# msitarzewski/agency-agents

[Open the repo](https://github.com/msitarzewski/agency-agents) · Setup level: **Easy to Medium** · Cost: **free (MIT)** · Works with: **Claude Code, Cursor, Codex, Gemini CLI, Copilot, Windsurf, Aider and more** · Written from its README on 2026-10-21

## What it is
A big collection of AI "specialist" personas (engineering, design, marketing, sales and more). Each is a markdown file describing a role, how it works and what it delivers, so you can say "act as my UI designer" and get a consistent, specialised helper.

## Who it's for
Solo founders and small agencies who want a virtual team: a designer, a marketer, a project lead, a reviewer, without writing prompts from scratch.

## Use cases
- Run a small project with different agents for planning, design, copy and review.
- Get a second opinion from a "reality checker" style agent before launch.
- Pick only the divisions you need (for example marketing) instead of everything.

## How to set up
1. **Easiest:** use the desktop app (macOS, Linux, Windows) linked from the README. It browses all agents and installs them into Claude Code, Cursor, Codex and others with a click. On a Mac: `brew install --cask msitarzewski/agency-agents/agency-agents`.
2. **Claude Code by script:** `./scripts/install.sh --tool claude-code`, or copy one category: `cp engineering/*.md ~/.claude/agents/`.
3. **Only some teams:** `./scripts/install.sh --tool claude-code --division engineering,security` (see `--list teams`).
4. Then ask: "Activate Frontend Developer mode and help me build a landing page."

## Watch out
- Install only the divisions you need. Some tools cap how many agents they load (the README mentions OpenCode dropping extras).
- Read an agent file before using it. These are prompts, not guarantees of quality.
