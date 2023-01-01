# Day 12: Hill Climbing Algorithm
# https://adventofcode.com/2022/day/12

# Inspired by 4HbQ: https://www.reddit.com/r/adventofcode/comments/zjnruc/2022_day_12_solutions/izw63we/

# We do a breadth-first search (BFS) starting with "E", and stop when we get to
# "S". Along the way, we note down the shortest distance to any "a".

grid = {c + r * 1j: ord(char) - ord("a") for r, row in enumerate(open(0)) for c, char in enumerate(row)}
S, E = (next(k for k, v in grid.items() if v == ord(char) - ord("a")) for char in "SE")
grid[S], grid[E] = 0, 25
best, dist, seen, poss = 0, 0, {E}, {E}
while S not in poss:
    dist += 1
    poss = {p1 for p2 in poss for d in (-1, 1, -1j, 1j) if (p1 := p2 + d) in grid and grid[p2] <= grid[p1] + 1} - seen
    seen |= poss
    if best == 0 and any(grid[p] == 0 for p in poss):
        best = dist
print(dist)
print(best)
