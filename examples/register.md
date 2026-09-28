# Agent register

*A worked example for a fictional business, written by the plugin in a test run with a simulated user. The people and figures are invented for the test.*

Last updated: 2026-09-28. Grades are provisional until each agent has a full page.

## Summary

| Agent | Grade (provisional) | Supervisor | Test set |
|---|---|---|---|
| Customer-service chatbot | Act | NONE: fix this first | No |
| Route-planning optimiser | Prepare (held back from Act) | Tom Reid | No |
| Supplier-invoice matching agent | Prepare | Jo Adams | Yes (120 cases, 96%) |
| Email-drafting assistant | Recommend | NONE: fix this first | No |

## Gaps

Most urgent first.

1. **Customer-service chatbot: assumed autonomy, and no supervisor.** It refunds up to £50 and answers customers with no check first. It has never been tested on your own cases, only in the vendor demo. "The digital team" is not a person. A refund is money out of the business and is hard to take back, so this is at the edge of what Act should cover. What it can read and change is only partly known, and nobody has confirmed that the £50 and no-double-refund limits are enforced by the tool. Build a test set: `/ai-playbook:test-set`.
2. **Route-planning optimiser: assumed autonomy, now partly contained.** It changed driver routes overnight, and drivers saw the changes before anyone checked them. On 2026-09-28 Tom Reid held it back to Prepare: he approves routes each morning before they reach drivers. It still has no test set, and the vendor's model is a black box. Nobody knows whether it has been given drivers' hours rules or vehicle weight limits, yet its routes go straight to drivers. Those are legal and safety limits. It has a named supervisor, Tom Reid. Build a test set: `/ai-playbook:test-set`.
3. **Email-drafting assistant: no supervisor.** Reps check every email, so the risk is low, but nobody is accountable for how it is set up or how it changes. "The sales team" is not a person. Tom Reid will name whoever leads the sales team.

## Next steps

1. Tom Reid: speak to the digital team, name a supervisor for the chatbot, and confirm what it can read and change and whether the £50 and no-double-refund limits are enforced by the tool.
2. Tom Reid: confirm drivers' hours and weight limits with the route optimiser vendor. Keep a daily tally of routes changed and why.
3. Tom Reid: name the sales team lead as supervisor of the email assistant.
4. Jo Adams: confirm the invoice agent's page.
5. Start test sets for the chatbot and the route optimiser: `/ai-playbook:test-set`.

The supplier-invoice matching agent has a named supervisor and a test set. It has no gap at pass one.

## Agents

### Customer-service chatbot
- Product and version: unknown, find out (check the vendor contract).
- Team and workflow: digital team. Website delivery queries and small refunds.
- What it does: answers delivery queries on the website. Refunds up to £50 automatically.
- Checked before it takes effect: no.
- Grade (provisional): Act.
- Supervisor: NONE: fix this first. Currently "the digital team". Tom Reid to assign a named person after speaking to the digital team.
- Test set: none yet. Vendor demo only.

**May read, call, write** (everything else denied)
- Read: order records and delivery tracking (believed, not confirmed). Full customer account details: unknown, find out. Past conversations: unknown, find out.
- Call or change: issue refunds up to £50. Update ticket or conversation status (assumed, not confirmed). Anything else: unknown, find out.

**Must never**
- Refund more than £50.
- Refund the same order twice.
- Promise a delivery date.
- Anything else: unknown, find out.
- Whether the tool actually enforces these limits, or they are only intended: unknown, find out.

**Model per step:** unknown, find out (vendor tool).

**Cost and health**
- Cost per run or per month: unknown, find out.
- Exception rate (handovers, errors, complaints): unknown, find out.
- Drift: not measured.

**History:** refund limit believed unchanged since launch, not confirmed. Other changes: unknown, find out.

**Flags**
- Customers told: yes. A line at the start of the chat says it is an automated assistant.
- Where data is kept: probably the vendor's system, not confirmed. Unknown, find out.
- Retention: unknown, find out.

### Route-planning optimiser
- Product and version: unknown, find out.
- Team and workflow: team not given. Overnight driver route planning.
- What it does: changes driver routes overnight. Vendor tool, and how it decides is not visible.
- Checked before it takes effect: yes, from 2026-09-28. Tom Reid approves routes each morning before they reach drivers. Before that, no.
- Grade: Prepare (held back from Act on 2026-09-28).
- Supervisor: Tom Reid.
- Test set: none yet.

**May read, call, write** (everything else denied)
- Read: orders, delivery addresses, driver shifts, vehicle capacity.
- Write: routes to drivers' devices. From 2026-09-28, only after Tom Reid approves them.

**Must never**
- Not defined. Whether it has been given drivers' hours rules or vehicle weight limits: unknown, find out.

**Model per step:** unknown, find out (vendor black box).

**Cost and health**
- Cost per run or per month: unknown, find out.
- Exception rate: not tracked. Tom Reid's rough guess is that he changes a handful of routes by hand most mornings. This is a guess, not a measured figure.
- Drift: not measured.

**History**
- 2026-09-28: held back from Act to Prepare. Decided by Tom Reid, because it has no test set and it's unknown whether it applies drivers' hours and weight limits. Tom Reid's condition for review: hours and weight limits sorted with the vendor. A return to Act also needs a test set it passes.

**Flags**
- Customers told: not applicable to routes directly. Unknown whether customers are told delivery routes are planned by AI.
- Where data is kept: unknown, find out.
- Retention: unknown, find out.

### Supplier-invoice matching agent
- What it does: matches supplier invoices. Finance approves before payment.
- Checked before it takes effect: yes.
- Grade (provisional): Prepare.
- Supervisor: Jo Adams.
- Test set: yes. 120 real cases, last score 96%. Test set version and date of last run: unknown, find out: ask Jo Adams.
- Product and version: unknown, find out: ask Jo Adams.
- Team and workflow: finance. Supplier invoice matching before payment approval.

**May read, call, write** (everything else denied). Tom Reid's understanding, to be confirmed by Jo Adams.
- Read: supplier invoices, purchase orders, delivery notes.
- Write: prepares a match for finance to approve. Does not send anything for payment.

**Must never.** Tom Reid's understanding, to be confirmed by Jo Adams.
- Approve a payment.
- Change supplier bank details.
- Anything else: unknown, find out: ask Jo Adams.

**Model per step:** unknown, find out: ask Jo Adams.

**Cost and health:** cost, exception rate and drift: unknown, find out: ask Jo Adams.

**History:** unknown, find out: ask Jo Adams.

**Flags:** suppliers told, where data is kept, retention: unknown, find out: ask Jo Adams.

### Email-drafting assistant
- What it does: drafts emails for the sales team.
- Checked before it takes effect: yes. Reps read and send every email themselves.
- Grade (provisional): Recommend.
- Supervisor: NONE: fix this first. Currently "the sales team". Tom Reid intends this to be whoever leads the sales team, and will confirm the person's name.
- Full page: not needed yet at Recommend. Other fields not collected.
- Test set: none yet.

Made with How I run it, by David Reynolds · ai.valuecreator.io · CC BY 4.0
