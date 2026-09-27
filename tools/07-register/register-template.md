# Register entry

Anything not declared here is denied.

| # | Field | Entry |
| --- | --- | --- |
| 1 | Identity and purpose | Name, version, the team it serves, the workflow |
| 2 | May read, call, write | Everything else is denied |
| 3 | Must never | What it must never do or infer |
| 4 | Grade | Observe, Recommend, Prepare or Act. Per market or team if they differ |
| 5 | Supervisor | One named person. Never a team or a role title |
| 6 | Model per step | Which model does which step, and why (tool 9) |
| 7 | Test set | Which set, which version, last score (tool 5) |
| 8 | Cost and health | Cost per run · exception rate · drift since last promotion |
| 9 | History | Every change of grade or permission, with the date and who decided |
| 10 | Flags | Customers told? · where data is kept · how long records are kept |

## Rules

- Any change to fields 2 or 3 is a new version. It goes back to Observe and earns its grade again.
- A new model in field 6 is re-tested against field 7 before the agent keeps its grade. If it fails, it goes back to Observe.
- **Small team:** look at the whole register together once a month.
- **Large business:** once a quarter, lay it out as agents down the side and markets across the top, with the grade in each cell. That's the board's picture.

## A worked example

What a filled-in page looks like. Copy the table above, not this one.

| # | Field | Entry |
| --- | --- | --- |
| 1 | Identity and purpose | Renewal prep agent, v3. Commercial team, contract renewals workflow. Gathers usage and flags likely changes before each contract renewal |
| 2 | May read, call, write | Reads usage data and contract history. Writes a draft renewal pack. Nothing else |
| 3 | Must never | Contact a customer. Infer anything about a named person |
| 4 | Grade | Recommend: a person decides on every pack. In a large business it can differ by market, for example Recommend in the UK and Observe in Germany |
| 5 | Supervisor | A named person on the commercial team (in your register, their name) |
| 6 | Model per step | A small model for extraction. The best available for the clause flags, because a missed clause is costly |
| 7 | Test set | Renewals v2: 41 past renewals with the right flags marked. Last score 94% |
| 8 | Cost and health | Cost per renewal pack, exception rate and drift since last promotion, filled in from your own figures |
| 9 | History | v2 went back to Observe after a pricing change touched its inputs. v3 promoted to Recommend after six weeks at Observe |
| 10 | Flags | Customers told that renewal packs are drafted with AI · data stays in region · records kept two years |

