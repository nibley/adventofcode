def rotate_coords(operation, n):
    if operation == 'row':
        for i in range(50):
            new_column = (i + rotation) % 50
            yield ((n, new_column), screen[n][i])
    else: # column
        for i in range(6):
            new_row = (i + rotation) % 6
            yield ((new_row, n), screen[i][n])

instructions = []
while True:
    try:
        line = input()
    except EOFError:
        break
    
    pieces = line.split(' ')
    if pieces[0] == 'rect':
        width, height = pieces[1].split('x')
        instructions.append(('rect', int(width), int(height)))
    else: # rotate
        direction = pieces[1]
        n = int(pieces[2].split('=')[1])
        rotation = int(pieces[-1])
        instructions.append((direction, int(n), int(rotation)))

screen = [[False] * 50 for _ in range(6)]
for operation, *args in instructions:
    if operation == 'rect':
        width, height = args
        for i in range(width):
            for j in range(height):
                screen[j][i] = True
    else:
        n, rotation = args
        coords = list(rotate_coords(operation, n))
        prev_value = None
        for coord, value in coords:
            i, j = coord
            screen[i][j] = prev_value = value

print(sum(len([column for column in row if column]) for row in screen))
