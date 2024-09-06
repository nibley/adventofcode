# modified from 2015 23

def run_instruction(i):
    if i > max_instruction_index:
        raise ValueError
    
    offset = program[i]
    program[i] += 1
    return i + offset

program = []
while True:
    try:
        line = input()
    except EOFError:
        break
    
    offset = int(line)
    program.append(offset)

max_instruction_index = len(program) - 1
next_instruction = 0
steps_taken = 0
try:
    while True:
        next_instruction = run_instruction(next_instruction)
        steps_taken += 1
except ValueError:
    print(steps_taken)
while True:
    try:
        line = input()
    except EOFError:
        break

