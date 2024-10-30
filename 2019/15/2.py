# modified from 2019 13

from collections import defaultdict

def communicating_program():
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

    # one input is used by the input opcode (3)
    # before the output opcode (4) first gets hit
    # and is able to receive further input
    # through its yield expression
    input_queue = [ (yield) ]

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
                write_position = get_argument(1, write=True)
                assert len(input_queue) > 0
                write_value = input_queue.pop()
            elif opcode == 4: # output
                output_value = get_argument(1)
                received_value = (yield output_value)
                assert type(received_value) is int
                input_queue.append(received_value)
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
            assert type(write_value) is int, f'op {opcode}'
            program[write_position] = write_value

program = defaultdict(lambda: 0)
program.update(
    (i, int(n))
    for i, n in enumerate(input().split(','))
)

robot = communicating_program()
next(robot) # prime program to receive input

grid = defaultdict(lambda: True)
x = 0
y = 0
visited = set([ (x, y) ])

neighbor_offsets = {
    1: ( 0,  1),
    2: ( 0, -1),
    3: (-1,  0),
    4: ( 1,  0),
}

def get_open_neighbors(x, y):
    for movement, (offset_x, offset_y) in neighbor_offsets.items():
        neighbor = (x + offset_x, y + offset_y)
        cell = grid[neighbor]
        if neighbor not in visited and cell:
            yield (movement, neighbor)

inverse_movements = {
    1: 2,
    2: 1,
    3: 4,
    4: 3,
}

movements = []
oxygen_source = None
found_move = True # stop while loop from exiting immediately
while found_move or movements:
    found_move = False
    for movement, neighbor in get_open_neighbors(x, y):
        neighbor_x, neighbor_y = neighbor

        result = robot.send(movement)
        if result == 0:
            grid[neighbor] = False
        else:
            found_move = True
            movements.append(movement)
            visited.add(neighbor)
            x, y = neighbor

            if result == 2:
                oxygen_source = neighbor

            break

    if not found_move:
        last_movement = movements.pop()
        backwards_movement = inverse_movements[last_movement]
        result = robot.send(backwards_movement)

        assert result == 1

        offset_x, offset_y = neighbor_offsets[backwards_movement]
        x += offset_x
        y += offset_y

num_open_cells = len(visited)
visited = set( [oxygen_source] )
oxygen_fronts = [oxygen_source]
turns = 0
while len(visited) < num_open_cells:
    new_oxygen_fronts = []
    for x, y in oxygen_fronts:
        for _, neighbor in get_open_neighbors(x, y):
            visited.add(neighbor)
            new_oxygen_fronts.append(neighbor)

    oxygen_fronts = new_oxygen_fronts
    turns += 1

print(turns)
