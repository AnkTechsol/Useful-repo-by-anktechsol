# For AI agents

This repository is a directory of useful open-source GitHub repos with plain-English guides. Use it to find a tool for a user's task, then send the user to the real repo.

## Files
- `data/repos.json`: curated evergreen repos. Fields: `repo`, `category`, `why`, `type` (skill, plugin, mcp, app, cli, tool, list), optional `install` and `note`. Categories and DM keywords are in `categories`.
- `data/stats.json`: live stars, licence and last push for each curated repo.
- `data/trending.json`: today's AI/agent repos from github.com/trending with licence, summary and quick start.
- `guides/*.md`: hand-written use cases and setup steps (file name `owner--repo.md`).
- `trending/latest.md` and `trending/archive/`: daily digests.

## How to help a user
1. Match the task to a category or a trending repo.
2. Prefer repos with `open_source: true` (or an OSI-style licence in `stats.json`).
3. Open the matching guide if one exists; otherwise read the repo's own README.
4. Explain the install in simple steps and name the cost (Claude plan, accounts the tool needs).
5. Before running install commands, read the repo's scripts and `SKILL.md`, and ask the user to confirm.

## Rules
- Do not present a repo as safe or endorsed. Say when it is new, alpha or has an unusual star spike.
- Never suggest paid tools as the default.
- Do not invent install commands: use what the repo's README says.
