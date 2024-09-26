polymer = input()
units = set(polymer.lower())

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

print(polymer_length)
