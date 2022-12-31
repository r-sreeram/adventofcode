# Day 11: Monkey in the Middle
# https://adventofcode.com/2022/day/11

import copy, itertools, math

# Straight-forward simulation of the throws, using the LCM of the divisors to
# keep the "worry level" from growing out of control.

# Say w is the worry level and N is the LCM. Why does it work to use w % N
# instead of w itself in all the calculations?

# What matters is the divisibility test. That is the only time the worry level
# has a consequence (depending on the outcome, the item will be thrown to one
# monkey or another). Apart from that, the worry level values aren't actually
# used anywhere else. So, if we can prove that using w % N gives the same result
# for the divisibility test as using w itself, we are good.

# Say m is some specific monkey's divisor (for the divisibility test). We shall
# prove that w = a (mod N) => w = a (mod m). I.e., ((w % N) % m) = a assures us
# that (w % m) = a. Proof: Let w = a (mod N). This means w = N * k + a for some
# integer k. Since N is a multiple of m, we have w = m * p * k + a, for some
# integer p (i.e., N = m * p). Thus, w = a (mod m). Q.E.D.

# How about the various operations (new = old * 26 and such)? Do they preserve
# this property? Yes. Addition (which includes subtraction) and multiplication
# are compatible under a modulus. E.g., w = a (mod m) => w * b = a * b (mod m).
# See: https://en.wikipedia.org/wiki/Modular_arithmetic#Properties

# This is not always true for division! w = a (mod m) => w / b = a / b (mod m)
# is true if and only if b is coprime to m. Luckily, the input only has addition
# and multiplication operations (no "new = old / 26"), so we are good. Part 1
# does involve division (by 3), so we _cannot_ use modular arithmetic there. See
# the commit description for an example where using it gives the wrong answer.

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


def solve(items, num_rounds, reduce):
    counts = [0] * len(items)
    for _, m in itertools.product(range(num_rounds), range(len(items))):
        counts[m] += len(items[m])
        for item in items[m]:
            worry = reduce(ops[m](item))
            items[targets[m][worry % mods[m] == 0]].append(worry)
        items[m] = []
    print(math.prod(sorted(counts)[-2:]))


solve(copy.deepcopy(items), 20, lambda x: x // 3)
lcm = math.lcm(*mods)
solve(items, 10000, lambda x: x % lcm)
