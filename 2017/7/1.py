program_names = set()
child_to_parent = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    pieces = line.split(' -> ')
    if len(pieces) == 1:
        name, _ = pieces[0].split(' ')
        children = ()
    else:
        left_side, right_side = pieces
        name, _ = left_side.split(' ')
        children = tuple(right_side.split(', '))

    for child in children:
        child_to_parent[child] = name

    program_names.add(name)

print(*( program_names - set(child_to_parent.keys()) ))
