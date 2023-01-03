# Day 3: Perfectly Spherical Houses in a Vacuum
# https://adventofcode.com/2015/day/3

import itertools

visited = lambda moves: set(itertools.accumulate(({"<": -1, ">": 1, "^": -1j, "v": 1j}[c] for c in moves), initial=0))

moves = input()
print(len(visited(moves)))
print(len(visited(moves[::2]) | visited(moves[1::2])))
