# modified from 2018 13

grid = []
while True:
    try:
        line = input()
    except EOFError:
        break

    grid.append(tuple(line))

grid = tuple(grid)
height = len(grid)
width = len(grid[0])

neighbor_offsets = {
    '<': (-1,  0),
    '>': ( 1,  0),
    '^': ( 0, -1),
    'v': ( 0,  1)
}

all_beams = set()
current_beams = set([ ((0, 0), '>') ])
while current_beams.difference(all_beams):
    all_beams.update(current_beams)
    new_beams = set()
    for (x, y), beam_char in current_beams:
        cell = grid[y][x]

        if (
            beam_char in '<>' and cell in '-.'
            or beam_char in '^v' and cell in '|.'
        ):
            new_directions = beam_char # pass through
        elif cell == '|' and beam_char in '<>':
            new_directions = '^v' # split
        elif cell == '-' and beam_char in '^v':
            new_directions = '<>' # split
        elif (
            cell == '/' and beam_char == 'v'
            or cell == '\\' and beam_char == '^'
        ):
            new_directions = '<' # bounce
        elif (
            cell == '/' and beam_char == '^'
            or cell == '\\' and beam_char == 'v'
        ):
            new_directions = '>' # bounce
        elif (
            cell == '/' and beam_char == '>'
            or cell == '\\' and beam_char == '<'
        ):
            new_directions = '^' # bounce
        elif (
            cell == '/' and beam_char == '<'
            or cell == '\\' and beam_char == '>'
        ):
            new_directions = 'v' # bounce

        for new_direction in new_directions:
            x_offset, y_offset = neighbor_offsets[new_direction]
            new_x, new_y = x + x_offset, y + y_offset
            if 0 <= new_x < width and 0 <= new_y < height:
                new_beams.add( ((new_x, new_y), new_direction) )

    current_beams = new_beams.difference(all_beams)

print(len(set(position for position, _ in all_beams)))
