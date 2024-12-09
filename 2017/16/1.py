commands = []
for command in input().split(','):
    operation = command[0]
    arguments = command[ 1 : ].split('/')

    if operation != 'p':
        arguments = tuple(map(int, arguments))

    commands.append(
        (operation, arguments)
    )

programs = list('abcdefghijklmnop')
for operation, arguments in commands:
    if operation == 's':
        spin_num, *_ = arguments
        front = programs[ : -1 * spin_num]
        back = programs[ -1 * spin_num : ]
        programs = back + front
    else:
        if operation == 'p':
            first_program, second_program = arguments

            first_index = programs.index(first_program)
            second_index = programs.index(second_program)
        elif operation == 'x':
            first_index, second_index = arguments

        programs[first_index], programs[second_index] = (
            programs[second_index], programs[first_index]
        )

print(''.join(programs))
