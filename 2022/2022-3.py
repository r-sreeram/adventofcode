# Day 3: Rucksack Reorganization
# https://adventofcode.com/2022/day/3

# The input is guaranteed to have exactly one letter common to all "parts"
# (for Part 1, the parts are the two halves of each line; for Part 2, the parts
# are groups of three lines). So, we can intersect the parts and blindly pop()
# an element from the resulting set (there should be exactly one element).

# We use string.ascii_letters for two purposes: (1) to find the index of the
# letter (to compute the "priority"), and (2) as a base for the intersection
# (otherwise, we'd have to explicitly create a set() from at least one part and
# then intersect with the rest of the parts, which is less elegant to code).

import string

priority = lambda parts: string.ascii_letters.index(set(string.ascii_letters).intersection(*parts).pop()) + 1
sacks = open(0).read().split()
print(sum(priority((s[0 : len(s) // 2], s[len(s) // 2 :])) for s in sacks))
print(sum(priority(sacks[i : i + 3]) for i in range(0, len(sacks), 3)))
