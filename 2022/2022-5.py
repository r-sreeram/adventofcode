# Day 5: Supply Stacks
# https://adventofcode.com/2022/day/5

# Inspired by 4HbQ: https://www.reddit.com/r/adventofcode/comments/zcxid5/2022_day_5_solutions/iyzf3qu/

# Straight-forward simulation of the moves, with a couple of small tricks:
# + Using `::-1` vs `::1` for Part 1 vs Part 2.
# + Adding an empty stack at position 0, so we can use the 1-based indices in
#   the input without changes.

# Note that the first part of the input is expected to be a full grid, including
# trailing spaces.

grid, commands = open(0).read().split("\n\n")
grid = [""] + ["".join(s).strip() for s in zip(*grid.splitlines())][1::4]
commands = [[int(n) for n in cmd.split()[1::2]] for cmd in commands.splitlines()]

for dir in -1, 1:
    stacks = grid[:]
    for n, src, dst in commands:
        stacks[dst] = stacks[src][:n][::dir] + stacks[dst]
        stacks[src] = stacks[src][n:]
    print("".join(s[0] for s in stacks[1:]))
