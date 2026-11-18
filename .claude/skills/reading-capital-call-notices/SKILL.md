---
name: reading-capital-call-notices
description: Reads a private fund's capital call notice and extracts the fund, investing entity, amount, due date and wire instructions into a standard record. Use when a capital call notice arrives, before anything is checked or paid.
---

# Reading Capital Call Notices

A task skill: turn one capital call notice into one standard record.

## Steps

1. Identify the fund and the investing entity named on the notice. Match the entity to the office's entity register; if it doesn't match exactly, stop and flag it.
2. Extract: call amount, due date, purpose of the call (investment, fees, expenses), and the call number.
3. If the notice nets a distribution against the call, record the gross call, the distribution and the net amount due separately. The net amount is what gets paid; the gross call is what counts against the commitment.
4. Extract the wire instructions exactly as written. Never correct, complete or reformat them.
5. Compare the wire instructions with the instructions on file for this fund. If anything differs, mark the record **Instructions changed: verify by call-back** and stop.
6. Output the record in the format below.

## Output

| Field | Value |
|---|---|
| Fund | |
| Investing entity | |
| Call number | |
| Gross call (USD) | |
| Distribution netted (USD) | 0 if none |
| Net amount due (USD) | |
| Due date | |
| Purpose | |
| Wire instructions match file | Yes / No |

## Never

- Never prepare a payment from a notice whose wire instructions differ from the file.
- Never guess a missing field; mark it "Not on notice".
