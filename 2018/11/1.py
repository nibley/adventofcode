serial = int(input())

grid = [ [0 for _ in range(300)] for _ in range(300) ]
for y in range(1, 300 + 1):
    for x in range(1, 300 + 1):
        rack = x + 10
        power = rack * y
        power += serial
        power *= rack
        if power < 100:
            power = 0
        else:
            power = power % 1000
            power = power // 100
        power -= 5

        grid[y - 1][x - 1] = power

best_position = None
best_score = 0
for y in range(1, 300 + 1 - 2):
    for x in range(1, 300 + 1 - 2):
        score = 0
        score += grid[y - 1][x - 1]
        score += grid[y - 1][x]
        score += grid[y - 1][x + 1]
        score += grid[y][x - 1]
        score += grid[y][x]
        score += grid[y][x + 1]
        score += grid[y + 1][x - 1]
        score += grid[y + 1][x]
        score += grid[y + 1][x + 1]
    
        if score > best_score:
            best_position = (x, y)
            best_score = score

print(f'{best_position[0]},{best_position[1]}')
