---
type: Workflow
title: "Payment Change Verification"
description: "Holds every request to change payment instructions until it is verified by a call-back to a known number."
generated: { by: process:analyze, at: 2026-11-18T18:00:00Z }
status: in-production
execution_mode: augmented
autonomy: deterministic
trigger: "When a request to change payment instructions arrives"
stale_after: 2027-02-15
---
Flags any request to change bank details, holds it, and lists the call-back steps a staff member must complete before anyone acts on it.

# Insights

<!-- GENERATED:insights -->
<!-- /GENERATED -->
