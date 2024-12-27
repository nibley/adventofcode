INITIAL_X = None
INITIAL_Y = None

grid = {}
y = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, cell in enumerate(line):
        grid[ (x, y) ] = (cell != '#')

        if cell == '^':
            assert (INITIAL_X, INITIAL_Y) == (None, None)
            INITIAL_X, INITIAL_Y = (x, y)

    y += 1

HEIGHT = y
WIDTH = len(line)

facing = 0 # index into DIRECTIONS
DIRECTIONS = (
    ( 0, -1), # north
    ( 1,  0), # east
    ( 0,  1), # south
    (-1,  0)  # west
)

def has_loop(obstacle):
    visited = set()

    facing = 0
    guard_x = INITIAL_X
    guard_y = INITIAL_Y
    while (guard_x, guard_y, facing) not in visited:
        if not (guard_x in range(WIDTH) and guard_y in range(HEIGHT)):
            return False

        visited.add(
            (guard_x, guard_y, facing)
        )

        x_offset, y_offset = DIRECTIONS[facing]
        check_position = (guard_x + x_offset, guard_y + y_offset)

        if check_position != obstacle and grid.get(check_position, True):
            guard_x, guard_y = check_position
        else:
            facing = (facing + 1) % 4

    return True

print(
    sum(
        has_loop(
            (x, y)
        )
        for x in range(WIDTH)
        for y in range(HEIGHT)
        if (x, y) != (INITIAL_X, INITIAL_Y) and grid[ (x, y) ]
    )
)
