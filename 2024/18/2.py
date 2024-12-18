from collections import defaultdict
from math import inf

lines_original = []
while True:
    try:
        line = input()
    except EOFError:
        break

    x, y = map(int, line.split(','))
    lines_original.append((x, y))

# for line in lines_original: print(line)

HEIGHT = 71
WIDTH = 71
# HEIGHT = 7
# WIDTH = 7

x = 0
y = 0

goal_x = WIDTH - 1
goal_y = HEIGHT - 1

def visualize():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print('.' if grid[(x, y)] else '#', end='')
        print()
    print()

# visualize()

DIRECTIONS = (
    # e s w n
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
)


def get_neighbors(position, grid):
    x, y = position

    for x_offset, y_offset in DIRECTIONS:
        neighbor_x = x + x_offset
        neighbor_y = y + y_offset
        neighbor = (neighbor_x, neighbor_y)

        if (
            neighbor_x in range(WIDTH)
            and neighbor_y in range(HEIGHT)
            and grid[neighbor]
        ):
            yield neighbor

def find_path(grid):
    unvisited = set(
        (x, y)
        for x in range(WIDTH)
        for y in range(HEIGHT)
        # for position, is_open in grid.items()
        if grid[(x, y)]
    )

    distances_from_start = defaultdict(lambda: inf)
    # distances_from_start[ (x, y) ] = 0
    distances_from_start[ (0, 0) ] = 0
    # visited = set()

    while unvisited:
        # if not len(unvisited) % 100: print(len(unvisited))

        position = min(unvisited, key=distances_from_start.__getitem__)

        if position == (goal_x, goal_y):
            break

        current_score = distances_from_start[position]
        for neighbor in get_neighbors(position, grid):
            if neighbor not in unvisited:
                continue

            old_score = distances_from_start[neighbor]
            new_score = current_score + 1

            if new_score < old_score:
                distances_from_start[neighbor] = new_score

        # visited.add(position)
        unvisited.remove(position)

    # print(visited)
    # print(unvisited)

    return distances_from_start[(goal_x, goal_y)]

t = 0
grid = defaultdict(lambda: True)
lines = lines_original[ : ]
while True:
    t += 1

    block, *lines = lines
    grid[block] = False

    if t < 2900: continue

    print(t)
    # print(grid)

    path = find_path(grid)
    print(path)
    print()

    if path == inf:
        break

print(t)
print(block)
