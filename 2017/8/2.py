# modified from 2017 5

from collections import defaultdict

program = []
while True:
    try:
        line = input()
    except EOFError:
        break

    left_side, right_side = line.split(' if ')

    register, direction, offset = left_side.split(' ')
    offset = (1 if direction == 'inc' else -1) * int(offset)
    test_register, test_operator, test_value = right_side.split(' ')
    test_code = f'registers[\'{test_register}\'] {test_operator} {test_value}'

    program.append( (register, offset, test_code) )

highest_value = 0
registers = defaultdict(lambda: 0)
for register, offset, test_code in program:
    if eval(test_code):
        registers[register] += offset

    current_highest_value = max(registers.values())
    if current_highest_value > highest_value:
        highest_value = current_highest_value

print(highest_value)
