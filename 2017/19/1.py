grid = []
while True:
    try:
        line = input()
    except EOFError:
        break

    grid.append(list(line))

height = len(grid)
width = len(grid[0])

def get_cell(x, y):
    if (
        0 <= x < width
        and 0 <= y < height
    ):
        return grid[y][x]
    else:
        return ' '

packet_x = grid[0].index('|')
packet_y = 0
direction_x = 0
direction_y = 1

def visualize():
    print(f'({packet_x}, {packet_y})', letters)
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if x == packet_x and y == packet_y:
                print('O', end='')
            else:
                print(grid[y][x], end='')
        print()
    print()

letters = ''
while True:
    # visualize()

    current_cell = get_cell(packet_x, packet_y)
    if current_cell.isalpha():
        letters += current_cell

    next_x = packet_x + direction_x
    next_y = packet_y + direction_y
    next_cell = get_cell(next_x, next_y)

    if direction_x == 0: # up or down
        packet_y = next_y
        if next_cell == '+':
            direction_y = 0
            direction_x = 1 if get_cell(next_x - 1, next_y) == ' ' else -1
        elif next_cell == ' ':
            break # done
    elif direction_y == 0: # left or right
        packet_x = next_x
        if next_cell == '+':
            direction_x = 0
            direction_y = 1 if get_cell(next_x, next_y - 1) == ' ' else -1
        elif next_cell == ' ':
            break # done

print(letters)
