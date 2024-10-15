from itertools import product as cartesian_product

def run_program(noun, verb):
    program = program_initial[:]

    program[1] = noun
    program[2] = verb

    position = 0
    while True:
        opcode = program[position]

        if opcode == 99:
            break

        first_argument = program[ program[position + 1] ]
        second_argument = program[ program[position + 2] ]
        result_position = program[position + 3]

        if opcode == 1:
            result = first_argument + second_argument
        elif opcode == 2:
            result = first_argument * second_argument
        else:
            assert False

        program[result_position] = result
        position += 4

    return program[0]

program_initial = [ int(n) for n in input().split(',') ]

goal_output = 19690720
for noun, verb in cartesian_product(range(100), repeat=2):
    if run_program(noun, verb) == goal_output:
        break

print((100 * noun) + verb)
