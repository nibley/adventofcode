from math import inf

raw = input()
shortest_length = inf
units = set(raw.lower())
for unit in units:
    unit_inverse = unit.upper()
    polymer = raw.replace(unit, '').replace(unit_inverse, '')
    
    while True:
        old_polymer_length = len(polymer)
    
        for unit in units:
            unit_inverse = unit.upper()
            polymer = polymer.replace( \
                f'{unit}{unit_inverse}', '').replace( \
                f'{unit_inverse}{unit}', '')

        polymer_length = len(polymer)
        if polymer_length == old_polymer_length:
            break

    if polymer_length < shortest_length:
        shortest_length = polymer_length

print(shortest_length)
