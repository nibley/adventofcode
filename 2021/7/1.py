from math import inf

crabs = sorted( int(n) for n in input().split(',') )

lowest_cost = inf
for position in range(crabs[0], crabs[-1] + 1):
    cost = sum(abs(crab - position) for crab in crabs)
    if cost < lowest_cost:
        lowest_cost = cost

print(lowest_cost)
