grid = []

while True:
    try:
        line = input()
    except EOFError:
        break

    row = tuple(line)
    grid.append(row)

assert len(grid) % 2 == 0

grid = grid[ : : 2 ] # don't need empty space rows

starting_beam_x = grid[0].index('S')
grid = grid[ 1 : ] # skip to the first row with splitters

timelines_per_column = [1] * len(grid[0])

for row in reversed(grid):
    for x, cell in enumerate(row):
        if cell == '^':
            timelines_per_column[x] = timelines_per_column[x - 1] + timelines_per_column[x + 1]

print(timelines_per_column[starting_beam_x])
