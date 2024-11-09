resolved_monkeys = {}
formula_monkeys = {}
root_inputs = None
while True:
    try:
        line = input()
    except EOFError:
        break

    monkey, formula = line.split(': ')

    if monkey == 'humn':
        continue

    if formula.isnumeric():
        resolved_monkeys[monkey] = int(formula)
    else:
        first_input, operator, second_input = formula.split(' ')

        if monkey == 'root':
            root_inputs = first_input, second_input
        else:
            formula_monkeys[monkey] = (first_input, operator, second_input)

def derive_formula(monkey):
    if monkey == 'humn':
        return monkey
    elif monkey in resolved_monkeys:
        return str(resolved_monkeys[monkey])
    else:
        first_input, operator, second_input = formula_monkeys[monkey]

        first_input_formula = derive_formula(first_input)
        second_input_formula = derive_formula(second_input)

        return f'({first_input_formula}) {operator} ({second_input_formula})'

first_root_input_formula = derive_formula(root_inputs[0])
second_root_input_formula = derive_formula(root_inputs[1])

def solve(formula):
    # from https://code.activestate.com/recipes/365013-linear-equations-solver-in-3-lines/
    formula = formula.replace('=', ' - (') + ')'
    complex_solution = eval(formula, {'humn': 1j})
    return int((-1 * complex_solution.real) / complex_solution.imag)

print(solve(f'{first_root_input_formula} = {second_root_input_formula}'))
