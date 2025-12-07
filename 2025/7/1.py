grid = []

while True:
    try:
        line = input()
    except EOFError:
        break

    row = tuple(line)
    grid.append(row)

assert len(grid) % 2 == 0

grid = grid[ : : 2 ] # don't need empty space rows

total = 0
beam_positions = set( (grid[0].index('S'), ) )

grid = grid[ 1 : ] # skip to the first row with splitters

for row in grid:
    new_beam_positions = set()
    for beam_position in beam_positions:
        if row[beam_position] == '^':
            new_beam_positions.add(beam_position - 1)
            new_beam_positions.add(beam_position + 1)

            total += 1
        else:
            new_beam_positions.add(beam_position)

    beam_positions = new_beam_positions

print(total)
