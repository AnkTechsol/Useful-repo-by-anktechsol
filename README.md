# Useful-repo-by-anktechsol

**The go-to hub for non-technical people, solo founders, small agencies, creators and AI agents who want to find useful open-source GitHub repos, and know how to use them.**

Every day this repo reads [github.com/trending](https://github.com/trending), keeps the AI, agent, skill and automation projects, checks their licence, and links to plain-English **use cases and how-to guides**. It also keeps an evergreen list of helpful repos that are not trending. We never copy the projects: every link goes to the real repo.

<!-- BEGIN:UPDATED -->
Last updated: 2026-10-21 (UTC). Star counts are live from the GitHub API.
<!-- END:UPDATED -->

## Who this is for
- **Non-technical and solo:** you pay for Claude, ChatGPT or Gemini but only use the chat box. Find a ready-made skill or plugin and a 5-step setup.
- **Small companies and agencies:** find tools for sales, support, content, accounting, legal and more.
- **AI agents:** read [AGENTS.md](AGENTS.md) and `data/*.json` to find the right repo for a task.

## Trending today (AI, agents, skills)
<!-- BEGIN:TODAY -->
From [github.com/trending](https://github.com/trending) on 2026-10-21. Full digest with quick starts: [trending/latest.md](trending/latest.md).

| Repo | Why it's trending | Stars gained | Guide |
|---|---|---|---|
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription &  | +17057 this week | [use cases + how to](guides/debpalash--VoiceStudio.md) |
| [storytold/artcraft](https://github.com/storytold/artcraft) | ArtCraft is an intentional crafting engine for artists, designers, and filmmakers | +10287 this week | [quick start](trending/latest.md) |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | Write HTML. Render video. Built for agents. | +5994 this week | [use cases + how to](guides/heygen-com--hyperframes.md) |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Official, Anthropic-managed directory of high quality Claude Code Plugins. | +5650 this week | [quick start](trending/latest.md) |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Editorial diagram design for Claude Code, Codex, GitHub Copilot, Cursor, Factory Droid, and Pi. 44 diagram types. Self-contained HTML + SVG. | +5473 this week | [use cases + how to](guides/cathrynlavery--diagram-design.md) |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 250,000+ scientists worldwide. 177 ready-to-use val | +4549 this week | [quick start](trending/latest.md) |
| [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | The job search that runs on your machine. AI job application framework built on Claude Code: evaluate postings, tailor CVs, write cover lett | +3861 today | [use cases + how to](guides/MadsLorentzen--ai-job-search.md) |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings | +1712 today | [quick start](trending/latest.md) |
<!-- END:TODAY -->

## How-to guides (use cases, setup, cautions)
<!-- BEGIN:GUIDES -->
- [MadsLorentzen/ai-job-search](guides/MadsLorentzen--ai-job-search.md) _(setup: Technical)_: A job-application workflow for Claude Code.
- [anthropics/knowledge-work-plugins](guides/anthropics--knowledge-work-plugins.md) _(setup: Easy)_: 11 ready-made plugins from Anthropic that turn Claude into a specialist for a job function: productivity, sales, customer support, product management, marketing, legal, finance, data, enterprise search, bio-research and a plugin builder.
- [cathrynlavery/diagram-design](guides/cathrynlavery--diagram-design.md) _(setup: Easy)_: A skill that makes your AI draw clean diagrams as a single HTML + SVG file you open by double-clicking.
- [debpalash/VoiceStudio](guides/debpalash--VoiceStudio.md) _(setup: Easy to Medium)_: A desktop app for voice cloning, voice design, video dubbing, dictation, transcription and audiobook creation in 646 languages.
- [heygen-com/hyperframes](guides/heygen-com--hyperframes.md) _(setup: Medium)_: A framework that turns HTML, CSS, media and animations into MP4 videos, with 21 agent skills so your AI can plan, write and render videos for you.
- [msitarzewski/agency-agents](guides/msitarzewski--agency-agents.md) _(setup: Easy to Medium)_: A big collection of AI "specialist" personas (engineering, design, marketing, sales and more).
<!-- END:GUIDES -->

More guides are added as repos trend. Template: [guides/_TEMPLATE.md](guides/_TEMPLATE.md).

## Start here: pick your keyword
<!-- BEGIN:INDEX -->
| Comment this | Go to |
|---|---|
| `SKILLS` | [Skill and plugin libraries (Claude Code, Codex and more)](#skill-and-plugin-libraries-claude-code-codex-and-more) |
| `TRENDING` | [Trending agent tools and productivity](#trending-agent-tools-and-productivity) |
| `CREATOR` | [Creator: video, reels and captions](#creator-video-reels-and-captions), [Creator: carousels, graphics and writing](#creator-carousels-graphics-and-writing), [Creator: voice and audio](#creator-voice-and-audio), [Creator: scheduling and comment-to-DM](#creator-scheduling-and-comment-to-dm) |
| `INDIA` | [India toolkit (GST, PAN, UPI, Indian languages)](#india-toolkit-gst-pan-upi-indian-languages) |
| `PROPERTY` | [Real estate](#real-estate) |
| `CA` | [CA, accounting and finance](#ca-accounting-and-finance) |
| `LEGAL` | [Legal](#legal) |
| `SELLER` | [Online sellers and e-commerce](#online-sellers-and-e-commerce) |
| `TEACH` | [Teachers, tutors and researchers](#teachers-tutors-and-researchers) |
| `FREELANCE` | [Freelancers, coaches, agencies and marketing](#freelancers-coaches-agencies-and-marketing) |
| `JOBS` | [Job search and careers](#job-search-and-careers) |
<!-- END:INDEX -->

## How to add these as skills in Claude
Look at the **Type** column in the lists below.

| Type | How to use it |
|---|---|
| **skill** | A folder with a `SKILL.md`. **Claude Code:** if the repo is a marketplace run `/plugin marketplace add owner/repo`, then `/plugin install <plugin>@<marketplace>`; or run `npx skills add owner/repo` (works with many agents). **Claude Desktop / claude.ai:** download the skill folder as a zip and upload it in *Settings → Capabilities → Skills* (menu names can change; skills depend on your plan). **No install:** paste the text of `SKILL.md` into a Claude Project's instructions. |
| **plugin** | Claude Code: `/plugin marketplace add owner/repo` then `/plugin install ...`. Some also work in Cowork. |
| **mcp** | An MCP server that lets Claude use another app. In Claude Desktop use *Settings → Extensions* if a one-click bundle exists, otherwise follow the repo's README. Start read-only. |
| **app / cli / tool** | A normal program. Follow its README. |
| **list** | A directory of more repos. |

**Before you install anything:** open the `SKILL.md` and scripts and read them. Skills can run commands on your computer.

## New in this hub
<!-- BEGIN:NEW -->
- **msitarzewski/agency-agents**: A whole AI agency of specialist agent personas; installs into Claude Code, Codex, Cursor and more (2026-10-21)
- **anthropics/knowledge-work-plugins**: 11 Anthropic plugins for sales, support, legal, finance, marketing and more (Cowork and Claude Code) (2026-10-21)
<!-- END:NEW -->

Video-ready cards for each new addition: [NEW.md](NEW.md).

## Fastest growing in the evergreen list
<!-- BEGIN:TRENDING -->
| Repo | New stars since last update | Total stars |
|---|---|---|
| [mattpocock/skills](https://github.com/mattpocock/skills) | +4 | 298.9k |
| [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +4 | 61.3k |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2 | 219.2k |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +1 | 59.1k |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +1 | 68.7k |
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +1 | 55.7k |
| [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +1 | 38.5k |
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +1 | 141.0k |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +1 | 30.9k |
<!-- END:TRENDING -->

## The evergreen list (helpful even when not trending)
<!-- BEGIN:LIST -->
### Skill and plugin libraries (Claude Code, Codex and more)

DM keyword: `SKILLS`

| Repo | What it does | Type | Stars | Licence | Last push | Notes |
|---|---|---|---|---|---|---|
| [mattpocock/skills](https://github.com/mattpocock/skills) | Developer workflow skills | skill | 298.9k (+4) | MIT | 2026-10-19 | `npx skills@latest add mattpocock/skills` |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 177+ science skills and 100+ databases | skill | 53.3k | MIT | 2026-10-19 |  |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Anthropic-managed directory of Claude Code plugins | plugin | 43.5k | Apache-2.0 | 2026-10-21 |  |
| [wshobson/agents](https://github.com/wshobson/agents) | Plugin marketplace that works across several agent tools | plugin | 41.3k | MIT | 2026-10-19 |  |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | Curated list of 1,000+ agent skills | list | 36.1k | MIT | 2026-10-20 |  |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | npx skills CLI installs one skill into many agents (Claude Code, Codex, Cursor...) | cli | 35.9k | MIT | 2026-10-19 | `npx skills@latest add <owner/repo>` |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 380+ skills for Claude Code, Codex, Gemini CLI, Cursor and more | skill | 28.5k | MIT | 2026-08-30 |  |
| [fcakyon/claude-codex-settings](https://github.com/fcakyon/claude-codex-settings) | Claude Code and Codex configs, hooks and plugins side by side | plugin | 1.2k | Apache-2.0 | 2026-10-20 |  |
| [charlie947/skills-for-everyone](https://github.com/charlie947/skills-for-everyone) | 7 skills for people who use Claude daily but do not code | skill | 6 | MIT | 2026-10-06 |  |

### Trending agent tools and productivity

DM keyword: `TRENDING`

| Repo | What it does | Type | Stars | Licence | Last push | Notes |
|---|---|---|---|---|---|---|
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | Open-source coding agent | app | 219.2k (+2) | MIT | 2026-10-21 |  |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | Turn any codebase into an explorable knowledge graph | skill | 87.3k | MIT | 2026-10-12 |  |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) · [guide](guides/heygen-com--hyperframes.md) | Render video from HTML, built for agents | tool | 68.7k (+1) | Apache-2.0 | 2026-10-21 |  |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · [guide](guides/cathrynlavery--diagram-design.md) | Agent skill with 44 diagram types as HTML/SVG | skill | 59.1k (+1) | MIT | 2026-10-20 |  |
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Make any software controllable by agents via CLI | tool | 55.7k (+1) | Apache-2.0 | 2026-09-22 |  |
| [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | One /v1 endpoint routing to many free LLM providers | tool | 38.5k (+1) | MIT | 2026-10-20 | Personal use. Read its terms. |
| [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | Use Codex from inside Claude Code for review and delegation | plugin | 34.4k | Apache-2.0 | 2026-07-08 |  |
| [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) | Control Blender with an LLM through MCP | mcp | 31.8k | MIT | 2026-10-20 |  |
| [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | Agents working with CAD models | tool | 22.1k | MIT | 2026-10-20 |  |
| [zanwei/design-dna](https://github.com/zanwei/design-dna) | Turn reference UIs into design tokens and matching UI | skill | 2.0k | MIT | 2026-08-28 |  |

### Creator: video, reels and captions

DM keyword: `CREATOR`

| Repo | What it does | Type | Stars | Licence | Last push | Notes |
|---|---|---|---|---|---|---|
| [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) | 42 FFmpeg tools + MCP for cutting, captions, 9:16 reframe. No cloud | skill | 2.0k | MIT | 2026-10-21 |  |
| [AgriciDaniel/claude-shorts](https://github.com/AgriciDaniel/claude-shorts) | Long video to shorts with animated captions | skill | 233 | MIT | 2026-07-11 |  |
| [6missedcalls/video-editing-skill](https://github.com/6missedcalls/video-editing-skill) | Trim, jump cuts, Hormozi-style captions via FFmpeg + Whisper | skill | 47 | MIT | 2026-02-27 |  |
| [waseemnasir2k26/reelforge](https://github.com/waseemnasir2k26/reelforge) | Raw take to captioned vertical reel, local and free | cli | 8 | MIT | 2026-10-11 |  |
| [philippprimisser-max/whisper-word-captions](https://github.com/philippprimisser-max/whisper-word-captions) | Word-by-word highlighted captions with faster-whisper | cli | 0 | MIT | 2026-10-09 |  |
| [h-f-fares/claude-remotion-skill](https://github.com/h-f-fares/claude-remotion-skill) | Claude makes motion graphics and captions with Remotion | skill | 0 | MIT | 2026-10-21 | Remotion has its own licence terms for companies. |
| [addsumtech/topic-to-video](https://github.com/addsumtech/topic-to-video) | Topic to narrated, captioned video; free voices by default | skill | 0 | MIT | 2026-10-17 |  |

### Creator: carousels, graphics and writing

DM keyword: `CREATOR`

| Repo | What it does | Type | Stars | Licence | Last push | Notes |
|---|---|---|---|---|---|---|
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | Node-based local image generation | app | 141.0k (+1) | GPL-3.0 | 2026-10-21 |  |
| [sergebulaev/instagram-skills](https://github.com/sergebulaev/instagram-skills) | Skills for captions, hooks, carousel plans and hashtags | skill | 539 | MIT | 2026-10-21 |  |
| [Hainrixz/open-carrusel](https://github.com/Hainrixz/open-carrusel) | Chat with Claude to design Instagram carousels, export PNGs | skill | 489 | MIT | 2026-04-15 | `Type /start in Claude Code` |
| [vyralcontent/content-skills](https://github.com/vyralcontent/content-skills) | Hooks, scripts and carousels for Reels, TikTok, Shorts | skill | 160 | MIT | 2026-06-22 |  |

### Creator: voice and audio

DM keyword: `CREATOR`

| Repo | What it does | Type | Stars | Licence | Last push | Notes |
|---|---|---|---|---|---|---|
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) · [guide](guides/debpalash--VoiceStudio.md) | Local voice cloning, dubbing and transcription | app | 79.3k | AGPL-3.0 | 2026-10-21 | Clone only voices you have consent for. |
| [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | Lightweight CPU text-to-speech | tool | 16.2k | Apache-2.0 | 2026-10-21 |  |

### Creator: scheduling and comment-to-DM

DM keyword: `CREATOR`

| Repo | What it does | Type | Stars | Licence | Last push | Notes |
|---|---|---|---|---|---|---|
| [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app) | Self-hosted social scheduler incl. Instagram, with API and agent CLI | app | 37.5k | AGPL-3.0 | 2026-10-21 | Use self-hosted only; the cloud version is paid. |
| [harshithgangone/open-autodm](https://github.com/harshithgangone/open-autodm) | Self-hosted comment, DM and story-reply automation | app | 16 | MIT | 2026-10-05 | Needs your own Meta developer app. |
| [AmitDas4321/EngagePilot](https://github.com/AmitDas4321/EngagePilot) | Self-hosted Instagram comment-to-DM via Meta Graph API | app | 4 | MIT | 2026-10-20 | Needs your own Meta developer app. |
| [A-S-W-I-N-S-P-A-R-K-Y/AutoDMX](https://github.com/A-S-W-I-N-S-P-A-R-K-Y/AutoDMX) | Self-hosted comment-to-DM with encrypted tokens | app | 0 | MIT | 2026-09-04 | Needs your own Meta developer app. |
| [charanjit-singh/opendm](https://github.com/charanjit-singh/opendm) | ManyChat-style DM automation on Cloudflare Workers | app | 0 | AGPL-3.0 | 2026-10-15 | Needs your own Meta developer app. |

### India toolkit (GST, PAN, UPI, Indian languages)

DM keyword: `INDIA`

| Repo | What it does | Type | Stars | Licence | Last push | Notes |
|---|---|---|---|---|---|---|
| [AI4Bharat/Indic-TTS](https://github.com/AI4Bharat/Indic-TTS) | Text-to-speech for 13 Indian languages | tool | 413 | MIT | 2024-11-08 ⚠️ stale |  |
| [resilient-tech/india-compliance](https://github.com/resilient-tech/india-compliance) | GST returns, e-invoice and e-waybill for ERPNext | app | 276 | GPL-3.0 | 2026-10-20 | Some automation features need a paid India Compliance account. Use free features only. |
| [rehan1020/MCP-India-Stack](https://github.com/rehan1020/MCP-India-Stack) | 76 offline tools: GSTIN, PAN, UPI, IFSC, HSN/SAC, tax calculators | mcp | 65 | MIT | 2026-10-08 | `pip install mcp-india-stack` |
| [vexyl-ai/vexyl-stt](https://github.com/vexyl-ai/vexyl-stt) | Self-hosted speech-to-text for 14 Indian languages | app | 11 | Apache-2.0 | 2026-07-19 |  |

### Real estate

DM keyword: `PROPERTY`

| Repo | What it does | Type | Stars | Licence | Last push | Notes |
|---|---|---|---|---|---|---|
| [miron-tech/wholesaler-claude-skills](https://github.com/miron-tech/wholesaler-claude-skills) | Comps, ARV, rehab estimates, seller scripts (US wholesaling) | skill | 49 | MIT | 2026-10-08 |  |
| [sasha-deneux/claude-skills-cre](https://github.com/sasha-deneux/claude-skills-cre) | Free copy-paste skills for the deal lifecycle (commercial focus) | skill | 4 | MIT | 2026-07-15 |  |

### CA, accounting and finance

DM keyword: `CA`

| Repo | What it does | Type | Stars | Licence | Last push | Notes |
|---|---|---|---|---|---|---|
| [openaccountant/skills](https://github.com/openaccountant/skills) | 44 financial skills: P&L, budgeting, tax prep | skill | 97 | MIT | 2026-04-09 |  |

### Legal

DM keyword: `LEGAL`

| Repo | What it does | Type | Stars | Licence | Last push | Notes |
|---|---|---|---|---|---|---|
| [evolsb/claude-legal-skill](https://github.com/evolsb/claude-legal-skill) | Contract review with risk detection and redlines | skill | 478 | MIT | 2026-07-23 |  |

### Online sellers and e-commerce

DM keyword: `SELLER`

| Repo | What it does | Type | Stars | Licence | Last push | Notes |
|---|---|---|---|---|---|---|
| [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills) | 157 skills for Amazon, Shopify, Etsy, TikTok Shop sellers | skill | 1.2k | MIT | 2026-08-26 |  |
| [GeLi2001/shopify-mcp](https://github.com/GeLi2001/shopify-mcp) | MCP server for the Shopify API (start read-only) | mcp | 237 | MIT | 2026-04-05 |  |
| [motiful/product-shots](https://github.com/motiful/product-shots) | One product photo to a full set of e-commerce visuals | skill | 111 | MIT | 2026-06-08 | Alpha status. |
| [kgelster/awesome-ecom-skills](https://github.com/kgelster/awesome-ecom-skills) | Shopify skills covering catalog, SEO and import traps | skill | 49 | MIT | 2026-08-22 |  |

### Freelancers, coaches, agencies and marketing

DM keyword: `FREELANCE`

| Repo | What it does | Type | Stars | Licence | Last push | Notes |
|---|---|---|---|---|---|---|
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) · [guide](guides/msitarzewski--agency-agents.md) | A whole AI agency of specialist agent personas; installs into Claude Code, Codex, Cursor and more | skill | 162.5k | MIT | 2026-10-19 |  |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) · [guide](guides/anthropics--knowledge-work-plugins.md) | 11 Anthropic plugins for sales, support, legal, finance, marketing and more (Cowork and Claude Code) | plugin | 30.9k (+1) | Apache-2.0 | 2026-10-20 | `claude plugin marketplace add anthropics/knowledge-work-plugins` |
| [AgriciDaniel/claude-blog](https://github.com/AgriciDaniel/claude-blog) | 30 blog skills for SEO and AI-citation-ready posts | skill | 2.4k | MIT | 2026-10-14 |  |
| [OpenClaudia/openclaudia-skills](https://github.com/OpenClaudia/openclaudia-skills) | 77 marketing skills: SEO, content, email, ads, analytics | skill | 718 | MIT | 2026-10-20 |  |
| [thatrebeccarae/claude-marketing](https://github.com/thatrebeccarae/claude-marketing) | Marketing skill packs for Klaviyo, Shopify, GA4 and paid media | skill | 176 | MIT | 2026-05-14 | Some skills use third-party platforms you may need an account for. |

### Job search and careers

DM keyword: `JOBS`

| Repo | What it does | Type | Stars | Licence | Last push | Notes |
|---|---|---|---|---|---|---|
| [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) · [guide](guides/MadsLorentzen--ai-job-search.md) | Forkable job-search framework on Claude Code | skill | 61.3k (+4) | MIT | 2026-10-21 |  |

### Excluded automatically (does not meet the free and open-source rule)

| Repo | Reason |
|---|---|
| [anthropics/skills](https://github.com/anthropics/skills) | licence not OSI-style (NONE) |
| [trailofbits/skills](https://github.com/trailofbits/skills) | licence not OSI-style (CC-BY-SA-4.0) |
| [composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills) | licence not OSI-style (NONE) |
| [zhuyansen/awesome-claude-video-skills](https://github.com/zhuyansen/awesome-claude-video-skills) | licence not OSI-style (NOASSERTION) |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | licence not OSI-style (NOASSERTION) |
| [dpearson2699/swift-ios-skills](https://github.com/dpearson2699/swift-ios-skills) | licence not OSI-style (NOASSERTION) |
| [sboghossian/master-claude-for-legal](https://github.com/sboghossian/master-claude-for-legal) | licence not OSI-style (NOASSERTION) |
| [GarethManning/claude-education-skills](https://github.com/GarethManning/claude-education-skills) | licence not OSI-style (NOASSERTION) |
| [imbad0202/academic-research-skills](https://github.com/imbad0202/academic-research-skills) | licence not OSI-style (NOASSERTION) |
| [proficientlyjobs/proficiently-claude-skills](https://github.com/proficientlyjobs/proficiently-claude-skills) | licence not OSI-style (NONE) |

<!-- END:LIST -->

## Gap-filler skills made here (India)
Only where nothing trending existed. Free, no API keys, offline.

```
/plugin marketplace add AnkTechsol/Useful-repo-by-anktechsol
/plugin install real-estate-india@anktechsol-useful-repos
/plugin install ca-accounting-india@anktechsol-useful-repos
/plugin install legal-india@anktechsol-useful-repos
```

| Plugin | Skills |
|---|---|
| `real-estate-india` | listing-writer, lead-followup, buyer-brief-and-comparison, property-due-diligence-checklist |
| `ca-accounting-india` | gstin-and-invoice-checker (offline script), client-document-reminders, notice-reply-drafter, bank-statement-categorizer |
| `legal-india` | contract-risk-review, legal-notice-drafter, client-intake-and-timeline, nda-drafter |

For Claude Desktop, run `python3 scripts/build_zips.py` and upload the zips from `dist/`.

## How this stays fresh
- A GitHub Action runs every day: it reads the trending page, refreshes stars and licences, rebuilds this README and `trending/archive/`.
- Past digests: [trending/archive/](trending/archive/).
- Open-source rule and exclusions: [RULES.md](RULES.md).

## Disclaimer
Listed repos are third-party projects, not endorsed or maintained here. Star counts and licences come from GitHub at the time of the last update; verify before relying on them. Guides summarise each README and may go out of date. Skills made here prepare drafts and checklists and do not replace a CA, advocate or other professional. See [docs/DISCLAIMER.md](docs/DISCLAIMER.md).

## Contributing
Suggest a repo or write a guide: [CONTRIBUTING.md](CONTRIBUTING.md). Licence: MIT.
