from itertools import combinations

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

height = y
width = len(line)

offsets = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
)

regions = []
positions_to_crawl = set(grid)
matched_positions = set()
while positions_to_crawl:
    position = positions_to_crawl.pop()
    matched_positions.add(position)

    new_region = set()
    new_region.add(position)
    regions.append(new_region)

    positions_to_crawl_for_region = set([position])
    while positions_to_crawl_for_region:
        new_in_region = set()
        for position_in_region in positions_to_crawl_for_region:
            x, y = position_in_region

            for x_offset, y_offset in offsets:
                neighbor = (
                    x + x_offset,
                    y + y_offset
                )
                if not (
                    neighbor[0] in range(width)
                    and neighbor[1] in range(height)
                ):
                    continue

                if neighbor in matched_positions:
                    continue

                if grid[neighbor] != grid[position_in_region]:
                    continue

                new_region.add(neighbor)
                matched_positions.add(neighbor)
                new_in_region.add(neighbor)

        positions_to_crawl_for_region = new_in_region

    positions_to_crawl.difference_update(new_region)


def group_into_runs(variable_coord_values, deb_const):
    print(deb_const, variable_coord_values)
    variable_coord_values = sorted(variable_coord_values)

    last_value, *variable_coord_values = variable_coord_values
    # grouped_values = [last_value]
    total = 1
    for value in variable_coord_values:
        print('  comp', last_value, value)
        if value - last_value == 1:
            # grouped_values.append(value)
            pass
        else:
            total += 1
            # grouped_values = [value]

            print('      (const ', deb_const, ')', value, 'ne', last_value)

        last_value = value


    return total


def group_fences(offset, positions):
    coord_groups = {}
    for x, y in positions:
        if offset[0] == 0: # vertical offset
            coord_groups.setdefault(y, set()).add(x)
        elif offset[1] == 0: # horizontal offset
            coord_groups.setdefault(x, set()).add(y)

    return sum(
        group_into_runs(variable, fixed)
        for fixed, variable in coord_groups.items()
    )

def perimeter(region):
    letter = grid[next(iter(region))]
    print()
    # print(letter, len(region), region)
    print(letter, len(region))

    # fence = set()
    fence = {}
    for position in region:
        x, y = position
        for offset in offsets:
            x_offset, y_offset = offset
            neighbor = (x + x_offset, y + y_offset)
            if grid.get(neighbor) != letter:
                # fence.add(
                #     (position, offset)
                # )
                fence.setdefault(offset, set()).add(position)
                # print('  ', position, 'pointing', offset)

    sides = 0
    # print(len(region), letter, sum(map(len, fence.values())))
    for offset, positions in fence.items():
        groups = group_fences(offset, positions)
        sides += groups
        print('  ', ('down', 'right', 'up', 'left')[offsets.index(offset)], 'groups', groups)

    print(sides, 'sides')
    return sides

print()
print(
    sum(
    # tuple(
        len(region) * perimeter(region)
        for region in regions
    )
)
