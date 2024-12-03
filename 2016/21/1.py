operations = []
while True:
    try:
        line = input()
    except EOFError:
        break

    operation_type, second_word, *rest = line.split()

    if operation_type == 'swap' and second_word == 'letter':
        operation_type = 'swap letter'
        first_argument, _, _, second_argument = rest
        arguments = (first_argument, second_argument)
    elif operation_type == 'rotate' and second_word == 'based':
        operation_type = 'rotate letter'
        *_, letter = rest
        arguments = (letter, )
    elif operation_type in ('swap', 'reverse', 'move'):
        first_argument, *_, second_argument = rest
        arguments = (int(first_argument), int(second_argument))
    else: # rotate left or rotate right
        steps, _ = rest
        arguments = (second_word, int(steps))

    operations.append(
        (operation_type, arguments)
    )

def apply_operation(operation):
    operation_type, arguments = operation

    if operation_type == 'swap':
        lower_index, higher_index = sorted(arguments)

        return (
            password[ : lower_index ]
            + password[higher_index]
            + password[lower_index + 1 : higher_index]
            + password[lower_index]
            + password[higher_index + 1 : ]
        )
    elif operation_type == 'swap letter':
        first_letter, second_letter = arguments

        return apply_operation(
            (
                'swap',
                (password.index(first_letter), password.index(second_letter))
            )
        )
    elif operation_type == 'rotate letter':
        letter, *_ = arguments
        steps = password.index(letter)

        if steps >= 4:
            steps += 1

        steps += 1

        return apply_operation(
            ('rotate', ('right', steps))
        )
    elif operation_type == 'rotate':
        direction, steps = arguments
        offset = steps * (1 if direction == 'left' else -1)
        password_length = len(password)

        return ''.join(
            password[ (i + offset) % password_length ]
            for i in range(password_length)
        )
    elif operation_type == 'reverse':
        lower_index, higher_index = sorted(arguments)
        reversed_area = password[lower_index : higher_index + 1][ : : -1 ]

        return (
            password[ : lower_index ]
            + reversed_area
            + password[higher_index + 1 : ]
        )
    elif operation_type == 'move':
        source_index, destination_index = arguments
        source_letter = password[source_index]
        password_without_source_letter = password.replace(source_letter, '')

        return (
            password_without_source_letter[ : destination_index ]
            + source_letter
            + password_without_source_letter[ destination_index : ]
        )

password = 'abcdefgh'
for operation in operations:
    password = apply_operation(operation)

print(password)
