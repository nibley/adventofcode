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

def get_score(x, y):
    score = 0

    if x > 0 and y > 0 and grid[y - 1][x - 1]:
        score += 1
    
    if x < WIDTH - 1 and y > 0 and grid[y - 1][x + 1]:
        score += 1

    if x > 0 and y < HEIGHT - 1 and grid[y + 1][x - 1]:
        score += 1

    if x < WIDTH - 1 and y < HEIGHT - 1 and grid[y + 1][x + 1]:
        score += 1

    if y > 0 and grid[y - 1][x]:
        score += 1
    
    if y < HEIGHT - 1 and grid[y + 1][x]:
        score += 1

    if x > 0 and grid[y][x - 1]:
        score += 1
    
    if x < WIDTH - 1 and grid[y][x + 1]:
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
    