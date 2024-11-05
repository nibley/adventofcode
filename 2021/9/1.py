from math import inf
from itertools import product as cartesian_product

grid = []
while True:
    try:
        line = input()
    except EOFError:
        break

    grid.append([ int(n) for n in line ])

height = len(grid)
width = len(grid[0])

neighbor_offsets = [
    (-1,  0),
    ( 1,  0),
    ( 0, -1),
    ( 0,  1)
]

def get_neighbors(x, y):
    for offset_x, offset_y in neighbor_offsets:
        neighbor_x = x + offset_x
        neighbor_y = y + offset_y

        if (
            0 <= neighbor_x < width
            and 0 <= neighbor_y < height
        ):
            yield grid[neighbor_y][neighbor_x]
        else:
            yield inf

print(
    sum(
        cell + 1
        for (x, y), cell in (
            ((x, y), grid[y][x])
            for x, y in cartesian_product(
                range(width),
                range(height)
            )
        )
        if all( cell < neighbor for neighbor in get_neighbors(x, y) )
    )
)
