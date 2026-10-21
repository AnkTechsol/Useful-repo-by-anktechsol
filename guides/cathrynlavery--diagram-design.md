# cathrynlavery/diagram-design

[Open the repo](https://github.com/cathrynlavery/diagram-design) · Setup level: **Easy** · Cost: **free (MIT)** · Works with: **Claude Code, Codex, Cursor, Copilot, Gemini CLI, Windsurf and others** · Written from its README on 2026-10-21

## What it is
A skill that makes your AI draw clean diagrams as a single HTML + SVG file you open by double-clicking. 45 diagram types (architecture, flows, quadrants, sequence and more), in your own brand colours and fonts.

## Who it's for
Founders, consultants and creators who need good-looking diagrams for decks, proposals, reels and carousels without learning a design tool.

## Use cases
- Explain a process or service to a client with a flow diagram.
- Make an impact-vs-effort quadrant for a strategy slide.
- Create visuals for Instagram carousels and videos that match your brand.
- Convert a Mermaid, draw.io or Excalidraw diagram into this style (the README lists import and export options).

## How to set up
1. Any supported agent: `npx skills add cathrynlavery/diagram-design`
2. Claude Code with updates and slash commands:
   ```
   /plugin marketplace add cathrynlavery/diagram-design
   /plugin install diagram-design@diagram-design
   ```
3. Codex: `codex plugin marketplace add cathrynlavery/diagram-design` then `codex plugin add diagram-design@diagram-design`.
4. Ask in plain words, for example: "Make an architecture diagram of my app: frontend, backend, database, cache." Then: "Onboard diagram-design to https://yoursite.com" to copy your site's colours and fonts.

## Watch out
- Install only from the official repo; the README warns that listings under other names are unofficial copies.
- It writes files to your computer; open the result in a browser to check it.
