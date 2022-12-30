# Day 9: Rope Bridge
# https://adventofcode.com/2022/day/9

# The move() function moves the tail one step closer to the head, in 1-D. By
# doing it for both coordinates in 2-D, we achieve the desired result.

knot = [0] * 10
move = lambda h, t: t + (h > t) - (h < t)

part1, part2 = {0}, {0}
for d, n in (line.split() for line in open(0)):
    for _ in range(int(n)):
        knot[0] += {"U": 1j, "D": -1j, "L": -1, "R": 1}[d]
        for i in range(9):
            if abs(knot[i] - knot[i + 1]) >= 2:
                knot[i + 1] = move(knot[i].real, knot[i + 1].real) + move(knot[i].imag, knot[i + 1].imag) * 1j
        part1.add(knot[1])
        part2.add(knot[9])
print(len(part1))
print(len(part2))
