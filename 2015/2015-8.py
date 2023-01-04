# Day 8: Matchsticks
# https://adventofcode.com/2015/day/8

strings = open(0).read().splitlines()
print(sum(len(s) - len(eval(s)) for s in strings))
print(sum(s.count("\\") + s.count('"') + 2 for s in strings))
