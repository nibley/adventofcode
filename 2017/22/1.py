from collections import defaultdict

grid = defaultdict(lambda: False)
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

        # True for infected, False for clean
        grid[ (column_id - offset, row_id - offset) ] = char == '#'

    row_id += 1

directions = [
    ( 0, -1), # up
    ( 1,  0), # right
    ( 0,  1), # down
    (-1,  0)  # left
]

def visualize():
    x_values = sorted(map(lambda pair: pair[0], grid.keys()))
    y_values = sorted(map(lambda pair: pair[1], grid.keys()))

    for y in range(y_values[0], y_values[-1] + 1):
        for x in range(x_values[0], x_values[-1] + 1):
            print('#' if grid[ (x, y) ] else '.', ' ', end='')
        print()
    print()

x = 0
y = 0
direction_index = 0

total_infections = 0
for _ in range(10_000):
    # turn based on current cell
    current_cell = grid[ (x, y) ]
    direction_index += 1 if current_cell else -1
    direction_index %= len(directions)

    # flip current cell
    if not current_cell:
        total_infections += 1

    grid[ (x, y) ] = not current_cell

    # move forward
    x_offset, y_offset = directions[direction_index]
    x += x_offset
    y += y_offset

# visualize()
print(total_infections)
