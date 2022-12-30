# Day 17: Pyroclastic Flow
# https://adventofcode.com/2022/day/17

# Inspired by 4HbQ: https://www.reddit.com/r/adventofcode/comments/znykq2/2022_day_17_solutions/j0kdnnj/

ROCKS = ((0, 1, 2, 3), (1, 1j, 1 + 1j, 2 + 1j, 1 + 2j), (0, 1, 2, 2 + 1j, 2 + 2j), (0, 1j, 2j, 3j), (0, 1, 1j, 1 + 1j))

can_place = lambda rock, pos: pos.imag >= 0 and all(0 <= (p := pos + d).real < 7 and p not in tower for d in rock)

tower, height = set(), 0
i, pos = 0, 2 + 3j
j, jet = 0, open(0).read().strip()

dp = {}
targets = [2022, 1000000000000]
count, bonus_count, bonus_height = 0, 0, 0

while targets:
    while count + bonus_count < targets[0]:
        d = -1 if jet[j] == "<" else 1
        if can_place(ROCKS[i], pos + d):
            pos += d
        j = (j + 1) % len(jet)
        if can_place(ROCKS[i], pos - 1j):
            pos -= 1j
            continue
        tower.update(pos + d for d in ROCKS[i])
        height = max([height] + [int((pos + d).imag) + 1 for d in ROCKS[i]])
        i = (i + 1) % len(ROCKS)
        pos = complex(2, height + 3)
        count += 1
        if (i, j) in dp:
            prev_count, prev_height = dp[i, j]
            batch_size = count - prev_count
            reps = (targets[0] - count - bonus_count) // batch_size
            bonus_count += batch_size * reps
            bonus_height += (height - prev_height) * reps
        dp[i, j] = count, height
    print(height + bonus_height)
    del targets[0]
