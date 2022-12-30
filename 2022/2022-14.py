# Day 14: Regolith Reservoir
# https://adventofcode.com/2022/day/14

# Inspired by 4HbQ: https://www.reddit.com/r/adventofcode/comments/zli1rd/2022_day_14_solutions/j061f6z/

import itertools, re

grid = set()
for points in ((int(x) + int(y) * 1j for x, y in re.findall("(\d+),(\d+)", line)) for line in open(0)):
    for p1, p2 in itertools.pairwise(points):
        grid.update(itertools.takewhile(lambda p: p != p2, itertools.count(p1, (p2 - p1) / abs(p2 - p1))))
    grid.add(p2)
start, floor = len(grid), max(p.imag for p in grid)

part1, path = 0, [500]
while path:
    try:
        while path[-1].imag <= floor:
            path.append(next(p for d in (1j, -1 + 1j, 1 + 1j) if (p := path[-1] + d) not in grid))
        else:
            part1 = len(grid) - start if part1 == 0 else part1
    except StopIteration:
        pass
    grid.add(path[-1])
    del path[-1]
print(part1)
print(len(grid) - start)
