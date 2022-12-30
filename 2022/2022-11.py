# Day 11: Monkey in the Middle
# https://adventofcode.com/2022/day/11

import copy, itertools, math

items, ops, mods, targets = [], [], [], []
for monkey in open(0).read().split("\n\n"):
    lines = monkey.splitlines()
    items.append([int(n) for n in lines[1].removeprefix("  Starting items: ").split(", ")])
    ops.append(eval("lambda old: " + lines[2].removeprefix("  Operation: new = ")))
    mods.append(int(lines[3].removeprefix("  Test: divisible by ")))
    targets.append(
        [
            int(lines[5].removeprefix("    If false: throw to monkey ")),
            int(lines[4].removeprefix("    If true: throw to monkey ")),
        ]
    )

N = math.lcm(*mods)


def solve(items, num_rounds, divisor):
    counts = [0] * len(items)
    for _, m in itertools.product(range(num_rounds), range(len(items))):
        counts[m] += len(items[m])
        for item in items[m]:
            worry = ops[m](item) // divisor % N
            items[targets[m][worry % mods[m] == 0]].append(worry)
        items[m] = []
    print(math.prod(sorted(counts)[-2:]))


solve(copy.deepcopy(items), 20, 3)
solve(items, 10000, 1)
