from math import inf

grid = {}
y = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, digit in enumerate(line):
        grid[ (x, y) ] = int(digit)

    y += 1

HEIGHT = y
WIDTH = len(line)

START = (0, 0)
GOAL = (WIDTH - 1, HEIGHT - 1)

NEIGHBOR_OFFSETS = (
    ( 1,  0), # right
    ( 0,  1), # down
    (-1,  0), # left
    ( 0, -1)  # up
)

distances = {
    (START, 0, 0) : 0
}

def get_neighbors(state):
    position, facing, steps = state
    assert not steps > 3

    if steps == 3:
        facing_offsets = (-1, 1)
    else:
        facing_offsets = (0, -1, 1)

    x, y = position
    for facing_offset in facing_offsets:
        new_facing = (facing + facing_offset) % 4
        x_offset, y_offset = NEIGHBOR_OFFSETS[new_facing]

        neighbor_position = (x + x_offset, y + y_offset)
        if neighbor_position not in grid:
            continue

        if facing_offset == 0:
            yield (neighbor_position, facing, steps + 1)
        else:
            yield (neighbor_position, new_facing, 1)

visited = set()
while True:
    state = min(
        set(distances) - visited,
        key=lambda state: distances.get(state, inf)
    )

    position, _, _ = state
    if position == GOAL:
        break

    state_score = distances.get(state, inf)
    for neighbor in get_neighbors(state):
        if neighbor in visited:
            continue

        neighbor_position, _, _ = neighbor
        neighbor_score = distances.get(neighbor, inf)
        new_score = state_score + grid[neighbor_position]

        if new_score < neighbor_score:
            distances[neighbor] = new_score

    visited.add(state)

position, _, _ = state
assert position == GOAL
assert distances[state] < inf

print(distances[state])
