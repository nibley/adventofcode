grid = {}
y = 0
start_x = None
start_y = None
goal_x = None
goal_y = None
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, height in enumerate(line):
        if height == 'S':
            start_x = x
            start_y = y
            height = 'a'
        elif height == 'E':
            goal_x = x
            goal_y = y
            height = 'z'

        grid[ (x, y) ] = ord(height)

    y += 1

height = y
width = len(line)

neighbor_offsets = [
    (-1,  0),
    ( 1,  0),
    ( 0, -1),
    ( 0,  1)
]

def get_neighbors(x, y):
    for offset_x, offset_y in neighbor_offsets:
        neigbor_x = x + offset_x
        neighbor_y = y + offset_y

        if (
            0 <= neigbor_x < width
            and 0 <= neighbor_y < height
            and grid[ (neigbor_x, neighbor_y) ] - grid[ (x, y) ] <= 1
        ):
            yield (neigbor_x, neighbor_y)

steps = 0
positions_to_crawl = set([ (start_x, start_y) ])
done = False
while positions_to_crawl:
    new_positions_found = set()
    for x, y in positions_to_crawl:
        if (x, y) == (goal_x, goal_y):
            done = True
            break

        new_positions_found.update(get_neighbors(x, y))

    if done:
        break

    steps += 1
    positions_to_crawl = new_positions_found

print(steps)
