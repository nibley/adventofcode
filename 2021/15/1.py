from collections import defaultdict
from math import inf

grid = {}
y = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, risk in enumerate(line):
        grid[ (x, y) ] = int(risk)

    y += 1

HEIGHT = y
WIDTH = len(line)

START = (0, 0)
GOAL = (WIDTH - 1, HEIGHT - 1)

costs_from_start = defaultdict(lambda: inf, { START : 0 })
unvisited = set(grid)

position = START
# while unvisited:
while unvisited and position != GOAL:
    x, y = position
    position_cost = costs_from_start[position]
    for x_offset, y_offset in (
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ):
        neighbor = (x + x_offset, y + y_offset)
        if neighbor not in grid:
            continue

        old_cost = costs_from_start[neighbor]
        new_cost = position_cost + grid[neighbor]

        if old_cost > new_cost:
            costs_from_start[neighbor] = new_cost

    # print('remove', position)
    position = min(
        unvisited,
        key=costs_from_start.__getitem__
    )
    unvisited.remove(position)

cost = costs_from_start[GOAL]
assert cost < inf
print(cost)
