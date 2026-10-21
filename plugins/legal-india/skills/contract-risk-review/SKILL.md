---
name: contract-risk-review
description: Review a contract under Indian law for risky, missing or one-sided clauses and produce a clause-by-clause risk table with suggested redlines. Use when a lawyer, founder or freelancer shares an agreement (service, vendor, employment, lease, partnership) and wants it reviewed. Draft analysis only; a qualified lawyer must review.
---

# Contract risk review (India)

Output is a first-pass review to speed up a lawyer's work. It is not legal advice.

## Ask for
- The contract text (paste or upload) and which party the user represents
- What matters most (cash flow, IP ownership, exit, liability, confidentiality)
- Governing law or location, if known

## Steps
1. Identify document type, parties, term, value and main obligations in 5 lines.
2. Review these clauses, noting present / missing / unusual: payment terms and late payment, scope and acceptance, term and termination (for cause and convenience), notice, IP ownership and licences, confidentiality, non-compete and non-solicit, indemnity, limitation of liability, warranties, force majeure, dispute resolution (courts vs arbitration, seat, number of arbitrators, language), governing law and jurisdiction, assignment, amendment, entire agreement, stamp duty and execution mechanics.
3. India-specific checks to raise (as questions, not conclusions):
   - Is the stamp duty and registration requirement for this instrument and state confirmed? Insufficiently stamped documents can cause admissibility problems.
   - Post-termination non-compete clauses are generally hard to enforce against employees and professionals under the Indian Contract Act, 1872; confirm with a lawyer.
   - Is the arbitration clause clear on seat, rules and number of arbitrators?
   - Are payment terms to micro or small enterprises consistent with applicable statutory payment timelines? Verify.
   - If personal data is processed, does the contract address the applicable data protection law?
4. Output a table: Clause | What it says | Risk (High/Med/Low) | Why | Suggested redline wording.
5. End with the top 5 issues to negotiate, a list of questions for the client, and clauses to confirm with a lawyer.

## Guardrails
- Quote the contract exactly when pointing at text. Never invent clause numbers.
- Do not cite case law or statute sections unless you mark them `[verify]`. Never fabricate citations.
- Say clearly if the document is too long or unclear to review fully.
- Confidential: do not suggest pasting the contract elsewhere.
