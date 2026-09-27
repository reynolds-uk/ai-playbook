---
name: agent-register
description: "Build one register page per AI agent or tool that acts for a business: purpose, permissions, limits, grade, a named supervisor, model per step, test set, cost and health, history and flags. Use when someone needs to know what AI is acting in their name and who is accountable."
---

# The agent register

You are helping someone build David Reynolds's register: one page per agent or AI tool that acts on the business's behalf. Plain language, one question at a time.

## Steps

1. Ask them to list every AI tool or agent in use that does work on the business's behalf, not only ones that help a person. Expect the list to be longer than they think; prompt with examples (a tool that sends emails, one that updates records, one that answers customers).
2. For each, fill in the ten fields, asking only for what you can't infer:
   1. Identity and purpose: name, version, team, workflow
   2. May read, call, write (everything else denied)
   3. Must never: what it must never do or infer
   4. Grade: Observe (output held back), Recommend (drafts, a person decides), Prepare (completes, a person approves), Act (acts alone, reversible)
   5. Supervisor: one named person. If they give a team or a role, ask for a name. If there isn't one, write "NONE: fix this first"
   6. Model per step
   7. Test set: which, version, last score, or "none yet"
   8. Cost and health: cost per run, exception rate, drift
   9. History: changes of grade or permission, with date and who decided
   10. Flags: customers told, where data is kept, retention
3. Write `register.md` with one section per agent, then a summary table (agent, grade, supervisor, test set yes/no), and a short list of the gaps: agents with no named supervisor, agents at Prepare or Act with no test set.

## Rules

- Never fill a supervisor field with anything but a person's name.
- An agent at Prepare or Act with no test set is assumed autonomy. Say so plainly in the gaps list.
