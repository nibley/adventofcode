from functools import cache
from math import inf

grid = {}
y = 0
goal_x = None
goal_y = None
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, height in enumerate(line):
        if height == 'S':
            height = 'a'
        elif height == 'E':
            goal_x = x
            goal_y = y
            height = 'z'

        grid[ (x, y) ] = ord(height)

    y += 1

height = y
width = len(line)

neighbor_offsets = [
    (-1,  0),
    ( 1,  0),
    ( 0, -1),
    ( 0,  1)
]

@cache
def get_neighbors(x, y):
    return tuple(
        (neighbor_x, neighbor_y)
        for neighbor_x, neighbor_y, in (
            (x + offset_x, y + offset_y)
            for offset_x, offset_y in neighbor_offsets
        )
        if (
            0 <= neighbor_x < width
            and 0 <= neighbor_y < height
            and grid[ (neighbor_x, neighbor_y) ] - grid[ (x, y) ] <= 1
        )
    )

def find_shortest_route(starting_position):
    steps = 0
    positions_to_crawl = set([starting_position])
    while positions_to_crawl:
        if steps > min(min_steps, HEURISTIC_BOUND_ON_STEPS):
            return inf

        new_positions_found = set()
        for x, y in positions_to_crawl:
            if (x, y) == (goal_x, goal_y):
                return steps

            new_positions_found.update(get_neighbors(x, y))

        steps += 1
        positions_to_crawl = new_positions_found

HEURISTIC_BOUND_ON_STEPS = height * width
min_steps = inf
for starting_position, elevation in grid.items():
    if elevation != ord('a'):
        continue

    steps = find_shortest_route(starting_position)
    if min_steps > steps:
        min_steps = steps

print(min_steps)
