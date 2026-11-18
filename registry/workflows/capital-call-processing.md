---
type: Workflow
title: "Capital Call Processing"
description: "Reads each capital call notice, checks it against the commitment, and prepares the payment for approval."
generated: { by: process:build, at: 2026-11-18T19:00:00Z }
status: in-production
execution_mode: augmented
autonomy: guided
trigger: "When a capital call notice arrives"
stale_after: 2027-02-15
---
Matches each notice to the right fund and entity, checks the amount against the remaining commitment, and prepares the wire for a person to approve. No money moves without that approval.

# Artifacts

- [SOP](sops/capital-call-processing-sop.md)

# Skills

- [reading-capital-call-notices](.claude/skills/reading-capital-call-notices/SKILL.md)
- [checking-commitments](.claude/skills/checking-commitments/SKILL.md)
- [family-office-house-style](.claude/skills/family-office-house-style/SKILL.md)

# Agents

- [capital-call-preparer](.claude/agents/capital-call-preparer.md)

# Insights

<!-- GENERATED:insights -->
<!-- /GENERATED -->
