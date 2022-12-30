# Day 15: Beacon Exclusion Zone
# https://adventofcode.com/2022/day/15

# Inspired by i_have_no_biscuits: https://www.reddit.com/r/adventofcode/comments/zmcn64/2022_day_15_solutions/j0b90nr/

import itertools, re

distance = lambda x1, y1, x2, y2: abs(x1 - x2) + abs(y1 - y2)

data = [[int(n) for n in re.findall("(-?\d+)", line)] for line in open(0)]
sensors = [(x, y, distance(x, y, *b)) for x, y, *b in data]
LINE, BOX = (2000000, 4000000) if max(itertools.chain(*sensors)) > 1000 else (10, 20)

a1, a2, part1 = 0, 0, -len({x for _, _, x, y in data if y == LINE})
for b1, b2 in sorted((x - p, x + p + 1) for x, y, d in sensors if (p := d - abs(LINE - y)) >= 0):
    if a2 < b1 or a1 == a2:
        part1 += a2 - a1
        a1 = b1
    a2 = max(a2, b2)
print(part1 + a2 - a1)

outside = lambda x1, y1: all(distance(x1, y1, x2, y2) > d for x2, y2, d in sensors)

part2 = None
coeffs = [{y - i * x + j * (d + 1) for x, y, d in sensors for j in (-1, 1)} for i in (-1, 1)]
for a, b in itertools.product(*coeffs):
    if a >= b and (a - b) % 2 == 0:
        x, y = (a - b) // 2, (a + b) // 2
        if 0 <= x <= BOX and 0 <= y <= BOX and outside(x, y):
            part2 = x, y
            break
if part2 == None:
    part2 = next((x, y) for x, y in itertools.product((0, BOX), repeat=2) if outside(x, y))
print(part2[0] * 4000000 + part2[1])
