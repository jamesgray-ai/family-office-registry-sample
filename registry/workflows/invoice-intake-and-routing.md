---
type: Workflow
title: "Invoice Intake and Routing"
description: "Sorts incoming invoices, codes each to the right entity and routes it for approval."
generated: { by: process:analyze, at: 2026-11-18T18:00:00Z }
status: in-production
execution_mode: automated
autonomy: guided
trigger: "When an invoice arrives in the bills inbox"
stale_after: 2027-02-15
---
Reads each invoice, codes it to the entity and expense category by the office's rules, and routes it to the approver for that entity. Anything that doesn't fit the rules goes to the controller.

# Insights

<!-- GENERATED:insights -->
<!-- /GENERATED -->
