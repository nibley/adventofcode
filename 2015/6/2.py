grid = []
for i in range(1000):
    grid.append([0] * 1000)

def process(x, y, command):
    if command == 'on':
        grid[x][y] += 1
    elif command == 'off':
        grid[x][y] -= 1 if grid[x][y] > 0 else 0
    else:
        grid[x][y] += 2

while True:
    try:
        line = input()
    except EOFError:
        break
    
    pieces = line.split(' through ')
    x_start, y_start = tuple(int(n) for n in pieces[0].split(' ')[-1].split(','))
    x_end, y_end = tuple(int(n) for n in pieces[1].split(','))

    if line.startswith('toggle'):
        command = 'toggle'
    elif line.startswith('turn off'):
        command = 'off'
    else:
        command = 'on'

    for y, row in enumerate(grid):
        if y_start > y or y_end < y:
            continue
        for x, light in enumerate(row):
            if x_start > x or x_end < x:
                continue
            process(x, y, command)

print(sum([sum(row) for row in grid]))
