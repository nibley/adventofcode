parent_to_children = {}
child_to_parent = {}
weights = {}
program_names = set()
while True:
    try:
        line = input()
    except EOFError:
        break

    pieces = line.split(' -> ')
    if len(pieces) == 1:
        left_side = pieces[0]
        children = ()
    else:
        left_side, right_side = pieces
        children = tuple(right_side.split(', '))

    name, weight = left_side.split(' ')
    weight = int(weight[1:-1])

    program_names.add(name)
    parent_to_children[name] = children
    for child in children:
        child_to_parent[child] = name
    weights[name] = weight

root = ( program_names - set(child_to_parent.keys()) ).pop()

def tower_weight(name):
    total = weights[name]
    for child in parent_to_children[name]:
        total += tower_weight(child)

    return total

def unbalanced_child(name):
    pairs = [ (child, tower_weight(child)) for child in parent_to_children[name] ]
    pairs.sort(key=lambda pair: pair[1])

    if pairs[0][1] == pairs[-1][1]:
        return None
    elif pairs[0][1] == pairs[1][1]:
        return pairs[-1][0]
    else:
        return pairs[0][0]

problem_program = root
while True:
    next_problem = unbalanced_child(problem_program)
    if next_problem is None:
        break

    problem_program = next_problem

parent_of_problem = child_to_parent[problem_program]
balanced_sibling = [
    sibling for sibling \
    in parent_to_children[parent_of_problem] \
    if sibling != problem_program
][0]
balanced_weight = tower_weight(balanced_sibling)

child_weight = weights[ parent_to_children[problem_program][0] ]
children_weight = child_weight * len(parent_to_children[problem_program])
needed_weight = balanced_weight - children_weight

print(needed_weight)
