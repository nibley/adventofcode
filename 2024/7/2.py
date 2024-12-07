from operator import add, mul
from itertools import product as cartesian_product

equations = []
while True:
    try:
        line = input()
    except EOFError:
        break

    test_value, *numbers = map(int, line.replace(':', '').split())
    equations.append( (test_value, numbers) )

concat = lambda first, second: int(f'{first}{second}')

def equation_is_possible(test_value, NUMBERS_INITIAL):
    for operators in cartesian_product(
        (add, mul, concat),
        repeat=len(NUMBERS_INITIAL) - 1
    ):
        left_operand, *numbers = NUMBERS_INITIAL
        for right_operand, operator in zip(numbers, operators):
            left_operand = operator(left_operand, right_operand)

        if left_operand == test_value:
            return True

    return False

print(
    sum(
        test_value
        for test_value, numbers in equations
        if equation_is_possible(test_value, numbers)
    )
)
