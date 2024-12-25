registers = {}

line = input()
while line:
    _, register, value = line.replace(':', '').split()
    value = int(value)

    registers[register] = value

    line = input()

_, program = input().split(': ')
program = tuple(map(int, program.split(',')))

assert not len(program) % 2

def get_combo(operand):
    if operand in {0, 1, 2, 3}:
        return operand
    elif operand == 4:
        return registers['A']
    elif operand == 5:
        return registers['B']
    elif operand == 6:
        return registers['C']
    elif operand == 7:
        assert False

def run_instruction(instruction):
    opcode = program[instruction]
    operand = program[instruction + 1]

    print(opcode, operand)

    if opcode == 0:
        # adv
        dividend = registers['A']
        divisor = 2 ** get_combo(operand)

        registers['A'] = dividend // divisor
        print('  set A to ', registers['A'])
    elif opcode == 1:
        # bxl
        registers['B'] = registers['B'] ^ operand
        print('  set B to', registers['B'])
    elif opcode == 2:
        # bst
        registers['B'] = get_combo(operand) % 8
        print('  set B to', registers['B'])
    elif opcode == 3:
        # jnz
        if registers['A']:
            print('jump to', operand)
            return operand
        print('  no jump')
    elif opcode == 4:
        # bxc
        registers['B'] = registers['B'] ^ registers['C']
        print('  set B to', registers['B'])
    elif opcode == 5:
        # out
        value = get_combo(operand) % 8
        print('output', value)
        output_queue.append(value)
    elif opcode == 6:
        # bdv
        dividend = registers['A']
        divisor = 2 ** get_combo(operand)

        registers['B'] = dividend // divisor
        print('  set B to', registers['B'])
    elif opcode == 7:
        # cdv
        dividend = registers['A']
        divisor = 2 ** get_combo(operand)

        registers['C'] = dividend // divisor
        print('  set C to', registers['C'])

    return instruction + 2

output_queue = []

instruction = 0
while instruction in range(len(program)):
    print(instruction)

    instruction = run_instruction(instruction)

print(
    ','.join(
        str(n)
        for n in output_queue
    )
)
