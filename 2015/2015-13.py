# Day 13: Knights of the Dinner Table
# https://adventofcode.com/2015/day/13

import algorithm, collections, itertools

delta = collections.defaultdict(lambda: collections.defaultdict(int))
for line in open(0):
    src, _, op, n, *_, dst = line.split()
    delta[src][dst[:-1]] = int(n) * (1 if op == "gain" else -1)

total = lambda perm: sum(delta[a][b] + delta[b][a] for a, b in itertools.pairwise(perm + (perm[0],)))
for me in ((), ("me",)):
    print(max(total(perm) for perm in algorithm.cyclic_permutations(tuple(delta.keys()) + me)))
