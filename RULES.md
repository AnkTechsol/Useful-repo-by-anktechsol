# Rules

## For listed repos
1. **Open source licence required.** MIT, Apache-2.0, BSD, ISC, MPL, GPL/AGPL/LGPL, Unlicense or CC0. No licence, source-available (for example Elastic License, Commons Clause) or archived repos are excluded automatically by `scripts/update.py`.
2. **Free to use.** No paid plan, paid API or subscription should be needed to get value. If a repo needs your own free developer account, say so in `note`.
3. **Publicly accepted.** Prefer repos with real adoption (stars, recent commits). Repos with suspicious star spikes or legal problems are not listed.
4. **Useful to non-technical people** where possible: skills, one-click extensions and simple apps first.
5. **Honest notes.** Mention cautions (alpha, needs a Meta app, consent for voice cloning, read-only first).

## For gap-filler skills made in this repo
- Only created when no trending repo covers the need (record the reason in `data/repos.json` under `gap_skills`).
- Free, no API keys, no accounts. Scripts are offline and standard-library only.
- Never invent facts, figures, citations or rates; mark uncertain items `[verify]`.
- Output is a draft or checklist for a professional to review; every skill has a `## Guardrails` section.

Run `python3 scripts/validate.py` before committing.
