grid = []
while True:
    try:
        line = input()
    except EOFError:
        break

    row = list(line)
    grid.append(row)

height = len(grid)
width = len(grid[0])

def get_neighbors(x, y):
    neighbors = []

    if x > 0: # right
        neighbors.append(grid[y][x - 1])

        if y > 0: # right and down
            neighbors.append(grid[y - 1][x - 1])
        if y < height - 1: # right and up
            neighbors.append(grid[y + 1][x - 1])
    
    if x < width - 1: # left
        neighbors.append(grid[y][x + 1])

        if y > 0: # left and down
            neighbors.append(grid[y - 1][x + 1])
        if y < height - 1: # left and up
            neighbors.append(grid[y + 1][x + 1])

    if y > 0: # down
        neighbors.append(grid[y - 1][x])

    if y < height - 1: # up
        neighbors.append(grid[y + 1][x])

    return neighbors

def visualize():
    for row in grid:
        print(''.join(row))
    print()

for _ in range(1_000_000_000):
    # visualize()
    if not _ % 10_000:
        print(_)

    next_grid = [ [None for _ in range(width)] for _ in range(height) ]
    for y in range(height):
        for x in range(width):
            cell = grid[y][x]
            neighbors = get_neighbors(x, y)
            if cell == '.':
                cell = '|' if neighbors.count('|') > 2 else '.'
            elif cell == '|':
                cell = '#' if neighbors.count('#') > 2 else '|'
            elif cell == '#':
                cell = '#' if neighbors.count('#') > 0 \
                    and neighbors.count('|') > 0 else '.'
            
            next_grid[y][x] = cell

    grid = next_grid

visualize()

forest_total = 0
lumberyard_total = 0

for row in grid:
    for cell in row:
        if cell == '|':
            forest_total += 1
        elif cell == '#':
            lumberyard_total += 1

print(forest_total * lumberyard_total)
