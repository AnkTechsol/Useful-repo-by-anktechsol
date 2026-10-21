# anthropics/knowledge-work-plugins

[Open the repo](https://github.com/anthropics/knowledge-work-plugins) · Setup level: **Easy** · Cost: **free plugins** (you need Claude, and some connectors need accounts in those tools) · Works with: **Claude Cowork, Claude Code** · Written from its README on 2026-10-21

## What it is
11 ready-made plugins from Anthropic that turn Claude into a specialist for a job function: productivity, sales, customer support, product management, marketing, legal, finance, data, enterprise search, bio-research and a plugin builder. They are just markdown and JSON files, no code.

## Who it's for
Solo founders, small teams and agencies who want Claude to follow a proper workflow for sales calls, support tickets, specs, contracts or month-end instead of starting from a blank chat.

## Use cases
- **Sales:** research a prospect, prep for a call, draft outreach, build a competitor battlecard.
- **Customer support:** triage tickets, draft replies, turn solved issues into help articles.
- **Marketing:** draft content, plan a campaign, keep brand voice consistent.
- **Legal:** triage an NDA, review a contract, prep for a meeting (draft support only).
- **Finance:** prepare journal entries, reconcile accounts, explain variances.
- **Productivity:** manage tasks and daily workflows.

## How to set up
1. **Cowork (no terminal):** install plugins from claude.com/plugins.
2. **Claude Code:**
   ```
   claude plugin marketplace add anthropics/knowledge-work-plugins
   claude plugin install sales@knowledge-work-plugins
   ```
3. Plugins switch on by themselves. Skills fire when relevant, and commands such as `/sales:call-prep` or `/data:write-query` become available.
4. Optional: edit a plugin's `.mcp.json` to point at your own tools, and add your company terms to the skill files.

## First prompts to try
- "Prep me for a call with [company] tomorrow. Here is what I know: ..."
- "Triage these 10 support emails by urgency and draft replies."

## Watch out
- Connectors (Slack, HubSpot, Notion and so on) need your own accounts in those tools. Start without connectors.
- Treat legal and finance output as drafts for a professional to check.
