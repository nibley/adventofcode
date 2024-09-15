import random

molecule = None
electron_direct_products = set()
replacements = []
while True:
    try:
        line = input()
    except EOFError:
        break

    if not line:
        molecule = input()
        continue

    end, start = line.split(' => ')
    if end == 'e':
        electron_direct_products.add(start)
    else:
        replacements.append( (start, end) )

def stochastic_approach(start_molecule):
    steps = 0
    molecule = start_molecule
    while True:
        old_molecule = molecule
        molecule_changed = False
        for _ in range(TRIES_BEFORE_GIVING_UP):
            replacement = random.choice(replacements)
            start, end = replacement

            num_matches = molecule.count(start)
            if num_matches:
                molecule_changed = True
                molecule = molecule.replace(start, end)
                steps += num_matches

        if not molecule_changed:
            return None

        if molecule in electron_direct_products:
            return steps + 1

TRIES_BEFORE_GIVING_UP = 40 # seems to work best
steps = None
while steps is None:
    steps = stochastic_approach(molecule)

print(steps)
