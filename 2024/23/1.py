from itertools import combinations

edges = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    first, second = line.split('-')

    edges.setdefault(first, set()).add(second)
    edges.setdefault(second, set()).add(first)

print(
    sum(
        any( computer[0] == 't' for computer in triplet )
        and all(
            first in edges[second] and second in edges[first]
            for first, second in combinations(triplet, 2)
        )
        for triplet in combinations(edges, 3)
    )
)
