# Day 20: Grove Positioning System
# https://adventofcode.com/2022/day/20

# Inspired by 4HbQ: https://www.reddit.com/r/adventofcode/comments/zqezkn/2022_day_20_solutions/j0y04h2/

# Instead of shuffling the numbers directly, we shuffle pointers to the numbers
# (indices). The "for i in indices * repeat" not only produces the right number
# of repetitions, but it also creates a temporary list, so we can modify the
# original indices list inside the loop without causing problems.


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
