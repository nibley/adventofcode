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

empty_rows = [ all(not cell for cell in row) for row in grid ]
empty_columns = [ all(not row[x] for row in grid) for x in range(width)]

galaxies = []
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell:
            galaxies.append( (x, y) )

expansion_factor = 1_000_000
total = 0
for [first_x, first_y], [second_x, second_y] in combinations(galaxies, 2):
    first_x, second_x = sorted((first_x, second_x))
    first_y, second_y = sorted((first_y, second_y))

    delta_x = abs(first_x - second_x)
    x_expansions = sum(empty_columns[first_x + 1 : second_x])
    total += delta_x - x_expansions
    total += x_expansions * expansion_factor

    delta_y = abs(first_y - second_y)
    y_expansions = sum(empty_rows[first_y + 1 : second_y])
    total += delta_y - y_expansions
    total += y_expansions * expansion_factor

print(total)
