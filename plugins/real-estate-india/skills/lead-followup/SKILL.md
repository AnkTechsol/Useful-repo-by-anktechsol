---
name: lead-followup
description: Draft WhatsApp and call follow-up sequences for property enquiries, site visits and negotiations, and turn a lead list into a daily follow-up plan. Use when a real estate agent has leads, enquiry notes or a pasted lead sheet and wants messages or a follow-up schedule.
---

# Lead follow-up (India real estate)

## Ask for
- Lead name, source (portal, Instagram, referral, walk-in), budget, preferred area, buy or rent, timeline
- Last interaction and date, and what the lead said they were worried about
- The agent's tone preference (formal, friendly, Hinglish)

## Steps
1. If the user pastes a lead list (CSV or table), group leads into: hot (visit planned or asked price), warm (interested, no date), cold (no reply for 7 or more days).
2. For each lead, pick the next best action: send details, propose two visit slots, share a similar property, ask a qualifying question, or close politely.
3. Write the message in the requested language and tone. Keep WhatsApp messages under 60 words, one question per message.
4. Build a 7-day sequence for new enquiries: Day 0 reply with details, Day 1 visit invite, Day 3 value add (neighbourhood info or comparable), Day 7 soft close.
5. Output a table: Lead | Status | Next action | Message | Suggested date.

## Message types to offer
- First reply to a portal enquiry
- Site visit confirmation and reminder (include a placeholder for address pin)
- Post-visit follow-up
- Price negotiation: acknowledge, restate value, offer a next step
- Polite close when the lead goes silent

## Guardrails
- Only message people who enquired. Remind the user to respect opt-outs and never to spam broadcast lists.
- No pressure or false urgency ("last unit", "price going up tomorrow") unless the user confirms it is true.
- Do not share a lead's details with anyone else.
- WhatsApp sending is manual: you draft, the agent sends.
