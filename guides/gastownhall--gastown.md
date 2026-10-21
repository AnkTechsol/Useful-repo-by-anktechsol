# gastownhall/gastown

[Open the repo](https://github.com/gastownhall/gastown) · Setup level: **Technical** · Cost: **free (MIT)** plus your coding-agent accounts · Works with: **Claude Code (default), Codex, Copilot, Gemini, Cursor** · Written from its README on 2026-10-22

## What it is
A workspace manager for many AI coding agents: a "Mayor" AI coordinator assigns work to worker agents across projects, with mailboxes, identities and handoffs. Work state is stored in git, so agents don't lose context when they restart.

## Who it's for
Developers running more than a handful of agents who need structure; the README says it scales to 20–30 agents.

## Use cases
- Coordinate several agents across two or more projects from one place.
- Keep work progress safe across agent restarts (git-backed hooks and a work ledger).
- Hand tasks between agents with built-in mailboxes.

## How to set up
1. Prerequisites from the README: Git 2.20+, tmux 3.0+, sqlite3 and the Claude Code CLI (default runtime). Go and Beads are needed for non-Homebrew installs.
2. (Terminal, macOS) `brew install gastown` installs `gt`, `bd` and `dolt` together.
3. Linux/Windows and Docker paths are in the README's Installation section.

## Watch out
- The README warns against `go install` on macOS (Gatekeeper kills the unsigned binary).
- Many agents at once means many times the usage cost.
