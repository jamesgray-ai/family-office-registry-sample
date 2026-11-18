---
type: Workflow
title: "Daily Cash Position"
description: "Pulls balances across all accounts into one daily cash summary."
generated: { by: process:analyze, at: 2026-11-18T18:00:00Z }
status: in-production
execution_mode: automated
autonomy: deterministic
trigger: "Every business day, 8am"
stale_after: 2027-02-15
---
Collects the morning's balances from every bank and custodian account into a one-page summary for the controller.

# Insights

<!-- GENERATED:insights -->
<!-- /GENERATED -->
