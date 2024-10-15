# modified from 2019 2

from collections import defaultdict

program = [ int(n) for n in input().split(',') ]

input_queue = [1]
output_queue = []

position = 0
while True:
    instruction = program[position]
    if instruction == 99:
        break

    opcode = instruction % 100

    argument_modes = defaultdict(lambda: '0')
    argument_modes.update({
        i: mode
        for i, mode in enumerate(str(instruction // 100)[::-1])
    })

    if opcode in [3, 4]: # one argument
        if opcode == 3: # input
            result_position = program[position + 1]
            result = input_queue.pop()
        elif opcode == 4: # output
            output_value = program[position + 1]
            if argument_modes[0] == '0':
                output_value = program[output_value]

            output_queue.append(output_value)

        position += 2

    elif opcode in [1, 2]: # three arguments
        first_argument = program[position + 1]
        if argument_modes[0] == '0':
            first_argument = program[first_argument]
        
        second_argument = program[position + 2]
        if argument_modes[1] == '0':
            second_argument = program[second_argument]

        result_position = program[position + 3]

        if opcode == 1: # add
            result = first_argument + second_argument
        elif opcode == 2: # multiply
            result = first_argument * second_argument

        position += 4

    else:
        assert False, f'reached corrupt opcode {opcode}'

    if opcode in [1, 2, 3]: # writing-oriented opcodes
        program[result_position] = result

print(output_queue[-1])
