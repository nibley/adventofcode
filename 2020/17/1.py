from collections import defaultdict
from itertools import product as cartesian_product

neighbor_offsets = tuple(
    offset
    for offset in cartesian_product((-1, 0, 1), repeat=3)
    if offset != (0, 0, 0)
)

def get_neighbor_count(position):
    x, y, z = position
    return sum(
        grid[ (x + x_offset, y + y_offset, z + z_offset) ]
        for x_offset, y_offset, z_offset in neighbor_offsets
    )

grid = defaultdict(lambda: False)
y = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, cell in enumerate(line):
        if cell == '#':
            grid[ (x, y, 0) ] = True

    y += 1

for t in range(6):
    active = tuple( position for position, state in grid.items() if state )
    min_x, *_, max_x = sorted(x for x, _, _ in active)
    min_y, *_, max_y = sorted(y for _, y, _ in active)
    min_z, *_, max_z = sorted(z for _, _, z in active)

    new_grid = defaultdict(lambda: False)

    for position in cartesian_product(
        range(min_x - 1, max_x + 2),
        range(min_y - 1, max_y + 2),
        range(min_z - 1, max_z + 2)
    ):
        cell = grid[position]
        neighbor_count = get_neighbor_count(position)
        if (
            neighbor_count == 3
            or (cell and neighbor_count == 2)
        ):
            new_grid[position] = True

    grid = new_grid

print(sum(grid.values()))
