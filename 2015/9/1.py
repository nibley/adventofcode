from itertools import permutations
from functools import cache
from math import inf

edges = {}
def parse_edge(line):
    left_side, cost = line.split(' = ')
    source, destination = left_side.split(' to ')
    edges.setdefault(source, {})
    edges[source][destination] = int(cost)

@cache
def get_edge(source, destination):
    if source in edges and destination in edges[source]:
        return edges[source][destination]
    
    return edges[destination][source]
    
def path_cost(path):
    total_cost = 0
    for i, source in enumerate(path[:-1]):
        destination = path[i + 1]
        total_cost += get_edge(source, destination)
    return total_cost

while True:
    try:
        line = input()
    except EOFError:
        break
    
    parse_edge(line)

cheapest_path = ()
cheapest_cost = inf

nodes = set()
for k, v in edges.items():
    nodes.add(k)
    for k2 in v.keys():
        nodes.add(k2)
paths = permutations(nodes)
for path in paths:
    cost = path_cost(path)
    if cost < cheapest_cost:
        print(f'Found cheaper path {cost}')
        cheapest_path = path
        cheapest_cost = cost

print()
print(' -> '.join(cheapest_path))
print(cheapest_cost)
