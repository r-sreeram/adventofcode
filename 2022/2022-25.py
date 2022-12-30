# Day 25: Full of Hot Air
# https://adventofcode.com/2022/day/25

# Inspired by 4HbQ: https://www.reddit.com/r/adventofcode/comments/zur1an/2022_day_25_solutions/j1l08w6/

to_dec = lambda s: 5 * to_dec(s[:-1]) + "=-012".index(s[-1]) - 2 if s else 0
to_snafu = lambda n: to_snafu((n + 2) // 5) + "=-012"[(n + 2) % 5] if n else ""

print(to_snafu(sum(to_dec(line.strip()) for line in open(0))))
