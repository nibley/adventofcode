program_names = set()
parent_to_children = {}
child_to_parent = {}
weights = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    name, weight, *rest = line.replace(',', '').split()
    program_names.add(name)
    weights[name] = eval(weight)

    if rest:
        _, *children = rest
    else:
        children = ()

    for child in children:
        child_to_parent[child] = name

    parent_to_children[name] = tuple(children)

programs_without_parents = program_names.difference(child_to_parent)
assert len(programs_without_parents) == 1
root_program = programs_without_parents.pop()

def subtree_weight(name):
    children = parent_to_children[name]
    return weights[name] + sum(map(subtree_weight, children))

def get_unbalanced_child(name):
    children_by_weight = {}
    for child in parent_to_children[name]:
        weight = subtree_weight(child)
        children_by_weight.setdefault(weight, set()).add(child)

    return next(
        (
            next(iter(children)) # like set.pop but don't pop
            for children in children_by_weight.values()
            if len(children) == 1
        ),
        None
    )

problem_program = root_program
child = get_unbalanced_child(problem_program)
while child is not None:
    problem_program, child = child, get_unbalanced_child(child)

balanced_weight = subtree_weight(
    next(
        sibling
        for sibling in parent_to_children[
            child_to_parent[problem_program]
        ]
        if sibling != problem_program
    )
)

children_of_problem = parent_to_children[problem_program]
child_weights = set(map(subtree_weight, children_of_problem))
assert len(child_weights) == 1

print()
print(balanced_weight - child_weights.pop() * len(children_of_problem))
