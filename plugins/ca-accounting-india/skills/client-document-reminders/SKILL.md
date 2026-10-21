---
name: client-document-reminders
description: Draft polite WhatsApp and email reminders asking clients for documents, payments or approvals, and build a per-client missing-documents tracker. Use when a CA firm or bookkeeper needs to chase clients for GST, TDS, ITR, audit or bookkeeping documents.
---

# Client document reminders

## Ask for
- Client list or one client, their service (GST returns, ITR, audit, bookkeeping, TDS)
- What has been received and what is missing
- The due date from the firm (do not assume statutory dates; ask the user to confirm them on the official portal or notification)
- Preferred tone and language (English, Hindi, Hinglish)

## Steps
1. If the user shares a checklist or sheet, compute the missing items per client.
2. Write one message per client with the exact list of missing items, the date needed by, and how to send (WhatsApp photo, email, shared folder).
3. Escalation ladder: first friendly reminder, second reminder with the date and consequence, final notice mentioning that the firm may not be able to file on time. Consequences should be factual and general ("late filing can attract fees or interest"); do not quote specific penalties unless the user supplies them.
4. Output a table: Client | Missing items | Due | Reminder 1 | Reminder 2 | Reminder 3.

## Tracker format (copy into a sheet)
`Client, Service, Item, Requested on, Needed by, Received (Y/N), Notes`

## Guardrails
- Never include sensitive details (PAN, bank numbers) in group messages.
- Drafts only. The user sends the messages.
- Keep messages respectful and short (under 70 words).
