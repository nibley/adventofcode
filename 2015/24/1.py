from itertools import combinations
from math import prod

weights = []
while True:
    try:
        line = input()
    except EOFError:
        break

    weights.append(int(line))

compartment_weight = sum(weights) // 3
valid_compartments = None
for sublist_length in range(1, len(weights) + 1):
    valid_sublists = tuple(
        sublist
        for sublist in combinations(weights, sublist_length)
        if sum(sublist) == compartment_weight
    )
    if valid_sublists:
        valid_compartments = valid_sublists
        break

assert valid_compartments is not None
print(
    min(
        prod(valid_compartment)
        for valid_compartment in valid_compartments
    )
)
