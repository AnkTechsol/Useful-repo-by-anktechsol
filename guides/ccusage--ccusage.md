# ccusage/ccusage

[Open the repo](https://github.com/ccusage/ccusage) · Setup level: **Easy** · Cost: **free (MIT)** · Works with: **Claude Code, Codex, Gemini CLI, OpenCode and many other coding agents** · Written from its README on 2026-10-25

## What it is
A small command-line tool that reads the usage logs your coding agent already keeps on your computer and shows tokens and cost per day, week, month or session.

## Who it's for
Anyone using Claude Code (or another coding agent) who wants to know where the bill or the plan limit is going before trying to cut it.

## Use cases
- See what one session or one day of Claude Code would cost at API prices.
- Find the heavy days and sessions, and which model they used.
- Compare usage across several coding agents on the same machine.

## How to set up
1. Needs Node.js. No install step: run it with `npx` in a terminal.
2. For Claude Code only: `npx ccusage@latest claude daily`
3. Other views: `npx ccusage@latest claude session`, `... claude monthly`. Add `--offline` to use cached prices.

## Tested
- 2026-10-25: ran on one real Claude Code session copied into a sandbox: **$3.03** at API list price, split by day and model.
- Plain `npx ccusage daily` (without `claude`) also read the logs of every other AI agent on the machine. Everything stayed local, but use the `claude` command if you only want Claude Code.

## Watch out
- The cost is calculated at API list price. On a subscription plan you are not billed per token; read it as "how much of my limit".
- It reads local logs only, so usage from other devices is not included.

## Our take
**What we think:** this is step one. You can't cut a bill you can't see, and it showed my real session cost in seconds with no setup.

**Where to use it:** before installing any token saver, and once a week to spot heavy sessions. Skip it if you only use Claude in the browser.
