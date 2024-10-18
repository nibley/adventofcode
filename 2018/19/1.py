# modified from 2018 16

program = []
instruction_binding = None
while True:
    try:
        line = input()
    except EOFError:
        break

    opcode, *arguments = line.split(' ')
    if opcode == '#ip':
        instruction_binding = int(arguments[0])
    else:
        program.append( (opcode, tuple( int(n) for n in arguments )) )

def run_instruction(instruction_index, opcode, arguments):
    if instruction_binding is not None:
        registers[instruction_binding] = instruction_index

    opcode_type = opcode[:3]
    if opcode_type[:2] in ('gt', 'eq'):
        # two-letter opcode types
        opcode_type = opcode_type[:2]
    
    a, b, c = arguments

    if opcode_type == 'set' and opcode[-1] == 'r':
        # i/r specifier only for register a
        a = registers[a]
    elif opcode_type in ('add', 'mul', 'ban', 'bor'):
        # i/r specifier only for register b
        a = registers[a]

        if opcode[-1] == 'r':
            b = registers[b]
    elif opcode_type in ('gt', 'eq'):
        # two i/r specifiers
        if opcode[-2] == 'r':
            a = registers[a]

        if opcode[-1] == 'r':
            b = registers[b]

    if opcode_type == 'add':
        output_value = a + b
    elif opcode_type == 'mul':
        output_value = a * b
    elif opcode_type == 'ban':
        output_value = a & b
    elif opcode_type == 'bor':
        output_value = a | b
    elif opcode_type == 'set':
        output_value = a
    elif opcode_type == 'gt':
        output_value = 1 if a > b else 0
    elif opcode_type == 'eq':
        output_value = 1 if a == b else 0

    registers[c] = output_value

    if instruction_binding is not None:
        instruction_index = registers[instruction_binding]

    instruction_index += 1
    return instruction_index

registers = [0, 0, 0, 0, 0, 0]
instruction_pointer = 0

while 0 <= instruction_pointer < len(program):
    opcode, arguments = program[instruction_pointer]
    instruction_pointer = run_instruction(
        instruction_pointer,
        opcode,
        arguments
    )

print(registers[0])
