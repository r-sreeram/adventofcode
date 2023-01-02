# Day 25: Full of Hot Air
# https://adventofcode.com/2022/day/25

# Inspired by 4HbQ: https://www.reddit.com/r/adventofcode/comments/zur1an/2022_day_25_solutions/j1l08w6/

# This is a "simple" conversion between base-5 and base-10 (to and from). The
# main challenge is in wrapping our head around the how the SNAFU system works.

# When converting from SNAFU to base-10 (decimal), looking at the units place
# (right-most digit) for example, we can see that it's basically like converting
# from base-5 to base-10, except we need to subtract two afterwards. The other
# digits work the same way, except at successive powers of 5. Going the other
# way (base-10 to SNAFU) is the reverse: Add two, and convert to base-5.

to_decimal = lambda s: 5 * to_decimal(s[:-1]) + "=-012".index(s[-1]) - 2 if s else 0
to_snafu = lambda n: to_snafu((n + 2) // 5) + "=-012"[(n + 2) % 5] if n else ""

print(to_snafu(sum(to_decimal(line.strip()) for line in open(0))))
