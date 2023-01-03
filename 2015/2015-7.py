# Day 7: Some Assembly Required
# https://adventofcode.com/2015/day/7

import functools, operator

OPS = {"AND": operator.and_, "OR": operator.or_, "LSHIFT": operator.lshift, "RSHIFT": operator.rshift}

wires = {}
for line in open(0):
    match line.split():
        case x, "->", w:
            wires[w] = x
        case "NOT", x, "->", w:
            wires[w] = [x, operator.inv]
        case x, op, y, "->", w:
            wires[w] = [x, y, OPS[op]]


@functools.cache
def solve(w):
    if isinstance(w, int) or w[0].isdigit():
        return int(w) & 0xFFFF
    val = wires[w]
    if isinstance(val, list):
        if len(val) == 2:
            val = val[1](solve(val[0]))
        else:
            val = val[2](solve(val[0]), solve(val[1]))
    else:
        val = solve(val)
    return val & 0xFFFF


print(part1 := solve("a"))
wires["b"] = part1
solve.cache_clear()
print(solve("a"))
