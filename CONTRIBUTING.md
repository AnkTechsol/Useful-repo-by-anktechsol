# Contributing

## Suggest a repo
1. Add an entry to `repos` in `data/repos.json`:
   ```json
   {"repo": "owner/name", "category": "<category id>", "why": "one line, what it does", "type": "skill", "install": "optional command", "note": "optional caution"}
   ```
   `type` is one of: skill, plugin, mcp, app, cli, tool, list.
2. Run `python3 scripts/validate.py`.
3. Run `python3 scripts/update.py` to fetch stats and refresh the README (or let the weekly Action do it).
4. Open a pull request. The repo must meet [RULES.md](RULES.md).

## Add a gap-filler skill
Create `plugins/<plugin>/skills/<skill-name>/SKILL.md` with `name` (same as folder) and `description` in the header, plus a `## Guardrails` section. Run `scripts/validate.py` and `scripts/build_zips.py`.
