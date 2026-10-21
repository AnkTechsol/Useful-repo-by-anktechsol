# desplega-ai/agent-swarm

[Open the repo](https://github.com/desplega-ai/agent-swarm) · Setup level: **Technical** · Cost: **free (MIT, self-hosted)** plus model/agent accounts · Works with: **Claude Code, Codex, pi, opencode, Cursor, Amp, Grok and more** · Written from its README on 2026-10-22

## What it is
"An open-source operating system for AI work." A lead agent receives work from Slack, GitHub/GitLab, email or an API and delegates it to worker agents that run in isolated Docker containers, with shared memory, schedules and workflows.

## Who it's for
Small companies and agencies that want an always-on AI team taking requests from the tools they already use.

## Use cases
- Post a request in Slack and let the lead agent plan and delegate it.
- Run recurring work on a schedule (reports, checks, maintenance).
- Get structured results back through the API for other tools.
- Swap the worker harness (Claude Code, Codex, pi, opencode…) per job.

## How to set up
1. (Terminal) Give your coding agent the operator skill: `npx skills add desplega-ai/agent-swarm` (or install it as a plugin in Claude Code, Codex, Cursor or Gemini CLI; commands are in the README).
2. (Terminal) Or self-host with the README's one-shot installer, which checks Docker and Compose v2 and starts onboarding:
   ```bash
   curl -fsSL https://raw.githubusercontent.com/desplega-ai/agent-swarm/main/install.sh | bash
   ```
3. Open the dashboard `/setup` page the installer prints.

## Watch out
- Self-hosting needs Docker Compose and API credentials for your chosen harness; keep `.env` and the encryption key private.
- The website's cloud service has its own privacy terms; the self-hosted code is MIT.
