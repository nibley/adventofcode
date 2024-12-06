grid = {}
y = 0

initial_x = None
initial_y = None

while True:
    try:
        line = input()
    except EOFError:
        break
    
    for x, cell in enumerate(line):
        grid[ (x, y) ] = cell in '.^'
        if cell == '^':
            initial_x = x
            initial_y = y

    y += 1

height = y
width = len(line)

print('height', height)
print('width', width)

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

def check(block_x, block_y):
    facing = 0
    visited = list()
    guard_x = initial_x
    guard_y = initial_y
    i = 0
    new_grid = grid.copy()
    new_grid[(block_x, block_y)] = False
    while guard_x in range(width) and guard_y in range(height):
        i += 1
        if i > 10_000:
            return True
        visited.append( (guard_x, guard_y) )
        if visited[-5:] == visited[:5]:
            return True
        # print(len(visited), guard_x, guard_y)
        x_offset, y_offset = offsets[facing]
        target = new_grid.get( (guard_x + x_offset, guard_y + y_offset) )
        if target is True:
            guard_x += x_offset
            guard_y += y_offset
        elif target is None:
            # print(guard_x, guard_y, 'NONE')
            # break
            return False
        else:
            facing = (facing + 1) % 4

    # print(len(visited))
    assert i < 10_000
    return False

total = 0
for x in range(width):
    for y in range(height):
        # print(x, y)
        if x == 0: print(y)
        if x == initial_x and y == initial_y:
            print('  skip')
            continue
        
        if check(x, y):
            print('got', total)
            total += 1

print(total)