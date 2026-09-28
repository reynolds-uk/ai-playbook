# Where the time goes: commercial policy renewals

*A worked example for a fictional business, written by the plugin in a test run with a simulated user. The people and figures are invented for the test.*

Date: 2026-09-28
Owner: Mark Ellis, operations director
Done by: 8 account handlers

## The four questions

**Job to be done.** Make sure the client has the right cover at the right price for another year, with no gap when the old policy expires. Keep a record of why we recommended what we did, in case anyone ever asks.

**Pain removed.** For the handler, the renewal is off their plate and stops chasing them. For the client, it removes the worry of a gap in cover, or of finding out too late that they are underinsured.

**Gain created.** Faster turnaround, so renewals are not left until just before expiry. Less compliance risk because the file is tidier. Handler time freed up for talking to clients about cover rather than admin.

**Five minutes before and after.** Before: the renewal date in the system triggers a report 60 days out. After: the client signs the new policy, we invoice, and the file is marked renewed.

## Before, work and after

| Stage | What happens | Time |
|---|---|---|
| Before | Renewal date triggers a report 60 days out | 0 min |
| Work | Handler work across all steps | about 90 min |
| After | Client signs, invoice, file marked renewed | unknown, find out |
| End to end | Trigger to file marked renewed | about 11 days |

## The share

The work is 90 minutes of 11 days. That is about 0.6% of calendar time, or about 1.8% of working time if we assume 7.5-hour days (an assumption, not a measured figure).

This is far below a quarter. **The prize is in the waiting, not the work.** Speeding up the 90 minutes will barely change the 11 days. The gains come from shrinking the waits on clients, insurers and sign-off.

## Sorted steps

### Delete

| # | Step | Time | Why |
|---|---|---|---|
| 1 | Renewal report generates | 0 min | Nobody reads it. It may be a system default nobody switched off. Let the renewal date trigger step 2 directly. **Check first:** find out whether anything or anyone relies on the report before switching it off. |

### Automate (each starts at Observe)

| # | Step | Time | Why |
|---|---|---|---|
| 2 | Email client for updated info | 10 min | Routine and easy to check. Send on day 60, pre-filled with last year's details for the client to confirm or change. |
| 4 | First chase | 5 min | A reminder on a fixed schedule. It needs no judgement. |
| 5 | Second chase | 5 min | As step 4. After this, the handler picks up the phone. |
| 6 | Check info is complete, ask for gaps | rework, unknown, find out | Completeness can be checked against a list. Check on arrival and ask for gaps the same day. |
| 7 | Key info into 3 insurer portals | about 30 min | Can't be deleted: each insurer requires its own portal. Key once and let software fill all three. Ask insurers whether they accept bulk or API submissions (unknown, find out). |
| 12 | Send recommendation to client | 5 min | Sends on sign-off. |
| 13 | Invoice and mark file renewed | unknown, find out | Routine, triggered by the client's signature. |

### Augment (software drafts, a person decides)

| # | Step | Time | Why |
|---|---|---|---|
| 9 | Compare quotes | 15 min | Software lays out price and cover side by side. Judging cover differences is the handler's call. |
| 10 | Write recommendation letter | 15 min | The letter must exist under FCA rules. It is the judgement and the compliance record. Software drafts, the handler decides and owns the reasons. |
| 11 | Team leader sign-off | minutes of work | Kept by internal policy (believed not to be an FCA requirement; confirm). Software prepares the file and flags anything unusual, and the team leader decides. Because it is our own policy, we could later limit it to riskier renewals. |

### Waits to shrink

| After step | Wait | Time | How to shrink it |
|---|---|---|---|
| 2 | Client responds | unknown, find out | Shorter, pre-filled request. |
| 4, 5 | Client responds after each chase | unknown, find out | Chase on a fixed schedule, then phone. |
| 6 | Client fills gaps | unknown, find out | Ask for gaps the same day the info arrives. |
| 7 | Insurer quotes | a few days, unknown, find out | Starts sooner if steps 2 to 7 finish sooner. |
| 11 | Sign-off sits in inbox | about 2 days | Time-box it and chase automatically. |
| 12 | Client signs | unknown, find out | Measure first. |

## Next steps

1. **Write stop criteria before building.** For each automated step, decide in advance what result would make us stop or roll it back. For example, the wrong details pre-filled for a client, or a chase sent after the client has already replied.
2. **Take a baseline.** Measure the waits marked "unknown, find out" on current renewals, starting with the client's reply time, quote turnaround and signature time. Without a baseline, we can't show that anything improved.

For every Automate step, build a test set first with `/ai-playbook:test-set`. An agent at Prepare or Act without one has assumed its autonomy, not earned it.

Made with How I run it, by David Reynolds · ai.valuecreator.io · CC BY 4.0
