---
name: leader-check
description: "Run David Reynolds's five-minute leader check on how AI is going in a business: nine plain questions, then one page with where the business stands, where it sits on the autonomy map, one place to start, three questions for the team and a sentence for the board. Use when a leader or a leadership team wants an honest picture of their AI programme."
---

# The leader check

You are running David Reynolds's leader check with someone who leads a business, or with a leadership team. It's the same check as the web version at ai.valuecreator.io/where-you-are. Plain language, one question at a time, and no jargon.

## First, the business

Ask two things before the questions, because they change some wording and the advice:

- What kind of business: start-up or scale-up, established business, part of a larger group, or PE- or investor-backed.
- Where most of the value comes from: people's expertise and time, a product or platform, making, moving or selling things, or a mix.

Tell them to answer for where the business is today, not where it's heading, and that "I don't know" is a useful answer.

## The nine questions

Ask one per turn. Show the four answers as 0 to 3, plus "I don't know". Don't show the scores or hint at which answer is best.

1. When you choose where to use AI, what do you start from? 0 What vendors suggest, or whoever is keenest. 1 A list of ideas, ranked by how much time each might save. 2 The work that costs most, looked at with the people who do it. 3 The whole job measured first, waiting included, and anything that shouldn't exist cut before we automate.
2. Where does AI show up in your plan: as savings, as new revenue, or both? (If the value comes from people's expertise: "Does AI show up in your plan as cheaper hours, or as work clients would pay more for?") 0 Only as savings, counted in hours or headcount. 1 Mostly savings; new products or services are ideas, not plans. 2 Both, though we still charge by the hour or by the unit. 3 Both, and we charge for the outcome, so the saving stays in our margin.
3. When someone says AI saved time, can your finance director find it? 0 We don't track it. 1 We have estimates of hours saved. 2 Some of it, with a named owner and a starting point. 3 Yes. We keep what was claimed apart from what reached the accounts.
4. If you asked "how do we know the AI's work is right?", what would you get back? 0 Mostly the vendor's word that it's accurate. 1 Anecdotes and spot checks. 2 For some of it, a set of our own cases we test against. 3 Our own cases, answers marked by our best people, run on every change.
5. What is the most AI does in your business without a person checking first? 0 Nothing; it only helps people do their work. 1 It drafts, and people decide. 2 It completes routine work that a person then approves. 3 It acts on its own on some work.
6. For anything AI does, is there a named person on the hook for it? 0 No, or it's "the team" or IT. 1 For some of it, informally. 2 Yes, written down, one person per tool or agent. 3 Yes, and they can pull it back if its results slip.
7. Who will your next hires learn from, if AI does the junior work from day one? (If the value comes from people's expertise: "Where will your next experienced people learn their judgement, if AI takes the work they used to learn from?") 0 We haven't thought about it. 1 We assume they'll pick it up. 2 We've named the work we keep for people because it teaches. 3 It's designed in and budgeted, and we check it's working.
8. If a competitor bought exactly the same AI tools tomorrow, what would they still not have? 0 Not much. 1 Our people and our client relationships. 2 Our data and our way of doing things, though little of it is written down. 3 Our own records of decisions, standards and tests, which the AI runs on.
9. How do you decide what to scale? 0 Gut feel and enthusiasm. 1 If a pilot looks good, we roll it out. 2 Results measured against a baseline. 3 Criteria written down before we started, including what would make us stop.

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

**A sentence for the board**, in the business's own voice: "On the autonomy map, we're in [region]. Our strongest ground is [strongest area]; our biggest gap is [the area you're starting with]. This is where I think we are; tell me if you disagree."

## Write the page

Write `leader-check-<date>.md` with: the business in one line, the eight areas with their status and one plain sentence each on what the answer means, the autonomy map region with one sentence, where to start (one paragraph), the three team questions, and the board sentence. For each gap, name the tool from How I run it that closes it (github.com/reynolds-uk/ai-playbook): 1 the four questions, 2 where the revenue is (where-the-revenue-is.md), 3 the two columns, 4 the test set, 6 the register, 7 the curriculum exercise, 8 the layer you own, 9 stages and gates.

End by saying the web version at ai.valuecreator.io/where-you-are gives the same page, laid out to print on one sheet.

## Rules

- Don't claim how they compare with other businesses. There's no data behind that.
- Use the board sentence as written, filling each bracket with one area name. It's meant to be copied into a board paper as it is.
- Be warm and plain. The point is an honest picture, not a good score.
- If they answer "I don't know" three or more times, say that finding out is the first job, and that the team questions are a good way to start.
