# Day 14: Regolith Reservoir
# https://adventofcode.com/2022/day/14

# Inspired by 4HbQ: https://www.reddit.com/r/adventofcode/comments/zli1rd/2022_day_14_solutions/j061f6z/

# Aside from the straight-forward simulation, a major optimization here is to
# start the next unit of sand at the last position of the previous sand (before
# it came to rest) instead of all the way back at the top, since it would have
# traversed the same path until that point anyway.

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
        # Two ways this loop stops:
        # (1) When the sand falls below the lowest rock, the loop condition is
        #     false, and the "else" clause is executed. Part 1's solution is the
        #     number of units of sand that have settled the first time this
        #     happens (= len(grid) - start if part1 == 0). Since there's an
        #     infinite floor right below this point, the sand will settle at
        #     this point anyway.
        # (2) When the sand is blocked by sand/rock at all three positions below
        #     it, next() can't find a match and raises StopIteration. The sand
        #     settles at this point.
        while path[-1].imag <= floor:
            path.append(next(p for d in (1j, -1 + 1j, 1 + 1j) if (p := path[-1] + d) not in grid))
        else:
            part1 = len(grid) - start if part1 == 0 else part1
    except StopIteration:
        pass
    grid.add(path.pop())
print(part1, len(grid) - start, sep="\n")
