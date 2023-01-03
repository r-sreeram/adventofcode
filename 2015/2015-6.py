# Day 6: Probably a Fire Hazard
# https://adventofcode.com/2015/day/6

import itertools, re


def solve(ops, instructions=list(open(0))):
    lights = [[0] * 1000 for _ in range(1000)]
    for line in instructions:
        command = line[: line.index(" ", 5)]
        r1, c1, r2, c2 = (int(n) for n in re.findall("\d+", line))
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                lights[r][c] = ops[command](lights[r][c])
    print(sum(itertools.chain(*lights)))


solve({"turn on": lambda n: 1, "turn off": lambda n: 0, "toggle": lambda n: 1 - n})
solve({"turn on": lambda n: n + 1, "turn off": lambda n: max(n - 1, 0), "toggle": lambda n: n + 2})
