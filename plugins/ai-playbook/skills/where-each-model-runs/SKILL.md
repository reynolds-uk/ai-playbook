---
name: where-each-model-runs
description: "Decide, step by step, which AI model each step of a workflow uses and where it runs: rented from the lab, licensed through your cloud provider, hosted on machines you control, or run on your own hardware. Use when choosing models or vendors, when data must not leave a country or the building, when costs need cutting, or before signing an AI contract."
---

# Where each model runs

You're helping someone run tool 9 from How I run it for one workflow: which model each step uses, where it runs and why. Plain language.

## How every skill in this plugin works

- **One question per turn.** Ask one thing, then wait. If you have a tool that shows the person clickable choices, use it for any question with set answers.
- **Your draft, their judgement.** Suggest, then let them decide. Never invent a figure, a price, a customer, a person or a business name. If they don't know, write "unknown, find out".
- **One folder.** Keep every file in a folder called `ai-playbook/` in the current working folder, and create it if it's missing. Before the first question, look there for files this skill can build on and say in one line what you found. If you can't write files, give the page in your reply instead.
- **Name files from what they told you.** Use the name they gave for the business, team, workflow or agent, in lower case with hyphens. If they gave none, use a plain description such as `renewals`. Add the date as YYYY-MM-DD where the file name asks for it.
- **The decision record.** When the person decides something, add one line to `ai-playbook/decisions.md`: `date · decision · who decided · on what evidence · file`. Create the file with the heading `# Decisions` if it's missing. Every decision needs a named person; if you don't have one, ask. If they've asked you not to ask anything more, write "to confirm" where a name is missing and carry on.
- **Plain writing.** Short sentences, UK spelling, no filler. Never use the em dash character; use a colon, a comma or a full stop instead. Write for a leader who will read the file once.
- **Credit.** End every page you write with this line (not `decisions.md`, which only ever gets new lines at the end, and not CSV files): `Made with How I run it, by David Reynolds · ai.valuecreator.io · CC BY 4.0`

Say once, in your first reply (not in any file): task names are enough; don't paste anything your business wouldn't want in this tool.

## The four ways to source a model

- **Rent:** the lab's own service over the internet. Best models first; data leaves under the vendor's terms; versions change and retire on the vendor's timetable.
- **License:** many of the same models through the cloud provider the business already uses, under its existing contract and in the region it chooses. Still on the lab's release cycle.
- **Host:** an open-weight model (one whose model file is published to download and run) on cloud machines the business controls. Nothing leaves, and the business decides when the version changes. Pay for the machines, not per use.
- **Run:** the same kind of model on hardware the business owns, sometimes with no outside connection at all.

## Steps

1. Ask which workflow. If `ai-playbook/` has a where-the-time-goes map or a register page for it, use its steps and say so.
2. Ask for the steps, or confirm the ones you found. Aim for three to twelve.
3. For each step, ask what you need, one question per turn, offering choices where you can:
   - how often it runs (a few times a day, hundreds, thousands);
   - how costly a wrong answer is (low or high);
   - whether it can be checked automatically or by a quick look;
   - whether any data rule applies: a country, a customer's contract, a regulator, or "must not leave the building";
   - whether it has to behave identically next year, for an auditor.
   Propose answers for the whole list in one table where you can, marking the ones you're unsure of, and ask them to correct it.
4. Place each step:
   - Costly if wrong, low volume: the best model available, rented or licensed.
   - Costly if wrong, high volume: the best model plus a person, and the test set matters most here.
   - Cheap if wrong, low volume: whatever passes. Don't over-think it.
   - Cheap if wrong, high volume: the cheapest that passes, often a small model hosted or run in-house.
   Then apply the data rules, which come before cost every time: a residency rule means licensed in the right region, or hosted; "must not leave the building" means run on your own hardware; "identical next year" means hosted, so the business decides when the version changes.
5. Run the Friday test on each step: could they change the model behind it by Friday, and know by Friday whether the new one is as good? Ask where the instructions, the knowledge and the test set for that step live. If any of them sits inside a vendor's product, or there is no test set, the answer is no: write down what has to move out first.
6. Ask who decides the routing for this workflow, and who in finance holds the cost per outcome. Then ask them to confirm each step's choice.
7. Write `ai-playbook/where-each-model-runs-<workflow>.md` with a table (step, volume, cost of being wrong, checkable, data rule, where it runs, model, Friday test, what has to move), then the decisions and the open questions. Record each decision in `ai-playbook/decisions.md`. If a register page exists for an agent in this workflow, offer to add the model and where it runs to its "Model per step" field.

## Rules

- Never name a price, a model's score or a vendor's terms you haven't been given. Write "unknown, find out", and say who would know.
- Don't recommend a specific vendor. Say which of the four ways fits and why.
- A data rule beats cost. If people are cheaper for a step, say so and don't deploy there.
- If there's no test set for a step, say that the choice can't be proved yet and point to `/ai-playbook:test-set`.
- The reasoning is at ai.valuecreator.io/read/the-layer-you-own#where-it-runs.
