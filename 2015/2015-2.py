# Day 2: I Was Told There Would Be No Math
# https://adventofcode.com/2015/day/2

boxes = [sorted(int(n) for n in line.split("x")) for line in open(0)]
print(sum(2 * (l * w + w * h + h * l) + l * w for l, w, h in boxes))
print(sum(2 * (l + w) + l * w * h for l, w, h in boxes))
