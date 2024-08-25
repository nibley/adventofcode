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
by_number = {} # number of containers to number of different ways under that number
for combination in valid_combinations:
    number = len(combination)
    by_number.setdefault(number, 0)
    by_number[number] += 1

print(by_number[ sorted(by_number.keys())[0] ])
