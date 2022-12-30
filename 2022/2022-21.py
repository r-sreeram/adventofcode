# Day 21: Monkey Math
# https://adventofcode.com/2022/day/21

import operator, re

OPS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

formula = {}
for line in open(0):
    monkey, *parts = re.split("[: ]+", line.strip())
    formula[monkey] = [int(parts[0])] if len(parts) == 1 else [parts[0], OPS[parts[1]], parts[2]]

solve = lambda monkey: f[0] if len(f := formula[monkey]) == 1 else f[1](solve(f[0]), solve(f[2]))
print(round(solve("root")))

formula["humn"] = [1j]
val = solve(formula["root"][0]) - solve(formula["root"][2])
print(round(-val.real / val.imag))
