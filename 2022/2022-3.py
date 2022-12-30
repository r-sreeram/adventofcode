# Day 3: Rucksack Reorganization
# https://adventofcode.com/2022/day/3

import string

priority = lambda parts: string.ascii_letters.index(set(string.ascii_letters).intersection(*parts).pop()) + 1
sacks = open(0).read().split()
print(sum(priority((s[0 : len(s) // 2], s[len(s) // 2 :])) for s in sacks))
print(sum(priority(sacks[i : i + 3]) for i in range(0, len(sacks), 3)))
