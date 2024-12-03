generate_tile = lambda x, y: (
    x * (x + 3 + 2*y) + y * (1 + y) + SECRET
).bit_count() % 2 == 0

NEIGHBOR_OFFSETS = ((0, 1), (0, -1), (1, 0), (-1, 0))
def get_neighbors(position):
    x, y = position
    for x_offset, y_offset in NEIGHBOR_OFFSETS:
        neighbor_x, neighbor_y = (x + x_offset, y + y_offset)
        if (
            neighbor_x in range(MAZE_WIDTH)
            and neighbor_y in range(MAZE_HEIGHT)
            and generate_tile(neighbor_x, neighbor_y)
        ):
            yield (neighbor_x, neighbor_y)

SECRET = int(input())
START_X, START_Y = (1, 1)
STEPS = 50

MAZE_WIDTH = STEPS + START_X + 1
MAZE_HEIGHT = STEPS + START_Y + 1

locations = set([(START_X, START_Y)])
neighbors = {}
for _ in range(STEPS):
    new_locations = set()
    for location in locations:
        if location not in neighbors:
            location_neighbors = get_neighbors(location)
            neighbors[location] = location_neighbors
            new_locations.update(location_neighbors)

    if not new_locations:
        break

    locations.update(new_locations)

print(len(locations))
