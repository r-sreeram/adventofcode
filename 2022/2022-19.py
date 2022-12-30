# Day 19: Not Enough Minerals
# https://adventofcode.com/2022/day/19

# Inspired by Boojum: https://www.reddit.com/r/adventofcode/comments/zpihwi/2022_day_19_solutions/j0tls7a/

import re

ORE, CLAY, OBSIDIAN, GEODE = 1, 2, 4, 8

# t = time remaining, goal = target robot types (bitmask)
# mineral amounts:  a=ore, b=clay, c=obsidian, d=geode
# number of robots: p=ore, q=clay, r=obsidian, s=geode
def solve(t, a=0, b=0, c=0, d=0, p=1, q=0, r=0, s=0, goal=ORE | CLAY | OBSIDIAN | GEODE):
    global best
    if t == 0:
        best = max(best, d)
        return
    if d + s * t + t * (t - 1) // 2 <= best:
        return
    done = 0
    if t >= 2 and a >= cost[4] and c >= cost[5] and goal & GEODE:
        solve(t - 1, a + p - cost[4], b + q, c + r - cost[5], d + s, p, q, r, s + 1)
        done |= GEODE
    if t >= 4 and c < (cost[5] - r) * (t - 2) and a >= cost[2] and b >= cost[3] and goal & OBSIDIAN:
        solve(t - 1, a + p - cost[2], b + q - cost[3], c + r, d + s, p, q, r + 1, s)
        done |= OBSIDIAN
    if t >= 6 and b < (cost[3] - q) * (t - 4) and a >= cost[1] and goal & CLAY:
        solve(t - 1, a + p - cost[1], b + q, c + r, d + s, p, q + 1, r, s)
        done |= CLAY
    if t >= 4 and a < (max(cost[0], cost[1], cost[2], cost[4]) - p) * (t - 2) and a >= cost[0] and goal & ORE:
        solve(t - 1, a + p - cost[0], b + q, c + r, d + s, p + 1, q, r, s)
        done |= ORE
    if goal ^ done:
        solve(t - 1, a + p, b + q, c + r, d + s, p, q, r, s, goal ^ done)


part1, part2 = 0, 1
for line in open(0):
    id, *cost = (int(n) for n in re.findall("\d+", line))
    best = 0
    solve(24)
    part1 += id * best
    if id <= 3:
        solve(32)
        part2 *= best
print(part1)
print(part2)
