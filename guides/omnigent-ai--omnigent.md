# omnigent-ai/omnigent

[Open the repo](https://github.com/omnigent-ai/omnigent) · Setup level: **Technical** · Cost: **free (Apache-2.0)** plus the model or agent accounts you plug in · Works with: **Claude Code, Codex, Cursor, OpenCode, Hermes, Pi and custom YAML agents** · Written from its README on 2026-10-22

## What it is
An open-source "meta-harness": one control layer over the coding agents you already use, so they work together as a team. One agent can review another's work, or a task can be split across agents that are good at different things.

## Who it's for
Freelancers, small agencies and developers who juggle several AI agents and want one place to run them, with any model they choose.

## Use cases
- Run Claude Code and a cheaper open agent (Pi or OpenCode) side by side; let one review the other.
- Use your own API key, a Claude/ChatGPT subscription or another compatible gateway: no single-vendor lock-in.
- Start a session in the terminal, continue it in the browser or on your phone.
- Share a live session with a teammate or client so they can watch or co-drive.
- Run agents in disposable cloud sandboxes (Modal, Daytona, E2B and others) instead of your laptop.

## How to set up
1. (Terminal) One-command install from the README:
   ```bash
   curl -fsSL https://raw.githubusercontent.com/omnigent-ai/omnigent/main/scripts/install_oss.sh | sh
   ```
   The installer also adds the Databricks CLI; pass `--no-databricks` to skip it.
2. (Terminal) Manual install instead, needs Python 3.12+: `uv tool install omnigent` (or `pip install "omnigent"`), or `brew install omnigent-ai/tap/omnigent`.
3. A macOS desktop app is also offered on omnigent.ai.
4. First thing to try: start a session and add a second agent to review the first one's change.

## Watch out
- New (created June 2026) and changing fast: pin a version for client work.
- Running several agents multiplies token/API cost.
- Read the install script before piping it to your shell.
