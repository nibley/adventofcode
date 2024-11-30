buttons = {
    (-1, -1) : '1', (-1,  0) : '4', (-1, 1) : '7',
    ( 0, -1) : '2', ( 0,  0) : '5', ( 0, 1) : '8',
    ( 1, -1) : '3', ( 1,  0) : '6', ( 1, 1) : '9'
}

def make_move(position, direction):
    x, y = position

    if direction == 'U':
        new_position = (x, y - 1)
    elif direction == 'D':
        new_position = (x, y + 1)
    elif direction == 'L':
        new_position = (x - 1, y)
    elif direction == 'R':
        new_position = (x + 1, y)

    return new_position if new_position in buttons else position

moves = []
while True:
    try:
        line = input()
    except EOFError:
        break

    moves.append(line)

position = (0, 0)
code = ''
for move in moves:
    for direction in move:
        position = make_move(position, direction)

    code += buttons[position]

print(code)
