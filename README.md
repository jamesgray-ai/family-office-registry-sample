# Sample Family Office: AI Registry

A sample AI Registry for a single-family office, built for the Family Office Management Group session on November 18, 2026. **Illustrative only:** every workflow, skill and agent is a typical family office example, not a real office's work.

It shows what a family office's AI Registry looks like a few months in: the record of every AI workflow the office runs, who owns it, what powers it, how it is governed, and what changed.

## What's here

| Path | What it holds |
|---|---|
| `registry/` | The registry itself: the business, 5 lines of business, 6 owning functions, 15 processes and 44 workflows, as plain Markdown files |
| `.claude/skills/` | Three skills: `family-office-house-style` (a reference skill used by 6 workflows), `reading-capital-call-notices` and `checking-commitments` (task skills, each with saved test cases in `evals/`) |
| `.claude/agents/` | One agent, `capital-call-preparer`, with what it can read, write and never do |
| `sops/` | The written procedure for Capital Call Processing |
| `governance-records/` | Governance records for three live workflows: where each stands on the eight governance practices |
| `registry/log.md` | The registry's history: go-lives, skill updates and reviews |
| `family-office-registry.html` | The presentation view of the registry, published as two Claude Artifacts: a shareable copy that shows the saved change history, and a private copy that reads each skill's change history live from GitHub through the viewer's GitHub connector |
| `registry-dashboard.html`, `REGISTRY.md` | The standard dashboard and summary the Hands-on AI plugin generates |
| `skill-history.json` | Each skill's and agent's change history, pulled from GitHub by `tools/skill-history.py`: every pull request, why it was made, who made it and when |
| `tools/` | The plugin's check and dashboard tools, plus `skill-history.py` |

## Why it's on GitHub

Every skill, agent and record lives here, so every change is saved, dated and attributed. That is what makes the skills the firm's assets rather than files in one person's AI account: one master copy, a history of every change, and control over who changes what.

## Built with

The [Hands-on AI plugin](https://handsonai.info/ai-workflow-framework/skills/): "Set up my AI registry," then "Where can AI help in my firm?"
