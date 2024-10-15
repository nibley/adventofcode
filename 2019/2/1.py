program = [ int(n) for n in input().split(',') ]

program[1] = 12
program[2] = 2

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

print(program[0])
