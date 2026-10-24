# tirth8205/code-review-graph

[Open the repo](https://github.com/tirth8205/code-review-graph) · Setup level: **Medium** · Cost: **free (MIT)** · Works with: **Claude Code, Codex, Cursor, Windsurf, Gemini CLI and more (via MCP)** · Written from its README on 2026-10-25

## What it is
It builds a local map of your codebase (functions, files, who calls what) so that when you review a change, your agent reads only the parts that change touches instead of the whole project.

## Who it's for
Developers working on medium or large codebases who use an AI agent for code review.

## Use cases
- Review a change: see the changed functions, what depends on them, and missing tests.
- Ask questions about a big codebase without loading all of it.
- Find untested or unused code.

## How to set up
1. Needs Python 3.10+. In a terminal: `pip install code-review-graph`
2. In your project: `code-review-graph install --platform claude-code`
3. Build the map: `code-review-graph build`, then restart Claude Code.
4. Try: `code-review-graph detect-changes --brief`

## Tested
- 2026-10-25 on a clone of an open-source web framework (94 files): build took 6.4 s.
- One-function change: the review context went from **6,137 to 452 tokens** (about 93% fewer, by the tool's own estimate), and it flagged that the changed function had no test.

## Watch out
- `install` edits your project: adds `.mcp.json`, `CLAUDE.md`, `.claude/` skills and hooks, a git pre-commit hook and a `.gitignore` line. Run `code-review-graph uninstall --dry-run` to see how to remove it.
- The savings figure is the tool's own estimate.
- No telemetry (FAQ); cloud embeddings are opt-in.

## Our take
**What we think:** instead of the whole project, it reads only what you changed. That's where the token savings come from, and it also caught a missing test.

**Where to use it:** bigger codebases and code reviews. Skip it for tiny scripts, and read what it adds to your project first.
