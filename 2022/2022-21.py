# Day 21: Monkey Math
# https://adventofcode.com/2022/day/21

import operator, re

# Part 1 is straight-forward depth-first resolution of the formulas.

# For Part 2, say the unknown value is "x". After resolving the formulas, assume
# we end up with a linear equation like so (from the LHS and RHS of the root):
#     LHS = a + b * x = p + q * x = RHS
# This means x = (p - a) / (b - q).

# A really nice way to do this (instead of trying to implement symbolic algebra)
# is to use complex numbers. Replace "x" with "i" above, and we have:
#     LHS = a + b * i = p + q * i = RHS
# This lets us do normal arithmetic calculations as in Part 1. To solve:
#     diff = LHS - RHS = (a - p) + (b - q) * i
#     answer = (p - a) / (b - q) = -diff.real / diff.imag

OPS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

formula = {}
for line in open(0):
    monkey, *parts = re.split("[: ]+", line.strip())
    formula[monkey] = [int(parts[0])] if len(parts) == 1 else [parts[0], OPS[parts[1]], parts[2]]

solve = lambda monkey: f[0] if len(f := formula[monkey]) == 1 else f[1](solve(f[0]), solve(f[2]))
print(round(solve("root")))

formula["humn"] = [1j]
diff = solve(formula["root"][0]) - solve(formula["root"][2])
print(round(-diff.real / diff.imag))
