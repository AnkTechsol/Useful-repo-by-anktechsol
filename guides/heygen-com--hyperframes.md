# heygen-com/hyperframes

[Open the repo](https://github.com/heygen-com/hyperframes) · Setup level: **Medium** · Cost: **free (Apache-2.0)**, needs Node.js 22+ and FFmpeg · Works with: **Claude Code, Codex, Cursor, Gemini CLI and more** · Written from its README on 2026-10-21

## What it is
A framework that turns HTML, CSS, media and animations into MP4 videos, with 21 agent skills so your AI can plan, write and render videos for you.

## Who it's for
Creators, agencies and founders who want motion graphics, product videos and explainers made by prompting an agent, and repeatable pipelines for content.

## Use cases
- Product launch and feature-announcement videos from a website URL.
- Explainer videos from plain text (no footage).
- Captions and designed overlays (lower-thirds, callouts) on a talking-head video.
- Beat-synced videos from a music track.
- Short motion graphics, charts and kinetic type.
- A pull-request walkthrough video from a GitHub PR.

## How to set up
1. Claude Code:
   ```
   claude plugin marketplace add heygen-com/hyperframes
   claude plugin install hyperframes@hyperframes
   ```
2. Any other agent: `npx skills add heygen-com/hyperframes`
3. Try: "Using /hyperframes, create a 10-second product intro with a fade-in title, a background video and subtle music."
4. Or by hand: `npx hyperframes init my-video`, then `npx hyperframes preview` and `npx hyperframes render`.

## Watch out
- Needs Node.js and FFmpeg installed.
- Cloud rendering options exist; use local rendering to stay free.
- Check any stock media or music you add for its licence.
