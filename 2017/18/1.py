# modified from 2015 23

from collections import defaultdict

def get_register(register_name):
    if type(register_name) is not str:
        return register_name # was a constant, not a register name

    return registers[register_name]

registers = defaultdict(lambda: 0)
last_sound_frequency = None
last_recovered_frequency = None
def run_instruction(i):
    if i > max_instruction_index:
        raise ValueError

    operation, arguments = program[i]
    print(i, operation, arguments)

    if operation == 'snd':
        frequency = get_register(arguments[0])
        global last_sound_frequency
        last_sound_frequency = frequency
    elif operation == 'set':
        register_name, value = arguments
        value = get_register(value)
        registers[register_name] = value
    elif operation == 'add':
        register_name, value = arguments
        value = get_register(value)
        registers[register_name] += value
    elif operation == 'mul':
        register_name, value = arguments
        value = get_register(value)
        registers[register_name] *= value
    elif operation == 'mod':
        register_name, value = arguments
        value = get_register(value)
        registers[register_name] %= value
    elif operation == 'rcv':
        test_value = get_register(arguments[0])
        if test_value != 0:
            global last_recovered_frequency
            last_recovered_frequency = last_sound_frequency
    elif operation == 'jgz':
        test_value, offset = map(get_register, arguments)
        if test_value > 0:
            return i + offset

    return i + 1

program = []
while True:
    try:
        line = input()
    except EOFError:
        break

    operation, *arguments = line.split(' ')
    arguments = [ argument if argument.isalpha() else int(argument) \
        for argument in arguments ]
    program.append( (operation, arguments) )

max_instruction_index = len(program) - 1
next_instruction = 0
try:
    while last_recovered_frequency is None:
        next_instruction = run_instruction(next_instruction)
except ValueError:
    pass
finally:
    print()
    print('FINAL STATE')
    for key in sorted(registers.keys()):
        print(f'{key}: \t{registers[key]}')
    print()
    print('Last recovered frequency:')
    print(last_recovered_frequency)
