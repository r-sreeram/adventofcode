# Day 4: The Ideal Stocking Stuffer
# https://adventofcode.com/2015/day/4

import hashlib

n, prefix = 1, input()
for zeros in 5, 6:
    while not hashlib.md5((prefix + str(n)).encode()).hexdigest().startswith("0" * zeros):
        n += 1
    print(n)
