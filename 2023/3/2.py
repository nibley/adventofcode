from collections import defaultdict
from math import prod

grid_raw = []
all_symbols = set()
while True:
    try:
        line = input()
    except EOFError:
        break

    for char in line:
        if char not in '0123456789.':
            all_symbols.add(char)

    grid_raw.append(line)

gear_symbol = '*'
all_symbols.remove(gear_symbol)
grid = []
for row in grid_raw:
    for symbol in all_symbols:
        row = row.replace(symbol, '.')

    grid.append(row)

height = len(grid)
width = len(grid[0])
def access_grid(x, y):
    # allow unbounded access defaulting to '.' character
    if 0 <= y < height and 0 <= x < width:
        return grid[y][x]
    else:
        return '.'

numbers = [] # first digit (x, y), length
for y in range(height):
    for x in range(width):
        if (
            not access_grid(x - 1, y).isnumeric()
            and access_grid(x, y).isnumeric()
        ):
            # found the start of a number, look for end
            number_end_index = x + 1
            while access_grid(number_end_index, y).isnumeric():
                number_end_index += 1 # one too high, like in slices

            numbers.append( ((x, y), number_end_index - x) )

numbers_touching_gear = defaultdict(set)
for (start_x, y), length in numbers:
    number = int(grid[y][start_x : start_x + length ])

    for cell in (
        (start_x - 1, y),
        (start_x + length, y),
        * (
            (x, y + up_or_down)
            for x in range(start_x - 1, start_x + length + 1)
            for up_or_down in (-1, 1)
        )
    ):
        if access_grid(*cell) == gear_symbol:
            numbers_touching_gear[cell].add(number)

print(
    sum(
        prod(numbers)
        for numbers in numbers_touching_gear.values()
        if len(numbers) == 2
    )
)
