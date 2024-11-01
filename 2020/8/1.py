# modified from 2015 23

def run_instruction(i):
    operation, argument = program[i]

    # return next instruction, increment for accumulator
    if operation == 'jmp':
        return (i + argument, 0)
    else:
        return (i + 1, 0 if operation == 'nop' else argument)

program = []
while True:
    try:
        line = input()
    except EOFError:
        break

    operation, argument = line.split(' ')
    program.append( (operation, int(argument)) )

try:
    accumulator = 0
    visited_instructions = set()
    next_instruction = 0
    while next_instruction not in visited_instructions:
        visited_instructions.add(next_instruction)
        next_instruction, increment = run_instruction(next_instruction)
        accumulator += increment
except IndexError:
    pass

print(accumulator)
