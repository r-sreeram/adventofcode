# Day 6: Tuning Trouble
# https://adventofcode.com/2022/day/6

# Note the slightly unusual `len(...) + 1` as the end of the range(), so that
# `[i - n : i]` will correctly go up to the last n chars.

stream = input()
pos = lambda n: next(i for i in range(n, len(stream) + 1) if len(set(stream[i - n : i])) == n)
print(pos(4), pos(14), sep="\n")
