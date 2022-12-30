# Day 2: Rock Paper Scissors
# https://adventofcode.com/2022/day/2

# Transform the input so that (for both players), rock=0, paper=1, scissors=2.
# In (mod 3) space, this makes it so that: N beats N-1 and loses to N+1.

# Given p1 and p2 (choices for players 1 and 2), from p2's perspective:
#     p2 - p1     = x (mod 3), where x = {0 => draw, 1 => win,  2 => loss}
# <=> p2 - p1 + 1 = y (mod 3), where y = {0 => loss, 1 => draw, 2 => win}
# Thus, the score for Part 1 is:
#     (p2 + 1) + (y * 3)
#   = (p2 + 1) + ((p2 - p1 + 1) mod 3) * 3

# For Part 2, we want to find z such that:
#     z - p1 + 1 = p2 (mod 3), where p2 = {0 => loss, 1 => draw, 2 => win}
# <=> z = p2 + p1 - 1 (mod 3)
# The score for Part 2 is:
#     (z + 1) + (p2 * 3)
#   = ((p2 + p1 - 1) mod 3) + 1) + (p2 * 3)

strategies = [[ord(guide[0]) - ord("A"), ord(guide[2]) - ord("X")] for guide in open(0)]
print(sum(p2 + 1 + (p2 - p1 + 1) % 3 * 3 for p1, p2 in strategies))
print(sum(p2 * 3 + (p2 + p1 - 1) % 3 + 1 for p1, p2 in strategies))
