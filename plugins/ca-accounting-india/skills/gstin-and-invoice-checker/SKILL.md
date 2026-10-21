---
name: gstin-and-invoice-checker
description: Check GSTIN and PAN format and checksum offline, verify the CGST/SGST/IGST split on a purchase or sales invoice, and flag invoice errors before booking or filing. Use when a CA, bookkeeper or business owner shares invoices, a GSTIN, PAN, or asks if a GST invoice is correct.
---

# GSTIN and invoice checker

Works fully offline using a bundled Python script (standard library only, nothing to install or pay for). If code cannot run in this environment, do the same checks manually and say so.

## Steps
1. For each GSTIN or PAN the user shares, run the script and report the result:
   ```
   python3 scripts/gst_check.py gstin <GSTIN>
   python3 scripts/gst_check.py pan <PAN>
   ```
   The script checks format and the GSTIN checksum, and decodes the state code and the PAN holder type. It cannot confirm the number is registered or active. Always tell the user to verify status on the official GST portal.
2. For each invoice (text, pasted table, or a photo or PDF the user shares), extract: supplier and recipient name, GSTINs, invoice number and date, place of supply, HSN/SAC, taxable value, rate, CGST/SGST/IGST amounts, total.
3. Re-compute the tax split:
   ```
   python3 scripts/gst_check.py split --taxable <amount> --rate <percent> --seller-state <code> --place-of-supply <code>
   ```
   Same state means CGST plus SGST. Different states means IGST.
4. Flag problems: GSTIN checksum or format failures, tax type mismatching place of supply, totals that do not add up, missing mandatory fields (invoice number, date, HSN/SAC, place of supply), duplicate invoice numbers in a batch, dates outside the period, rate that looks unusual for the stated HSN/SAC (flag as "verify", do not assert).
5. Output a table: Invoice | Issues found | Severity (Error / Check / OK) | Suggested fix.

## Guardrails
- GST rates, HSN mappings and rules change. Never state a rate as current without telling the user to confirm it on official notifications or with a professional.
- Do not file or submit anything. This skill prepares a review; the CA decides.
- Treat client financial data as confidential. Do not paste it into third-party websites.
- State code reference: the first two digits of a GSTIN are the state code (for example 27 is Maharashtra, 29 is Karnataka). If unsure of a code, ask the user.
