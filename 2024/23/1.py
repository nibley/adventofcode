from itertools import combinations

edges = {}
computers = set()
while True:
    try:
        line = input()
    except EOFError:
        break

    first, second = line.split('-')

    edges.setdefault(first, set())
    edges[first].add(second)

    edges.setdefault(second, set())
    edges[second].add(first)

    computers.add(first)
    computers.add(second)

triplets = set()
for triplet in combinations(computers, 3):
    a, b, c = triplet
    if (
        b in edges[a] and c in edges[a]
        and a in edges[b] and c in edges[b]
        and a in edges[c] and b in edges[c]
    ):
        triplets.add(frozenset(triplet))

print(len(triplets))

total = 0
for triplet in triplets:
    if any(
        computer[0] == 't'
        for computer in triplet
    ):
        total += 1

print(total)
