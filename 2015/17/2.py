from itertools import combinations

containers = []
while True:
    try:
        line = input()
    except EOFError:
        break

    containers.append(int(line))

combinations_by_length = (
    combinations(containers, i)
    for i in range(1, len(containers) + 1)
)

print(
    min(
        len(combination)
        for combinations in combinations_by_length
        for combination in combinations
        if sum(combination) == 150
    )
)
