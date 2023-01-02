# Day 4: Camp Cleanup
# https://adventofcode.com/2022/day/4

# For Part 1, we want interval pairs where one fully contains the other, which
# means one of the following situations (along the horizontal axis):
#      a1 o-------------o a2            a1 o-o a2
#            b1 o-o b2            b1 o-------------o b2
# <=> (a1 <= b1 and b2 <= a2) or (b1 <= a1 and a2 <= b2)

# For Part 2, we want interval pairs which have at least some overlap, which
# means NEITHER of the following situations (along the horizontal axis):
#   a1 o-o a2   b1 o-o b2  or  b1 o-o b2   a1 o-o a2
# <=> NOT (a2 < b1         or         b2 < a1)
# <=> (a2 >= b1 and b2 >= a1)

# We are assuming that in the input, a <= b for each interval (a, b).

import re

sections = [[int(id) for id in re.findall("\d+", pairs)] for pairs in open(0)]
assert all(a1 <= a2 and b1 <= b2 for a1, a2, b1, b2 in sections)
print(sum(a1 <= b1 and b2 <= a2 or b1 <= a1 and a2 <= b2 for a1, a2, b1, b2 in sections))
print(sum(a2 >= b1 and b2 >= a1 for a1, a2, b1, b2 in sections))
