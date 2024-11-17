from collections import defaultdict, Counter

grid = defaultdict(lambda: None) # None for open acres
y = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, char in enumerate(line):
        if char != '.':
            grid[ (x, y) ] = char

    y += 1

height = y
width = len(line)

def get_neighbors(x, y):
    forest_total = 0
    lumberyard_total = 0

    for x_offset, y_offset in (
        (-1, -1), (0, -1), (1, -1), (-1, 0),
        (1, 0), (-1, 1), (0, 1), (1, 1)
    ):
        cell = grid[ (x + x_offset, y + y_offset) ]
        if cell == '|':
            forest_total += 1
        elif cell == '#':
            lumberyard_total += 1

    return (forest_total, lumberyard_total)

for _ in range(10):
    next_grid = defaultdict(lambda: None)
    for y in range(height):
        for x in range(width):
            cell = grid[ (x, y) ]
            forest_total, lumberyard_total = get_neighbors(x, y)

            if cell is None:
                cell = '|' if forest_total > 2 else None
            elif cell == '|':
                cell = '#' if lumberyard_total > 2 else '|'
            elif cell == '#':
                cell = '#' if lumberyard_total and forest_total else None

            next_grid[ (x, y) ] = cell

    grid = next_grid

def visualize():
    for y in range(height):
        print(
            ''.join(
                str(grid[ (x, y) ]) if grid[ (x, y) ] is not None else '.'
                for x in range(width)
            )
        )
    print()
# visualize()

acre_totals = Counter(grid.values())
print(acre_totals['|'] * acre_totals['#'])
