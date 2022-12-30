# Day 2: Rock Paper Scissors
# https://adventofcode.com/2022/day/2

strategies = [[ord(guide[0]) - ord("A"), ord(guide[2]) - ord("X")] for guide in open(0)]
print(sum(p2 + 1 + (p2 - p1 + 1) % 3 * 3 for p1, p2 in strategies))
print(sum(p2 * 3 + (p2 + p1 - 1) % 3 + 1 for p1, p2 in strategies))
