from functools import cache
from itertools import permutations

nodes = set()
edges = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    source, _, destination, _, cost = line.split()

    nodes.update({source, destination})

    edges.setdefault(source, {})
    edges[source][destination] = int(cost)

@cache
def get_edge(source, destination):
    if source in edges and destination in edges[source]:
        return edges[source][destination]
    else:
        return edges[destination][source]

print(
    min(
        sum(
            get_edge(source, destination)
            for source, destination in zip(
                path[    : -1 ],
                path[  1 :    ],
            )
        )
        for path in permutations(nodes)
    )
)
