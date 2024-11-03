# modified from 2018 8

from operator import add, mul

operators = {
    '+': add,
    '*': mul
}

def parse_expression(expression, cursor=0):
    operator = None
    left_operand = None
    right_operand = None

    while cursor < len(expression):
        char = expression[cursor]

        if char == ' ':
            cursor += 1
            continue
        elif char == ')':
            break
        elif char in '+*':
            operator = operators[char]
        else: # '(' or number
            if char == '(':
                cursor += 1
                cursor, operand = parse_expression(expression, cursor)
            else: # char is a number -- they seem to all be one-digit
                operand = int(char)

            if left_operand is None:
                left_operand = operand
            else:
                right_operand = operand


        if right_operand is not None: # accumulate into left_operand
            left_operand = operator(left_operand, right_operand)

            operator = None
            right_operand = None

        cursor += 1

    return (cursor, left_operand)

total = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    _, evaluation = parse_expression(line)
    total += evaluation

print(total)
