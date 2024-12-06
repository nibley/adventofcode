grid = {}
y = 0

guard_x = None
guard_y = None

while True:
    try:
        line = input()
    except EOFError:
        break
    
    for x, cell in enumerate(line):
        grid[ (x, y) ] = cell in '.^'
        if cell == '^':
            guard_x = x
            guard_y = y

    y += 1

height = y
width = len(line)

print(guard_x, guard_y)
print('height', height)
print('width', width)

facing = 0

offsets = (
    # north
    (0, -1),
    # east
    (1, 0),
    # south
    (0, 1),
    # west
    (-1, 0)
)

visited = set()
while guard_x in range(width) and guard_y in range(height):
    visited.add( (guard_x, guard_y) )
    print(len(visited), guard_x, guard_y)
    x_offset, y_offset = offsets[facing]
    target = grid.get( (guard_x + x_offset, guard_y + y_offset) )
    if target is True:
        guard_x += x_offset
        guard_y += y_offset
    elif target is None:
        print(guard_x, guard_y, 'NONE')
        break
    else:
        facing = (facing + 1) % 4

print(len(visited))