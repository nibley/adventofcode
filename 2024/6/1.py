guard_x = None
guard_y = None

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
            assert (guard_x, guard_y) == (None, None)
            guard_x, guard_y = (x, y)

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

visited = set()
while guard_x in range(WIDTH) and guard_y in range(HEIGHT):
    visited.add(
        (guard_x, guard_y)
    )

    x_offset, y_offset = DIRECTIONS[facing]
    check_position = (guard_x + x_offset, guard_y + y_offset)

    if grid.get(check_position, True):
        # allow stepping outside the map
        guard_x, guard_y = check_position
    else:
        facing = (facing + 1) % 4

print(len(visited))
