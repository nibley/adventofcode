import datetime

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

# for square_size in range(1, 300 + 1):
t = datetime.datetime.now()
for square_size in range(1, 300 + 1)[::-1]:
    print(square_size)
    now = datetime.datetime.now()
    print(now - t)
    t = now
    print()

    for y in range(300 - square_size + 1):
        for x in range(300 - square_size + 1):
            # print('  ', x, y, square_size)
            score = 0
            for y_offset in range(square_size):
                for x_offset in range(square_size):
                    score += grid[y + y_offset][x + x_offset]
        
            if score > best_score:
                best_position = (x + 1, y + 1, square_size)
                best_score = score

print(','.join(map(str, best_position)))
