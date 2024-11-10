from collections import defaultdict

grid = defaultdict(lambda: None)
width = 0
y = 1
while True:
    line = input()
    if not line:
        break

    if len(line) > width:
        width = len(line)

    for x, cell in enumerate(line):
        one_indexed_position = (x + 1, y)
        if cell == '.':
            grid[one_indexed_position] = True # True for walkable space
        elif cell == '#':
            grid[one_indexed_position] = False # False for wall
        # (defaultdict value of None for empty space)

    y += 1

height = y
width += 1

instructions_raw = input()

instructions = []
number = ''
for char in instructions_raw:
    if char.isnumeric():
        number += char
    else:
        instructions.append(int(number))
        number = ''

        instructions.append(char)

instructions.append(int(number) if number else char)

directions_for_visualizer = {}
carat_symbols = '>v<^'
def visualize():
    print()
    for y in range(1, height):
        for x in range(1, width):
            last_direction = directions_for_visualizer.get( (x, y) )
            cell = grid.get( (x, y) )

            if last_direction is not None:
                char = carat_symbols[last_direction]
            elif cell is True:
                char = '.'
            elif cell is False:
                char = '#'
            else:
                char = ' '

            print(char, end='')
        print()
    print()

directions = [
    ( 1,  0), # 0 for right
    ( 0,  1), # 1 for down
    (-1,  0), # 2 for left
    ( 0, -1)  # 3 for up
]
direction_index = 0

y = 1
x = next(
    x
    for x in range(1, width)
    if grid[ (x, y) ]
)

for instruction in instructions:
    if type(instruction) is int:
        x_offset, y_offset = directions[direction_index]
        for _ in range(instruction):
            scan_x = x + x_offset
            scan_y = y + y_offset
            scan_cell = grid[ (scan_x, scan_y) ]
            while scan_cell is None: # None for empty space to wrap through
                scan_x = (scan_x + x_offset - 1) % (width + 1) + 1
                scan_y = (scan_y + y_offset - 1) % (height + 1) + 1
                scan_cell = grid[ (scan_x, scan_y) ]

            directions_for_visualizer[ (x, y) ] = direction_index

            if scan_cell is False: # False for wall
                break

            x, y = scan_x, scan_y
    else:
        direction_index += 1 if instruction == 'R' else -1
        direction_index %= 4

# visualize()
print(1000 * y + 4 * x + direction_index)
