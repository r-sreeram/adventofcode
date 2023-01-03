# Day 5: Doesn't He Have Intern-Elves For This?
# https://adventofcode.com/2015/day/5

from re import search

strings = open(0).read().splitlines()
print(sum(1 for s in strings if search("([aeiou].*){3}", s) and search(r"(.)\1", s) and not search("ab|cd|pq|xy", s)))
print(sum(1 for s in strings if search(r"(..).*\1", s) and search(r"(.).\1", s)))
