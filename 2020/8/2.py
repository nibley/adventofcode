# modified from 2015 23

def run_instruction(i):
    operation, argument = program[i]

    # return next instruction, increment for accumulator
    if operation == 'jmp':
        return (i + argument, 0)
    else:
        return (i + 1, 0 if operation == 'nop' else argument)

original_program = []
while True:
    try:
        line = input()
    except EOFError:
        break

    operation, argument = line.split(' ')
    original_program.append( (operation, int(argument)) )

max_instruction_index = len(original_program) - 1

change_indeces = (
    i
    for i, (operation, _) in enumerate(original_program)
    if operation in ('nop', 'jmp')
)

for change_index in change_indeces:
    try:
        program = original_program[:]
        change_operation, argument = program[change_index]
        program[change_index] = (
            'nop' if change_operation == 'jmp' else 'jmp',
            argument
        )

        accumulator = 0
        visited_instructions = set()
        next_instruction = 0
        while next_instruction not in visited_instructions:
            visited_instructions.add(next_instruction)
            next_instruction, increment = run_instruction(next_instruction)
            accumulator += increment
    except IndexError:
        break

print(accumulator)
