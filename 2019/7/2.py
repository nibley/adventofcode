# modified from 2019 5

from collections import defaultdict
from itertools import permutations

def parallel_program():
    program = program_initial[:]

    # the phase and the first input are used by
    # the input opcode (3) before the output opcode (4)
    # first gets hit and is able to receive further input
    # through its yield expression
    phase = (yield)
    first_input = (yield)
    input_queue = [first_input, phase]

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
                write_position = program[position + 1]
                write_value = input_queue.pop()
            elif opcode == 4: # output
                output_value = program[position + 1]
                if argument_modes[0] == '0':
                    output_value = program[output_value]

                input_queue.append( (yield output_value) )

            position += 2

        elif opcode in [5, 6]: # two arguments
            first_argument = program[position + 1]
            if argument_modes[0] == '0':
                first_argument = program[first_argument]

            second_argument = program[position + 2]
            if argument_modes[1] == '0':
                second_argument = program[second_argument]

            if opcode == 5: # jump if nonzero
                if first_argument != 0:
                    position = second_argument
                    continue
            elif opcode == 6: # jump if zero
                if first_argument == 0:
                    position = second_argument
                    continue

            position += 3

        elif opcode in [1, 2, 7, 8]: # three arguments
            first_argument = program[position + 1]
            if argument_modes[0] == '0':
                first_argument = program[first_argument]

            second_argument = program[position + 2]
            if argument_modes[1] == '0':
                second_argument = program[second_argument]

            write_position = program[position + 3]

            if opcode == 1: # add
                write_value = first_argument + second_argument
            elif opcode == 2: # multiply
                write_value = first_argument * second_argument
            elif opcode == 7: # less than
                write_value = \
                    1 if first_argument < second_argument else 0
            elif opcode == 8: # equals
                write_value = \
                    1 if first_argument == second_argument else 0

            position += 4

        else:
            assert False, f'reached corrupt opcode {opcode}'

        if opcode in [1, 2, 3, 7, 8]: # writing-oriented opcodes
            program[write_position] = write_value

program_initial = [ int(n) for n in input().split(',') ]

phase_orders = permutations(range(5, 10))
highest_output = 0
for phase_order in phase_orders:
    programs = []
    for phase in phase_order:
        program = parallel_program()

        next(program) # prime program to receive input
        program.send(phase)

        programs.append(program)

    output = 0
    while True:
        try:
            for program in programs:
                output = program.send(output)
        except StopIteration:
            break

    if output > highest_output:
        highest_output = output

print(highest_output)
