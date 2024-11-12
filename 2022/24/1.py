blizzards_initial = []
y = 0
start_x = None
while True:
    try:
        line = input()
    except EOFError:
        break

    if y == 0:
        start_x = line.index('.') - 1

    for x, char in enumerate(line):
        if char in '.#':
            continue

        direction = '<>^v'.index(char)
        blizzards_initial.append((
            direction,
            (x - 1, y - 1) # exclude walls from coords
        ))

    y += 1

# exclude walls
height = y - 2
width = len(line) - 2

start_position = (start_x, -1)
goal_position = (line.index('.') - 1, height)

def get_blizzard_position(turn, blizzard):
    direction, (x, y) = blizzard

    if direction == 0: # left
        return ( (x - turn) % width, y )
    elif direction == 1: # right
        return ( (x + turn) % width, y )
    elif direction == 2: # up
        return ( x, (y - turn) % height )
    elif direction == 3: # down
        return ( x, (y + turn) % height )

neighbor_offsets = [
    ( 0,  1),
    ( 0, -1),
    (-1,  0),
    ( 1,  0),
]

def get_neighbors(position):
    x, y = position

    for offset_x, offset_y in neighbor_offsets:
        neighbor_x = x + offset_x
        neighbor_y = y + offset_y

        if 0 <= neighbor_x < width and (
            0 <= neighbor_y < height
            or (neighbor_x, neighbor_y) == goal_position
        ):
            yield (neighbor_x, neighbor_y)

done = False
turns = 0
positions_to_crawl = set([start_position])
while positions_to_crawl:
    turns += 1
    blizzards = set(
        get_blizzard_position(turns, blizzard)
        for blizzard in blizzards_initial
    )
    new_positions_found = set()
    for position in positions_to_crawl:
        # neighbors plus waiting in the same spot
        for neighbor in (position, *get_neighbors(position)):
            if neighbor in blizzards:
                continue
            elif neighbor == goal_position:
                done = True
                break
            else:
                new_positions_found.add(neighbor)

    if done:
        break

    positions_to_crawl = new_positions_found

print(turns)
