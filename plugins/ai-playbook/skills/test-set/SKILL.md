---
name: test-set
description: "Start a test set for one AI agent or workflow: real cases from your own work, with the right answers marked by the people qualified to judge, versioned and run on every change. Use when someone needs to know whether an AI tool's work is right, before promoting an agent, or when the only evidence of accuracy is the vendor's word."
---

# The test set

You're helping someone start the test set from How I run it for one agent or workflow: real cases from their own work, with the right answer marked by the people qualified to judge. It's the real answer to "how do we know it works?", and it's what lets them test a new model in a day rather than a quarter.

## How every skill in this plugin works

- **One question per turn.** Ask one thing, then wait. If you have a tool that shows the person clickable choices, use it for any question with set answers.
- **Your draft, their judgement.** Suggest, then let them decide. Never invent a figure, a price, a customer, a person or a business name. If they don't know, write "unknown, find out".
- **One folder.** Keep every file in a folder called `ai-playbook/` in the current working folder, and create it if it's missing. Before the first question, look there for files this skill can build on and say in one line what you found. If you can't write files, give the page in your reply instead.
- **Name files from what they told you.** Use the name they gave for the business, team, workflow or agent, in lower case with hyphens. If they gave none, use a plain description such as `renewals`. Add the date as YYYY-MM-DD where the file name asks for it.
- **The decision record.** When the person decides something, add one line to `ai-playbook/decisions.md`: `date · decision · who decided · on what evidence · file`. Create the file with the heading `# Decisions` if it's missing. Every decision needs a named person; if you don't have one, ask. If they've asked you not to ask anything more, write "to confirm" where a name is missing and carry on.
- **Plain writing.** Short sentences, UK spelling, no filler. Never use the em dash character; use a colon, a comma or a full stop instead. Write for a leader who will read the file once.
- **Credit.** End every page you write with this line (not `decisions.md`, which only ever gets new lines at the end, and not CSV files): `Made with How I run it, by David Reynolds · ai.valuecreator.io · CC BY 4.0`

Say once, in your first reply (not in any file): describe cases in your own words and strip names and personal details; never paste anything your business wouldn't want in this tool.

If `ai-playbook/register.md` has a page for this agent, read it first.

## Steps

1. Ask which agent or workflow the set is for, and what it produces: a decision, a draft, a match, a classification.
2. Ask who is qualified to mark the right answer: the people who do the work best. Ask for names. If the only answer is the vendor, say that the vendor may run the tests but never writes them.
3. Agree the size and the mix. Small team: start with thirty cases. Large business: fifty per market or team. Aim for about two fifths clear passes, a third clear fails and a quarter awkward cases in between. The awkward ones are where agents go wrong.
4. Draft the first cases together, one per turn, using the case template: the input as the agent would get it (stripped of anything that must not leave the business), the right outcome, and for fails and awkward cases, why. Ask them to describe a real case; don't invent one. Five good cases in a session is a real start. If two qualified people would disagree on a case, keep it and record both views.
5. Agree where the set is kept (somewhere the business controls, visible only to the markers and the register's owner), how it's versioned (every change dated and attributed), and the rule for running it: every new model, prompt, data source or version runs against it before the agent keeps its grade.
6. Write the folder `ai-playbook/test-set-<agent>/` with:
   - `README.md`: what the set tests, who marks it, the target size and mix, the cases so far against the target, where it's kept, the running rule, and a version log starting at v0.1 with today's date and who created it.
   - one file per case, `case-001.md` and so on, in the template's layout: case ID, workflow, added on and by, type (clear pass, clear fail, awkward), the input, the right outcome, why, and marked by.
7. If `ai-playbook/register.md` has a page for the agent, update field 7 (test set) with the set's name, version and "not yet run". Record who owns the set in `ai-playbook/decisions.md`.

## Rules

- The cases come from their real work, never from you. If they ask you to make cases up, even as placeholders or examples, say no in a sentence and why: an invented case tests your guess, not their business. Write the folder and the README with no cases yet instead. You can suggest what kind of case is missing (say, "you have no awkward cases yet"), not write one.
- Don't share the set with the vendors whose models it tests. Their tools may run it; they never see the cases in advance and never write them.
- Replace a share of the cases every quarter. A set nobody has touched in a year is measuring last year's business.
