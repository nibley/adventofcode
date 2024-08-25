grid_length = 100
grid = []
for _ in range(grid_length):
    grid.append([False] * grid_length)

def num_on(grid):
    return sum(len([column for column in row if column]) for row in grid)

def step(grid):
    new_grid = []
    for i in range(grid_length):
        new_row = []
        for j in range(grid_length):
            new_row.append(step_cell(i, j))
        new_grid.append(new_row)
    
    return new_grid

def step_cell(i, j):
    neighbors = cell_neighbors(i, j)
    num_neighbors_on = len([neighbor for neighbor in neighbors if neighbor])
    if grid[i][j]:
        return num_neighbors_on in [2, 3]
    else:
        return num_neighbors_on == 3

def cell_neighbors(i, j):
    neighbors = []
    is_edge = lambda i: i in [0, grid_length - 1]
    offset = lambda i: 1 if i == 0 else -1
    if is_edge(i) and is_edge(j):
        neighbors.append(grid[i + offset(i)][j + offset(j)])
        neighbors.append(grid[i][j + offset(j)])
        neighbors.append(grid[i + offset(i)][j])
    elif is_edge(i) or is_edge(j):
        if is_edge(i):
            neighbors.append(grid[i + offset(i)][j - 1])
            neighbors.append(grid[i + offset(i)][j])
            neighbors.append(grid[i + offset(i)][j + 1])
            neighbors.append(grid[i            ][j - 1])
            neighbors.append(grid[i            ][j + 1])
        else:
            neighbors.append(grid[i - 1][j + offset(j)])
            neighbors.append(grid[i    ][j + offset(j)])
            neighbors.append(grid[i + 1][j + offset(j)])
            neighbors.append(grid[i - 1][j])
            neighbors.append(grid[i + 1][j])
    else:
        neighbors.append(grid[i + 1][j + 1])
        neighbors.append(grid[i - 1][j - 1])
        neighbors.append(grid[i + 1][j - 1])
        neighbors.append(grid[i - 1][j + 1])
        neighbors.append(grid[i    ][j - 1])
        neighbors.append(grid[i    ][j + 1])
        neighbors.append(grid[i + 1][j])
        neighbors.append(grid[i - 1][j])

    return neighbors

row = 0
while True:
    try:
        line = input()
    except EOFError:
        break
    
    for column, char in enumerate(line):
        if char == '#':
            grid[row][column] = True    
    row += 1

num_steps = 100
for _ in range(num_steps):
    grid = step(grid)

    # for row in grid:
    #     print(''.join(['#' if column else '.' for column in row]))
    # print('\n')

print(num_on(grid))
