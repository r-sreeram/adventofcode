# Day 19: Not Enough Minerals
# https://adventofcode.com/2022/day/19

# Inspired by Boojum: https://www.reddit.com/r/adventofcode/comments/zpihwi/2022_day_19_solutions/j0tls7a/

# The algorithm for both parts is essentially a brute-force depth-first search.
# The search space is huge (especially for Part 2), so we make it tractable with
# a few optimizations:

# + The absolute best-case scenario is if we assume that we'll somehow be able
#   to make a geode-cracking robot every turn from now until time runs out. In
#   that wildly optimistic scenario, the number of geodes we'll have is
#       =   d (geodes we already have)
#         + s * t (geodes our existing geode robots will open)
#         + t * (t - 1) / 2 (geodes opened by the robots we'll make every turn)
#   If that's not going to improve the `best` seen so far, stop. Hence:
#       if d + s * t + t * (t - 1) // 2 <= best: return

# + If we were able to make a certain type of robot (`done`) this turn, there's
#   no point trying an alternative search path where we DON'T make any robot
#   (and simply wait) this turn, and then try to make that robot (`goal`) in the
#   future. This only applies to waiting (doing nothing this turn). If instead
#   of making that robot, we make some other robot this turn, then of course, we
#   can try to make the former robot in the future. Hence:
#       if (goal ^ done): solve(..., goal ^ done)

# + There's no point making a robot if it's not going to produce anything useful
#   in time for opening geodes. For example:
#   o No point making a geode robot on the last turn (t = 1). Hence:
#         if (t >= 2 and ...): solve(..., s + 1)  # make a geode robot
#   o No point making an obsidian robot on the last 3 turns (t <= 3), because
#     any obsidian it produces cannot be used for making geode bots in time:
#         if (t >= 4 and ...): solve(..., r + 1, ...)  # make an obsidian robot
#   ... and so on for clay and ore robots.

# + If we have enough "ore capacity", no point making any more ore robots. By
#   "ore capacity", we mean the amount of ore we have (`a`) plus what we expect
#   to make in the future given the ore robots we have (`p`). By "enough", we
#   mean that even if we needed a lot of ore every turn (= max of all the ore
#   requirements) to make some type of robot, we are good. Hence:
#       if (... a < (max(...) - p) * (t - 2) and ...):  # make an ore robot
#   Likewise for clay and obsidian capacity.

import re

ORE, CLAY, OBSIDIAN, GEODE = 1, 2, 4, 8

# t = time remaining, goal = target robot types (bitmask)
# mineral amounts:  a=ore, b=clay, c=obsidian, d=geode
# number of robots: p=ore, q=clay, r=obsidian, s=geode
def solve(t, a=0, b=0, c=0, d=0, p=1, q=0, r=0, s=0, goal=ORE | CLAY | OBSIDIAN | GEODE):
    global best
    if t == 0:
        best = max(best, d)
        return best
    if d + s * t + t * (t - 1) // 2 <= best:
        return best
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
    return best


part1, part2 = 0, 1
for line in open(0):
    id, *cost = (int(n) for n in re.findall("\d+", line))
    best = 0
    part1 += id * solve(24)
    if id <= 3:
        part2 *= solve(32)
print(part1, part2, sep="\n")
