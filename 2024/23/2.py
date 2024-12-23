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
    edges[first].add(first)

    edges.setdefault(second, set())
    edges[second].add(first)
    edges[second].add(second)

    computers.add(first)
    computers.add(second)

good = []
for computer in computers:
    connected = edges[computer]

    for length in range(1, len(connected) + 1):
        for combination in combinations(connected, length):
            if all(
                computer in edges[other]
                for computer in combination
                for other in combination
                if computer != other
            ):
                good.append(frozenset(combination))

biggest = max(
    good,
    key=len
)

print(
    ','.join(
        map(str, sorted(biggest))
    )
)
