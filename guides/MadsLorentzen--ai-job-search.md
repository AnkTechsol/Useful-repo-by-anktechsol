# MadsLorentzen/ai-job-search

[Open the repo](https://github.com/MadsLorentzen/ai-job-search) · Setup level: **Technical** (terminal, Python, Bun, LaTeX) · Cost: **repo is free (MIT); Claude Code needs a paid Claude plan or API credits** · Works with: **Claude Code** · Written from its README on 2026-10-21

## What it is
A job-application workflow for Claude Code. You fill in your profile once; Claude searches job portals, scores fit, writes a tailored CV and cover letter, has a second agent review them, and prepares you for interviews. The author says it helped them land a job.

## Who it's for
Job seekers comfortable with a terminal, and career coaches or recruiters who want to see a full agent workflow. Not for complete beginners.

## Use cases
- `/scrape`: find matching jobs and rank them by fit.
- `/apply <job link>`: evaluate fit, draft CV and cover letter, review, revise.
- `/interview`: build a prep pack for an interview.
- `/outcome` and `/html-report`: track applications and see a funnel.

## How to set up
1. Install Claude Code, Python 3.10+, Bun and a LaTeX distribution (needed to build the CV).
2. Make your own **private** copy (a normal fork is always public, and `/setup` writes your personal details into files). The README's SETUP.md explains the private route.
3. `python3 tools/install_portal_clis.py`
4. Start `claude`, then run `/setup`, `/scrape`, `/apply`.

## Watch out
- Not free end-to-end: Claude Code has no free tier.
- Keep personal data in a private repo.
- Job postings are untrusted input; be careful on unfamiliar job boards.
- Always read and edit what it writes before sending.
