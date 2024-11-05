grid = []
while True:
    try:
        line = input()
    except EOFError:
        break

    grid.append([ int(char) for char in line ])

height = len(grid)
width = len(grid[0])

neighbor_offsets = [
    (-1, -1),
    (-1,  0),
    (-1,  1),
    ( 0, -1),
    ( 0,  1),
    ( 1, -1),
    ( 1,  0),
    ( 1,  1),
]

def get_neighbors(x, y):
    for offset_x, offset_y in neighbor_offsets:
        neighbor_x = x + offset_x
        neighbor_y = y + offset_y
        if (
            0 <= neighbor_x < width
            and 0 <= neighbor_y < height
        ):
            yield (neighbor_x, neighbor_y)

def simulate_turn(grid):
    flashes = set()
    num_flashes = 0
    next_generation = [ [cell + 1 for cell in row] for row in grid ]
    while True:
        found_flash = False
        for y in range(height):
            for x in range(width):
                if (
                    (x, y) not in flashes
                    and next_generation[y][x] > 9
                ):
                    found_flash = True
                    flashes.add( (x, y) )
                    num_flashes += 1
                    for neighbor_x, neighbor_y in get_neighbors(x, y):
                        next_generation[neighbor_y][neighbor_x] += 1

        if not found_flash:
            break

    for x, y in flashes:
        next_generation[y][x] = 0

    return (next_generation, num_flashes)

total_flashes = 0
for _ in range(100):
    grid, num_flashes = simulate_turn(grid)
    total_flashes += num_flashes

print(total_flashes)
