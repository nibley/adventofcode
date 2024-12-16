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


def get_neighbors(state):
    (x, y), facing = state

    for facing_offset in (-1, 0, 1):
        new_facing = (facing + facing_offset) % 4

        x_offset, y_offset = DIRECTIONS[new_facing]
        new_position = (x + x_offset, y + y_offset)

        if grid.get(new_position):
            yield (
                (new_position, new_facing),
                1 if facing == new_facing else 1001
            )

unvisited = set(
    (position, facing)
    for position, is_open in grid.items()
    for facing in range(4)
    if is_open
)

distances_from_start = defaultdict(lambda: inf)
distances_from_start[ (start, 0) ] = 0
visited = set()
came_from = defaultdict(set)

while unvisited:
    if not len(unvisited) % 100: print(len(unvisited))

    current = min(unvisited, key=distances_from_start.__getitem__)
    position, facing = current

    if position == goal:
        break

    current_score = distances_from_start[current]
    for neighbor, score_increase in get_neighbors(current):
        if neighbor in visited:
            continue

        old_score = distances_from_start[neighbor]
        new_score = current_score + score_increase

        if new_score <= old_score:
            came_from[neighbor].add(current)

        if new_score < old_score:
            distances_from_start[neighbor] = new_score
            # print(neighbor, old_score, '->', new_score)

    visited.add(current)
    unvisited.remove(current)

optimal_facing_final = min(
    range(4),
    key=lambda facing: distances_from_start[ (goal, facing) ]
)
optimal = (
    goal,
    optimal_facing_final
)
optimal_score = distances_from_start[optimal]

assert sum(
    distances_from_start[ (goal, facing) ] == optimal_score
    for facing in range(4)
) == 1

trace = set()
positions = [optimal]
while positions:
    # print(len(trace), len(positions))

    position = positions.pop()
    loc, facing = position
    trace.add(loc)

    for before in came_from[position]:
        before_loc, _ = before
        if before_loc not in trace:
            positions.append(before)

# visualize(trace)

print(len(trace))
