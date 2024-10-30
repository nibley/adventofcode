# modified from 2019 11

from collections import defaultdict

def output_only_program():
    def get_argument(n, write=False):
        mode = argument_modes[n]
        argument = program[position + n]

        if mode == '0': # position mode
            if not write:
                argument = program[argument]
        elif mode == '2': # relative mode
            relative = argument + relative_base
            if write:
                argument = relative
            else:
                argument = program[relative]

        # ('1' would be immediate mode, no action needed)

        return argument

    position = 0
    relative_base = 0
    while True:
        instruction = program[position]
        if instruction == 99:
            break

        opcode = instruction % 100

        argument_modes = defaultdict(lambda: '0')
        argument_modes.update({
            i + 1: mode
            for i, mode in enumerate(str(instruction // 100)[::-1])
        })

        if opcode in [3, 4, 9]: # one argument
            if opcode == 3:
                assert False, 'output-only program'
            elif opcode == 4: # output
                output_value = get_argument(1)
                yield output_value
            elif opcode == 9:
                base_adjustment = get_argument(1)
                relative_base += base_adjustment

            position += 2

        elif opcode in [5, 6]: # two arguments
            check_value = get_argument(1)
            jump_target = get_argument(2)

            if opcode == 5: # jump if nonzero
                if check_value != 0:
                    position = jump_target
                    continue
            elif opcode == 6: # jump if zero
                if check_value == 0:
                    position = jump_target
                    continue

            position += 3

        elif opcode in [1, 2, 7, 8]: # three arguments
            first_argument = get_argument(1)
            second_argument = get_argument(2)
            write_position = get_argument(3, write=True)

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

program = defaultdict(lambda: 0)
program.update(
    (i, int(n))
    for i, n in enumerate(input().split(','))
)

grid = defaultdict(lambda: 0)
game = output_only_program()
while True:
    try:
        x = next(game)
        y = next(game)
        tile_id = next(game)

        grid[ (x, y) ] = tile_id
    except StopIteration:
        break

print(list(grid.values()).count(2))
