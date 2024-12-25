from itertools import chain

sequences = []
while True:
    try:
        line = input()
    except EOFError:
        break

    sequences.append(line)

numeric_keypad = {
    (0, 0) : '7',
    (1, 0) : '8',
    (2, 0) : '9',
    (0, 1) : '4',
    (1, 1) : '5',
    (2, 1) : '6',
    (0, 2) : '1',
    (1, 2) : '2',
    (2, 2) : '3',
    # no 0, 3
    (1, 3) : '0',
    (2, 3) : 'A'
}

directional_keypad = {
    # no 0, 0
    (1, 0) : '^',
    (2, 0) : 'A',
    (0, 1) : '<',
    (1, 1) : 'v',
    (2, 1) : '>',
}

DIRECTIONS = {
    '^' : (0, -1),
    '>' : (1, 0),
    'v' : (0, 1),
    '<' : (-1, 0)
}

def get_paths_to_button(keypad, start_position, goal_position):
    if start_position == goal_position:
        return ('', )

    start_x, start_y = start_position
    goal_x, goal_y = goal_position

    if start_x == goal_x:
        return (abs(start_y - goal_y) * ('^' if start_y > goal_y else 'v'), )
    elif start_y == goal_y:
        return (abs(start_x - goal_x) * ('<' if start_x > goal_x else '>'), )

    paths = []

    low_x, high_x = sorted([start_x, goal_x])
    if all(
        (x, start_y) in keypad
        for x in range(low_x, high_x + 1)
    ):
        x_path = get_paths_to_button(
            keypad,
            start_position,
            (goal_x, start_y)
        )[0]
        y_path = get_paths_to_button(
            keypad,
            (goal_x, start_y),
            goal_position
        )[0]

        paths.append(x_path + y_path)

    low_y, high_y = sorted([start_y, goal_y])
    if all(
        (start_x, y) in keypad
        for y in range(low_y, high_y + 1)
    ):
        y_path = get_paths_to_button(
            keypad,
            start_position,
            (start_x, goal_y)
        )[0]
        x_path = get_paths_to_button(
            keypad,
            (start_x, goal_y),
            goal_position
        )[0]

        paths.append(y_path + x_path)

    return tuple(paths)

def get_control_sequences(keypad, desired_output, start_position):
    # print('START', position, keypad[position], 'want', desired_output)

    results = ('', )
    position = start_position
    for next_button in desired_output:
        assert position in keypad

        # print(f'{keypad[position]} to {next_button}')
        next_position = next(
            position
            for position, button in keypad.items()
            if button == next_button
        )

        results = tuple(
        # results = (
            f'{result}{path}A'
            for result in results
            for path in get_paths_to_button(
                keypad,
                position,
                next_position
            )
        )

        position = next_position

    return results
    # return tuple(results)

total = 0

numeric_keypad_initial = next(
    position
    for position, button in numeric_keypad.items()
    if button == 'A'
)

directional_keypad_initial = next(
    position
    for position, button in directional_keypad.items()
    if button == 'A'
)

def validate(control_sequence, keypad, start_position):
    result = ''

    x, y = start_position

    for char in control_sequence:
        if char == 'A':
            result += keypad[ (x, y) ]
        else:
            x_offset, y_offset = DIRECTIONS[char]
            x += x_offset
            y += y_offset

            assert (x, y) in keypad

    return result

for sequence in sequences:
# for sequence in ['029A']:
    # break
    print(sequence)

    first_robot = get_control_sequences(
        numeric_keypad,
        sequence,
        numeric_keypad_initial
    )
    first_robot_length = min(map(len, first_robot))
    first_robot_optimal = tuple(
        path
        for path in first_robot
        if len(path) == first_robot_length
    )

    second_robot = tuple(
        chain.from_iterable(
            get_control_sequences(
                directional_keypad,
                path,
                directional_keypad_initial
            )
            for path in first_robot_optimal
        )
    )
    second_robot_length = min(map(len, second_robot))
    second_robot_optimal = tuple(
        path
        for path in second_robot
        if len(path) == second_robot_length
    )

    human = tuple(
        chain.from_iterable(
            get_control_sequences(
                directional_keypad,
                path,
                directional_keypad_initial
            )
            for path in second_robot_optimal
        )
    )
    human_length = min(map(len, human))
    # human_optimal = tuple(
    #     path
    #     for path in human
    #     if len(path) == human_length
    # )

    numeric = int(sequence[ : -1 ])
    # print('  human', len(human))
    # print('  numeric', numeric)
    # print('  product', len(human) * numeric)
    total += human_length * numeric

    # v1 = validate(human, directional_keypad, directional_keypad_initial)
    # v2 = validate(v1, directional_keypad, directional_keypad_initial)
    # v3 = validate(v2, numeric_keypad, numeric_keypad_initial)
    # assert v3 == sequence

    # print()
    # print('  human to 1')
    # print('  ', v1)
    # print('  1 to 2')
    # print('  ', v2)
    # print('  2 to 3')
    # print('  ', v3)

    print()

print()
print('total')
print(total)
