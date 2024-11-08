grid = []
while True:
    try:
        line = input()
    except EOFError:
        break

    grid.append([*map(int, line)])

height = len(grid)
width = len(grid[0])

num_visible_tree_heights = 0
for y in range(height):
    for x in range(width):
        this_tree_height = grid[y][x]

        if any(
            all(
                tree_height < this_tree_height
                for tree_height in line_of_sight
            )
            for line_of_sight in (
                [ grid[i][x] for i in range(0, y) ],
                [ grid[i][x] for i in range(y + 1, height) ],
                [ grid[y][i] for i in range(0, x) ],
                [ grid[y][i] for i in range(x + 1, width) ]
            )
        ):
            num_visible_tree_heights += 1

print(num_visible_tree_heights)
