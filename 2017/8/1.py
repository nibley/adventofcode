from collections import defaultdict

program = []
while True:
    try:
        line = input()
    except EOFError:
        break

    operation, test_expression = line.split(' if ')
    register, direction, offset = operation.split()
    offset = (1 if direction == 'inc' else -1) * int(offset)

    program.append(
        (register, offset, test_expression)
    )

registers = defaultdict(lambda: 0)
for register, offset, test_expression in program:
    if eval(test_expression, None, registers):
        registers[register] += offset

print(max(registers.values()))

