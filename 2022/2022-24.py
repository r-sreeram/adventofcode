# Day 24: Blizzard Basin
# https://adventofcode.com/2022/day/24

DIRS = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0), "X": (0, 0)}

grid = open(0).read().splitlines()
ROWS, COLS = len(grid) - 2, len(grid[0]) - 2
time, start, stop = 0, (-1, 0), (ROWS, COLS - 1)

snow = {(r, c): DIRS[ch] for r in range(ROWS) for c in range(COLS) if (ch := grid[r + 1][c + 1]) in DIRS}
ok = lambda r, c: 0 <= r < ROWS and 0 <= c < COLS or (r, c) in (start, stop)

trip, pos = 3, {start}
while trip:
    time += 1
    ice = {((r + dr * time) % ROWS, (c + dc * time) % COLS) for (r, c), (dr, dc) in snow.items()}
    pos = {(r2, c2) for r, c in pos for dr, dc in DIRS.values() if ok(r2 := r + dr, c2 := c + dc)} - ice
    if stop in pos:
        if trip in (1, 3):
            print(time)
        start, stop = stop, start
        trip, pos = trip - 1, {start}
