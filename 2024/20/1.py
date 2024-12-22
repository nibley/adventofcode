from collections import defaultdict, deque
from math import inf

start_x = None
start_y = None

goal_x = None
goal_y = None

# grid = defaultdict(lambda: False)
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
        new_x = x + x_offset
        new_y = y + y_offset
        new_position = (new_x, new_y)

        if (
            new_x in range(1, WIDTH - 1)
            and new_y in range(1, HEIGHT - 1)
            and grid[new_position]
        ):
            yield new_position

unvisited = set(
    position
    for position, is_open in grid.items()
    if is_open
)

distances_from_start = defaultdict(lambda: inf)
distances_from_start[start] = 0
came_from = {}

while unvisited:
    # if not len(unvisited) % 100: print(len(unvisited))
    # print(len(unvisited))

    position = min(unvisited, key=distances_from_start.__getitem__)
    if position == goal:
        print('DONE')
        break

    position_score = distances_from_start[position]
    for neighbor in get_neighbors(position):
        old_score = distances_from_start[neighbor]
        new_score = position_score + 1

        if new_score < old_score:
            distances_from_start[neighbor] = new_score
            came_from[neighbor] = position

    unvisited.remove(position)

assert distances_from_start[goal] < inf

position = goal
path = set()
while position != start:
    path.add(position)
    position = came_from.get(position)

path.add(position)

# baseline_path = len(path) - 1
baseline_path = len(path)
print('baseline', len(path))

print()

def get_cheats():
    for x, y in path:
    # for x, y in [(7, 7)]:
        # print('cheat', x, y)

        for x_offset, y_offset in DIRECTIONS:
        # for x_offset, y_offset in [(-1, 0)]:

            # print('  ', x_offset, y_offset)
            first_cheat = (x + x_offset, y + y_offset)
            second_cheat = (x + 2 * x_offset, y + 2 * y_offset)

            # print(' ', *first_cheat)
            # print(' ', *second_cheat)

            if not grid.get(second_cheat):
                continue

            # print('  clear')

            # print('     first', distances_from_start[ (x, y) ] + 2)
            # print('     final', baseline_path - distances_from_start[second_cheat])
            # print(
            #     '     saved',
            #     distances_from_start[second_cheat]
            #     - distances_from_start[ (x, y) ]
            #     - 2
            # )

            savings = (
                distances_from_start[second_cheat]
                - distances_from_start[ (x, y) ]
                - 2
            )
            # print(savings)
            yield savings

freq = {}
for savings in get_cheats():
    freq.setdefault(savings, 0)
    freq[savings] += 1

# for savings in sorted(freq): print(f'{savings}: {freq[savings]}')

total = 0
for savings in sorted(freq):
    if savings >= 100:
        total += freq[savings]

print(total)

print(start in path)
print(goal in path)

# TODO is baseline high by ̄1 (includes start and goal)
# but accidentally giving the answer?
