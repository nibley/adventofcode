def access_grid(position):
    x, y = position
    if 0 <= y < height and 0 <= x < width:
        return grid[y][x]
    else:
        return '.'

def get_neighbors(position):
    for offset in neighbor_offsets:
        neighbor = get_offset(position, offset)
        neighbor_terrain = access_grid(neighbor)
        yield (offset, neighbor, neighbor_terrain)

def get_offset(position, offset):
    x, y = position
    offset_x, offset_y = offset
    return (x + offset_x, y + offset_y)

def get_neighbor_pipes(position):
    position_terrain = access_grid(position)
    for offset, neighbor, neighbor_terrain in get_neighbors(position):
        if (
            neighbor_terrain != '.'
            and neighbor_terrain in connection_options[position_terrain][offset]
        ):
            yield (offset, neighbor, neighbor_terrain)

def get_inverse_offset(offset):
    offset_x, offset_y = offset
    return (-1 * offset_x, -1 * offset_y)

neighbor_offsets = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]
connection_options = {
    '|': {
        (-1,  0): '',
        ( 1,  0): '',
        ( 0, -1): '|7F',
        ( 0,  1): '|JL',
    },
    '-': {
        (-1,  0): '-LF',
        ( 1,  0): '-J7',
        ( 0, -1): '',
        ( 0,  1): '',
    },
    'L': {
        (-1,  0): '',
        ( 1,  0): '-J7',
        ( 0, -1): '|7F',
        ( 0,  1): '',
    },
    'J': {
        (-1,  0): '-LF',
        ( 1,  0): '',
        ( 0, -1): '|7F',
        ( 0,  1): '',
    },
    '7': {
        (-1,  0): '-LF',
        ( 1,  0): '',
        ( 0, -1): '',
        ( 0,  1): '|JL',
    },
    'F': {
        (-1,  0): '',
        ( 1,  0): '-J7',
        ( 0, -1): '',
        ( 0,  1): '|JL',
    }
}

grid = []
while True:
    try:
      line = input()
    except EOFError:
        break

    grid.append(list(line))

height = len(grid)
width = len(grid[0])

start_x = None
start_y = None
for y, row in enumerate(grid):
    if 'S' in row:
        assert start_x is None and start_y is None
        start_y = y
        start_x = row.index('S')
        break
start = (start_x, start_y)

# deduce pipe type for starting location
for pipe_type in '|-LJ7F':
    found_mismatch = False
    valid_connections = 0
    for offset, neighbor, neighbor_terrain in get_neighbors(start):
        inverse_offset = get_inverse_offset(offset)
        if neighbor_terrain == '.':
            continue

        possibilities = connection_options[neighbor_terrain][inverse_offset]
        if pipe_type in possibilities:
            valid_connections += 1

        if valid_connections == 2:
            break

    if valid_connections == 2:
        grid[start_y][start_x] = pipe_type
        break

position = next(get_neighbor_pipes(start))[1]
prev_position = start
loop = [start, position]
while loop[-1] != start:
    connected = get_neighbor_pipes(position)
    for _, pipe, _ in connected:
        if pipe != prev_position:
            prev_position = position
            position = pipe
            break

    loop.append(position)

print(len(loop) // 2)
