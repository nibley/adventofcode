def run_instruction(i):
    operation, (first_argument, *other_arguments) = program[i]

    if operation == 'hlf':
        registers[first_argument] //= 2
    elif operation == 'tpl':
        registers[first_argument] *= 3
    elif operation == 'inc':
        registers[first_argument] += 1
    elif operation == 'jmp':
        return i + first_argument
    else: # jie or jio
        second_argument, *_ = other_arguments
        test_value = registers[first_argument]

        if (
            operation == 'jie' and not test_value % 2
            or operation == 'jio' and test_value == 1
        ):
            return i + second_argument

    return i + 1

program = []
while True:
    try:
        line = input()
    except EOFError:
        break

    operation, *arguments = line.replace(',', '').split()
    arguments = tuple(
        argument if argument in 'ab' else int(argument)
        for argument in arguments
    )

    program.append( (operation, arguments) )

registers = dict.fromkeys('ab', 0)
registers['a'] = 1
next_instruction = 0
while 0 <= next_instruction < len(program):
    next_instruction = run_instruction(next_instruction)

print(registers['b'])
