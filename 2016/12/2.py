# modified from 2015 23

register_a = 0
register_b = 0
register_c = 1
register_d = 0

def get_register(register_code):
    if register_code == 'a':
        return register_a
    elif register_code == 'b':
        return register_b
    elif register_code == 'c':
        return register_c
    elif register_code == 'd':
        return register_d

def run_instruction(i):
    if i > max_instruction_index:
        raise ValueError
    
    global register_a
    global register_b
    global register_c
    global register_d
    operation, arguments = program[i]
    print(i, operation, arguments)
    print(f'a: {register_a}')
    print(f'b: {register_b}')
    print(f'c: {register_c}')
    print(f'd: {register_d}')
    print()

    if operation == 'cpy':
        source, destination = arguments
        if type(source) is str:
            source = get_register(source)
        if destination == 'a':
            register_a = source
        elif destination == 'b':
            register_b = source
        elif destination == 'c':
            register_c = source
        elif destination == 'd':
            register_d = source

        return i + 1
    elif operation in ['inc', 'dec']:
        register_code = arguments[0]
        delta = 1 if operation == 'inc' else -1

        if register_code == 'a':
            register_a += delta
        elif register_code == 'b':
            register_b += delta
        elif register_code == 'c':
            register_c += delta
        elif register_code == 'd':
            register_d += delta

        return i + 1
    elif operation == 'jnz':
        condition, offset = arguments
        if type(condition) is str:
            condition = get_register(condition)

        if condition == 0:
            return i + 1
        else:
            return i + offset

program = []
while True:
    try:
        line = input()
    except EOFError:
        break
    
    operation, *right_side = line.split(' ')
    arguments = []
    for piece in right_side:
        if piece not in ['a', 'b', 'c', 'd']:
            piece = int(piece)
        arguments.append(piece)
    program.append((operation, arguments))

max_instruction_index = len(program) - 1
next_instruction = 0
try:
    while True:
        next_instruction = run_instruction(next_instruction)
except ValueError:
    print('FINAL STATE')
    print(f'a: {register_a}')
    print(f'b: {register_b}')
    print(f'c: {register_c}')
    print(f'd: {register_d}')
