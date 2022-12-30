# Day 23: Unstable Diffusion
# https://adventofcode.com/2022/day/23

# Inspired by dcclct13: https://www.reddit.com/r/adventofcode/comments/zt6xz5/2022_day_23_solutions/j1dq8oj/

DIRS = [(-1 - 1j, -1j, 1 - 1j), (-1 + 1j, 1j, 1 + 1j), (-1 - 1j, -1, -1 + 1j), (1 - 1j, 1, 1 + 1j)]

grove = {c + r * 1j for r, row in enumerate(open(0)) for c, char in enumerate(row) if char == "#"}
turn, moves = 0, 1
while moves:
    turn, moves = turn + 1, {}
    for elf in grove:
        if any(elf + dir in grove for dir in (-1 - 1j, -1j, 1 - 1j, -1, 1, -1 + 1j, 1j, 1 + 1j)):
            for dir in DIRS:
                if all(elf + d not in grove for d in dir):
                    if (prev := moves.pop(elf + dir[1], None)) == None:
                        moves[elf + dir[1]] = elf
                    break
    grove.difference_update(moves.values())
    grove.update(moves.keys())
    DIRS.append(DIRS.pop(0))
    if turn == 10:
        x1, y1 = min(elf.real for elf in grove), min(elf.imag for elf in grove)
        x2, y2 = max(elf.real for elf in grove), max(elf.imag for elf in grove)
        print(round((x2 - x1 + 1) * (y2 - y1 + 1)) - len(grove))
print(turn)
