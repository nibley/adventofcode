program_names = set()
child_to_parent = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    name, _, *rest = line.replace(',', '').split()
    program_names.add(name)

    if rest:
        _, *children = rest
    else:
        children = ()

    for child in children:
        child_to_parent[child] = name

programs_without_parents = program_names.difference(child_to_parent)
assert len(programs_without_parents) == 1
print(programs_without_parents.pop())
