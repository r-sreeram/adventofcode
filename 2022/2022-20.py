# Day 20: Grove Positioning System
# https://adventofcode.com/2022/day/20

# Inspired by 4HbQ: https://www.reddit.com/r/adventofcode/comments/zqezkn/2022_day_20_solutions/j0y04h2/

# Instead of shuffling the input numbers directly, we shuffle the indices of the
# numbers. This has the nice property that we can use list.index(...) to find
# the entry, since indices are unique (whereas the input numbers are not).

# Another nice touch is the use of "indices * repeat" for the loop. Not only
# does this produce the desired repetitions, but it also creates a temporary
# list, so we can modify the original indices list inside the loop, without
# causing problems.

# Note the use of len(indices). The more natural expression is len(numbers) - 1,
# but since we just did indices.pop() on the previous line, they are the same.


def solve(repeat):
    indices = list(range(len(numbers)))
    for i in indices * repeat:
        indices.pop(j := indices.index(i))
        indices.insert((j + numbers[i]) % len(indices), i)
    zero = indices.index(numbers.index(0))
    print(sum(numbers[indices[(zero + pos) % len(numbers)]] for pos in (1000, 2000, 3000)))


numbers = [int(n) for n in open(0)]
solve(1)

numbers = [n * 811589153 for n in numbers]
solve(10)
