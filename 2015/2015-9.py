# Day 9: All in a Single Night
# https://adventofcode.com/2015/day/9

# The puzzle guarantees that the input is a complete graph ("distances between
# every pair of locations"), so we don't need to check if distance[src][dst]
# exists during the pairwise() iteration (it will). Also, doing a DFS or BFS
# will not be any faster, since we have to try all n! paths anyway. It's more
# elegant and just as fast to use itertools.permutations().

# The graph is undirected, so we really only need to try n!/2 paths. I.e., for
# every path we consider, it's effectively the same as its reverse. Generating
# exactly n!/2 paths (without reverses) involves a lot of code. Generating all
# the n! paths and filtering out the reverses is just 1 extra line of code, but
# not much more efficient. So here, we swallow the 2x inefficiency and consider
# all n! paths, since that makes for more elegant code.

import collections, itertools as it

distance = collections.defaultdict(dict)
for line in open(0):
    src, _, dst, _, cost = line.split()
    distance[src][dst] = distance[dst][src] = int(cost)
paths = [sum(distance[src][dst] for src, dst in it.pairwise(perm)) for perm in it.permutations(distance.keys())]
print(min(paths), max(paths), sep="\n")
