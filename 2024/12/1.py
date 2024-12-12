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
    # print(len(positions_to_crawl))

    # for region in regions: print(len(region))
    # print()

    position = positions_to_crawl.pop()
    matched_positions.add(position)
    # print(grid[position], 'at', position)

    new_region = set()
    new_region.add(position)
    regions.append(new_region)

    positions_to_crawl_for_region = set([position])
    while positions_to_crawl_for_region:
        # print('  ', len(positions_to_crawl_for_region))

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
                # print('    ', grid[neighbor], 'at', neighbor)

        positions_to_crawl_for_region = new_in_region

    # print(new_region)
    # print()

    positions_to_crawl.difference_update(new_region)

# positions_to_crawl = unmatched_positions



print()
print(len(positions_to_crawl))
print(len(matched_positions))
print(len(regions))

def perimeter(region):
    print()
    print(len(region), region)

    fence = 0
    for position in region:
        x, y = position
        neighbors_in_region = sum(
            (x + x_offset, y + y_offset) in region
            for x_offset, y_offset in offsets
        )

        print(position, 4 - neighbors_in_region)
        fence += 4 - neighbors_in_region

    return fence

print()
for region in regions:
    # break

    assert len(set( grid[position] for position in region )) == 1
    print('region', len(region), grid[next(iter(region))])
    print('  ', perimeter(region))


print()
print(
    sum(
    # tuple(
        len(region) * perimeter(region)
        for region in regions
    )
)
