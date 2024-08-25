molecule = ''
final_line_next = False
replacements = {}
new_molecules = set()
while True:
    try:
        line = input()
        if final_line_next:
            molecule = line
        elif line == '':
            final_line_next = True
        else:
            start, end = line.split(' => ')
            replacements.setdefault(start, [])
            replacements[start].append(end)
    except EOFError:
        break

starts = replacements.keys()
start_indices = {}
for start in starts:
    indices = [i for i in range(len(molecule) - len(start) + 1) if molecule[i : i + len(start)] == start]
    start_indices[start] = indices
    
for start in starts:
    for start_index in start_indices[start]:
        for end in replacements[start]:
            before_start = molecule[:start_index]
            after_start = molecule[start_index + len(start):]
            new_molecule = f'{before_start}{end}{after_start}'
            new_molecules.add(new_molecule)

print(len(new_molecules))
