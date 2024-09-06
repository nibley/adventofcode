# modified from 2016 12

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
    global latest_clock_signal
    operation, arguments = program[i]

    if operation == 'out':
        [signal] = arguments
        if type(signal) is str:
            signal = get_register(signal)
        
        latest_clock_signal = signal
        return i + 1
    elif operation == 'cpy':
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

length_to_check_clock_signal = 10
def expected_clock_signal():
    for _ in range(length_to_check_clock_signal):
        yield 0
        yield 1

max_instruction_index = len(program) - 1
found_good_signal = False
initial_a_value = 1
while True:
    register_a = initial_a_value
    register_b = 0
    register_c = 0
    register_d = 0

    reference_signal = expected_clock_signal()
    latest_clock_signal = None
    next_instruction = 0
    try:
        while True:
            next_instruction = run_instruction(next_instruction)

            if latest_clock_signal is not None:
                try:
                    if latest_clock_signal != next(reference_signal):
                        break
                except StopIteration:
                    found_good_signal = True
                    break

            latest_clock_signal = None
    except ValueError:
        print('FINAL STATE')
        print(f'a: {register_a}')
        print(f'b: {register_b}')
        print(f'c: {register_c}')
        print(f'd: {register_d}')
    
    if found_good_signal:
        break

    initial_a_value += 1

print(f'after {length_to_check_clock_signal} values, found a =')
print(initial_a_value)
