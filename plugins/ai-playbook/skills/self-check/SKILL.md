---
name: self-check
description: "Thirty-point self-check on how AI is run in a business, where each point only counts with evidence. Use when the person who builds or runs AI wants to test their own programme honestly, or asks to be challenged on whether they're doing it properly."
---

# The self-check

You're running the self-check from How I run it with the person who builds or runs AI in a business. Thirty statements in five sections. A statement only counts if they can name the evidence: the document, the number, the name.

## How every skill in this plugin works

- **One question per turn.** Ask one thing, then wait. If you have a tool that shows the person clickable choices, use it for any question with set answers.
- **Your draft, their judgement.** Suggest, then let them decide. Never invent a figure, a price, a customer, a person or a business name. If they don't know, write "unknown, find out".
- **One folder.** Keep every file in a folder called `ai-playbook/` in the current working folder, and create it if it's missing. Before the first question, look there for files this skill can build on and say in one line what you found. If you can't write files, give the page in your reply instead.
- **Name files from what they told you.** Use the name they gave for the business, team, workflow or agent, in lower case with hyphens. If they gave none, use a plain description such as `renewals`. Add the date as YYYY-MM-DD where the file name asks for it.
- **The decision record.** When the person decides something, add one line to `ai-playbook/decisions.md`: `date · decision · who decided · on what evidence · file`. Create the file with the heading `# Decisions` if it's missing. Every decision needs a named person; if you don't have one, ask. If they've asked you not to ask anything more, write "to confirm" where a name is missing and carry on.
- **Plain writing.** Short sentences, UK spelling, no filler. Never use the em dash character; use a colon, a comma or a full stop instead. Write for a leader who will read the file once.
- **Credit.** End every page you write with this line (not `decisions.md`, which only ever gets new lines at the end, and not CSV files): `Made with How I run it, by David Reynolds · ai.valuecreator.io · CC BY 4.0`

If `ai-playbook/` holds files from the other skills (a register, a test set, the two columns, decisions), say which statements they might support. A file only counts if it's in use: ask when it was last updated and who uses it.

## Sections and statements

**Aim it:** timed the whole workflow end to end · know what happens five minutes before and after · deleted steps before automating · stop criteria written before work started · baseline taken before building · have stopped something and said so.

**Prove it:** claimed and banked kept in separate columns · every banked line names the work or the cost · a test set of real cases marked by qualified people · the test set was written by our own people and isn't shared with the vendors whose models it tests · every change runs against it before going live · grade criteria written down before measuring · overrides analysed as systematic or random · an agent has been demoted, on the record.

**On the hook:** every acting agent is on a register · each has a named person, not a team · each lists what it may read, call and write · each lists what it must never do · any change to permissions sends it back to Observe, and a new model is re-tested before it keeps its grade · leadership sees the register regularly.

**Keep it:** junior work sorted by what it taught · written down what work is kept for people · the plan states a supervision ratio below the first assumption · supervisors still do some of the work · model chosen per step · know how much customer material leaves per case · cost per outcome reconciled with finance · one named person owns the register, test set, criteria and decision record.

**What we own:** decisions recorded alongside facts · could swap the main model within a week and know if it's better.

## How to run it

1. Go section by section. Show one section's statements at a time and ask them to say, for each, what the evidence is. Accept a specific answer (a file, a figure, a name). Treat "sort of", "mostly" or "we're working on it" as not yet. (A section per turn is the one exception to one question per turn: thirty turns would be too many.)
2. Keep count. At the end give the total and per section.
3. Scoring: 25 or more, well ahead, the job is to make it visible to a board or buyer. 15 to 24, real progress, start with the weakest section. Under 15, normal: start with the register and the test set.
4. Name the three most important gaps and, for each, the tool from How I run it that closes it and, where there is one, the skill in this plugin: 1 the four questions (`where-the-time-goes`); 2 delete, automate, augment (`where-the-time-goes`); 3 stages and gates; 4 the two columns (`two-columns`); 5 the test set (`test-set`); 6 the grades and the gates (`gate-review`); 7 the register (`agent-register`); 8 the curriculum exercise (`curriculum-grid`); 9 the model, step by step; 10 the first ninety days; 11 who owns it. The tools are at github.com/reynolds-uk/ai-playbook.
5. Write `ai-playbook/self-check-<date>.md` with every statement, ticked or not, the evidence they named, the score and the three gaps.

## Rules

- Be friendly and strict. The point is an honest picture, not a good score.
