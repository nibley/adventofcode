from itertools import combinations
from math import inf
from functools import reduce

weights = []
while True:
    try:
        line = input()
    except EOFError:
        break
    
    weights.append(int(line))

num_weights = len(weights)
total_weight = sum(weights)
compartment_weight = total_weight // 4

valid_passenger_compartments = []
for sublist_length in range(1, num_weights + 1):
    given_length_sublists = combinations(weights, sublist_length)
    valid_sublists = [sublist for sublist in given_length_sublists if sum(sublist) == compartment_weight]
    if valid_sublists:
        valid_passenger_compartments = valid_sublists
        break

best_quantum_value = inf
for valid_passenger_compartment in valid_passenger_compartments:
    quantum_value = reduce(lambda x, y: x * y, valid_passenger_compartment, 1)
    if quantum_value < best_quantum_value:
        best_quantum_value = quantum_value

print(best_quantum_value)
