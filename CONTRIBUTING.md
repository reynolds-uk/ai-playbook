# Helping with the playbook

Thank you for looking. The most useful thing you can do is try one tool on real work and tell me what happened. The second most useful is to change a file so it works better, and send the change.

## Tell me how a tool worked

[Open an issue](https://github.com/reynolds-uk/ai-playbook/issues/new?template=i-used-a-tool.md). Say which tool, whether you're a small team or a large business, what you changed to make it fit, and what didn't work. A sentence each is plenty. Nothing confidential, please.

## Suggest a change

For anything bigger than a typo, [open an issue first](https://github.com/reynolds-uk/ai-playbook/issues/new?template=suggest-a-change.md) so we can agree what the change should be. Then send a pull request.

What makes a change easy to accept:

- **One change per pull request.** A new question for the self-check and a fix to the register template are two pull requests.
- **Plain English.** Short sentences, no jargon, UK spelling. Every tool is read by leaders as well as builders, so the README in each tool folder should make sense to someone who will never open the working files.
- **Sized for both.** Where the advice differs for a team of five and a group of five thousand, say so under **Small team** and **Large business**, the way the other files do.
- **From real use.** Say where the change came from: the business, the kind of team, what went wrong before. I'll take a change from one real team over a good idea nobody has tried.
- **Judgement stays with people.** The tools help a business decide. They don't decide for it, and the skills don't invent anyone's numbers.

## Changing the Claude plugin

The plugin is in `plugins/ai-playbook`. Each skill is one `SKILL.md` file. If you change or add one:

1. Check it still loads: `claude plugin validate .` and `claude plugin validate plugins/ai-playbook`.
2. Run the test set from `plugins/ai-playbook`: `claude plugin eval . --allow-tools Write Edit --scaffold`. Every case must pass. If you change a case, say why in the pull request.
3. If you're fixing something a skill got wrong, add a case for it first, and show it failing before your change and passing after.
4. Install your copy and run the skill once on a real example: `claude plugin marketplace add ./` then `claude plugin install ai-playbook@ai-playbook`. Say in the pull request what you ran it on and what the file it wrote looked like.
5. Raise `version` in `plugins/ai-playbook/.claude-plugin/plugin.json`, or people who already have the plugin won't get the change.

Skills should ask one thing at a time, suggest rather than decide, never invent a figure or a name, and write into the `ai-playbook/` folder. The block headed "How every skill in this plugin works" is the same in every skill; change it in all of them or none. Update [REGISTER.md](plugins/ai-playbook/REGISTER.md) if a skill's permissions, rules or test cases change.

## Licence

The playbook is [CC BY 4.0](LICENSE). By sending a change, you agree it's shared under the same licence, credited as part of *How I run it*.
