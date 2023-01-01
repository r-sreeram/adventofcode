# Day 15: Beacon Exclusion Zone
# https://adventofcode.com/2022/day/15

# Inspired by i_have_no_biscuits: https://www.reddit.com/r/adventofcode/comments/zmcn64/2022_day_15_solutions/j0b90nr/

import itertools, re

# Part 1 involves counting points along a line. These points are collected from
# multiple (possibly overlapping) intervals, where each interval is a subset of
# the coverage area of some sensor. One way to avoid double-counting points that
# are covered by multiple sensors is to iterate over all the points in each
# interval and throw them into a set. A much more efficient way is to simply
# merge the intervals together wherever they overlap.

# To solve Part 2, for each sensor's coverage area, imagine the diamond just
# outside its coverage diamond (i.e., one unit away). The distress beacon must
# lie on one of these "outer" diamonds. In fact, this point must lie on the
# outer diamond of at least two sensors (but see line 76 below). Thus, we can
# find it by finding all possible intersections amongst all the lines that form
# these outer diamonds. Since all the lines form two sets of parallel lines, we
# only need to intersect a line with every line from the other set.

distance = lambda x1, y1, x2, y2: abs(x1 - x2) + abs(y1 - y2)

data = [[int(n) for n in re.findall("(-?\d+)", line)] for line in open(0)]
sensors = [(x, y, distance(x, y, *b)) for x, y, *b in data]

# This is a crude effort to distinguish the example input from the real input.
# The example uses a different line (Part 1) and bounding box (Part 2).
LINE, BOX = (2000000, 4000000) if max(itertools.chain(*sensors)) > 1000 else (10, 20)

# [a1, a2) is the current interval, [b1, b2) is the next interval in sorted
# order. [a1, a2) will be extended if they overlap; otherwise, we add [a1, a2)
# to the solution and make [b1, b2) "current". The "-len(...)" part is to
# subtract points that have beacons.
a1, a2, part1 = 0, 0, -len({x for _, _, x, y in data if y == LINE})
for b1, b2 in sorted((x - p, x + p + 1) for x, y, d in sensors if (p := d - abs(LINE - y)) >= 0):
    if a2 < b1 or a1 == a2:
        part1 += a2 - a1
        a1 = b1
    a2 = max(a2, b2)
print(part1 + a2 - a1)

# Returns True if (x, y) is outside the coverage areas of all sensors.
outside = lambda x1, y1: all(distance(x1, y1, x2, y2) > d for x2, y2, d in sensors)

# For a sensor at (x, y), its "outer" diamond (the diamond just outside its
# coverage area, as described above) has the four corners at:
#     (x - (d + 1), y), (x + (d + 1), y), (x, y - (d + 1)), (x, y + (d + 1))

# The equations for the four lines that form the outer diamond are therefore
# (using X and Y for the variables):
#     Y = -X + (y + x - (d + 1))      Y = X + (y - x - (d + 1))
#     Y = -X + (y + x + (d + 1))      Y = X + (y - x + (d + 1))
# The two lines on the left are parallel (they both have slope -1); likewise,
# the two on the right are parallel (slope of +1).

# intercepts[0] contains the y-intercepts for all LHS lines (y + x ± (d + 1))
# intercepts[1] contains the y-intercepts for all RHS lines (y - x ± (d + 1))

# A line from the LHS set (Y = -X + a) and a line from the RHS set (Y = X + b)
# intersect at the point ((a - b) / 2, (a + b) / 2). Any intersection within the
# BOX and outside all sensors' coverage areas is our desired solution.
part2 = None
intercepts = [{y - i * x + j * (d + 1) for x, y, d in sensors for j in (-1, 1)} for i in (-1, 1)]
for a, b in itertools.product(*intercepts):
    x, y = (a - b) // 2, (a + b) // 2
    if 0 <= x <= BOX and 0 <= y <= BOX and outside(x, y):
        part2 = x, y
        break

# If we didn't find the position, that means it must be one of the four corners
# of BOX, where it's possible that it lies on only one of the outer diamonds
# (thus not an intersection of two outer diamond lines). So, check those four
# points, namely: (0, 0), (BOX, 0), (0, BOX), (BOX, BOX).
if part2 == None:
    part2 = next((x, y) for x, y in itertools.product((0, BOX), repeat=2) if outside(x, y))

print(part2[0] * 4000000 + part2[1])
