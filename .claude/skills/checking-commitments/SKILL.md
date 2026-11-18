---
name: checking-commitments
description: Checks a capital call against the family's commitment schedule for that fund, confirming the amount fits the unfunded commitment and the entity has the cash. Use after a capital call notice has been read and before a payment is prepared.
---

# Checking Commitments

A task skill: confirm a capital call is expected and affordable before anyone prepares the payment.

## Steps

1. Find the fund and investing entity in the commitment schedule.
2. Check the call amount is no more than the unfunded commitment remaining.
3. Check the call against the fund's pacing; flag a call that is more than twice the average of the last four calls.
4. Check the entity's cash balance in today's Daily Cash Position covers the call.
5. Return one of: **Ready for approval**, **Ready with a note** (explain), or **Stop** (explain).

## Never

- Never mark a call "Ready for approval" if the amount exceeds the unfunded commitment.
- Never move or schedule money; this skill only checks.
