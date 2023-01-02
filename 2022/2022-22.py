# Day 22: Monkey Map
# https://adventofcode.com/2022/day/22

# Inspired by smrq: https://www.reddit.com/r/adventofcode/comments/zsct8w/2022_day_22_solutions/j184mn7/

import re

# First, some notation: A face is one of the 6 square regions (size x size) in
# the input grid. No matter how the faces wrap or fold, our coordinate system is
# aligned to the input grid. The top-left is (0, 0). x (real) increases left to
# right, and y (imag) increases top to bottom. During the simulation, `pos` is
# relative to the top-left of the face we are currently on. `dir` is aligned to
# grid as well, and equals the amount to add to `pos` to move one step in that
# direction: east = DIRS[0] = 1 + 0j, south = DIRS[1] = 0 + 1j, etc.

# Given that the 6 faces must fold into a cube (for Part 2), the input grid can
# only be one of 11 hexominos (or some rotation/reflection thereof):
#     https://en.wikipedia.org/wiki/Hexomino#Polyhedral_nets_for_the_cube

# Both Parts 1 and 2 can be solved with the same simulation (see solve() below),
# as long as we pass in the appropriate "wrap" object:
#     wrap[f][dir] = m means:
#         if you are on face f, and you are going in direction dir, and you go
#         past the edge of the face, you'll end up on face m.
#     0 <= f < 6, 0 <= m < 6, dir is an element of DIRS.

# Part 1 (see wrap_2d() below): To compute wrap[f][dir], start at the top-left
# of face f, and keep going in direction dir (jumping by size units each time),
# wrapping around if we reach the end of the input grid (via the `mod` lambda),
# until we land on some valid face (which could be f itself). Given the possible
# hexominos (see above), this will take at most 4 jumps, hence range(1, 5).

# Part 2 (see wrap_3d() below): Assume the cube is as follows, with sides U=UP,
#   +-------+      D=DOWN, L=LEFT, R=RIGHT, F=FRONT and B=BACK. Based on this,
#   |\       \     we know the four sides each side is connected to, going
#   | \   U   \    clockwise in some order, stored as `ADJACENT` in the code.
#   |  \       \   Note that DIRS is also in clockwise order. We don't yet know
#   | L +-------+  exactly which face (0 through 5) is UP or LEFT, for example,
#   +   |       |  nor which direction to go from UP to connect to LEFT. We'll
#    \  |   F   |  traverse the input grid to figure it out. The faces form a
#     \ |       |  connected graph, so we can reach all faces starting from any
#       +-------+  of them. If face f is connected to face m going in direction
# dir in the input grid, obviously wrap[f][dir] = m, and wrap[m][-dir] = f. But
# we can also update our map of the other connections based on the clockwise
# arrangement of the neighbouring sides.

# To keep things clear, I'll consistently use "face" to describe the faces as
# seen on the input grid (0 through 5) and "side" to describe the sides of the
# 3-D cube (UP, DOWN, etc). `s2f` tracks the mapping from "side to face".

# This is best explained with an example. Consider a T-shaped hexomino as the
# input grid. The `s2f` and `wrap` data structures start out empty:
#   .........    s2f = {}
#   .0..1..2.    wrap[0] = wrap[1] = ... = wrap[5] = None
#   .........  We arbitrarily pick face 0 as UP, its east as RIGHT, and update
#      ...     the map, using ADJACENT[UP] to figure out the other connections:
#      .3.       s2f[UP] = 0
#      ...       wrap[0] = {east: RIGHT, south: FRONT, west: LEFT, north: BACK}
#      ...     When we do the dfs() traversal, we'll go east from face 0 to
#      .4.     face 1. This tells us two things: Since wrap[0][east] = RIGHT,
#      ...     face 1 must be RIGHT. Also, we must obviously go in the opposite
#      ...     direction (west) to go from face 1 to face 0 (UP), so we can
#      .5.     populate wrap[1] based on that info (and ADJACENT[RIGHT]):
#      ...       s2f[RIGHT] = 1
#                wrap[1] = {west: UP, north: BACK, east: DOWN, south: FRONT}
# Continuing the dfs, we reach face 2 going east from face 1. Again, based on
# wrap[1][east], we know this must be the DOWN side, and we must go west to
# go from face 2 to face 1 (RIGHT). Using that and ADJACENT[DOWN], we have:
#     s2f[DOWN] = 2
#     wrap[2] = {west: RIGHT, north: BACK, east: LEFT, south: FRONT}
# There are no more faces reachable from face 2, so we backtrack to face 1 and
# find face 3 going south. wrap[1][south] = FRONT, so face 3 must be FRONT.
# Again, using the fact that wrap[3][north] must be face 1 (RIGHT) and the
# clockwise rotational information in ADJACENT[FRONT], we have:
#     s2f[FRONT] = 3
#     wrap[3] = {north: RIGHT, east: DOWN, south: LEFT, west: UP}
# Etc. In the end, we'll have:
#     s2f = {UP: 0, RIGHT: 1, DOWN: 2, FRONT: 3, LEFT: 4, BACK: 5}
#     wrap[0] = {east: RIGHT, south: FRONT, west: LEFT,  north: BACK}
#     wrap[1] = {east: DOWN,  south: FRONT, west: UP,    north: BACK}
#     wrap[2] = {east: LEFT,  south: FRONT, west: RIGHT, north: BACK}
#     wrap[3] = {east: DOWN,  south: LEFT,  west: UP,    north: RIGHT}
#     wrap[4] = {east: DOWN,  south: BACK,  west: UP,    north: FRONT}
#     wrap[5] = {east: DOWN,  south: RIGHT, west: UP,    north: LEFT}
# All we have to do is use `s2f` to replace the sides with faces in `wrap`:
#     wrap[0] = {east: 1, south: 3, west: 4, north: 5}
#     wrap[1] = {east: 2, south: 3, west: 0, north: 5}
#     wrap[2] = {east: 4, south: 3, west: 1, north: 5}
#     wrap[3] = {east: 2, south: 4, west: 0, north: 1}
#     wrap[4] = {east: 2, south: 5, west: 0, north: 3}
#     wrap[5] = {east: 2, south: 1, west: 0, north: 4}

# Okay, so `wrap` tells us which face to go to, when we go past the edge. In
# the 3-D case, we also need to update the position and direction. In the above
#   +-----+  T-shaped hexomino, for example, we can see that face 0's south edge
#   |  N  |  is connected to the west edge of face 3, as wrap[0][south] = 3, but
#   |W 0 E|  wrap[3][west] = 0. Thus, when going south from face 0 and wrapping
#   |  S  |  to face 3, we must change our direction to "going east". To figure
#   +-----+  this out, we "rotate" the target face (face 3) until the expected
#   |  W  |  edge matches up with the source face (face 0). With each rotation,
#   |S 3 N|  we also rotate the x and y coordinates using a "rotation matrix":
#   |  E  |      (new_x, new_y) = (size - 1 - old_y, old_x)
#   +-----+  What does "expected edge matches up" mean? In this example, when
# going south, if face 3's north edge had been connected to face 0, all would've
# been well, and the direction and position would not need to be updated. But
# given the actual connection, it would take 3 clockwise rotations of face 3
# to get its north side to match to face 0. Thus, we also need to rotate the
# direction and position 3 times.

# We do this rotation in solve(), because it's a no-op for the 2-D case (the
# faces already have the expected edges matching up), thus there's no need to
# special-case it just for the 3-D case.

DIRS = [1j**i for i in range(4)]

*grid, _, commands = open(0).read().splitlines()
commands = re.findall("\d+|L|R", commands)

rows, cols = len(grid), max(len(row) for row in grid)
size = (rows + cols) // 7

# f2p is "face to pos". f2p[f] = p means that face f's top-left corner is at
# position p, where 0 <= f < 6, 0 <= p.real < cols and 0 <= p.imag < rows.
# p2f is the opposite mapping, so we can find which face a given position is on.
f2p = [c + r * 1j for r in range(0, rows, size) for c in range(0, len(grid[r]), size) if grid[r][c] in ".#"]
p2f = {pos: face for face, pos in enumerate(f2p)}

# Returns True if the given position is a wall.
wall = lambda pos: grid[int(pos.imag)][int(pos.real)] == "#"


def wrap_2d():
    mod = lambda pos: int(pos.real) % cols + (int(pos.imag) % rows) * 1j
    return [{d: next(p2f[q] for n in range(1, 5) if (q := mod(p + n * d * size)) in p2f) for d in DIRS} for p in f2p]


def wrap_3d():
    # Neighbours of each side, in clockwise order.
    ADJACENT = {"U": "RFLB", "R": "UBDF", "F": "URDL", "D": "BLFR", "L": "FDBU", "B": "LDRU"}

    # s2f is a mapping from "side to face".
    s2f, wrap = {}, [None] * 6

    # We are at face `face`, also known as side `side`. We also know that the
    # side named `neighbour` is in direction `dir` from us.
    def dfs(face, side, dir, neighbour):
        s2f[side] = face
        i = (adj := ADJACENT[side]).index(neighbour)
        wrap[face] = {dir * DIRS[k]: adj[(i + k) % 4] for k in range(4)}
        for d in DIRS:
            # If we are connected to a face g via dir d, and we haven't
            # processed g yet, recurse to it.
            if (g := p2f.get(f2p[face] + d * size, None)) != None and wrap[g] == None:
                dfs(g, wrap[face][d], -d, side)

    dfs(0, "U", 1, "R")
    return [{dir: s2f[side] for dir, side in neighbours.items()} for neighbours in wrap]


def solve(wrap):
    dir, pos = 1, grid[0].index(".")
    face = next(f for f, p in enumerate(f2p) if p.real <= pos < p.real + size)
    pos -= f2p[face]
    for cmd in commands:
        if cmd in "LR":
            dir *= 1j if cmd == "R" else -1j
        else:
            for _ in range(int(cmd)):
                f, d, p = face, dir, pos + dir
                if not (0 <= p.real < size and 0 <= p.imag < size):
                    # We went off the edge. Find the new face to wrap to.
                    f = wrap[face][dir]
                    p = p.real % size + (p.imag % size) * 1j
                    # Rotate our position and direction if needed.
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
