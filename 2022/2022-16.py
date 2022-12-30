# Day 16: Proboscidea Volcanium
# https://adventofcode.com/2022/day/16

# Inspired by juanplopes: https://www.reddit.com/r/adventofcode/comments/zn6k1l/2022_day_16_solutions/j0hrdpt/

import collections, math, re

rate, edge, bits = {}, {}, {}
for line in open(0):
    id, flow, *valves = re.findall("\d+|[A-Z]{2}", line)
    edge[id] = collections.defaultdict(lambda: math.inf, {v: 1 for v in valves})
    if flow != "0":
        bits[id] = 1 << len(rate)
        rate[id] = int(flow)

for k in edge:
    for i in edge:
        for j in edge:
            edge[i][j] = min(edge[i][j], edge[i][k] + edge[k][j])


def solve(time, best, u="AA", flow=0, opened=0):
    best[opened] = max(best.get(opened, 0), flow)
    for v, r in rate.items():
        if r and not opened & (b := bits[v]) and (dist := edge[u][v]) < time - 1:
            solve(time - 1 - dist, best, v, flow + r * (time - 1 - dist), opened | b)
    if (r := rate.get(u, 0)) and not opened & (b := bits[u]):
        solve(time - 1, best, u, r * (time - 1), b)
    return best


print(max(solve(30, {}).values()))
best = solve(26, {}).items()
print(max(v1 + v2 for (k1, v1) in best for (k2, v2) in best if k1 & k2 == 0))
