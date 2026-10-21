---
name: bank-statement-categorizer
description: Categorise bank statement or UPI transaction lines into ledger heads for bookkeeping, flag unusual entries, and produce a clean CSV ready to import into a spreadsheet or accounting software. Use when a bookkeeper or small business owner shares a bank statement CSV, pasted transactions or an export and wants them classified.
---

# Bank statement categoriser

## Ask for
- The statement (CSV, pasted text, or sheet) and the period
- Business type (trader, service, freelancer, restaurant, etc.) so categories fit
- Any existing chart of accounts or ledger names to reuse
- Which GST status applies (registered or not) if GST handling is wanted

## Steps
1. Parse columns: date, narration, debit, credit, balance. If the format is unclear, ask or show how you read it.
2. Assign each line a ledger head, using the user's chart of accounts if given. Default heads: Sales/Receipts, Purchases, Salary, Rent, Utilities, Software/Subscriptions, Travel, Marketing, Professional fees, Bank charges, Interest, GST payment, TDS, Loan/EMI, Owner drawings/Capital, Transfers between own accounts, Suspense (unknown).
3. Use narration patterns (UPI/NEFT/IMPS references, known vendors) but never guess confidently. Put uncertain lines in **Suspense** with a note on why.
4. Flag: duplicates, round-figure cash withdrawals, large transfers to individuals, entries that may need TDS or GST treatment (mark "check", do not assert).
5. Reconcile: opening balance + credits - debits should equal closing balance. Report any difference.
6. Output: (a) summary by ledger head with totals, (b) list of flagged and suspense lines for the user to resolve, (c) a CSV with columns `Date, Narration, Debit, Credit, Ledger, Flag, Note`.

## Guardrails
- Categorisation is a first draft. The accountant reviews before booking.
- Never claim a tax treatment is final. Say "check TDS/GST applicability".
- Mask account numbers in any output the user plans to share.
- Do not upload statements to third-party tools; work with what the user provides here.
