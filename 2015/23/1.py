register_a = 0
register_b = 0

def run_instruction(i):
    if i > max_instruction_index:
        raise ValueError
    
    global register_a
    global register_b
    operation, arguments = program[i]
    print(i, operation, arguments)
    print(f'a: {register_a}')
    print(f'b: {register_b}')
    print()

    if operation == 'hlf':
        if arguments[0] == 'a':
            register_a = register_a // 2
        else:
            register_b = register_b // 2
        return i + 1
    elif operation == 'tpl':
        if arguments[0] == 'a':
            register_a = register_a * 3
        else:
            register_b = register_b * 3
        return i + 1
    elif operation == 'inc':
        if arguments[0] == 'a':
            register_a += 1
        else:
            register_b += 1
        return i + 1
    elif operation == 'jmp':
        return i + arguments[0]
    elif operation == 'jie':
        if arguments[0] == 'a':
            condition_register = register_a
        else:
            condition_register = register_b
        if condition_register % 2 == 0:
            return i + arguments[1]
        else:
            return i + 1
    elif operation == 'jio':
        if arguments[0] == 'a':
            condition_register = register_a
        else:
            condition_register = register_b
        if condition_register == 1:
            return i + arguments[1]
        else:
            return i + 1

program = []
while True:
    try:
        line = input()
    except EOFError:
        break
    
    operation, *right_side = line.split(' ')
    arguments = []
    for i, piece in enumerate(right_side):
        piece = piece.replace(',', '')
        if piece not in ['a', 'b']:
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
