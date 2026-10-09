# The layer you own

How I'd put AI into a business that runs on judgement and data, whether it sells advice, insurance, data or software. The reasoning is in [The layer you own](https://ai.valuecreator.io/read/the-layer-you-own), and the pictures are free to use from [ai.valuecreator.io/pictures](https://ai.valuecreator.io/pictures#services-architecture).

## In plain terms

Every competitor can get the same models, and they get better and cheaper every few months. So the model shouldn't be where your advantage lives. For each step of the work, choose the model that suits that step: rented, licensed, hosted or run on your own machines. Then own the three things every model plugs into: a connected picture of the business, a register of what's running, and a test set of your own cases. Own those, and changing a model becomes a setting rather than a project.

## The four layers

| Layer | What it is | Source or own |
| --- | --- | --- |
| **Source** | The models, rented, licensed, hosted or run, step by step. Swap them when something better or cheaper passes your tests | Source |
| **Route** | Each step to the cheapest model that passes, in the place its data rules allow. Hard judgement to the best | Own the rules |
| **Run** | Agents, each built once as a template and deployed as numbered versions (for example intake, research, drafting, quality check, reporting), all on the register | Build or buy the agents, own the register |
| **Own** | The knowledge graph (customers, work, people, rules, documents, decisions), the register and the test set | Own |

Underneath: your systems of record stay where they are, connected rather than replaced.

## Rent, license, host or run

| If the step | Lean towards |
| --- | --- |
| needs the best judgement available, and runs a few times a day | Rent or license the best model |
| uses data that mustn't leave a country or a customer's control | License in the right region, or host |
| runs thousands of times a day and can be checked | Host a small model, or the cheapest that passes |
| must work with nothing leaving the building | Run it on your own hardware |
| has to behave identically for an auditor next year | Host, so you decide when the version changes |

[Tool 9](../tools/09-model-routing/) has the routing sheet.

## The model is a plug; the layer is the socket

Keep the instructions in your own version control, the knowledge in your own picture of the business, and the standard of a good answer in your own test set. Then run the Friday test on each step: could we change the model behind it by Friday, and know by Friday whether the new one is as good? If not, you're renting more than the model.

## Always a person

Taking on a new customer, signing off advice, approving a claim or a loan, anything a customer will rely on without checking it themselves. The machine prepares. The person decides.

## Build once, configure, promote independently

Build each workflow agent once. Put the differences between teams or countries in the knowledge graph as configuration, including which models a market may use. Let each deployment earn its own grade, so the same agent can act on its own in one place while it's still recommending in another.

## Where to start

One workflow, one team, end to end. If you can bring one customer's history together from the systems it's scattered across inside eight weeks, the graph is real. Write down, for each step, which model it uses, where it runs and why, and run the Friday test on one of them. Put one agent on the register at Observe, publish the criteria it has to meet, measure before and after, and decide in the room whether to carry on.
