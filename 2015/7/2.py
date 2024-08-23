from functools import cache

values = {}

@cache
def evaluate(wire):
    try:
        const_value = int(wire)
        return const_value
    except ValueError:
        wire_in = values[wire]
    
    operator = wire_in[0]
    if operator == 'CONST':
        arg = wire_in[1]
        value = evaluate(arg)
    elif operator == 'NOT':
        arg = wire_in[1]
        value = ~ evaluate(arg)
    elif operator == 'AND':
        arg_left = wire_in[1]
        arg_right = wire_in[2]
        value = evaluate(arg_left) & evaluate(arg_right)
    elif operator == 'OR':
        arg_left = wire_in[1]
        arg_right = wire_in[2]
        value = evaluate(arg_left) | evaluate(arg_right)
    elif operator == 'LSHIFT':
        arg_left = wire_in[1]
        arg_right = wire_in[2]
        value = evaluate(arg_left) << evaluate(arg_right)
    elif operator == 'RSHIFT':
        arg_left = wire_in[1]
        arg_right = wire_in[2]
        value = evaluate(arg_left) >> evaluate(arg_right)
    
    return value

while True:
    try:
        line = input()
    except EOFError:
        break
    
    wire_in, wire_out = line.split(' -> ')
    pieces_in = wire_in.split(' ')
    
    if len(pieces_in) == 1:
        value_in = ('CONST', pieces_in[0])
    elif len(pieces_in) == 2:
        value_in = ('NOT', pieces_in[1])
    else:
        value_in = (pieces_in[1], pieces_in[0], pieces_in[2])
    
    values[wire_out] = value_in

values['b'] = ('CONST', '46065')

print(evaluate('a'))
