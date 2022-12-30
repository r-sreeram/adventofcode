# Day 4: Camp Cleanup
# https://adventofcode.com/2022/day/4

import re

sections = [[int(id) for id in re.findall("\d+", pairs)] for pairs in open(0)]
print(sum(a1 <= b1 and b2 <= a2 or b1 <= a1 and a2 <= b2 for a1, a2, b1, b2 in sections))
print(sum(a2 >= b1 and b2 >= a1 for a1, a2, b1, b2 in sections))
