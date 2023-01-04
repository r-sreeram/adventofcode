# Day 11: Corporate Policy
# https://adventofcode.com/2015/day/11

sequence = lambda s: any(ord(a) + 2 == ord(b) + 1 == ord(c) for a, b, c in zip(s, s[1:], s[2:]))
doublets = lambda s: len(set(a for a, b in zip(password, password[1:]) if a == b)) > 1
todo, password = 2, input()
while todo:
    password = password.rstrip("z")
    if password:
        index, char = next(((i, c) for i, c in enumerate(password) if c in "ilo"), (-1, password[-1]))
        password = password[0:index] + ("jmp"[q] if (q := "hkn".find(char)) != -1 else chr(ord(char) + 1))
    password = password.ljust(8, "a")
    if sequence(password) and doublets(password):
        print(password)
        todo -= 1
