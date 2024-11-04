from math import inf

crabs = sorted( int(n) for n in input().split(',') )

lowest_cost = inf
for position in range(crabs[0], crabs[-1] + 1):
    cost = 0
    for crab in crabs:
        delta = abs(crab - position)
        cost += (delta * (delta + 1)) // 2

    if cost < lowest_cost:
        lowest_cost = cost

print(lowest_cost)
