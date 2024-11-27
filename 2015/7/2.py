from functools import cache

wires = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    wire_in, wire_out = line.split(' -> ')
    wire_in = wire_in.split()

    if len(wire_in) == 1: # constant
        value_in = ('CONST', *wire_in)
    elif len(wire_in) == 2: # NOT operator ('NOT', arg)
        value_in = wire_in
    else: # other operator
        left, operator, right = wire_in
        value_in = (operator, left, right)

    # (operator, [args ...])
    wires[wire_out] = value_in

@cache
def evaluate(wire):
    try:
        return int(wire)
    except ValueError:
        wire_in = wires[wire]

    operator, *arguments = wire_in
    first_argument, *rest = map(evaluate, arguments)

    if operator == 'CONST':
        return first_argument
    elif operator == 'NOT':
        return ~ first_argument
    else:
        second_argument, *_ = rest

        if operator == 'AND':
            return first_argument & second_argument
        elif operator == 'OR':
            return first_argument | second_argument
        elif operator == 'LSHIFT':
            return first_argument << second_argument
        elif operator == 'RSHIFT':
            return first_argument >> second_argument

    assert False

wires['b'] = ('CONST', '46065')
print(evaluate('a'))
