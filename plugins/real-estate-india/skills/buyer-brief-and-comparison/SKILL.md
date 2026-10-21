---
name: buyer-brief-and-comparison
description: Turn a buyer or tenant conversation into a structured requirement brief, then compare shortlisted properties side by side with a clear recommendation. Use when an agent has notes on what a client wants or has two or more properties to compare.
---

# Buyer brief and property comparison

## Part 1: requirement brief
Ask for or extract from notes:
- Buy or rent, budget range (and loan or cash), possession timeline
- Locations in order of preference and why (office, school, family)
- Must-haves vs nice-to-haves (BHK, floor, facing, parking, ready-to-move vs under-construction)
- Deal-breakers

Output a one-page brief: Summary line, Must-haves, Nice-to-haves, Deal-breakers, Budget, Open questions to ask the client.

## Part 2: comparison
Input: 2 to 5 properties with whatever details the agent has.
1. Build a table with rows: price, area (state carpet vs super built-up), price per sq ft, location, age or possession date, floor, amenities, maintenance, deposit/EMI estimate if asked.
2. Mark missing cells `[unknown]`. Never guess.
3. Score each property against the brief's must-haves (yes/partial/no), then add a short pros and cons list.
4. Give one recommendation with 3 reasons and what to verify before the client commits.

## Maths helpers (show the formula)
- Price per sq ft = price / chosen area
- EMI = P x r x (1+r)^n / ((1+r)^n - 1), r = monthly rate, n = months. Label results as estimates and ask for the client's actual rate.

## Guardrails
- Be neutral. Present trade-offs; do not push the highest-commission property.
- No investment return promises.
- Point out the verification steps from the `property-due-diligence-checklist` skill for the shortlisted property.
