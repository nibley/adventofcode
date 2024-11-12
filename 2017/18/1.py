# modified from 2015 23

from collections import defaultdict

registers = defaultdict(lambda: 0)
get_register = lambda value: (
    value if type(value) is not str
    else registers[value]
)

last_sound_frequency = None
last_recovered_frequency = None
def run_instruction(i):
    operation, arguments = program[i]

    if operation in ('snd', 'rcv'):
        argument, *_ = arguments
        argument = get_register(argument)

        if operation == 'snd':
            global last_sound_frequency
            last_sound_frequency = argument
        elif operation == 'rcv' and argument:
            assert last_sound_frequency is not None
            global last_recovered_frequency
            last_recovered_frequency = last_sound_frequency
    elif operation == 'jgz':
        test_value, offset = map(get_register, arguments)
        if test_value > 0:
            return i + offset
    else:
        register_name, argument = arguments
        value = registers[register_name]
        argument = get_register(argument)

        if operation == 'set':
            value = argument
        elif operation == 'add':
            value += argument
        elif operation == 'mul':
            value *= argument
        elif operation == 'mod':
            value = value % argument

        registers[register_name] = value

    return i + 1

program = []
while True:
    try:
        line = input()
    except EOFError:
        break

    operation, *arguments = line.split(' ')
    arguments = [
        argument if argument.isalpha() else int(argument)
        for argument in arguments
    ]
    program.append( (operation, arguments) )

max_instruction_index = len(program)

next_instruction = 0
while (
    last_recovered_frequency is None
    and 0 <= next_instruction < max_instruction_index
):
    next_instruction = run_instruction(next_instruction)

print(last_recovered_frequency)
