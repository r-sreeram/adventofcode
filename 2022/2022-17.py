# Day 17: Pyroclastic Flow
# https://adventofcode.com/2022/day/17

# Inspired by 4HbQ: https://www.reddit.com/r/adventofcode/comments/znykq2/2022_day_17_solutions/j0kdnnj/

# Part 1 is a straight-forward simulation. Part 2 requires "cycle finding",
# i.e., if we find ourselves in a state we've already seen before, we can
# quickly add up the difference between the counts/heights from the last time we
# saw the state till now, as many times as needed, to get us close to the target
# count/height. The trick is in defining what constitutes "state".

# In addition to the specific rock and jet we're at currently, ideally the state
# ought to contain the "shape" of the chamber or tower as seen from the top. The
# tower has lots of gaps, so modelling it accurately would lead to a very large
# state space, and we would almost never see the same state twice.

# If we describe the shape up to a max tower depth of N (as seen from the top),
# that limits the state space, and we are able to benefit from cycles. It gives
# the correct answer if N is sufficiently large. It isn't even necessary to
# describe the shape (up to that depth of N) accurately. It seems enough to only
# track, for each of the 7 columns, the highest point where there's a rock. For
# the AoC inputs I've seen, this technique works with N = 30.

# It turns out that ignoring the tower entirely (i.e., N = 0), and using only
# the rock and jet for the state works just as well, if we look for a cycle only
# after a bunch of rocks have already fallen. The code below does that by
# solving both Parts 1 and 2 using the same loop. Thus, Part 2's cycle finding
# doesn't kick in until Part 1 is done (and 2022 rocks have fallen).

# These shortcuts (N = 30 or N = 0) are of course not robust. It's certainly
# possible to craft inputs where they give the wrong answer.

# In our coordinate system, (0,0) is at the bottom-left. x (real) increases left
# to right, and y (imag) increases bottom to top.
ROCKS = ((0, 1, 2, 3), (1, 1j, 1 + 1j, 2 + 1j, 1 + 2j), (0, 1, 2, 2 + 1j, 2 + 2j), (0, 1j, 2j, 3j), (0, 1, 1j, 1 + 1j))

can_place = lambda rock, pos: pos.imag >= 0 and all(0 <= (p := pos + d).real < 7 and p not in tower for d in rock)

# `i` is the index of the falling rock. `pos` is its position. `j` is the index
# of the jet.
i, pos = 0, 2 + 3j
j, jet = 0, open(0).read().strip()

# count is the number of rocks that have settled.
tower, height, count = set(), 0, 0

# For each state we've seen before, `seen` records the count of settled rocks
# and the height of the tower at that state. When we see a previous state again,
# the increases in count and height from then to now are added (as many times as
# possible) to cycle_count and cycle_height.
seen, cycle_count, cycle_height = {}, 0, 0
for target in 2022, 1000000000000:
    while count + cycle_count != target:
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
        if (i, j) in seen:
            prev_count, prev_height = seen[i, j]
            batch_size = count - prev_count
            reps = (target - count - cycle_count) // batch_size
            cycle_count += batch_size * reps
            cycle_height += (height - prev_height) * reps
        seen[i, j] = count, height
    print(height + cycle_height)
