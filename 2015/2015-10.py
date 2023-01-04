# Day 10: Elves Look, Elves Say
# https://adventofcode.com/2015/day/10

import itertools

# Alternative approach that's slighly slower:
#     string = re.sub("1+|2+|3+", lambda m: str(len(m.group())) + m.group()[0], string)

string = input()
for n in 40, 10:
    for _ in range(n):
        string = "".join(str(len(list(v))) + k for k, v in itertools.groupby(string))
    print(len(string))
