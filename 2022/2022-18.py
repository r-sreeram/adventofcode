# Day 18: Boiling Boulders
# https://adventofcode.com/2022/day/18

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
