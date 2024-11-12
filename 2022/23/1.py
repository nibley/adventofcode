from collections import defaultdict, deque

elves = set()
y = 0
width = None
while True:
    try:
        line = input()
    except EOFError:
        break

    if width is None:
        width = len(line)

    for x, cell in enumerate(line):
        if cell == '#':
            elves.add((x, y))

    y += 1

height = y

neighbor_offsets = [
    (-1, -1),
    ( 0, -1),
    ( 1, -1),
    (-1,  0),
    ( 1,  0),
    (-1,  1),
    ( 0,  1),
    ( 1,  1)
]
def check_for_neighbors(elf_x, elf_y):
    return tuple(
        (elf_x + x_offset, elf_y + y_offset) in elves
        for x_offset, y_offset in neighbor_offsets
    )

# three indeces into neighbor_offsets to check for other elves,
# then one index into neighbor_offsets for the proposed move
proposed_move_rules = deque([
    ( (0, 1, 2), 1 ),
    ( (5, 6, 7), 6 ),
    ( (0, 3, 5), 3 ),
    ( (2, 4, 7), 4 )
])

for _ in range(10):
    new_elves = set()
    move_proposals = defaultdict(set)
    for elf_x, elf_y in elves:
        found_rule = False
        neighbors = check_for_neighbors(elf_x, elf_y)
        if any(neighbors):
            for neighbor_checks, proposed_move in proposed_move_rules:
                if not any(neighbors[check_index] for check_index in neighbor_checks):
                    proposed_x_offset, proposed_y_offset = neighbor_offsets[proposed_move]
                    proposed_location = (elf_x + proposed_x_offset, elf_y + proposed_y_offset)
                    move_proposals[proposed_location].add( (elf_x, elf_y) )

                    found_rule = True
                    break

        if not found_rule:
            new_elves.add( (elf_x, elf_y) )

    for proposed_location, proposing_elves in move_proposals.items():
        if len(proposing_elves) == 1:
            new_elves.add(proposed_location)
        elif len(proposing_elves) > 1:
            for proposing_elf in proposing_elves:
                new_elves.add(proposing_elf)

    elves = new_elves
    proposed_move_rules.rotate(-1)

min_x, *_, max_x = sorted(x for x, _ in elves)
min_y, *_, max_y = sorted(y for _, y in elves)
print((max_x - min_x + 1) * (max_y - min_y + 1) - len(elves))
