from collections import defaultdict
from math import inf

start_x = None
start_y = None

goal_x = None
goal_y = None

grid = {}
y = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, char in enumerate(line):
        if char in 'SE':
            if char == 'S':
                start_x = x
                start_y = y
            else:
                goal_x = x
                goal_y = y

            char = '.'

        grid[ (x, y) ] = char == '.'

    y += 1

HEIGHT = y
WIDTH = len(line)

start = (start_x, start_y)
goal = (goal_x, goal_y)

def visualize(visited=()):
    for y in range(WIDTH):
        for x in range(HEIGHT):
            if (x, y) == (start_x, start_y):
                print('S', end='')
            elif (x, y) == (goal_x, goal_y):
                print('E', end='')
            elif (x, y) in visited:
                print('o', end='')
            else:
                print('.' if grid[ (x, y )] else '#', end='')
        print()
    print()

DIRECTIONS = (
    # e s w n
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
)

def get_neighbors(position):
    x, y = position

    for x_offset, y_offset in DIRECTIONS:
        new_position = (x + x_offset, y + y_offset)

        if grid.get(new_position):
            yield new_position

unvisited = set(
    position
    for position, is_open in grid.items()
    if is_open
)

distances_from_start = defaultdict(lambda: inf)
distances_from_start[start] = 0
came_from = {}

position = start
while unvisited and position != goal:
    position_score = distances_from_start[position]

    for neighbor in get_neighbors(position):
        old_score = distances_from_start[neighbor]
        new_score = position_score + 1

        if new_score < old_score:
            distances_from_start[neighbor] = new_score
            came_from[neighbor] = position

    unvisited.remove(position)
    position = min(unvisited, key=distances_from_start.__getitem__)

assert distances_from_start[goal] < inf

position = goal
path = set()
while position != start:
    position = came_from.get(position)
    path.add(position)

path.add(position)
baseline_path = len(path)

def get_cheats():
    for position in path:
        x, y = position

        for x_offset, y_offset in DIRECTIONS:
            end_position = (x + 2 * x_offset, y + 2 * y_offset)

            if grid.get(end_position):
                yield (
                    distances_from_start[end_position]
                    - distances_from_start[position]
                    - 2
                )

print(
    sum(
        savings >= 100
        for savings in get_cheats()
    )
)
