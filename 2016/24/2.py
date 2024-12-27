nodes = {}
grid = {}
y = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, char in enumerate(line):
        if char not in '.#':
            nodes[char] = (x, y)

        grid[ (x, y) ] = char

    y += 1

def get_edges(start_node):
    steps = 0
    visited = set()
    positions_to_crawl = {nodes[start_node]}
    while positions_to_crawl:
        new_positions_found = set()

        for position in positions_to_crawl:
            visited.add(position)

            cell = grid[position]
            if cell in nodes and cell != start_node:
                yield (cell, steps)

            x, y = position
            for x_offset, y_offset in (
                (-1,  0),
                ( 1,  0),
                ( 0, -1),
                ( 0,  1)
            ):
                neighbor = (x + x_offset, y + y_offset)

                if (
                    neighbor not in visited
                    and grid.get(neighbor, '#') != '#'
                ):
                    new_positions_found.add(neighbor)

        steps += 1
        positions_to_crawl = new_positions_found

edges = { node : {} for node in nodes }
for node in nodes:
    for other_node, steps in get_edges(node):
        edges[node][other_node] = steps
        edges[other_node][node] = steps

def get_route_costs(node, visited=None, steps=0):
    if visited is None:
        visited = frozenset({node})
    elif not set(nodes) - visited:
        yield node, steps
        return

    for goal, edge in edges[node].items():
        if goal not in visited:
            yield from get_route_costs(
                goal,
                visited | {goal},
                steps + edge
            )

print(
    min(
        steps + edges[end_node]['0']
        for end_node, steps in get_route_costs('0')
    )
)
