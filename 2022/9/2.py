instructions = []
while True:
    try:
        line = input()
    except EOFError:
        break

    direction, steps = line.split(' ')
    instructions.append( (direction, int(steps)) )

taxicab_distance = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])

def move_node(node):
    predecessor_position = nodes[node - 1]
    node_position = nodes[node]
    distance = taxicab_distance(predecessor_position, node_position)

    if distance < 2:
        return node_position

    predecessor_x, predecessor_y = predecessor_position
    node_x, node_y = node_position

    same_row = predecessor_y == node_y
    same_column = predecessor_x == node_x
    x_distance = abs(predecessor_x - node_x)
    y_distance = abs(predecessor_y - node_y)

    diagonal_needed = (
        not (same_row or same_column)
        and (x_distance == 2 or y_distance == 2)
    )

    if diagonal_needed or same_row:
        node_x += 1 if predecessor_x > node_x else -1

    if diagonal_needed or same_column:
        node_y += 1 if predecessor_y > node_y else -1

    return (node_x, node_y)

nodes = {
    i : (0, 0)
    for i in range(10)
}
tail_locations = set([ (0, 0) ])
for direction, steps in instructions:
    for _ in range(steps):
        head_x, head_y = nodes[0]

        if direction == 'U':
            head_y -= 1
        elif direction == 'D':
            head_y += 1
        elif direction == 'L':
            head_x -= 1
        elif direction == 'R':
            head_x += 1

        nodes[0] = (head_x, head_y)

        for node in range(1, 10):
            nodes[node] = move_node(node)

        tail_locations.add(nodes[9])

def visualize():
    x_sorted = sorted(tail_locations, key=lambda pair: pair[0])
    y_sorted = sorted(tail_locations, key=lambda pair: pair[1])
    for y in range(y_sorted[0][1], y_sorted[-1][1] + 1):
        for x in range(x_sorted[0][0], x_sorted[-1][0] + 1):
            print('x' if (x, y) in tail_locations else ' ', end='')
        print()
# visualize()

print(len(tail_locations))
