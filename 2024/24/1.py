presets = {}
line = input()
while line:
    wire, value = line.split(': ')
    presets[wire] = value == '1'

    line = input()

formulas = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    inputs, result = line.split(' -> ')
    inputs = inputs.split()

    formulas[result] = inputs

def evaluate(formula):
    left, operator, right = formula

    if left in presets:
        left = presets[left]
    else:
        left = evaluate(formulas[left])

    if right in presets:
        right = presets[right]
    else:
        right = evaluate(formulas[right])

    if operator == 'AND':
        return left and right
    elif operator == 'OR':
        return left or right
    elif operator == 'XOR':
        return left ^ right

z_bits = {}
for wire, formula in formulas.items():
    if wire[0] != 'z':
        continue

    z_bits[ int(wire[1:]) ] = evaluate(formula)

final = int(
    ''.join(
        '1' if z_bits[bit] else '0'
        for bit in sorted(z_bits, reverse=True)
    ),
    2
)
print(final)
