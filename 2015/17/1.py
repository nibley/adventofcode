from itertools import combinations

containers = []
while True:
    try:
        line = input()
        containers.append(int(line))
    except EOFError:
        break

all_combinations = list()
for i in range(len(containers)):
    all_combinations.extend(combinations(containers, i + 1))

valid_combinations = list(combination for combination in all_combinations if sum(combination) == 150)
print(len(valid_combinations))
