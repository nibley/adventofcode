ORIGINAL_PROGRAMS = list('abcdefghijklmnop')

commands = []
for command in input().split(','):
    operation = command[0]
    arguments = command[ 1 : ].split('/')

    if operation != 'p':
        arguments = tuple(map(int, arguments))

    commands.append(
        (operation, arguments)
    )

def run_dance(programs):
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

    return programs

programs = run_dance(ORIGINAL_PROGRAMS[ : ])
iterations_til_original = 1
while programs != ORIGINAL_PROGRAMS:
    programs = run_dance(programs)
    iterations_til_original += 1

remainder_iterations = 1_000_000_000 % iterations_til_original
programs = ORIGINAL_PROGRAMS[:]
for _ in range(remainder_iterations):
    programs = run_dance(programs)

print(''.join(programs))
