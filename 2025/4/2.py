from itertools import product as cartesian_product

grid = []

while True:
    try:
        line = input()
    except EOFError:
        break

    grid.append(list( cell == '@' for cell in line ))

HEIGHT = len(grid)
WIDTH = len(line)

direction_offsets = (
    (-1, -1),
    ( 0, -1),
    ( 1, -1),
    (-1,  0),
    ( 1,  0),
    (-1,  1),
    ( 0,  1),
    ( 1,  1)
)

def get_score(x, y):
    score = 0

    for x_offset, y_offset in direction_offsets:
        neighbor_x = x + x_offset
        neighbor_y = y + y_offset
        if not (neighbor_x in range(WIDTH) and neighbor_y in range(HEIGHT)):
            continue

        if grid[neighbor_y][neighbor_x]:
            score += 1

    return score

total = 0
while True:
    found_removal = False
    for x, y in cartesian_product(range(WIDTH), range(HEIGHT)):
        if grid[y][x] and get_score(x, y) < 4:
            total += 1
            found_removal = True
            grid[y][x] = False
    
    if not found_removal:
        break

print(total)
