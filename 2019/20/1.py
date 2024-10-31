# modified from 2019 17

from collections import defaultdict, deque

neighbor_offsets = [
    ( 0,  1),
    ( 0, -1),
    (-1,  0),
    ( 1,  0),
]

def get_neighbors(position):
    if position in portals:
        yield portals[position]

    x, y = position
    for offset_x, offset_y in neighbor_offsets:
        neighbor = (x + offset_x, y + offset_y)

        if grid[neighbor]:
            yield neighbor

def visualize(highlight=()):
    print('  ', ''.join(str(x)[-1] for x in range(width)), '\n')

    for y in range(height):
        print(str(y)[-1], ' ', end='')

        for x in range(width):
            if (x, y) in portals and (x, y) in highlight:
                print('0', end='')
            elif position in portals:
                print('O', end='')
            elif neighbor in highlight:
                print('_', end='')
            elif grid[neighbor]:
                print('.', end='')
            else:
                print('#', end='')
        print()
    print()

y = 0
width = None
grid = defaultdict(lambda: False)
portal_letters = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    if width is None:
        width = len(line)

    for x, cell in enumerate(line):
        if cell == '.':
            grid[ (x, y) ] = True
        elif cell.isalpha():
            portal_letters[ (x, y) ] = cell

    y += 1

height = y

start_position = None
goal_position = None
portal_groups = defaultdict(list)
for (x, y), cell in portal_letters.items():
    if (x + 1, y) in portal_letters: # first letter of horizontal portal
        portal_name = cell + portal_letters[ (x + 1, y) ]
        if grid[ (x + 2, y) ]: # label left of portal
            portal_location = (x + 2, y)
        else: # label right of portal
            portal_location = (x - 1, y)
    elif (x, y + 1) in portal_letters: # first letter of vertical portal
        portal_name = cell + portal_letters[ (x, y + 1) ]
        if grid[ (x, y + 2) ]: # label above portal
            portal_location = (x, y + 2)
        else: # label below portal
            portal_location = (x, y - 1)
    else: # second letter of portal
        continue

    if portal_name == 'AA':
        assert start_position is None
        start_position = portal_location
    elif portal_name == 'ZZ':
        assert goal_position is None
        goal_position = portal_location
    else:
        portal_groups[portal_name].append(portal_location)

portals = {}
for portal_group in portal_groups.values():
    assert len(portal_group) == 2
    first_portal, second_portal = portal_group

    portals[first_portal] = second_portal
    portals[second_portal] = first_portal

done = False
steps = 0
visited = set([start_position])
positions_to_crawl = deque([start_position])
while positions_to_crawl:
    new_positions_found = deque()
    # visualize(visited)

    for position in positions_to_crawl:
        if position == goal_position:
            done = True
            break

        for neighbor in get_neighbors(position):
            if neighbor not in visited:
                visited.add(neighbor)
                new_positions_found.append(neighbor)

    if done:
        break

    steps += 1
    positions_to_crawl = new_positions_found

print(steps)
