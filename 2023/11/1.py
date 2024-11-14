from itertools import combinations

grid = []
while True:
    try:
        line = input()
    except EOFError:
        break

    row = [ char == '#' for char in line ]
    grid.append(row)

height = len(grid)
width = len(grid[0])

empty_rows = [ y for y, row in enumerate(grid)
    if all(not cell for cell in row) ]
empty_columns = [ x for x in range(width)
    if all(not row[x] for row in grid) ]

for empty_row in reversed(empty_rows):
    grid.insert(empty_row + 1, [False] * width)

for empty_column in reversed(empty_columns):
    for y, row in enumerate(grid):
        row.insert(empty_column + 1, False)

galaxies = []
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell:
            galaxies.append( (x, y) )

total = 0
for first_galaxy, second_galaxy in combinations(galaxies, 2):
    total += abs(first_galaxy[0] - second_galaxy[0]) + \
        abs(first_galaxy[1] - second_galaxy[1])

print(total)
