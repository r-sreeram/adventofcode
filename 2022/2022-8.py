# Day 8: Treetop Tree House
# https://adventofcode.com/2022/day/8

import itertools, math

rows = open(0).read().splitlines()
cols = list(zip(*rows))

is_visible = lambda trees: all(h < trees[0] for h in trees[1:])
view_distance = lambda trees: next((i for i, h in enumerate(trees[1:], 1) if h >= trees[0]), len(trees) - 1)

part1, part2 = 0, 0
for r, c in itertools.product(range(len(rows)), range(len(cols))):
    tree_lines = rows[r][c:], rows[r][c::-1], cols[c][r:], cols[c][r::-1]
    part1 += any(is_visible(trees) for trees in tree_lines)
    part2 = max(part2, math.prod(view_distance(trees) for trees in tree_lines))
print(part1)
print(part2)
