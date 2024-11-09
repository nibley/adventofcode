from operator import add, sub, mul, floordiv

number_monkeys = {}
formula_monkeys = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    monkey, formula = line.split(': ')
    if formula.isnumeric():
        number_monkeys[monkey] = int(formula)
    else:
        formula_monkeys[monkey] = formula.split(' ')

operators = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : floordiv
}

while formula_monkeys:
    monkeys_resolved = []
    for monkey, formula in formula_monkeys.items():
        (first_input, operator, second_input) = formula
        if first_input in number_monkeys and second_input in number_monkeys:
            first_input = number_monkeys[first_input]
            second_input = number_monkeys[second_input]

            resolved_number = operators[operator](first_input, second_input)
            number_monkeys[monkey] = resolved_number
            monkeys_resolved.append(monkey)

    for monkey_resolved in monkeys_resolved:
        del formula_monkeys[monkey_resolved]

print(number_monkeys['root'])
