from itertools import pairwise

grid = {}
y = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, char in enumerate(line):
        grid[ (x, y) ] = char

    y += 1

HEIGHT = y
WIDTH = len(line)

OFFSETS = (
    ( 0, -1),
    ( 1,  0),
    ( 0,  1),
    (-1,  0)
)

regions = []
positions_to_crawl = set(grid)
grouped_positions = set()
while positions_to_crawl:
    position = positions_to_crawl.pop()
    grouped_positions.add(position)

    new_region = set()
    new_region.add(position)
    regions.append(new_region)

    positions_to_crawl_in_region = set([position])
    while positions_to_crawl_in_region:
        new_positions_in_region = set()

        for position_in_region in positions_to_crawl_in_region:
            position_letter = grid[position_in_region]
            x, y = position_in_region

            for x_offset, y_offset in OFFSETS:
                neighbor_x = x + x_offset
                neighbor_y = y + y_offset
                neighbor = (neighbor_x, neighbor_y)

                if (
                    neighbor not in grouped_positions
                    and grid.get(neighbor) == position_letter
                    and  (
                        neighbor_x in range(WIDTH)
                        and neighbor_y in range(HEIGHT)
                    )
                ):
                    new_region.add(neighbor)
                    grouped_positions.add(neighbor)
                    new_positions_in_region.add(neighbor)

        positions_to_crawl_in_region = new_positions_in_region

    positions_to_crawl.difference_update(new_region)

def how_many_runs(variable_coord_values):
    return 1 + sum(
        second_value - first_value != 1
        for first_value, second_value in pairwise(
            sorted(variable_coord_values)
        )
    )

def group_fences(offset, positions):
    positions_grouped_by_fixed_coord = {}
    offset_is_vertical = offset[0] == 0
    for x, y in positions:
        if offset_is_vertical:
            positions_grouped_by_fixed_coord.setdefault(y, set()).add(x)
        else:
            positions_grouped_by_fixed_coord.setdefault(x, set()).add(y)

    return sum(map(how_many_runs, positions_grouped_by_fixed_coord.values()))

def perimeter(region):
    letter = grid[
        next(iter(region))
    ]

    fence = {}
    for position in region:
        x, y = position

        for offset in OFFSETS:
            x_offset, y_offset = offset

            neighbor = (x + x_offset, y + y_offset)
            if grid.get(neighbor) != letter:
                fence.setdefault(offset, set()).add(position)

    return sum(
        group_fences(offset, positions)
        for offset, positions in fence.items()
    )

print(
    sum(
        len(region) * perimeter(region)
        for region in regions
    )
)
