from collections import Counter
from itertools import pairwise

molecule_raw = input()
*_, LAST_CHAR = molecule_raw

molecule = Counter(pairwise(molecule_raw))
input()

rules = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    start, end = line.split(' -> ')
    rules[ tuple(start) ] = end

def simulate_turn(molecule):
    result = Counter()

    for pair, count in molecule.items():
        insertion = rules[pair]

        first, second = pair
        result[ (first, insertion) ] += count
        result[ (insertion, second) ] += count

    return result

for _ in range(10):
    molecule = simulate_turn(molecule)

counter = Counter()
for (first, _), count in molecule.items():
    counter[first] += count

counter[LAST_CHAR] += 1

(_, high_count), *_, (_, low_count) = counter.most_common()
print(high_count - low_count)
