robot_x = None
robot_y = None

grid = {}
y = 0
while True:
    line = input()
    if not line:
        break

    for x, char in enumerate(line):
        if char == '@':
            assert robot_x is None
            assert robot_y is None

            robot_x = x
            robot_y = y

            char = '.'

        grid[ (x, y) ] = char

    y += 1

HEIGHT = y
WIDTH = sum( x == 0 for x, y in grid )

directions = {
    '^': (0, -1),
    'v': (0, 1),
    '<': (-1, 0),
    '>': (1, 0)
}

moves = []
while True:
    try:
        line = input()
    except EOFError:
        break

    for char in line:
        moves.append(directions[char])

def visualize():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == (robot_x, robot_y):
                if grid[ (x, y) ] == 'O':
                    print('R', end='')
                else:
                    print('@', end='')
            else:
                print(grid[ (x, y) ], end='')
        print()
    print()

for x_offset, y_offset in moves:
    goal_x = robot_x + x_offset
    goal_y = robot_y + y_offset

    # print(next(key for key, value in directions.items() if value == (x_offset, y_offset) ), x_offset, y_offset)

    goal_char = grid[ (goal_x, goal_y) ]
    if goal_char == '.':
        robot_x, robot_y = (goal_x, goal_y)
    elif goal_char == '#':
        # continue
        pass
    elif goal_char == 'O':
        scan_x = goal_x
        scan_y = goal_y

        while grid.get( (scan_x, scan_y) ) == 'O':
            scan_x += x_offset
            scan_y += y_offset

        if grid.get( (scan_x, scan_y) ) == '.':
            # move boxes
            while (scan_x, scan_y) != (robot_x, robot_y):
                grid[ (scan_x, scan_y) ] = 'O'

                scan_x -= x_offset
                scan_y -= y_offset

                grid[ (scan_x, scan_y) ] = '.'

            robot_x = goal_x
            robot_y = goal_y

            grid[ (goal_x, goal_y) ] = '.'
        else:
            pass

    visualize()

    print()

# for move in moves: print(move)

print(
    sum(
        x + 100 * y
        for (x, y), char in grid.items()
        if char == 'O'
    )
)
