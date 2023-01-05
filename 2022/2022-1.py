# Day 1: Calorie Counting
# https://adventofcode.com/2022/day/1

totals = sorted(sum(int(calories) for calories in elf.split()) for elf in open(0).read().split("\n\n"))
print(totals[-1], sum(totals[-3:]), sep="\n")
