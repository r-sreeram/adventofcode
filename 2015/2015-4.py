# Day 4: The Ideal Stocking Stuffer
# https://adventofcode.com/2015/day/4

import hashlib

prefix = input()
n, zeros = 0, [5, 6]
while zeros:
    n += 1
    if hashlib.md5((prefix + str(n)).encode()).hexdigest().startswith("0" * zeros[0]):
        print(n)
        del zeros[0]
