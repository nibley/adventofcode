raw = input()
commands = []
for raw_command in raw.split(','):
    operation, arguments = raw_command[0], raw_command[1:]
    if operation == 'p':
        commands.append((operation, *arguments.split('/')))
    else:
        commands.append((operation, *map(int, arguments.split('/'))))

programs = list('abcdefghijklmnop')
for command in commands:
    operation, *arguments = command
    if operation == 's':
        spin_num, _* = arguments
        front = programs[ : -1 * spin_num]
        back = programs[-1 * spin_num : ]
        programs = back + front
    elif operation == 'x':
        first_index, second_index = arguments
        programs[first_index], programs[second_index] = \
            programs[second_index], programs[first_index]
    elif operation == 'p':
        first_program, second_program = arguments
        first_index = programs.index(first_program)
        second_index = programs.index(second_program)
        programs[first_index], programs[second_index] = \
            programs[second_index], programs[first_index]
    
print(''.join(programs))
