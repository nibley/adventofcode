grid = []
while True:
    try:
        line = input()
    except EOFError:
        break

    grid.append(list(line))

height = len(grid)
width = len(grid[0])

def get_cell(x, y):
    row = grid[y]
    return row[ x % width ]

x = 0
y = 0
num_trees = 0
while y < height:
    cell = get_cell(x, y)
    if cell == '#':
        num_trees += 1

    x += 3
    y += 1

print(num_trees)
