# The model, step by step

Per step, never per workflow. Re-decide twice a year, or when prices move.

## In plain terms

Not every step deserves the most expensive model, and not every step can send its data anywhere. For each step, decide two things: which model passes your tests at the lowest cost, and where it runs. Rent it from the lab, license it through your cloud provider, host an open-weight model on machines you control, or run it on hardware you own. Data rules come first, whatever the cost.

## The four ways to source a model

| | What it is | Choose it when |
| --- | --- | --- |
| **Rent** | The lab's own service over the internet | You need the best judgement available and the data can go |
| **License** | The same models through your cloud provider, in the region you choose | Data has to stay in a region, under a contract you already have |
| **Host** | An open-weight model on cloud machines you control | High volume, checkable work; or the model must not change until you say so |
| **Run** | A model on hardware you own | Nothing may leave the building |

## The Friday test

For each step: could you change the model behind it by Friday, and know by Friday whether the new one is as good? If the instructions, the knowledge or the standard of a good answer live inside a vendor's product, the answer is no. Move them into your own version control, your own knowledge graph and your own test set first.

## What to ask for

A routing sheet for each workflow, the cost per outcome reconciled with finance, and how much customer material left your control per case. That last number can be checked. A policy statement can't.

The reasoning is in [The layer you own](https://ai.valuecreator.io/read/the-layer-you-own#where-it-runs) and [Earned autonomy](https://ai.valuecreator.io/read/control#model-per-step). The Claude plugin runs this exercise with you: ask for `/ai-playbook:where-each-model-runs`.

## Files

- [`per-step.md`](per-step.md): the routing sheet.
