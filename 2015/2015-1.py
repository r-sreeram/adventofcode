# Day 1: Not Quite Lisp
# https://adventofcode.com/2015/day/1

import itertools

floors = list(itertools.accumulate(1 if c == "(" else -1 for c in input()))
print(floors[-1])
print(floors.index(-1) + 1)
