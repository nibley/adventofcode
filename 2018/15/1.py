from itertools import chain

grid = {}
hp = {}
y = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, char in enumerate(line):
        grid[ (x, y) ] = char

        if char in 'EG':
            hp[ (x, y) ] = 200

    y += 1

HEIGHT = y
WIDTH = len(line)

reading_order = lambda positions: (
    sorted(
        positions,
        key=lambda position: position[ : : -1 ]
    )
)

reading_order_first = lambda positions: (
    min(
        positions,
        key=lambda position: position[ : : -1 ]
    )
)

def get_units():
    elves = []
    goblins = []

    for y in range(HEIGHT):
        for x in range(WIDTH):
            position = (x, y)
            cell = grid[position]

            if cell == 'E':
                elves.append(position)
            elif cell == 'G':
                goblins.append(position)

    return (elves, goblins)

NEIGHBOR_OFFSETS = [
    ( 0, -1),
    (-1,  0),
    ( 1,  0),
    ( 0,  1)
]

def get_neighbors(position, desired_type='.'):
    x, y = position

    neighbors = (
        (x + x_offset, y + y_offset)
        for x_offset, y_offset in NEIGHBOR_OFFSETS
    )

    return tuple(
        neighbor
        for neighbor in neighbors
        if grid[neighbor] == desired_type
    )

def find_nearest_targets(start, targets):
    targets_found = {}

    positions_to_crawl = { (start, ()) }
    visited = {start}
    steps = 0
    while not targets_found and positions_to_crawl:
        new_positions_found = set()
        steps += 1

        for position, path in positions_to_crawl:
            for neighbor in get_neighbors(position):
                if neighbor not in visited:
                    new_path = path + (neighbor, )

                    if neighbor in targets:
                        targets_found.setdefault(neighbor, []).append(new_path)

                    visited.add(neighbor)
                    new_positions_found.add(
                        (neighbor, new_path)
                    )

        positions_to_crawl = new_positions_found

    return targets_found

def simulate_turn():
    elves, goblins = get_units()
    for position in reading_order(chain(elves, goblins)):
        if position not in hp: # unit died since initial scan
            continue

        unit_type = grid[position]
        enemy_type = 'G' if unit_type == 'E' else 'E'
        targets = get_neighbors(position, enemy_type)

        # move
        if not targets:
            elves, goblins = get_units()
            enemies = elves if enemy_type == 'E' else goblins

            if not enemies:
                return False # simulation is over

            attack_positions = set(
                neighbor
                for enemy in enemies
                for neighbor in get_neighbors(enemy)
            )

            nearest = find_nearest_targets(position, attack_positions)
            if nearest:
                move_target = reading_order_first(nearest)

                paths_to_target = nearest[move_target]
                assert all(paths_to_target)

                first_steps = set(
                    first_step
                    for first_step, *_ in paths_to_target
                )

                new_position = reading_order_first(first_steps)
                grid[position] = '.'
                grid[new_position] = unit_type

                hp[new_position] = hp.pop(position)

                targets = get_neighbors(new_position, enemy_type)

        # attack
        if targets:
            target = min(
                targets,
                key=lambda target: (hp[target], target[ : : -1 ])
            )

            hp[target] -= 3
            if hp[target] <= 0:
                # kill target
                grid[target] = '.'
                del hp[target]

    return True

def visualize():
    print('Turn', turns)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(grid[ (x, y) ], end='')

        print(
            '  ',
            ', '.join(
                f'{grid[ (x, y) ]}({hp[ (x, y) ]})'
                for x in range(WIDTH)
                if grid[ (x, y) ] in 'EG'
            )
        )

    print()

turns = 0
while simulate_turn():
    turns += 1
    # visualize()

print(turns * sum(hp.values()))
