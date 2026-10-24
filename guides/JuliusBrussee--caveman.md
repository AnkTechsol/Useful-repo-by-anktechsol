# JuliusBrussee/caveman

[Open the repo](https://github.com/JuliusBrussee/caveman) · Setup level: **Easy** · Cost: **free (Apache-2.0)**; an optional "Auto" feature needs a free account and Caveman Cloud is a separate paid service · Works with: **Claude Code, Codex, Gemini CLI and 30+ agents** · Written from its README on 2026-10-25

## What it is
A skill and plugin that makes your AI agent answer in short, direct sentences while keeping code, commands and error messages exactly as they are. Newer versions add more parts (shrinking logs, picking the model).

## Who it's for
People who have long chats with their agent and want shorter answers.

## Use cases
- Shorter explanations during long coding sessions.
- Cleaner answers when you only need the fix.

## How to set up
1. Claude Code plugin: `claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman`
2. Only the short-answer skill: `npx skills add JuliusBrussee/caveman -g`
3. Full installer (more parts): `npx @caveman-ai/cli@latest`. Read what it changes before pressing Enter.
4. Say `stop caveman` to switch it off.

## Tested
- 2026-10-25, plugin 4.0.1, the same coding question asked twice with and twice without it:
  - answers had 29% and 48% fewer output tokens and kept the same fix;
  - **but the total cost of each single question went up** ($0.089 → $0.096, $0.083 → $0.095), because its own rules add input tokens.
- It wrote small state files and a `hooks/` folder into `~/.claude` even when only loaded for one session (settings.json untouched).

## Watch out
- On small, one-off questions it can cost more, not less. Its README also says that against a simple "answer concisely" instruction the gain is small.
- It leaves state files in your Claude config folder.
- The full installer changes several agents at once; prefer the plugin or skill if you only want short answers.

## Our take
**What we think:** answers really got shorter, but on one small question my bill went up, not down. It's the catch in this set.

**Where to use it:** long sessions with lots of back-and-forth. Keep it off for small, quick tasks.
