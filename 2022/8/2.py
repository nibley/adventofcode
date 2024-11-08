from math import prod

grid = []
while True:
    try:
        line = input()
    except EOFError:
        break

    grid.append([*map(int, line)])

def get_view_distance(line_of_sight, this_tree_height):
    view_distance = 0
    for tree_height in line_of_sight:
        view_distance += 1
        if tree_height >= this_tree_height:
            return view_distance

    return view_distance

height = len(grid)
width = len(grid[0])

best_scenic_score = 0
for y in range(height):
    for x in range(width):
        this_tree_height = grid[y][x]

        scenic_score = prod(
            (
                get_view_distance(line_of_sight, this_tree_height)
                for line_of_sight in (
                    [ grid[i][x] for i in range(y - 1, -1, -1) ],
                    [ grid[i][x] for i in range(y + 1, height) ],
                    [ grid[y][i] for i in range(x - 1, -1, -1) ],
                    [ grid[y][i] for i in range(x + 1, width) ]
                )
            )
        )

        if scenic_score > best_scenic_score:
            best_scenic_score = scenic_score

print(best_scenic_score)
