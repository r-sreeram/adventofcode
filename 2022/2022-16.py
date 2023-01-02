# Day 16: Proboscidea Volcanium
# https://adventofcode.com/2022/day/16

# Inspired by juanplopes: https://www.reddit.com/r/adventofcode/comments/zn6k1l/2022_day_16_solutions/j0hrdpt/

# For Part 1, we can do a simple depth-first search (DFS), made slightly more
# efficient by precomputing all pairwise distances between rooms that have some
# flow, and considering only those rooms in the search. Along the way, we keep
# track of the max total flow achieved for every combination of opened valves;
# the max amongst them is of course the solution.

# For Part 2, we do the same thing as in Part 1 (except starting with a smaller
# amount of time remaining). Since `best` contains every possible combination of
# valves that can be opened, one of those will be the set we open, and another
# one of those will be the set the elephant opens (since we and the elephant
# start at the same room and have the same amount of time). These sets have to
# be disjoint, since we can't open the same valve twice (hence k1 & k2 == 0).

# There are alternative approaches, but this turns out to be the fastest.

import collections, math, re

# bits and rate are not populated for rooms with zero flow.
rate, edge, bits = {}, {}, {}
for line in open(0):
    id, flow, *valves = re.findall("\d+|[A-Z]{2}", line)
    edge[id] = collections.defaultdict(lambda: math.inf, {v: 1 for v in valves})
    if flow != "0":
        bits[id] = 1 << len(rate)
        rate[id] = int(flow)

# All pairs shortest paths (Floyd-Warshall). These explicit loops are measurably
# faster than the more compact itertools.product(edge, repeat=3).
for k in edge:
    for i in edge:
        for j in edge:
            edge[i][j] = min(edge[i][j], edge[i][k] + edge[k][j])

# We are at room u, with `time` minutes remaining. `opened` is a bitmask of
# valves that have been opened so far. Room u's valve has already been opened
# (except in the case of the starting room, see line 52 below). `flow` is the
# total flow achieved so far (each opened valve has already accounted for future
# flow till time runs out).
def solve(time, best, u="AA", flow=0, opened=0):
    best[opened] = max(best.get(opened, 0), flow)
    for v, r in rate.items():
        # If v hasn't been opened yet and there's time to reach it and open it,
        # then do so, add its flow (till the end of time) and recurse.
        if opened & (b := bits[v]) == 0 and (dist := edge[u][v]) + 1 < time:
            solve(time - 1 - dist, best, v, flow + r * (time - 1 - dist), opened | b)
    # Handle the case where the starting room ("AA") has non-zero flow.
    if (r := rate.get(u, 0)) and opened & (b := bits[u]) == 0:
        solve(time - 1, best, u, r * (time - 1), b)
    return best


print(max(solve(30, {}).values()))
best = solve(26, {}).items()
print(max(v1 + v2 for (k1, v1) in best for (k2, v2) in best if k1 & k2 == 0))
