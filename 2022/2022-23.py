# Day 23: Unstable Diffusion
# https://adventofcode.com/2022/day/23

# Inspired by dcclct13: https://www.reddit.com/r/adventofcode/comments/zt6xz5/2022_day_23_solutions/j1dq8oj/

# This is a simple simulation of the puzzle rules, using a neat observation that
# if multiple elves propose moving to the same spot, they must be coming at it
# from opposite directions, and there can only be two such elves (for each
# target position).

# In each row r, DIRS[r][1] is the actual direction the elf will move, if all
# the positions indicated by DIRS[r][:] are unoccupied.
DIRS = [(-1 - 1j, -1j, 1 - 1j), (-1 + 1j, 1j, 1 + 1j), (-1 - 1j, -1, -1 + 1j), (1 - 1j, 1, 1 + 1j)]

grove = {c + r * 1j for r, row in enumerate(open(0)) for c, char in enumerate(row) if char == "#"}
turn, plan = 0, 1
while plan:
    # plan is a map of valid proposals. If an elf currently at position p is
    # proposing a move to position q, then plan[q] = p. If multiple elves
    # propose to move to the same position, plan will contain none of them (by
    # the end of the loop).
    turn, plan = turn + 1, {}
    for elf in grove:
        if any(elf + dir in grove for dir in (-1 - 1j, -1j, 1 - 1j, -1, 1, -1 + 1j, 1j, 1 + 1j)):
            for dir in DIRS:
                if all(elf + d not in grove for d in dir):
                    # If a previous elf had already proposed moving to the same
                    # position (elf + dir[1]), remove it from the plan, and
                    # don't add us either. If not, add ourselves to the plan.
                    if (prev := plan.pop(elf + dir[1], None)) == None:
                        plan[elf + dir[1]] = elf
                    break
    grove.difference_update(plan.values())
    grove.update(plan.keys())
    DIRS.append(DIRS.pop(0))
    if turn == 10:
        x1, y1 = min(elf.real for elf in grove), min(elf.imag for elf in grove)
        x2, y2 = max(elf.real for elf in grove), max(elf.imag for elf in grove)
        print(round((x2 - x1 + 1) * (y2 - y1 + 1)) - len(grove))
print(turn)
