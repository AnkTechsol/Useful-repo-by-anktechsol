# mvschwarz/openrig

[Open the repo](https://github.com/mvschwarz/openrig) · Setup level: **Technical** · Cost: **free (Apache-2.0)** plus a Claude Code or Codex account · Works with: **Claude Code, Codex, Pi** · Written from its README on 2026-10-22

## What it is
"A harness wraps a model. A rig wraps your harnesses." You describe an agent team in YAML (roles, shared context, owned work) and start it with one command, so a pile of terminal sessions becomes one organized, persistent team.

## Who it's for
Developers and small teams who want a standing "AI agency" for a project instead of one-off agent sessions.

## Use cases
- Keep a persistent team (planner, builder, reviewer) on a codebase with shared context.
- Mix Claude Code and Codex in one rig and manage them as one system.
- Start from the shipped starter team and adapt it to your project.

## How to set up
1. Requirements: Node.js 22 or 24 (22 on Apple silicon), tmux, macOS or Linux (WSL2 on Windows), and Claude Code or Codex signed in.
2. (Terminal) Add the `rigs` skill to your agent, as in the README (Claude Code example):
   ```sh
   npx skills add https://github.com/mvschwarz/openrig/tree/v0.6.12/skills/rigs --skill rigs --agent claude-code
   ```
   Check the README for the current version tag before running it.
3. Type `/rigs` in Claude Code (or `$rigs` in Codex) and describe what you want built; the agent explains what it will run before installing OpenRig.

## Watch out
- Installs `@openrig/cli` globally with npm and changes your machine as listed in its README: read that section first.
- Still uses your Claude Code/Codex accounts, so usage limits and costs apply.
