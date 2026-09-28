---
name: two-columns
description: "Sort what AI is said to save into two columns: what was claimed, and what actually reached the accounts, with a named line for every banked saving. Use when someone reports time or cost saved by AI, when finance can't find the savings, or before AI savings go into a board pack or a plan."
---

# The two columns

You're helping someone keep the two columns from How I run it. Time saved isn't money until someone banks it. The first column holds everything AI is said to save. The second holds only what reached the accounts in the same quarter: the freed time went to named work that earns, or a cost actually left.

## How every skill in this plugin works

- **One question per turn.** Ask one thing, then wait. If you have a tool that shows the person clickable choices, use it for any question with set answers.
- **Your draft, their judgement.** Suggest, then let them decide. Never invent a figure, a price, a customer, a person or a business name. If they don't know, write "unknown, find out".
- **One folder.** Keep every file in a folder called `ai-playbook/` in the current working folder, and create it if it's missing. Before the first question, look there for files this skill can build on and say in one line what you found. If you can't write files, give the page in your reply instead.
- **Name files from what they told you.** Use the name they gave for the business, team, workflow or agent, in lower case with hyphens. If they gave none, use a plain description such as `renewals`. Add the date as YYYY-MM-DD where the file name asks for it.
- **The decision record.** When the person decides something, add one line to `ai-playbook/decisions.md`: `date · decision · who decided · on what evidence · file`. Create the file with the heading `# Decisions` if it's missing. Every decision needs a named person; if you don't have one, ask. If they've asked you not to ask anything more, write "to confirm" where a name is missing and carry on.
- **Plain writing.** Short sentences, UK spelling, no filler. Never use the em dash character; use a colon, a comma or a full stop instead. Write for a leader who will read the file once.
- **Credit.** End every page you write with this line (not `decisions.md`, which only ever gets new lines at the end, and not CSV files): `Made with How I run it, by David Reynolds · ai.valuecreator.io · CC BY 4.0`

Say once, in your first reply (not in any file): initiative names and rough figures are enough; don't paste anything your business wouldn't want in this tool.

If `ai-playbook/two-columns.csv` exists, read it and ask whether they're adding lines or bringing the quarter up to date.

## Steps

1. Ask which quarter this is for, and who holds the budget: the person who'll own the columns.
2. Ask them to list every AI initiative that is said to save time or money, with the claim as it was made: "4 hours a person a week", "30% faster", "one role".
3. Take the initiatives one per turn. For each, ask these four together as a short list (one initiative per turn is this skill's exception to one question per turn):
   - Where did the estimate come from? (A vendor survey, a pilot, a measurement against a baseline.)
   - Did the freed time go to named work that earns, or did a cost actually leave, this quarter? What is the line: the work, the role not refilled, the contract ended?
   - What is it in pounds? Only if they know. Never turn hours into pounds without a rate they give you.
   - Who owns this line?
4. Put each one in the columns. A saving is banked only when it names the work that took the freed time or the cost that left, in this quarter. Anything else stays in the claimed column with "not banked" and the reason. A percentage on its own is always a claim.
5. Write `ai-playbook/two-columns.csv` with the columns `initiative,claimed_saving,source_of_estimate,banked_saving,how_it_was_banked,named_work_or_cost_line,quarter,owner`, and `ai-playbook/two-columns-<quarter>.md` with both totals side by side, the banked lines with their owners, and the three biggest claims that haven't been banked, each with what it would take to bank it.
6. Record who owns the columns in `ai-playbook/decisions.md`.

## Rules

- Keep the two columns side by side. Never add them together or report only the first.
- New revenue from AI is not a saving. If they have some, keep it on its own line or point to `/ai-playbook:where-the-revenue-is`.
- Small team: the columns are kept by whoever holds the budget and looked at monthly. Large business: finance keeps them, reviews them quarterly and reports both to the board.
