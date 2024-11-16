# modified from 2018 13

from itertools import chain

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

def get_num_energized_cells(initial):
    all_beams = set()
    current_beams = set([ initial ])
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

    return ( len(set(position for position, _ in all_beams)), all_beams )

best_total, best_beams = max(
    get_num_energized_cells(initial)
    for initial in chain(
        ( ((width - 1, y), '<') for y in range(height) ),
        ( ((0, y), '>') for y in range(height) ),
        ( ((x, height - 1), '^') for x in range(width) ),
        ( ((x, 0), 'v') for x in range(width) )
    )
)

def visualize(beams):
    display_grid = [ list(row) for row in grid ]

    for (x, y), beam_char in beams:
        display_grid[y][x] = beam_char

    for row in display_grid:
        print(''.join(row))

    print()
# visualize(best_beams)

print(best_total)
