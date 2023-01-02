# Day 7: No Space Left On Device
# https://adventofcode.com/2022/day/7

# Straight-forward simulation of the commands with a small trick to ignore some
# parts of the input that are not necessary for the solution. This assumes that
# the input will never have the same file listed twice.

import collections, itertools

cwd = ["/"]
sizes = collections.defaultdict(int)
for line in open(0):
    match line.strip().split():
        case "$", "cd", "/":
            cwd = ["/"]
        case "$", "cd", "..":
            cwd.pop()
        case "$", "cd", dir:
            cwd.append(dir + "/")
        case size, _ if size not in ("$", "dir"):
            for path in itertools.accumulate(cwd):
                sizes[path] += int(size)

print(sum(s for s in sizes.values() if s <= 100000))
print(min(s for s in sizes.values() if s >= sizes["/"] - 40000000))
