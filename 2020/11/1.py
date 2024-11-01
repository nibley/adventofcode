neighbor_offsets = [
    (-1, -1),
    (-1,  0),
    (-1,  1),
    ( 0, -1),
    ( 0,  1),
    ( 1, -1),
    ( 1,  0),
    ( 1,  1),
]

def get_cell(x, y):
    if (
        0 <= x < width
        and 0 <= y < height
    ):
        return grid[y][x]
    else:
        return '.'

def get_neighbors(x, y):
    for offset_x, offset_y in neighbor_offsets:
        yield get_cell(x + offset_x, y + offset_y)

grid = []
while True:
    try:
        line = input()
    except EOFError:
        break

    grid.append(list(line))

height = len(grid)
width = len(grid[0])

while True:
    next_generation = [ [ '.' for _ in range(width) ] for _ in range(height) ]

    for x in range(width):
        for y in range(height):
            cell = grid[y][x]
            if cell == '.':
                continue

            num_occupied_neighbors = sum(
                neighbor == '#'
                for neighbor in get_neighbors(x, y)
            )

            if num_occupied_neighbors == 0:
                next_cell_value = '#'
            elif num_occupied_neighbors >= 4:
                next_cell_value = 'L'
            else:
                next_cell_value = cell

            next_generation[y][x] = next_cell_value

    if grid == next_generation:
        break
    else:
        grid = next_generation

print(sum(row.count('#') for row in next_generation))
