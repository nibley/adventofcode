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

            robot_x = 2 * x
            robot_y = y

            char = '.'

        if char == 'O':
            grid[ (2 * x, y) ] = '['
            grid[ (2 * x + 1, y) ] = ']'
        else:
            grid[ (2 * x, y) ] = char
            grid[ (2 * x + 1, y) ] = char

    y += 1

HEIGHT = y
WIDTH = sum( y == 0 for x, y in grid )

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

def is_corrupt():
    for (x, y), char in grid.items():
        if char == '[' and grid.get( (x + 1, y) ) != ']':
            print('left has', grid.get( (x + 1, y) ))
            return True

        if char == ']' and grid.get( (x - 1, y) ) != '[':
            print('right has', grid.get( (x - 1, y) ))
            return True

    return False


def visualize():
    # return

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

# print('start')
# visualize()

def get_pushes(position, offset, boxes_to_push=None):
    if boxes_to_push is None:
        # different than the use of None below to indicate hitting a wall
        boxes_to_push = []

    x, y = position

    position_char = grid.get(position)

    # print('push?', position_char, position, boxes_to_push)
    # print('push?', position_char, position)

    if position_char == '.':
        # print('  push .')
        return ()
    elif position_char == '#':
        # print('  push #')
        return None
    elif position_char == ']':
        # print('  hop over')
        return get_pushes((x - 1, y), offset, boxes_to_push)

    x_offset, y_offset = offset

    if y_offset == 0: # get_pushes horizontally, simpler case
        if x_offset == 1: # get_pushes right
            # print('  right')
            target_x = x + 2
        else: # get_pushes left
            # print('  left')
            target_x = x - 1

        target = (target_x, y)

        if get_pushes(target, offset, boxes_to_push) is None:
            return None

        # print('free')

        boxes_to_push.append(position)
        # print('  added', position)
        # print('  ', boxes_to_push)

    else: # get_pushes vertically, more complicated case
        first_target = (x, y + y_offset)
        second_target = (x + 1, y + y_offset)

        if (
            get_pushes(first_target, offset, boxes_to_push) is None
            or get_pushes(second_target, offset, boxes_to_push) is None
        ):
            return None

        # print('free')

        boxes_to_push.append(position)
        # print('  added', position)
        # print('  ', boxes_to_push)

    # print('final', boxes_to_push)
    return boxes_to_push


for t, (x_offset, y_offset) in enumerate(moves):
    # print(
    #     f'{t=}',
    #     next(key for key, value in directions.items() if value == (x_offset, y_offset) )
    # )

    goal_x = robot_x + x_offset
    goal_y = robot_y + y_offset

    goal_char = grid[ (goal_x, goal_y) ]
    if goal_char == '.':
        robot_x, robot_y = (goal_x, goal_y)
    elif goal_char == '#':
        # print('nope')
        pass
    elif goal_char in {'[', ']'}:
        boxes_to_push = get_pushes((goal_x, goal_y), (x_offset, y_offset))

        # TODO no need to check goal_char at all here if get_pushes checks?
        # False return for wall would stop robot from moving here

        # print()
        # print('could get_pushes?', type(boxes_to_push))

        boxes_to_push = () if boxes_to_push is None else boxes_to_push

        if boxes_to_push:
            # print()
            # visualize()
            # print()

            # print(next(key for key, value in directions.items() if value == (x_offset, y_offset) ))
            pass

        already_pushed = set()
        for box in boxes_to_push:
            if box in already_pushed:
                continue
            else:
                already_pushed.add(box)

            (box_x, box_y) = box

            # print('actually push', box_x, box_y)
            grid[ (box_x, box_y) ] = '.'
            grid[ (box_x + 1, box_y) ] = '.'

            if y_offset == 0:
                if x_offset == 1:
                    grid[ (box_x + 1, box_y) ] = '['
                    grid[ (box_x + 2, box_y) ] = ']'
                else:
                    grid[ (box_x - 1, box_y) ] = '['
                    grid[ (box_x, box_y) ] = ']'
            else:
                first_target = (box_x, box_y + y_offset)
                second_target = (box_x + 1, box_y + y_offset)

                grid[first_target] = '['
                grid[second_target] = ']'

        if boxes_to_push:
            robot_x += x_offset
            robot_y += y_offset

            # print()
            # visualize()
            # print()

    # print()
    # visualize()
    # print()

    if is_corrupt():
        # print('----- corrupt -----')
        break

# print()
# print('done')
# visualize()

print(
    sum(
        x + 100 * y
        for (x, y), char in grid.items()
        if char == '['
    )
)

# TODO simpler driving loop where push handles wall and space simple cases?
# TODO layer-synchronized BFS for push logic? wouldn't need set when actually pushing
