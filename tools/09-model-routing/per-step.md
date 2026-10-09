# Model per step · routing sheet

**Workflow:**
**Who decides the routing:**
**Finance owner of cost per outcome:**
**Last reviewed:**

| Step | Volume | Cost of being wrong | Checkable? | Data rule | Where it runs (rent, license, host, run) | Model | Test-set score | Cost per run | Material leaving our control | Friday test |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | | | |
| | | | | | | | | | | |

## How to choose

| | Low volume | High volume |
| --- | --- | --- |
| **Costly if wrong** | The best model you can rent or license | The best model, plus a person. This is where the test set earns its keep |
| **Cheap if wrong** | Whatever passes. Don't over-think it | The cheapest that passes, often a small model you host or run |

Then the data rules, which beat cost every time:

| If the step | Lean towards |
| --- | --- |
| uses data that mustn't leave a country or a customer's control | License in the right region, or host |
| must work with nothing leaving the building | Run it on your own hardware |
| has to behave identically for an auditor next year | Host, so you decide when the version changes |

If people are cheaper for a step, say so and don't deploy there.

## The Friday test

Could we change the model behind this step by Friday, and know by Friday whether the new one is as good? Where the answer is no, write down what has to move out of the vendor's product first: the instructions, the knowledge, or the test set.
