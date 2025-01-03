from itertools import chain

grid_original = {}
hp_original = {}
y = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, char in enumerate(line):
        grid_original[ (x, y) ] = char

        if char in 'EG':
            hp_original[ (x, y) ] = 200

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

def get_units(grid):
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

def get_neighbors(position, grid, desired_type='.'):
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

def find_nearest_targets(start, targets, grid):
    targets_found = {}

    positions_to_crawl = { (start, ()) }
    visited = {start}
    steps = 0
    while not targets_found and positions_to_crawl:
        new_positions_found = set()
        steps += 1

        for position, path in positions_to_crawl:
            for neighbor in get_neighbors(position, grid):
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

def simulate_turn(grid, hp, attack_value):
    elves, goblins = get_units(grid)
    for position in reading_order(chain(elves, goblins)):
        if position not in hp: # unit died since initial scan
            continue

        unit_type = grid[position]
        enemy_type = 'G' if unit_type == 'E' else 'E'
        targets = get_neighbors(position, grid, enemy_type)

        # move
        if not targets:
            elves, goblins = get_units(grid)
            enemies = elves if enemy_type == 'E' else goblins

            attack_positions = set(
                neighbor
                for enemy in enemies
                for neighbor in get_neighbors(enemy, grid)
            )

            nearest = find_nearest_targets(position, attack_positions, grid)
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

                targets = get_neighbors(new_position, grid, enemy_type)

        # attack
        if targets:
            target = min(
                targets,
                key=lambda target: (hp[target], target[ : : -1 ])
            )

            hp[target] -= 3 if unit_type == 'G' else attack_value
            if hp[target] <= 0:
                # kill target

                if unit_type == 'G':
                    return False # elf dead, simulation is over

                grid[target] = '.'
                del hp[target]

    if any(
        grid[position] == 'G'
        for position in hp
    ):
        return None
    else:
        return True # elves won

def visualize(grid, hp):
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

def try_attack_value(attack_value):
    grid = grid_original.copy()
    hp = hp_original.copy()

    turns = 0
    victory = None
    while victory is None:
        victory = simulate_turn(grid, hp, attack_value)

        # TODO still off by one for either some of the tests or the rest
        # maybe to do with a "full round" and changing termination logic
        # from p1

        # "The Elves look quite outnumbered.
        # You need to determine the outcome of the battle:
        # the number of full rounds that were completed
        # (not counting the round in which combat ends)
        # multiplied by the sum of the hit points of all remaining units
        # at the moment combat ends.
        # (Combat only ends when a unit finds no targets during its turn.)""

        if victory is None:
        # if True:
            turns += 1

        # print('  Turn', turns)
        # visualize(grid, hp)

    if victory:
        # print(f'{attack_value = }')
        # print(f'{turns = }')
        # print(f'hp = {sum(hp.values())}')
        return turns * sum(hp.values())
    else:
        return 0

outcome = 0
attack_value = 4
while not outcome:
    # print(attack_value)
    outcome = try_attack_value(attack_value)
    attack_value += 1

print(outcome)
