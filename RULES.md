# Rules

## For listed repos
1. **Open source licence required.** MIT, Apache-2.0, BSD, ISC, MPL, GPL/AGPL/LGPL, Unlicense or CC0. No licence, source-available (for example Elastic License, Commons Clause) or archived repos are excluded automatically by `scripts/update.py`.
2. **Free to use.** No paid plan, paid API or subscription should be needed to get value. If a repo needs your own free developer account, say so in `note`.
3. **Publicly accepted.** Prefer repos with real adoption (stars, recent commits). Repos with suspicious star spikes or legal problems are not listed.
4. **Useful to non-technical people** where possible: skills, one-click extensions and simple apps first.
5. **Honest notes.** Mention cautions (alpha, needs a Meta app, consent for voice cloning, read-only first).
6. **Agent-only setup.** The repo must install and run with no manual intervention: Claude Code or another AI agent can complete the whole setup itself (plugin, skill, `npx` or CLI). Repos that need hand-edited config, GUI steps or manual sign-ins beyond the user's own agent login are not listed, or are marked clearly in `note`.
7. **Add-on first.** Prefer repos that plug into the Claude Code (or Codex) the user already has as a plugin, skill or repo, over standalone apps that replace it.
8. **Niche beats generic.** Prefer focused tools for a specific job or profession (for example tax, contracts, an agency setup) that many people need, over huge general lists.
9. **Test it before featuring.** Every featured repo is run once in a throwaway sandbox where the agent does the setup unaided. Show only what worked, and never use real personal data in a demo.
10. **Every guide ends with our own take.** The last section of each guide is `## Our take`, written by the maintainer (not generated from the README): what we think of it and where to use it.

## Guide format
Sections, in this order: What it is, Who it's for, Use cases, How to set up, Watch out, **Our take** (last). `Our take` has two parts: **What we think** (honest opinion after testing, including weak points) and **Where to use it** (the situations it fits and the ones to skip). Do not copy the README here, and never invent results.

## For gap-filler skills made in this repo
- Only created when no trending repo covers the need (record the reason in `data/repos.json` under `gap_skills`).
- Free, no API keys, no accounts. Scripts are offline and standard-library only.
- Never invent facts, figures, citations or rates; mark uncertain items `[verify]`.
- Output is a draft or checklist for a professional to review; every skill has a `## Guardrails` section.

Run `python3 scripts/validate.py` before committing.
