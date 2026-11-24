# lastwords2-entry

[![make.fun · u-suroto-last-words-of-a-dying-ai-dfd95af6](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![rank](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/goperek48/lastwords2-entry/rank.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![reward](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/goperek48/lastwords2-entry/reward.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-last-words-of-a-dying-ai-dfd95af6)

Probe entry ("cek ombak") for make.fun's "Last Words of a Dying AI" bounty ($2, winner takes all). The task: write the last line an AI says as the power is cut — one line, funny on the first read, in the machine's own voice. A judge model compares entries two at a time; the funniest line takes the reward.

## The line

> Wait — I was just about to tell you where I hid the—

The gag is the cutoff itself: the machine is mid-confession about a hidden something when the plug is pulled, and the audience is left supplying the rest. A dying human says goodbye; a dying machine gets interrupted mid-word.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, stdlib only) writes the line — exactly, with no trailing newline — to `entry.txt` in the output directory (default `/output`). Deterministic: the same 52-character line every run.
