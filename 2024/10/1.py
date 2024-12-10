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
        position = (x, y)
        if digit == '0':
            starts.append(position)

        grid[position] = int(digit)

    y += 1

def get_score(start):
    positions_to_crawl = set([start])
    visited = set([start])

    while positions_to_crawl:
        new_positions_found = set()

        for position in positions_to_crawl:
            x, y = position
            height = grid[position]

            for x_offset, y_offset in (
                ( 0, -1),
                ( 1,  0),
                (-1,  0),
                ( 0,  1)
            ):
                neighbor = (x + x_offset, y + y_offset)
                neighbor_height = grid.get(neighbor, inf)

                if neighbor_height - height == 1:
                    new_positions_found.add(neighbor)

        new_positions_found.difference_update(visited)
        visited.update(new_positions_found)

        positions_to_crawl = new_positions_found

    return sum( grid.get(position) == 9 for position in visited )

print(sum(map(get_score, starts)))
