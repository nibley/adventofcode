HEIGHT = 6
WIDTH = 50

instructions = []
while True:
    try:
        line = input()
    except EOFError:
        break

    operation, *arguments = line.split()
    if operation == 'rect':
        size, *_ = arguments
        width, height = map(int, size.split('x'))
        instructions.append( ('rect', width, height) )
    else: # rotate
        direction, fixed_coord, _, rotation = arguments
        instructions.append(
            (direction, int(fixed_coord.split('=')[-1]), int(rotation))
        )

def rotate_coords(operation, fixed_coord, rotation):
    if operation == 'row':
        for x in range(WIDTH):
            new_column = (x + rotation) % WIDTH
            yield ( (new_column, fixed_coord), grid[ (x, fixed_coord) ] )
    elif operation == 'column':
        for y in range(HEIGHT):
            new_row = (y + rotation) % HEIGHT
            yield ( (fixed_coord, new_row), grid[ (fixed_coord, y) ] )

grid = {
    (x, y) : False
    for x in range(WIDTH)
    for y in range(HEIGHT)
}

for operation, *arguments in instructions:
    if operation == 'rect':
        width, height = arguments
        grid.update(
            {
                (x, y) : True
                for x in range(width)
                for y in range(height)
            }
        )
    else: # row or column
        fixed_coord, rotation = arguments
        prev_value = None
        for new_position, value in tuple(
            rotate_coords(operation, fixed_coord, rotation)
        ): # tuple otherwise mutations break rotate_coords
            prev_value = value
            grid[new_position] = value

print(sum(grid.values()))
