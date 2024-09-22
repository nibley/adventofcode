def run_dance(programs):
    for operation, *arguments in commands:
        if operation == 's':
            spin_num, *_ = arguments
            front = programs[ : -1 * spin_num]
            back = programs[-1 * spin_num : ]
            programs = back + front
        elif operation == 'x':
            first_index, second_index = arguments
            programs[first_index], programs[second_index] = programs[second_index], programs[first_index]
        elif operation == 'p':
            first_program, second_program = sorted(arguments)
            first_index = programs.index(first_program)
            second_index = programs.index(second_program)
            programs[first_index], programs[second_index] = \
                programs[second_index], programs[first_index]

    return programs

raw = input()
commands = []
for raw_command in raw.split(','):
    operation, arguments = raw_command[0], raw_command[1:]
    if operation == 'p':
        commands.append( (operation, *arguments.split('/')) )
    else:
        commands.append( (operation, *map(int, arguments.split('/'))) )

original_programs = list('abcdefghijklmnop')
programs = original_programs[:]

iterations_til_original = 0
while True:
    programs = run_dance(programs)
    iterations_til_original += 1

    if programs == original_programs:
        break

remainder_iterations = 1_000_000_000 % iterations_til_original
programs = original_programs[:]
for _ in range(remainder_iterations):
    programs = run_dance(programs)

print(''.join(programs))
