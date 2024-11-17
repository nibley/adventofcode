from math import sqrt
from collections import Counter

def get_input_lines():
    try:
        while True:
            yield input()
    except EOFError:
        return

input_char_conversion = {
    '.': None,
    '|': False,
    '#': True
}

# use a flat data structure instead of a grid
# one row directly follows the end of the next
# values are None for open, True for lumber, False for forest
grid_original = tuple(
    input_char_conversion[char]
    for line in get_input_lines()
    for char in line
)

side_length_test = sqrt(len(grid_original))
assert side_length_test.is_integer()
SIDE_LENGTH = int(side_length_test)
COORD_BOUNDS = range(SIDE_LENGTH)

neighbor_offsets = (
    (-1, -1), ( 0, -1), (1, -1), (-1, 0),
    ( 1,  0), (-1,  1), (0,  1), ( 1, 1)
)

def get_cell_next_value(index, cell):
    y, x = divmod(index, SIDE_LENGTH)

    forest_total = 0
    lumberyard_total = 0
    for x_offset, y_offset in neighbor_offsets:
        neighbor_x = x + x_offset
        neighbor_y = y + y_offset

        neighbor = (
            grid[neighbor_y * SIDE_LENGTH + neighbor_x]
            if neighbor_x in COORD_BOUNDS and neighbor_y in COORD_BOUNDS
            else None
        )

        if neighbor is False:
            forest_total += 1
        elif neighbor is True:
            lumberyard_total += 1

    if cell is None and forest_total > 2:
        return False
    elif cell is False:
        return lumberyard_total > 2
    elif cell is True and lumberyard_total and forest_total:
        return True
    else:
        return None

simulate_turn = lambda grid: tuple(
    get_cell_next_value(*index_and_cell)
    for index_and_cell in enumerate(grid)
)

grid_hashes = []
grid = grid_original
grid_hash = hash(grid)
while grid_hash not in grid_hashes:
    grid_hashes.append(grid_hash)

    grid = simulate_turn(grid)
    grid_hash = hash(grid)

REQUIRED_TURNS = 1_000_000_000
turns_til_repeat = len(grid_hashes) - grid_hashes.index(grid_hash)
further_required_turns = REQUIRED_TURNS - len(grid_hashes)
required_modulo = further_required_turns % turns_til_repeat

for _ in range(required_modulo):
    grid = simulate_turn(grid)

def visualize():
    for y in range(SIDE_LENGTH):
        print(
            ''.join(
                next(
                    k
                    for k, v in input_char_conversion.items()
                    if v == grid[y * SIDE_LENGTH + x]
                )
                for x in range(SIDE_LENGTH)
            )
        )
    print()
# visualize()

acre_totals = Counter(grid)
print(acre_totals[True] * acre_totals[False])
