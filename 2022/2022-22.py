# Day 22: Monkey Map
# https://adventofcode.com/2022/day/22

# Inspired by smrq: https://www.reddit.com/r/adventofcode/comments/zsct8w/2022_day_22_solutions/j184mn7/

import re

DIRS = [1j**i for i in range(4)]

*grid, _, commands = open(0).read().splitlines()
commands = re.findall("\d+|L|R", commands)

rows, cols = len(grid), max(len(row) for row in grid)
size = (rows + cols) // 7

f2p = [c + r * 1j for r in range(0, len(grid), size) for c in range(0, len(grid[r]), size) if grid[r][c] in ".#"]
p2f = {pos: face for face, pos in enumerate(f2p)}
wall = lambda pos: grid[int(pos.imag)][int(pos.real)] == "#"


def wrap_2d():
    mod = lambda pos: int(pos.real) % cols + (int(pos.imag) % rows) * 1j
    return [{d: next(p2f[p] for n in range(1, 5) if (p := mod(f + n * d * size)) in p2f) for d in DIRS} for f in f2p]


def wrap_3d():
    # clockwise neighbours of each cube face
    CWSIDES = {"u": "rflb", "r": "ubdf", "f": "urdl", "d": "blfr", "l": "fdbu", "b": "ldru"}
    s2f, wrap = {}, [None] * len(f2p)

    def dfs(face, side, dir, neighbour):
        s2f[side] = face
        i = (adj := CWSIDES[side]).index(neighbour)
        wrap[face] = {dir * 1j**k: adj[(i + k) % len(adj)] for k in range(len(DIRS))}
        for d in DIRS:
            if (f2 := p2f.get(f2p[face] + d * size, None)) != None and wrap[f2] == None:
                dfs(f2, wrap[face][d], -d, side)

    dfs(0, "u", 1, "r")
    return [{dir: s2f[side] for dir, side in neighbours.items()} for neighbours in wrap]


def solve(wrap):
    dir, pos = 1, grid[0].index(".")
    face = next(i for i, f in enumerate(f2p) if f.real <= pos < f.real + size)
    pos -= f2p[face]
    for cmd in commands:
        if cmd in "LR":
            dir *= 1j if cmd == "R" else -1j
        else:
            for _ in range(int(cmd)):
                f, d, p = face, dir, pos + dir
                if not (0 <= p.real < size and 0 <= p.imag < size):
                    f = wrap[face][dir]
                    p = p.real % size + (p.imag % size) * 1j
                    while wrap[f][-d] != face:
                        p = size - 1 + p * 1j
                        d *= 1j
                if wall(f2p[f] + p):
                    break
                face, dir, pos = f, d, p
    pos += f2p[face]
    print(round((pos.imag + 1) * 1000 + (pos.real + 1) * 4 + DIRS.index(dir)))


solve(wrap_2d())
solve(wrap_3d())
