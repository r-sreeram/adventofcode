# Day 6: Tuning Trouble
# https://adventofcode.com/2022/day/6

stream = input()
pos = lambda n: next(i for i in range(n, len(stream) + 1) if len(set(stream[i - n : i])) == n)
print(pos(4))
print(pos(14))
