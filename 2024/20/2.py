from collections import defaultdict, deque
from math import inf

start_x = None
start_y = None

goal_x = None
goal_y = None

# grid = defaultdict(lambda: False)
grid = {}
y = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, char in enumerate(line):
        if char in 'SE':
            if char == 'S':
                start_x = x
                start_y = y
            else:
                goal_x = x
                goal_y = y

            char = '.'

        grid[ (x, y) ] = char == '.'

    y += 1

HEIGHT = y
WIDTH = len(line)

start = (start_x, start_y)
goal = (goal_x, goal_y)

def visualize(visited=()):
    for y in range(WIDTH):
        for x in range(HEIGHT):
            if (x, y) == (start_x, start_y):
                print('S', end='')
            elif (x, y) == (goal_x, goal_y):
                print('E', end='')
            elif (x, y) in visited:
                print('o', end='')
            else:
                print('.' if grid[ (x, y )] else '#', end='')
        print()
    print()

DIRECTIONS = (
    # e s w n
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
)

def get_neighbors(position):
    x, y = position

    for x_offset, y_offset in DIRECTIONS:
        new_x = x + x_offset
        new_y = y + y_offset
        new_position = (new_x, new_y)

        if (
            new_position in grid
            # new_x in range(1, WIDTH - 1)
            # and new_y in range(1, HEIGHT - 1)
            and grid[new_position]
        ):
            yield new_position

unvisited = set(
    position
    for position, is_open in grid.items()
    if is_open
)

distances_from_start = defaultdict(lambda: inf)
distances_from_start[start] = 0
came_from = {}

while unvisited:
    # if not len(unvisited) % 100: print(len(unvisited))
    # print(len(unvisited))

    position = min(unvisited, key=distances_from_start.__getitem__)
    if position == goal:
        print('DONE')
        break

    position_score = distances_from_start[position]
    for neighbor in get_neighbors(position):
        old_score = distances_from_start[neighbor]
        new_score = position_score + 1

        if new_score < old_score:
            distances_from_start[neighbor] = new_score
            came_from[neighbor] = position

    unvisited.remove(position)

assert distances_from_start[goal] < inf

position = goal
path = set()
while position != start:
    position = came_from.get(position)
    path.add(position)

path.add(position)
print('start is last', start == position)

print('start in path', start in path)
print('goal in path', goal in path)

baseline_path = len(path)
# baseline_path = len(path) - 1
print('baseline', len(path))









print()

def get_cheats(position):
    steps = 0
    end_positions = set()
    visited = {position}
    # end_positions = { (position, 0) }
    # end_positions = {position}
    positions_to_crawl = {position}

    # while steps < 6:
    while steps < 20:
        steps += 1
        new_positions_found = set()

        for x, y in positions_to_crawl:
            for x_offset, y_offset in DIRECTIONS:
                neighbor = (x + x_offset, y + y_offset)

                if neighbor in grid and neighbor not in visited:
                    end_positions.add(
                        (neighbor, steps)
                    )
                    # end_positions.add(neighbor)
                    new_positions_found.add(neighbor)

                visited.add(neighbor)

        positions_to_crawl = new_positions_found

    # print(len(end_positions))

    return end_positions

# deb_position = start
deb_position = None

freq = {}
# for position in [start]:
# for position in path:
for i, position in enumerate(path):
    # break
    if not i % 100: print(i)

    if position == deb_position:
        print(position, 'cheats')

    end_positions = get_cheats(position)
    for end_position, steps in end_positions:
    # for end_position, steps in get_cheats(position):
        dx = abs(end_position[0] - position[0])
        dy = abs(end_position[1] - position[1])
        if steps != dx + dy:
            visualize((position, end_position))
            # visualize((end_position, ))
            print(f'{position=} {end_position=}')
            print(f'{steps=} {dx=} {dy=}')
            assert False

        if grid.get(end_position):
            cost = (
                distances_from_start[position] # to start
                + baseline_path - distances_from_start[end_position] # to goal
                + steps
            )
            savings = baseline_path - cost

            # savings = (
            #     distances_from_start[end_position]
            #     - distances_from_start[position]
            #     - steps
            # )

            freq.setdefault(savings, 0)
            freq[savings] += 1

            if position == deb_position:
                visualize((end_position, ))
                print('  end', end_position, 'in', steps, ', save', savings)

    if position == deb_position:
        visualize(
            tuple( p for p, _ in end_positions )
        )

print('\n\n\n')
for savings in sorted(freq): print(f'{freq[savings]} save {savings}')

total = 0
for savings in sorted(freq):
    # if savings >= 50:
    if savings >= 100:
        total += freq[savings]

print()
print(total)

# TODO haven't run
