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

unified_symbol = all_symbols.pop()
grid = []
for row in grid_raw:
    for symbol in all_symbols:
        row = row.replace(symbol, unified_symbol)

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

part_numbers_total = 0
for (start_x, y), length in numbers:
    if unified_symbol in (
        access_grid(*cell)
        for cell in (
            (start_x - 1, y),
            (start_x + length, y),
            * (
                (x, y + up_or_down)
                for x in range(start_x - 1, start_x + length + 1)
                for up_or_down in (-1, 1)
            )
        )
    ):
        part_numbers_total += int(grid[y][ start_x : start_x + length ])

print(part_numbers_total)
