replacements = {}
line = input()
while line:
    start, end = line.split(' => ')
    replacements.setdefault(start, []).append(end)

    line = input()

molecule = input()

start_indices = {
    start : tuple(
        i
        for i in range(len(molecule) - len(start) + 1)
        if molecule[i : i + len(start)] == start
    )
    for start in replacements
}

new_molecules = set()
for start, ends in replacements.items():
    for start_index in start_indices[start]:
        for end in ends:
            before_start = molecule[ : start_index ]
            after_start = molecule[ start_index + len(start) : ]
            new_molecule = f'{before_start}{end}{after_start}'

            new_molecules.add(new_molecule)

print(len(new_molecules))
