# Day 10: Cathode-Ray Tube
# https://adventofcode.com/2022/day/10

# Inspired by 4HbQ: https://www.reddit.com/r/adventofcode/comments/zhjfo4/2022_day_10_solutions/izmspl7/

import itertools, lib.ocr

# We exploit the fact that the input tokens ('noop', 'addx', number) match up
# exactly with their clock cycles and with their respective effect on the value
# of X (treating non-numbers as adding 0 to X). We also add a couple of entries
# to the beginning of the sequence so that the index of an element matches the
# cycle _during_ which X's value is the element.

X = list(itertools.accumulate([0, 1] + [int(n) if n[-1].isdigit() else 0 for n in open(0).read().split()]))
print(sum(i * n for i, n in list(enumerate(X))[20::40]))
crt = ["".join("#" if abs(c - X[r * 40 + c + 1]) <= 1 else "." for c in range(40)) for r in range(6)]
print(*crt, sep="\n")
print("".join(lib.ocr.font6x4.get("".join(row[i : i + 4] for row in crt), "?") for i in range(0, 40, 5)))
