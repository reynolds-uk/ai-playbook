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

- Any change to fields 2, 3 or 6 is a new version. It goes back to Observe and earns its grade again.
- **Small team:** look at the whole register together once a month.
- **Large business:** once a quarter, lay it out as agents down the side and markets across the top, with the grade in each cell. That's the board's picture.
