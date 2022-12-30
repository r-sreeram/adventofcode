# Day 13: Distress Signal
# https://adventofcode.com/2022/day/13

# Inspired by 4HbQ: https://www.reddit.com/r/adventofcode/comments/zkmyh4/2022_day_13_solutions/j00qay8/

def cmp(a, b):
    match a, b:
        case int(), int():
            return a - b
        case list(), list():
            if any(r := cmp(a2, b2) for a2, b2 in zip(a, b)):
                return r
            return cmp(len(a), len(b))
        case int(), list():
            return cmp([a], b)
        case list(), int():
            return cmp(a, [b])


packets = [eval(line) for line in open(0).read().split()]
print(sum([i // 2 + 1 for i in range(0, len(packets), 2) if cmp(packets[i], packets[i + 1]) < 0]))

# A three-way check would have ~33% fewer comparisons (i.e., if cmp(p, 2) < 0,
# there's no need to check cmp(p, 6)), but results in less elegant code.
pos = [sum(cmp(p, divider) < 0 for p in packets) for divider in (2, 6)]
print((pos[0] + 1) * (pos[1] + 2))
