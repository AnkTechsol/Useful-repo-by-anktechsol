---
name: property-due-diligence-checklist
description: Generate a document-verification and red-flag checklist for an Indian residential property purchase, tailored to the property type and state. Use when an agent or buyer asks what to check before booking or buying a flat, plot, house or under-construction unit. Not legal advice.
---

# Property due-diligence checklist (India)

This produces a checklist for the agent and buyer to take to a property lawyer. It does not replace a title search or legal opinion.

## Ask for
- State and city, property type (resale flat, under-construction, plot, independent house)
- Seller type (individual, builder, society transfer), loan needed or not
- Documents the seller has already shared

## Checklist sections to generate (adapt to the answers)
1. **Title and ownership:** chain of sale deeds, previous agreements, mutation or khata records, encumbrance certificate for a suitable period, name matches on all documents.
2. **Approvals:** sanctioned building plan, commencement and occupancy or completion certificate, land use conversion where relevant.
3. **RERA (if under construction or a registered project):** registration number, check status and project details on the state RERA website, compare promised possession date and carpet area.
4. **Society or builder:** no-objection certificate, share certificate, maintenance dues and any pending litigation or notices.
5. **Dues and taxes:** property tax receipts, utility bills, society dues cleared.
6. **Physical and legal checks:** actual possession, tenants, boundaries, litigation search on court portals, whether the seller is a power-of-attorney holder (extra caution).
7. **Money and stamp duty:** how payment will be made, TDS on property purchase where applicable, stamp duty and registration charges for that state (ask the user to confirm current rates with the sub-registrar or a lawyer).
8. **Loan:** bank's legal and technical verification status.

## Output
A tick-box checklist with three columns: Item | Why it matters | Status (Have / Missing / Not applicable). End with a list of red flags found from what the user shared and the top 5 questions to ask the seller.

## Guardrails
- State laws, rates and portals differ by state and change often. Tell the user to verify on official sites.
- If any red flag appears (missing papers, rushed payment, unclear ownership), advise getting a property lawyer's opinion before paying a token or advance.
- Never state that a title is "clear".
