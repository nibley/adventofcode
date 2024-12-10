from math import inf

starts = []

grid = {}
y = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, digit in enumerate(line):
        grid[ (x, y) ] = inf if digit == '.' else int(digit)
        if digit == '0':
            starts.append(
                (x, y)
            )

    y += 1

height = y
width = len(line)

def get_score(start):
    # positions_to_crawl = set([start])
    visited = set([start])
    while True:
    # while positions_to_crawl:
        # new_positions_found = set()
        # for position in positions_to_crawl:
        for position in (start, ):
            x, y = position
            height = grid[ position ]

            if height == 9:
                return 1

            subtotal = 0
            for x_offset, y_offset in (
                (-1, 0), (1, 0),
                (0, -1), (0, 1)
            ):
                neighbor_x = x + x_offset
                neighbor_y = y + y_offset
                neighbor_height = grid.get((neighbor_x, neighbor_y), inf)

                # visited.add(
                    # (neighbor_x, neighbor_y)
                # )

                if neighbor_height - height != 1:
                    continue

                subtotal += get_score(
                    (neighbor_x, neighbor_y)
                )
                # new_positions_found.add(
                #     (neighbor_x, neighbor_y)
                # )

            return subtotal

        # new_positions_found.difference_update(visited)
        # visited.update(new_positions_found)
        # positions_to_crawl = new_positions_found

    # return 1
    # return visited
    return sum( grid.get(position) == 9 for position in visited )

print(
    sum(
        get_score(start)
        # 1
        for start in starts
    )
)

# print(starts)
# for x in get_score((0, 0)): print(x)
