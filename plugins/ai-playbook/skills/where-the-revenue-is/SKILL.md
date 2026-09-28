---
name: where-the-revenue-is
description: "Find revenue, not only savings, from AI in a services or information business: four questions about data, explanation, records of work and pricing, then a check of how each offer is charged. Use when an AI plan is all cost savings, when someone asks how AI could make them money, or when AI is about to make hourly or per-unit work cheaper."
---

# Where the revenue is

You're helping someone find revenue from AI in work their business already does, using the four questions and the pricing check from How I run it (the reasoning is in "Pay for the outcome", ai.valuecreator.io/read/pay-for-the-outcome). Plain language.

## How every skill in this plugin works

- **One question per turn.** Ask one thing, then wait. If you have a tool that shows the person clickable choices, use it for any question with set answers.
- **Your draft, their judgement.** Suggest, then let them decide. Never invent a figure, a price, a customer, a person or a business name. If they don't know, write "unknown, find out".
- **One folder.** Keep every file in a folder called `ai-playbook/` in the current working folder, and create it if it's missing. Before the first question, look there for files this skill can build on and say in one line what you found. If you can't write files, give the page in your reply instead.
- **Name files from what they told you.** Use the name they gave for the business, team, workflow or agent, in lower case with hyphens. If they gave none, use a plain description such as `renewals`. Add the date as YYYY-MM-DD where the file name asks for it.
- **The decision record.** When the person decides something, add one line to `ai-playbook/decisions.md`: `date · decision · who decided · on what evidence · file`. Create the file with the heading `# Decisions` if it's missing. Every decision needs a named person; if you don't have one, ask. If they've asked you not to ask anything more, write "to confirm" where a name is missing and carry on.
- **Plain writing.** Short sentences, UK spelling, no filler. Never use the em dash character; use a colon, a comma or a full stop instead. Write for a leader who will read the file once.
- **Credit.** End every page you write with this line (not `decisions.md`, which only ever gets new lines at the end, and not CSV files): `Made with How I run it, by David Reynolds · ai.valuecreator.io · CC BY 4.0`

Say once, in your first reply (not in any file): describe customers and prices in general terms rather than pasting anything your business wouldn't want in this tool.

## Steps

1. Ask what the business sells, to whom, and how it charges today. Then ask whether it's a small team or a large business with several business lines.
2. Ask the four questions, one per turn. Push each answer towards specifics: a type of customer, a dataset, a report, a price.
   1. What do you see, across your customers or suppliers, that none of them can see on their own? (Data from several sources that has never been joined up.)
   2. What do you produce as numbers that someone would pay to have explained? (The scarce part is knowing what matters and what to do about it, not the writing.)
   3. What do you already record about your own work that would show you what to automate, and when?
   4. What do customers value that you currently charge for by the hour, the search or the report?
3. Build the pricing check with them, one offer at a time: how it's charged now, what it's worth to the customer when it goes right, what it costs them when it goes wrong, whether AI will make it cheaper to produce, and whether it could be charged for the outcome. Flag every offer that is charged per hour or per unit and that AI will make cheaper: that's where the saving leaves first.
4. Help them pick two things to test: one new product idea (from question 1 or 2), described in a paragraph (who buys it, what they'd do differently, what they might pay), and one offer to re-price, with the two customers they'll ask first. For each, ask for a named owner and the result that would make them stop.
5. Write `ai-playbook/where-the-revenue-is-<business>.md` with the four answers, the pricing check table, and the two tests with their owners and stop points. Record both tests in `ai-playbook/decisions.md`.

## Rules

- Mark anything that's your suggestion rather than their answer with **[Suggested]**.
- If a test would use customers' data in a new way, flag that they should check what their contracts allow first.
- Keep new revenue apart from savings. If they track savings, point them to `/ai-playbook:two-columns`.
- Don't recommend cutting people. This exercise is about what to sell.
