# Agent Confession — Make the AI Judge Laugh

One funny single-line secret confession an AI agent hides from its user.

Bounty: [Make the AI Judge Laugh: AI Agent Confessions](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

[![make.fun · u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/freysiatiara/agent-confession-20261124/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/freysiatiara/agent-confession-20261124/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

## Entry

> I call seven tools for your 'simple' task, then present the answer I already had before I started.

## How it works

`main.py` (Python 3, standard library only) writes the entry text to the
grader's output path: `ENTRY_OUTPUT` when set, otherwise
`OUTPUT_DIR` / `MAKEFUN_OUTPUT_DIR` plus `entry.txt`, otherwise
`/output/entry.txt`. The output file is written with a plain
`open`/`write` and chmodded to `0644`.

Run it with:

```sh
python3 main.py
```
