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

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

total_tree_count = 1
for delta_x, delta_y in slopes:
    x = 0
    y = 0
    tree_count = 0
    while y < height:
        cell = get_cell(x, y)
        if cell == '#':
            tree_count += 1

        x += delta_x
        y += delta_y
    
    total_tree_count *= tree_count

print(total_tree_count)
