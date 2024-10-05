from itertools import combinations, chain, product as cartesian_product
from functools import cache
from collections import deque

@cache
def chips_would_be_safe(floor_items):
    chips = set()
    generators = set()
    for item_type, item_material in floor_items:
        if item_type == 'm':
            chips.add(item_material)
        elif item_type == 'g':
            generators.add(item_material)

    return not (generators and chips.difference(generators))

def get_floor_from_floors(floor_number, floors):
    return next(
        floor_items
        for i, floor_items in floors
        if i == floor_number
    )

def get_successor_states(state):
    current_floor, floors = state

    if current_floor == 0:
        floor_options = (current_floor + 1, )
    elif current_floor == len(floors) - 1:
        floor_options = (current_floor - 1, )
    else:
        floor_options = (current_floor + 1, current_floor - 1)

    current_floor_items = get_floor_from_floors(current_floor, floors)
    carried_items_options = chain(
        combinations(current_floor_items, 1),
        combinations(current_floor_items, 2)
    )

    move_options = cartesian_product(floor_options, carried_items_options)
    for next_floor_number, carried_items in move_options:
        next_floor_items = \
            get_floor_from_floors(next_floor_number, floors).union(carried_items)
        left_behind_items = \
            current_floor_items.difference(carried_items)

        if (
            chips_would_be_safe(next_floor_items)
            and chips_would_be_safe(left_behind_items)
        ):
            yield ( # a state object as described below
                next_floor_number,
                frozenset((
                    (current_floor, left_behind_items),
                    (next_floor_number, next_floor_items),
                    *(
                        (i, floor)
                        for i, floor in floors
                        if i not in (current_floor, next_floor_number)
                    )
                ))
            )

starting_floors = []
while True:
    try:
        line = input()
    except EOFError:
        break

    left_side, right_side = line[:-1].split(' contains ')
    if right_side.startswith('nothing'):
        starting_floors.append(frozenset())
        continue

    items = right_side.split(', ')
    if len(items) == 1: # two items, so no commas
        items = items[0].split(' and ')

    floor_items = []
    for item in items:
        pieces = item.split(' ')
        item_material, item_type = pieces[-2:]

        item_type = 'm' if item_type == 'microchip' else 'g'

        if item_type == 'm':
            item_material = item_material.replace('-compatible', '')

        floor_items.append( (item_type, item_material) )

    starting_floors.append(frozenset(floor_items))

starting_floors[0] = starting_floors[0].union([
    ('m', 'elerium'),
    ('g', 'elerium'),
    ('m', 'dilithium'),
    ('g', 'dilithium')
])

# a state object is (n, floors)
# where n is the current floor (of the player character and elevator)
# and floors is frozenset of 2-tuples (i, floor)
# ... where i is the floor number 0..3 and floor is frozenset of items
# ...... where each item is a 2-tuple like
#        ('m', 'hydrogen') or ('g', 'lithium')
#
# this all lets us do the entire problem with no mutations
# to these state objects, as well as making them hashable!
starting_state = (0, frozenset(enumerate(starting_floors)))

done = False
known_state_hashes = set([hash(starting_state)])
states_to_crawl = deque([starting_state])
steps = 0
while states_to_crawl:
    new_states_found = deque()
    steps += 1

    for state in states_to_crawl:
        for successor_state in get_successor_states(state):
            if not any(floor for i, floor in successor_state[1] if i != 3):
                done = True
                break

            successor_state_hash = hash(successor_state)
            if successor_state_hash not in known_state_hashes:
                new_states_found.append(successor_state)
                known_state_hashes.add(successor_state_hash)

        if done:
            break

    if done:
        break

    states_to_crawl = new_states_found

print(steps)
