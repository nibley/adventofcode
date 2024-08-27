buttons = {
    -1: {
        -1: '7',
        0: '4',
        1: '1',
    },
    0: {
        -1: '8',
        0: '5',
        1: '2',
    },
    1: {
        -1: '9',
        0: '6',
        1: '3',
    },
}

def make_move(direction):
    if direction == 'U':
        blocked = y == 1
    elif direction == 'D':
        blocked = y == -1
    elif direction == 'L':
        blocked = x == -1
    elif direction == 'R':
        blocked = x == 1
    
    if blocked:
        return (x, y)
    
    if direction == 'U':
        return (x, y + 1)
    elif direction == 'D':
        return (x, y - 1)
    elif direction == 'L':
        return (x - 1, y)
    elif direction == 'R':
        return (x + 1, y)

lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    
    lines.append(line)

x, y = (0, 0)
code = ''
for line in lines:
    for direction in line:
        x, y = make_move(direction)
    button = buttons[x][y]
    code += button

print(code)
