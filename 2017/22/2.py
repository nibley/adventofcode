from collections import defaultdict

grid = defaultdict(lambda: 0) # 0 for clean
row_id = 0
offset = None
while True:
    try:
        line = input()
    except EOFError:
        break

    for column_id, char in enumerate(line):
        if offset is None:
            offset = len(line) // 2

        # 2 for infected, 0 for clean (later, weakened is 1 and flagged is 3)
        grid[ (column_id - offset, row_id - offset) ] = 2 if char == '#' else 0

    row_id += 1

directions = [
    ( 0, -1), # up
    ( 1,  0), # right
    ( 0,  1), # down
    (-1,  0)  # left
]

def visualize():
    chars = {0: '.', 1: '*', 2: '#', 3: '&'}
    x_values = sorted(map(lambda pair: pair[0], grid.keys()))
    y_values = sorted(map(lambda pair: pair[1], grid.keys()))

    for y in range(y_values[0], y_values[-1] + 1):
        for x in range(x_values[0], x_values[-1] + 1):
            print(chars[ grid[ (x, y) ] ], ' ', end='')
        print()
    print()

x = 0
y = 0
direction_index = 0

total_infections = 0
for _ in range(10_000_000):
    # turn based on current cell
    current_cell = grid[ (x, y) ]

    if current_cell == 0: # clean
        direction_index += -1
    elif current_cell == 2: # infected
        direction_index += 1
    elif current_cell == 3: # flagged
        direction_index += 2

    direction_index %= len(directions)

    # flip current cell
    if current_cell == 1:
        total_infections += 1

    grid[ (x, y) ] = (current_cell + 1) % 4

    # move forward
    x_offset, y_offset = directions[direction_index]
    x += x_offset
    y += y_offset

# visualize()
print(total_infections)
