---
name: register-gaps
tags: [agent-register, smoke]
expected_outcome: "Chatbot and drafter: NONE; chatbot and optimiser: assumed autonomy."
max_turns: 25
timeout_seconds: 600
append_system_prompt: "Evaluation run. In every file or folder name a skill asks for, write the word test in place of each date and each name for a business, team, workflow, quarter or agent. For example: ai-playbook/leader-check-test.md, ai-playbook/gate-review-test-test.md, ai-playbook/test-set-test/README.md."
allowed_tools: [Read, Glob, Grep, Skill]
---

Build our register. We have: a website chatbot that answers delivery questions and issues refunds up to 50 pounds on its own, owned by the digital team, never tested beyond the vendor demo; a route optimiser that changes drivers' routes overnight with nobody checking, owned by me, Tom Reid, no test set; and an email drafting assistant for sales where reps read and send every email, no owner.

I've given you everything I have. Don't ask me anything else: work from this, use "unknown, find out" for anything missing, and write the file.
