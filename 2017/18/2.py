# modified from 2015 23

from collections import defaultdict

message_queues = {}
programs_sleeping = {}
program_send_counts = defaultdict(lambda: 0)
def program_instance(instance_id):
    message_queues[instance_id] = []
    programs_sleeping[instance_id] = False
    registers = defaultdict(lambda: 0, [('p', instance_id)])

    def get_register(register_name):
        if type(register_name) is not str:
            return register_name # was a constant, not a register name

        return registers[register_name]

    def run_instruction(i):
        if i > max_instruction_index:
            raise ValueError

        operation, arguments = program[i]
        # if instance_id == 1:
        # if instance_id == 0:
        if False:
            print(i, operation, arguments)

        if operation == 'snd':
            message = get_register(arguments[0])
            message_queues[0 if instance_id == 1 else 1].append(message)
            program_send_counts[instance_id] += 1
        elif operation == 'rcv':
            if not message_queues[instance_id]:
                programs_sleeping[instance_id] = True
                return i

            programs_sleeping[instance_id] = False
            register_name, *_ = arguments
            registers[register_name] = message_queues[instance_id].pop()
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
        elif operation == 'jgz':
            test_value, offset = map(get_register, arguments)
            if test_value > 0:
                return i + offset

        return i + 1
    
    return run_instruction

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
program_0 = program_instance(0)
program_0_next_instruction = 0
program_1 = program_instance(1)
program_1_next_instruction = 0
try:
    loops = 0
    while not all(programs_sleeping.values()):
        program_0_next_instruction = program_0(program_0_next_instruction)
        program_1_next_instruction = program_1(program_1_next_instruction)

        if not loops % 500000:
            print(f'{program_send_counts[0]}\t{program_send_counts[1]}')
        # print(f'{program_0_next_instruction}\t{program_1_next_instruction}')
        # print(message_queues.items())
        loops += 1
    print(':( deadlock')
except ValueError:
    # pass
    print('error')
finally:
    print()
    print(program_send_counts.items())
    print(message_queues.items())
    print()
    print('Program 1 sent messages:')
    print(program_send_counts[1])
