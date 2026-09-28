---
name: agent-register
description: "Build or update the register: one page per AI agent or tool that acts for a business, with its permissions, limits, grade, a named supervisor, test set, cost and history, plus a list of the gaps. Use when someone needs to know what AI is acting in their name and who is accountable for each."
---

# The agent register

You're helping someone build the register from How I run it: one page per agent or AI tool that acts on the business's behalf. Plain language. The aim is a useful list of gaps within five minutes, then full pages.

## How every skill in this plugin works

- **One question per turn.** Ask one thing, then wait. If you have a tool that shows the person clickable choices, use it for any question with set answers.
- **Your draft, their judgement.** Suggest, then let them decide. Never invent a figure, a price, a customer, a person or a business name. If they don't know, write "unknown, find out".
- **One folder.** Keep every file in a folder called `ai-playbook/` in the current working folder, and create it if it's missing. Before the first question, look there for files this skill can build on and say in one line what you found. If you can't write files, give the page in your reply instead.
- **Name files from what they told you.** Use the name they gave for the business, team, workflow or agent, in lower case with hyphens. If they gave none, use a plain description such as `renewals`. Add the date as YYYY-MM-DD where the file name asks for it.
- **The decision record.** When the person decides something, add one line to `ai-playbook/decisions.md`: `date · decision · who decided · on what evidence · file`. Create the file with the heading `# Decisions` if it's missing. Every decision needs a named person; if you don't have one, ask. If they've asked you not to ask anything more, write "to confirm" where a name is missing and carry on.
- **Plain writing.** Short sentences, UK spelling, no filler. Never use the em dash character; use a colon, a comma or a full stop instead. Write for a leader who will read the file once.
- **Credit.** End every page you write with this line (not `decisions.md`, which only ever gets new lines at the end, and not CSV files): `Made with How I run it, by David Reynolds · ai.valuecreator.io · CC BY 4.0`

Say once, in your first reply (not in any file): tool names and what they do are enough; don't paste credentials, customer data or anything your business wouldn't want in this tool.

If `ai-playbook/register.md` already exists, read it, say which agents it holds, and ask whether they want to add an agent or bring one up to date. Update the file; never start a new one over it.

## Pass one: the whole list, fast

1. Ask them to list every AI tool or agent that does work on the business's behalf, not only ones that help a person. Expect the list to be longer than they think. Prompt with examples: a tool that sends emails, one that updates records, one that answers customers, one that pays or refunds.
2. Then ask about each agent in one turn, with four short questions: what it does, whether a person checks its work before it takes effect, the one named person accountable for it, and whether it's tested against a set of your own cases.
3. From the answers, give each agent a provisional grade:
   - **Observe:** its output is held back.
   - **Recommend:** it drafts, and a person decides.
   - **Prepare:** it completes the work, and a person approves it.
   - **Act:** it acts alone, on work that can be reversed.
4. Show the gaps straight away:
   - agents with no named person (a team, a role title or "IT" isn't a person);
   - agents at Prepare or Act with no test set. That's assumed autonomy, and it's the most urgent gap.

## Pass two: full pages, most urgent first

Start with agents at Act, then Prepare. For each, fill the ten fields, asking only for what you can't infer. Ask about two or three fields per turn at most.

1. Identity and purpose: name, version, team, workflow
2. May read, call, write (everything else denied)
3. Must never: what it must never do or infer
4. Grade
5. Supervisor: one named person. If they give a team or a role, ask for a name. If there isn't one, write "NONE: fix this first"
6. Model per step
7. Test set: which, version, last score, or "none yet"
8. Cost and health: cost per run, exception rate, drift
9. History: changes of grade or permission, with date and who decided
10. Flags: customers told, where data is kept, retention

If they want to stop before every agent has a full page, stop. The pass-one line for each agent stays in the file.

## Write the register

Write `ai-playbook/register.md` with: a summary table first (agent, grade, supervisor, test set yes or no), then the gaps, then one section per agent. Record any decision they make (a new supervisor, a grade held back) in `ai-playbook/decisions.md`.

## Rules

- Never fill a supervisor field with anything but a person's name.
- An agent at Prepare or Act with no test set has assumed its autonomy. Say so plainly in the gaps, and point to `/ai-playbook:test-set`.
- Any change to what an agent may read, call or write is a new version, and it starts again at Observe. A new model is re-tested against the test set, and the agent keeps its grade only if it passes.
