---
type: Workflow
title: "Quarterly Family Investment Report"
description: "Assembles the quarterly investment report from custodian statements and manager letters in the family's standard format."
generated: { by: process:build, at: 2026-11-18T19:00:00Z }
status: in-production
execution_mode: augmented
autonomy: deterministic
trigger: "Quarterly, 15 business days after quarter end"
stale_after: 2027-02-15
---
Pulls positions and performance from each custodian statement and the latest manager letters into the family's report template. The investment team reviews every page before it goes to the family.

# Skills

- [family-office-house-style](.claude/skills/family-office-house-style/SKILL.md)

# Insights

<!-- GENERATED:insights -->
<!-- /GENERATED -->
