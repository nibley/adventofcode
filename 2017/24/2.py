parts = []
while True:
    try:
        line = input()
    except EOFError:
        break

    parts.append(tuple(map(int, line.split('/'))))

def get_other_end(free_end, part):
    return (
        part[1] if part[0] == free_end
        else part[0] if part[1] == free_end
        else None
    )

def get_bridges(free_end, used=None):
    if used is None:
        used = frozenset()

    found_another_part = False
    for i, part in enumerate(parts):
        if i not in used:
            other_end = get_other_end(free_end, part)
            if other_end is not None:
                found_another_part = True
                yield from get_bridges(other_end, used | {i})

    if not found_another_part:
        yield used

bridges = {}
for starting_part_index, starting_part in enumerate(parts):
    if 0 not in starting_part:
        continue

    for bridge in get_bridges(
        get_other_end(0, starting_part),
        frozenset({starting_part_index})
    ):
        bridges.setdefault(len(bridge), set()).add(bridge)

longest_bridges = bridges[ max(bridges) ]
print(
    max(
        sum(
            end
            for part in map(parts.__getitem__, bridge)
            for end in part
        )
        for bridge in longest_bridges
    )
)
