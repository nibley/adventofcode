from collections import defaultdict

directions = {
    'U': ( 0, -1),
    'R': ( 1,  0),
    'D': ( 0,  1),
    'L': (-1,  0)
}

instructions = []
while True:
    try:
        line = input()
    except EOFError:
        break

    direction, distance, _ = line.split(' ')
    instructions.append( (direction, int(distance)) )

x = 0
y = 0
# False for ground, True for trench
grid = defaultdict(lambda: False, { (x, y): True })
for direction, distance in instructions:
    x_offset, y_offset = directions[direction]
    for _ in range(distance):
        x += x_offset
        y += y_offset

        grid[ (x, y) ] = True

# should have gone in a loop
assert (x, y) == (0, 0)

trench_directions = tuple(
    (x_offset, y_offset)
    for x_offset, y_offset in directions.values()
    if grid[ (x + x_offset, y + y_offset) ]
)

# should have exactly 2 directions dug from (0, 0)
assert len(trench_directions) == 2

interior_x, interior_y = x, y
for x_offset, y_offset in trench_directions:
    if not grid[ (interior_x + x_offset, interior_y + y_offset) ]:
        # found free space in this direction
        interior_x += x_offset
        interior_y += y_offset
    else:
        # found a wall, go in the opposite direction
        interior_x -= x_offset
        interior_y -= y_offset

# now we have one position in the interior of the loop
interior_position = (interior_x, interior_y)
assert not grid[interior_position]

# BFS to find entire interior
direction_offsets = directions.values()
visited = set([interior_position])
positions_to_crawl = set([interior_position])
while positions_to_crawl:
    new_positions_found = set()
    for position_x, position_y in positions_to_crawl:
        for x_offset, y_offset in direction_offsets:
            neighbor = (position_x + x_offset, position_y + y_offset)
            if (
                not grid[neighbor]
                and neighbor not in visited
            ):
                new_positions_found.add(neighbor)
                visited.add(neighbor)

    positions_to_crawl = new_positions_found

def visualize(highlight=()):
    min_x, *_, max_x = sorted(x for x, _ in grid)
    min_y, *_, max_y = sorted(y for _, y in grid)

    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            position = (x, y)
            if position in highlight:
                char = ' '
            elif grid[position]:
                char = '#'
            else:
                char = '.'
            print(char, end='')
        print()
    print()
# visualize(visited)

# trench cells + interior cells
print(sum(grid.values()) + len(visited))
