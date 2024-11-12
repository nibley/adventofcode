# modified from 2015 23

from collections import defaultdict, deque

def make_duet_program(program_id):
    registers = defaultdict(lambda: 0, {'p': program_id})
    get_register = lambda value: (
        value if type(value) is not str
        else registers[value]
    )
    message_queue = message_queues[program_id]
    other_message_queue = message_queues[1 if program_id == 0 else 0]

    def duet_program(i):
        operation, arguments = program[i]
        blocked[program_id] = False

        if operation == 'snd':
            argument, *_ = arguments
            argument = get_register(argument)

            other_message_queue.append(argument)
            send_counts[program_id] += 1
        elif operation == 'rcv':
            if not message_queue:
                blocked[program_id] = True
                return i # wait

            register_name, *_ = arguments
            registers[register_name] = message_queue.popleft()
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

    return duet_program

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

message_queues = (deque(), deque())
blocked = [False, False]
send_counts = [0, 0]
next_instructions = [0, 0]
duet_programs = tuple(
    make_duet_program(program_id) for program_id in range(2)
)
while (
    not all(blocked)
    and all(
        0 <= next_instruction < max_instruction_index
        for next_instruction in next_instructions
    )
):
    for program_id, (next_instruction, duet_program) in enumerate(
        zip(next_instructions, duet_programs)
    ):
        next_instructions[program_id] = duet_program(next_instruction)

print(send_counts[1])
