buttons = {
    -2: {
        0: '5',
    },
    -1: {
        -1: 'A',
        0: '6',
        1: '2',
    },
    0: {
        -2: 'D',
        -1: 'B',
        0: '7',
        1: '3',
        2: '1',
    },
    1: {
        -1: 'C',
        0: '8',
        1: '4',
    },
    2: {
        0: '9',
    },
}

def make_move(direction):
    current_button = buttons[x][y]

    if direction == 'U':
        blocked = current_button in '52149'
    elif direction == 'D':
        blocked = current_button in '5ADC9'
    elif direction == 'L':
        blocked = current_button in '125AD'
    elif direction == 'R':
        blocked = current_button in '149CD'
    
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
        # print(f'{buttons[x][y]} {direction}')
        x, y = make_move(direction)
    button = buttons[x][y]
    code += button

print(code)
