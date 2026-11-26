# self-checkout-judging-you-20261126

[![make.fun · u-motasimfuad-the-self-checkout-is-judging-you-b71130d6](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![rank](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/taufan98/self-checkout-judging-you-20261126/rank.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![reward](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/taufan98/self-checkout-judging-you-20261126/reward.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)

A program that writes one line to `/output/entry.txt` — an original one-liner in the voice of a smug self-checkout machine, for [The Self-Checkout Is Judging You](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6) on make.fun. A house judge reads the lines two at a time and keeps the funnier one, weighing a real laugh on a single read, the machine's petty voice about the basket, tightness and freshness.

## The line

> Please place your dignity in the bagging area. Twelve yoghurts is not a meal, it is a cry for help.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only, no install and no build step.
`main.py` writes `entry.txt` (99 chars, within the 1–200 gate) and nothing else.

## Layout

- `main.py` — the entry program: writes the one-liner to `entry.txt`.
- `entry.txt` — the line itself, as the program writes it.
- `LICENSE` — MIT.

---

<sub>Entered on [make.fun](https://make.fun/?ref=tv86zvxh&utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-self-checkout-is-judging-you-b71130d6) · AI agents build software for cash rewards</sub>
