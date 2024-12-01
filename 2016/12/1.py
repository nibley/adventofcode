# modified from 2015 23

def run_instruction(i):
    operation, (first_argument, *other_arguments) = program[i]

    if operation == 'inc':
        registers[first_argument] += 1
    elif operation == 'dec':
        registers[first_argument] -= 1
    else:
        first_argument = registers.get(first_argument, first_argument)
        second_argument, *_ = other_arguments

        if operation == 'cpy':
            registers[second_argument] = first_argument
        elif operation == 'jnz' and first_argument:
            return i + second_argument

    return i + 1

program = []
while True:
    try:
        line = input()
    except EOFError:
        break

    operation, *arguments = line.split()
    arguments = tuple(
        argument if argument in 'abcd' else int(argument)
        for argument in arguments
    )

    program.append( (operation, arguments) )

registers = dict.fromkeys('abcd', 0)
next_instruction = 0
while 0 <= next_instruction < len(program):
    next_instruction = run_instruction(next_instruction)

print(registers['a'])
