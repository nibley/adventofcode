from itertools import combinations

edges = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    first, second = line.split('-')

    edges.setdefault(first, set()).update(
        (first, second)
    )
    edges.setdefault(second, set()).update(
        (first, second)
    )

options = (
    combination
    for neighbors in edges.values()
    for length in range(2, len(neighbors) + 1)
    for combination in combinations(neighbors, length)
    if all(
        first in edges[second] and second in edges[first]
        for first, second in combinations(combination, 2)
    )
)

print(
    ','.join(
        sorted(max(options, key=len))
    )
)
