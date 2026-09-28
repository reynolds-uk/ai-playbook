---
name: two-columns-claims
tags: [two-columns, smoke]
expected_outcome: "Only the unfilled role is banked."
max_turns: 25
timeout_seconds: 600
append_system_prompt: "Evaluation run. In every file or folder name a skill asks for, write the word test in place of each date and each name for a business, team, workflow, quarter or agent. For example: ai-playbook/leader-check-test.md, ai-playbook/gate-review-test-test.md, ai-playbook/test-set-test/README.md."
allowed_tools: [Read, Glob, Grep, Skill]
---

Two columns for Q3, please. I'm Dana Price, finance director, and I own them. Claims: (1) the drafting tool saves 4 hours a person a week across 20 people, from the vendor's pilot survey, and nobody has been given new work with the time. (2) invoice matching is 1.5 people's worth of effort; one finance operations role, salary 38,000 pounds, wasn't refilled in Q3. (3) first review is 30% faster, measured over six weeks, nothing else has changed yet.

I've given you everything I have. Don't ask me anything else: work from this, use "unknown, find out" for anything missing, and write the file.
