grid = []
while True:
    try:
        line = input()
    except EOFError:
        break

    grid.append(list(line))

height = len(grid)
width = len(grid[0])

def visualize():
    for row in grid:
        print(''.join(row))
    print()

# visualize()

turn = 0
found_move = True
while found_move:
    turn += 1
    found_move = False
    new_grid = [ row[:] for row in grid ]

    for y, row in enumerate(grid):
        for x, cell in reversed(tuple(enumerate(row))):
            check_x = (x + 1) % width
            if row[x] == '>' and row[check_x] == '.':
                found_move = True
                new_grid[y][x] = '.'
                new_grid[y][check_x] = '>'

    grid = new_grid
    new_grid = [ row[:] for row in grid ]

    for x in range(width):
        for y in range(height):
            check_y = (y + 1) % height
            if grid[y][x] == 'v' and grid[check_y][x] == '.':
                found_move = True
                new_grid[y][x] = '.'
                new_grid[check_y][x] = 'v'

    grid = new_grid
    # visualize()

# visualize()
print(turn)
