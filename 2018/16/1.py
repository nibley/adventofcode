samples = []
while True:
    try:
        line = input()
    except EOFError:
        break

    if not line:
        break # ignore the lower section of input

    before = list(map(int, line.split(' [')[1][:-1].split(', ')))
    bytecode = tuple(map(int, input().split(' ')))
    after = list(map(int, input().split(' [')[1][:-1].split(', ')))
    input()

    samples.append( (before, bytecode, after) )

opcodes = [
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
        # i/r specifier only for register b, a always register
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

ambiguous_total = 0
for before, bytecode, after in samples:
    possibilities = 0
    for opcode in opcodes:
        if possibilities >= 3:
            break

        result = simulate(opcode, bytecode[1:], before[:])
        if result == after:
            possibilities += 1

    if possibilities >= 3:
        ambiguous_total += 1

print(ambiguous_total)
