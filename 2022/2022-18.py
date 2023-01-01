# Day 18: Boiling Boulders
# https://adventofcode.com/2022/day/18

# For Part 1, for each cube, for each of its 6 faces, the face is "connected"
# to an adjacent cube if that adjacent cube is in our input set. The desired
# answer is the total number of faces (6 * cubes) minus the number of these
# connected faces.

# For Part 2, we do a "flood fill". I.e., starting from a cube known to be
# outside all other cubes, we do a depth-first search (DFS) to reach all outside
# cubes (within a bounding box). Whenever the DFS is blocked, we have run into
# an outside face of a cube in our input set. The number of such faces is our
# desired answer.

DXYZ = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))
adjacent = lambda cube: {tuple(sum(c) for c in zip(cube, d)) for d in DXYZ}

cubes = {tuple(int(n) for n in line.split(",")) for line in open(0)}

print(len(cubes) * 6 - sum(len(adjacent(c) & cubes) for c in cubes))

lo = tuple(min(c) - 1 for c in zip(*cubes))
hi = tuple(max(c) + 1 for c in zip(*cubes))
stack, seen = [lo], {lo}

part2 = 0
while stack:
    for c in adjacent(stack.pop()):
        if c in cubes:
            part2 += 1
        elif all(p <= q <= r for p, q, r in zip(lo, c, hi)) and c not in seen:
            stack.append(c)
            seen.add(c)
print(part2)
