from collections import defaultdict
from math import inf

grid = defaultdict(lambda: True)
while len(grid) < 1024:
    position = tuple( int(n) for n in input().split(',') )
    grid[position] = False

HEIGHT = 71
WIDTH = 71

START = (0, 0)
GOAL = (WIDTH - 1, HEIGHT - 1)

def get_neighbors(position):
    x, y = position

    for x_offset, y_offset in (
        ( 1,  0),
        ( 0,  1),
        (-1,  0),
        ( 0, -1)
    ):
        neighbor_x = x + x_offset
        neighbor_y = y + y_offset

        if (
            neighbor_x in range(WIDTH)
            and neighbor_y in range(HEIGHT)
            and grid[(neighbor_x, neighbor_y)]
        ):
            yield (neighbor_x, neighbor_y)

distances_from_start = defaultdict(lambda: inf, { START : 0 })

unvisited = set(
    (x, y)
    for x in range(WIDTH)
    for y in range(HEIGHT)
    if grid[(x, y)]
)
while unvisited:
    position = min(unvisited, key=distances_from_start.__getitem__)
    if position == GOAL:
        break

    current_score = distances_from_start[position]
    for neighbor in get_neighbors(position):
        if neighbor in unvisited:
            old_score = distances_from_start[neighbor]
            new_score = current_score + 1

            if new_score < old_score:
                distances_from_start[neighbor] = new_score

    unvisited.remove(position)

print(distances_from_start[GOAL])
