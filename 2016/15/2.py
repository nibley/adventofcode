from itertools import count

discs = []
while True:
    try:
        line = input()
    except EOFError:
        break

    (
        _, _, _,
        num_positions, _, _, _, _, _, _, _,
        initial_position
    ) = line[ : -1 ].split()

    num_positions, initial_position = map(
        int,
        (num_positions, initial_position)
    )

    discs.append(
        (
            num_positions,
            (initial_position + len(discs) + 1) % num_positions
        )
    )

discs.append( (11, 7) )

print(
    next(
        time
        for time in count()
        if not any(
            (initial_position + time) % num_positions
            for num_positions, initial_position in discs
        )
    )
)
