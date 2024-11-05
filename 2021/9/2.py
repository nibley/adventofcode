from math import inf, prod
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
            and grid[neighbor_y][neighbor_x] < 9
        ):
            yield grid[neighbor_y][neighbor_x]
        else:
            yield inf

all_points = lambda: (
    ((x, y), grid[y][x])
    for x, y in cartesian_product(range(width), range(height))
)

low_points = set(
    position
    for position, cell in all_points()
    if all( cell < neighbor for neighbor in get_neighbors(*position) )
)

basins = {
    low_point : set([low_point])
    for low_point in low_points
}

points_to_crawl = set(
    position
    for position, cell in all_points()
    if cell != 9
).difference(low_points)

while points_to_crawl:
    new_points_matched = []
    for point in points_to_crawl:
        x, y = point
        found_basin = False
        for offset_x, offset_y in neighbor_offsets:
            neighbor = (x + offset_x, y + offset_y)
            for basin, basin_points in basins.items():
                if neighbor in basin_points:
                    found_basin = True
                    break

            if found_basin:
                break

        if found_basin:
            new_points_matched.append( (point, basin) )

    for point, basin in new_points_matched:
        basins[basin].add(point)
        points_to_crawl.remove(point)

def visualize():
    for y in range(height):
        for x in range(width):
            found_basin = False
            for i, basin_points in enumerate(basins.values()):
                if (x, y) in basin_points:
                    print(str(i)[-1], end='')
                    found_basin = True
                    break

            if not found_basin:
                print('#', end='')
        print()
# visualize()

print(
    prod(
        sorted(
            len(basin_points) for basin_points in basins.values()
        )[ -3 : ]
    )
)
