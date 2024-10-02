from collections import defaultdict

samples = []
while True:
    try:
        line = input()
    except EOFError:
        break

    if not line:
        input()
        break

    before = list(map(int, line.split(' [')[1][:-1].split(', ')))
    bytecode = tuple(map(int, input().split(' ')))
    after = list(map(int, input().split(' [')[1][:-1].split(', ')))
    input()

    samples.append( (before, bytecode, after) )

program = []
while True:
    try:
        line = input()
    except EOFError:
        break

    program.append(tuple( int(n) for n in line.split(' ') ))

opcode_names = [
    'addr', 'addi', 'mulr', 'muli',
    'banr', 'bani', 'borr', 'bori',
    'setr', 'seti', 'gtir', 'gtri',
    'gtrr', 'eqir', 'eqri', 'eqrr',
]

def simulate(opcode, args, before):
    a, b, c = args

    opcode_type = opcode[:3]
    if opcode_type[:2] in ('gt', 'eq'):
        # two-letter opcode types
        opcode_type = opcode_type[:2]

    if opcode_type == 'set' and opcode[-1] == 'r':
        # i/r specifier only for register a
        a = before[a]
    elif opcode_type in ('add', 'mul', 'ban', 'bor'):
        # i/r specifier only for register b
        a = before[a]

        if opcode[-1] == 'r':
            b = before[b]
    elif opcode_type in ('gt', 'eq'):
        # two i/r specifiers
        if opcode[-2] == 'r':
            a = before[a]

        if opcode[-1] == 'r':
            b = before[b]

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

    before[c] = output_value
    return before

# determine possible correspondences from samples
opcodes_to_crawl = defaultdict(set) # opcode name : opcode number
for before, bytecode, after in samples:
    opcode_number, *arguments = bytecode

    for opcode_name in opcode_names:
        if simulate(opcode_name, arguments, before[:]) == after:
            opcodes_to_crawl[opcode_name].add(opcode_number)

# determine actual correspondences
known_opcodes = {} # opcode number : opcode name
while opcodes_to_crawl:
    new_known_opcodes = {} # opcode number : opcode name
    for opcode_name, opcode_numbers in opcodes_to_crawl.items():
        if len(opcode_numbers) == 1:
            new_known_opcodes[opcode_numbers.pop()] = opcode_name

    for opcode_number, opcode_name in new_known_opcodes.items():
        del opcodes_to_crawl[opcode_name]
        known_opcodes[opcode_number] = opcode_name

        for possible_opcode_numbers in opcodes_to_crawl.values():
            possible_opcode_numbers.discard(opcode_number)

# run the program
register_0 = 0
register_1 = 0
register_2 = 0
register_3 = 0

for opcode_number, *arguments in program:
    register_0, register_1, register_2, register_3 = \
    simulate(
        known_opcodes[opcode_number],
        arguments,
        [register_0, register_1, register_2, register_3]
    )

print(register_0)
