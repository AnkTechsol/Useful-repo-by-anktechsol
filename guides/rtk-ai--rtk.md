# rtk-ai/rtk

[Open the repo](https://github.com/rtk-ai/rtk) · Setup level: **Easy** · Cost: **free (Apache-2.0 for the rtk-oss edition)** · Works with: **Claude Code, Codex, Gemini CLI, Cursor, Copilot and other agents** · Written from its README on 2026-10-25

## What it is
A single small program that sits between your AI agent and the terminal. When the agent runs commands like tests, git or ls, it hands back a short summary instead of the full wall of text, so the agent reads (and you pay for) much less.

## Who it's for
Developers whose agent runs tests, git and build commands a lot.

## Use cases
- Long test runs: keep only the failures and a pass count.
- Git log and status: compact, one line per item.
- Directory listings, grep and logs: grouped and trimmed.

## How to set up
1. Install the Apache-2.0 edition: `brew install rtk-ai/tap/rtk-oss` (macOS/Linux), or the install script with `RTK_EDITION=oss`.
2. Connect it to Claude Code: `rtk init -g` (adds one hook; restart Claude Code).
3. Check: `rtk --version` and `rtk gain` (savings dashboard).

## Tested
- 2026-10-25, rtk-oss 1.0.1 (checksum verified) on a sample project with 62 tests (2 failing):
  - test output 6,237 → 310 characters (about 20× smaller), both failures kept with file and line;
  - git log 4,730 → 780, git status 501 → 139, ls 1,878 → 522 characters.
- `rtk init -g` in an isolated config added one PreToolUse hook to Claude Code's settings and an RTK.md note.

## Watch out
- There are two editions with the same `rtk` name: the default one includes BUSL-licensed parts; pick **rtk-oss** for pure Apache-2.0.
- Another project called "rtk" exists on crates.io; check `rtk gain` works.
- The hook only works on shell commands, not on the agent's built-in file reading.
- Telemetry is off by default (README).

## Our take
**What we think:** the biggest saving of the four I tested, with no change to how you work. Test output 20× smaller and the errors were still there.

**Where to use it:** projects with long test or build output. Little benefit if your agent mostly reads files rather than running commands.
