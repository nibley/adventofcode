from collections import defaultdict
from math import inf

t = 1
blocks = defaultdict(lambda: inf)
while True:
    try:
        line = input()
    except EOFError:
        break

    position = tuple( int(n) for n in line.split(',') )
    blocks[position] = t

    t += 1

HEIGHT = 71
WIDTH = 71

START = (0, 0)
GOAL = (WIDTH - 1, HEIGHT - 1)

is_open = lambda position, t: blocks[position] > t

def get_neighbors(position, t):
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
            and is_open(
                (neighbor_x, neighbor_y),
                t
            )
        ):
            yield (neighbor_x, neighbor_y)

def find_path(t):
    distances_from_start = defaultdict(lambda: inf, { START : 0 })

    unvisited = set(
        (x, y)
        for x in range(WIDTH)
        for y in range(HEIGHT)
        if is_open(
            (x, y),
            t
        )
    )
    while unvisited:
        position = min(unvisited, key=distances_from_start.__getitem__)
        if position == GOAL:
            break

        current_score = distances_from_start[position]
        for neighbor in get_neighbors(position, t):
            if neighbor in unvisited:
                old_score = distances_from_start[neighbor]
                new_score = current_score + 1

                if new_score < old_score:
                    distances_from_start[neighbor] = new_score

        unvisited.remove(position)

    return distances_from_start[GOAL]

t -= 1
while find_path(t) == inf:
    t -= 1

print(
    '{},{}'.format(
        *next(
            block
            for block, block_t in blocks.items()
            if block_t == t + 1
        )
    )
)
