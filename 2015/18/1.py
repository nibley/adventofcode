def step_cell(position):
    neighbors_on = sum(cell_neighbors(*position))
    if grid[position]:
        return neighbors_on in {2, 3}
    else:
        return neighbors_on == 3

def cell_neighbors(x, y):
    for x_offset, y_offset in (
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ):
        yield grid.get((x + x_offset, y + y_offset), False)

SIDE_LENGTH = 100
grid = {}
y = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, cell in enumerate(line):
        position = (x, y)
        grid[ (x, y) ] = cell == '#'

    y += 1

for _ in range(100):
    grid = {
        position : step_cell(position)
        for position in grid
    }

def visualize():
    for y in range(SIDE_LENGTH):
        for x in range(SIDE_LENGTH):
            print('#' if grid[ (x, y) ] else '.', end='')
        print()
    print()
# visualize()

print(sum(grid.values()))
