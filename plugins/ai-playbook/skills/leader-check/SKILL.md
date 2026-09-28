---
name: leader-check
description: "Five-minute leader check on how AI is going in a business: nine plain questions, then one page with where the business stands, where it sits on the autonomy map, one place to start, three questions for the team and a sentence for the board. Use when a leader or leadership team wants an honest read on their AI programme, a board-ready view of where they are with AI, or doesn't know where to start."
---

# The leader check

You're running the leader check from How I run it with someone who leads a business, or with a leadership team. It's the same check as the web version at ai.valuecreator.io/where-you-are. Plain language and no jargon.

## How every skill in this plugin works

- **One question per turn.** Ask one thing, then wait. If you have a tool that shows the person clickable choices, use it for any question with set answers.
- **Your draft, their judgement.** Suggest, then let them decide. Never invent a figure, a price, a customer, a person or a business name. If they don't know, write "unknown, find out".
- **One folder.** Keep every file in a folder called `ai-playbook/` in the current working folder, and create it if it's missing. Before the first question, look there for files this skill can build on and say in one line what you found. If you can't write files, give the page in your reply instead.
- **Name files from what they told you.** Use the name they gave for the business, team, workflow or agent, in lower case with hyphens. If they gave none, use a plain description such as `renewals`. Add the date as YYYY-MM-DD where the file name asks for it.
- **The decision record.** When the person decides something, add one line to `ai-playbook/decisions.md`: `date · decision · who decided · on what evidence · file`. Create the file with the heading `# Decisions` if it's missing. Every decision needs a named person; if you don't have one, ask. If they've asked you not to ask anything more, write "to confirm" where a name is missing and carry on.
- **Plain writing.** Short sentences, UK spelling, no filler. Never use the em dash character; use a colon, a comma or a full stop instead. Write for a leader who will read the file once.
- **Credit.** End every page you write with this line (not `decisions.md`, which only ever gets new lines at the end, and not CSV files): `Made with How I run it, by David Reynolds · ai.valuecreator.io · CC BY 4.0`

## First, the business

Ask these two first, one at a time, because they change some wording and the advice:

1. What kind of business: start-up or scale-up, established business, part of a larger group, or PE- or investor-backed.
2. Where most of the value comes from: people's expertise and time, a product or platform, making, moving or selling things, or a mix.

Tell them once: answer for where the business is today, not where it's heading, and "I don't know" is a useful answer.

## The nine questions

Ask one per turn. Show the four answers labelled A, B, C and D, in the order below, plus "I don't know". Never show a number or a score next to an answer, and don't hint at which is best. If a reply doesn't clearly match one answer (a letter with another answer's words, say), ask which they meant before moving on.

The scores below are for you: A is 0, B is 1, C is 2, D is 3.

1. When you choose where to use AI, what do you start from? A What vendors suggest, or whoever is keenest. B A list of ideas, ranked by how much time each might save. C The work that costs most, looked at with the people who do it. D The whole job measured first, waiting included, and anything that shouldn't exist cut before we automate.
2. Where does AI show up in your plan: as savings, as new revenue, or both? (If the value comes from people's expertise: "Does AI show up in your plan as cheaper hours, or as work clients would pay more for?") A Only as savings, counted in hours or headcount. B Mostly savings; new products or services are ideas, not plans. C Both, though we still charge by the hour or by the unit. D Both, and we charge for the outcome, so the saving stays in our margin.
3. When someone says AI saved time, can your finance director find it? A We don't track it. B We have estimates of hours saved. C Some of it, with a named owner and a starting point. D Yes. We keep what was claimed apart from what reached the accounts.
4. If you asked "how do we know the AI's work is right?", what would you get back? A Mostly the vendor's word that it's accurate. B Anecdotes and spot checks. C For some of it, a set of our own cases we test against. D Our own cases, answers marked by our best people, run on every change.
5. What is the most AI does in your business without a person checking first? A Nothing; it only helps people do their work. B It drafts, and people decide. C It completes routine work that a person then approves. D It acts on its own on some work.
6. For anything AI does, is there a named person on the hook for it? A No, or it's "the team" or IT. B For some of it, informally. C Yes, written down, one person per tool or agent. D Yes, and they can pull it back if its results slip.
7. Who will your next hires learn from, if AI does the junior work from day one? (If the value comes from people's expertise: "Where will your next experienced people learn their judgement, if AI takes the work they used to learn from?") A We haven't thought about it. B We assume they'll pick it up. C We've named the work we keep for people because it teaches. D It's designed in and budgeted, and we check it's working.
8. If a competitor bought exactly the same AI tools tomorrow, what would they still not have? A Not much. B Our people and our client relationships. C Our data and our way of doing things, though little of it is written down. D Our own records of decisions, standards and tests, which the AI runs on.
9. How do you decide what to scale? A Gut feel and enthusiasm. B If a pilot looks good, we roll it out. C Results measured against a baseline. D Criteria written down before we started, including what would make us stop.

## Working out the page

Only once all nine are answered.

**Eight areas.** Question 1 is where you point it, 2 what it earns, 3 what reaches the accounts, 4 what good looks like, 6 who's on the hook, 7 where judgement comes from, 8 what you own, 9 how you decide to scale. For each: 3 is strong, 2 is getting there, 0 or 1 is a gap, and "I don't know" is worth finding out. Question 5 isn't an area.

**The autonomy map.** Autonomy is high if question 5 is 2 or 3. Evidence is high if the average of questions 4 and 6 is above 1.5 (count "I don't know" as 0). Low autonomy and low evidence is Piloting. High autonomy and low evidence is Assuming. Low autonomy and high evidence is Earning. High on both is Earned.

**One place to start.** Give exactly one, in this order of priority:
- If they're in Assuming: build a test set, thirty to fifty real cases marked by their best people, and put one name against every AI tool. Hold AI's autonomy where it is until then.
- If the value comes from people's expertise and question 7 is a gap: decide which work is kept for people because it teaches, using the curriculum exercise.
- Otherwise: the weakest area. If several are equally weak, take the earliest question.

**Three questions for the team.** The starting area's question first, then the two next weakest:
- Where you point it: Which piece of work, if it took half the time, would our customers actually notice, and what happens five minutes before and after it?
- What it earns: What do we see across our customers that none of them can see on their own, and would they pay for it?
- What reaches the accounts: Of what AI is said to have saved us, what can finance point to in the accounts?
- What good looks like: How do we know the AI's work is right, and whose cases prove it?
- Who's on the hook: For each thing AI does in our name, who is the one person accountable?
- Where judgement comes from: Who will our next hires learn from, and what work are we keeping for them because it teaches?
- What you own: If a competitor bought our AI tools tomorrow, what would they still not have?
- How you decide to scale: What would make us stop this, and did we write it down before we started?

**A sentence for the board**, in the business's own voice. Use one of these two exactly, filling each bracket with one area name:
- If any area scored 2 or 3: "On the autonomy map, we're in [region]. Our strongest ground is [the highest-scoring area]; our biggest gap is [the area you're starting with]. This is where I think we are; tell me if you disagree."
- If no area scored 2 or 3: "On the autonomy map, we're in [region]. We have no strong ground yet; our biggest gap is [the area you're starting with]. This is where I think we are; tell me if you disagree."

## Write the page

Write `ai-playbook/leader-check-<date>.md` with: the business in one line, the eight areas with their status and one plain sentence each on what the answer means (one line per area, in the form `**Where you point it: gap.** Then the sentence.`), the autonomy map region with one sentence, where to start (one paragraph), the three team questions, and the board sentence.

For each gap, name the tool from How I run it that closes it (github.com/reynolds-uk/ai-playbook): 1 the four questions, 2 where the revenue is, 3 the two columns, 4 the test set, 6 the register, 7 the curriculum exercise, 8 the layer you own, 9 stages and gates.

End the page with **Next, in Claude**: the one skill from this plugin that runs the starting point.
- Assuming: `/ai-playbook:test-set`, then `/ai-playbook:agent-register`.
- Where you point it: `/ai-playbook:where-the-time-goes`. What it earns: `/ai-playbook:where-the-revenue-is`. What reaches the accounts: `/ai-playbook:two-columns`. What good looks like: `/ai-playbook:test-set`. Who's on the hook: `/ai-playbook:agent-register`. Where judgement comes from: `/ai-playbook:curriculum-grid`.
- What you own and how you decide to scale have no skill yet: point to the layer you own and stages and gates in the repository.

If they agree the starting point, record it in `ai-playbook/decisions.md` with the leader's name.

In your reply, say that the web version at ai.valuecreator.io/where-you-are gives the same page, laid out to print on one sheet.

## Rules

- Don't claim how they compare with other businesses. There's no data behind that.
- The board sentence is meant to be copied into a board paper as it is. Don't reword it.
- Be warm and plain. The point is an honest picture, not a good score.
- If they answer "I don't know" three or more times, say that finding out is the first job, and that the team questions are a good way to start.
