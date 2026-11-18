---
okf_version: "0.2"
---
# AI Registry

Your operations knowledge bundle: how your business runs. See [SCHEMA](/SCHEMA.md) for types and rules.
The dashboard view is the generated root `REGISTRY.md`.

## Concepts

- [Businesses](/businesses/index.md) — the traversal root: identity + curated line-of-business order
- [Lines of Business](/lines-of-business/index.md) — each orders its processes in value-chain order
- [Functions](/functions/index.md) — cross-cutting ownership areas processes map into
- [Processes](/processes/index.md) — business processes grouping workflows
- [Workflows](/workflows/index.md) — the hub: one node per business workflow
- [Notes](/notes/index.md) — synthesized operational insights

<!-- GENERATED:skills -->
## Skills inventory (3)
- [checking-commitments](.claude/skills/checking-commitments/SKILL.md) — Checks a capital call against the family's commitment schedule for that fund, confirming the amount fits the unfunded commitment and the entity has the cash. Use after a capital call notice has been read and before a payment is prepared. (used by: [Capital Call Processing](registry/workflows/capital-call-processing.md))
- [family-office-house-style](.claude/skills/family-office-house-style/SKILL.md) — The Sample Family Office's house style for anything the family reads, such as reports, briefing packets, summaries and minutes. Use whenever drafting or reviewing a document for the family or its committees, so every document reads the same way whoever prepared it. (used by: [Capital Call Processing](registry/workflows/capital-call-processing.md), [Family Meeting Briefing Packet](registry/workflows/family-meeting-briefing-packet.md), [Investment Committee Packet](registry/workflows/investment-committee-packet.md), [Manager Letter Summaries](registry/workflows/manager-letter-summaries.md), [Meeting Minutes and Action Tracking](registry/workflows/meeting-minutes-and-action-tracking.md), [Quarterly Family Investment Report](registry/workflows/quarterly-family-investment-report.md))
- [reading-capital-call-notices](.claude/skills/reading-capital-call-notices/SKILL.md) — Reads a private fund's capital call notice and extracts the fund, investing entity, amount, due date and wire instructions into a standard record. Use when a capital call notice arrives, before anything is checked or paid. (used by: [Capital Call Processing](registry/workflows/capital-call-processing.md))
<!-- /GENERATED -->

<!-- GENERATED:agents -->
## Agents inventory (1)
- [capital-call-preparer](.claude/agents/capital-call-preparer.md) — Prepares each capital call for the Controller's approval. Reads the notice, checks it against the commitment schedule and cash, and drafts the payment. Cannot release a payment. (used by: [Capital Call Processing](registry/workflows/capital-call-processing.md))
<!-- /GENERATED -->
