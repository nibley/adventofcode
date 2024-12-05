from itertools import permutations

rules = []
line = input()
while line:
    a, b = map(int, line.split('|'))
    line = input()
    rules.append((a, b))

updates = []
while True:
    try:
        line = input()
    except EOFError:
        break

    updates.append(
        list(map(int, line.split(',')))
    )

for update in updates:
    assert len(update) % 2

def valid(update):
    for first, second in zip(
        update[:-1], update[1:]
    ):
        for before, after in rules:
            if set((before, after)) == set((first, second)):
                if not (before == first and after == second):
                    return False

    return True

# def fix(update):
#     print('fix')
#     for permutation in permutations(update):
#         permutation = tuple(permutation)
#         if valid(permutation):
#             return permutation

#     assert False

def fix(update):
    update = update[:]
    # print('fix', update)

    result = list(update)

    for i, (first, second) in enumerate(zip(
        update[:-1], update[1:]
    )):
        for before, after in rules:
            if set((before, after)) == set((first, second)):
                if (before == first and after == second):
                    # result.append(first)
                    # result.append(second)
                    pass
                else:
                    # print(update, update[i], update[i + 1], i, len(update))
                    result[i], result[i + 1] = result[i + 1], result[i]
                    # print(result)
                    # break
                    return result

    # print()
    return tuple(result)

invalid_updates = tuple(
    # fix(update)
    update
    for update in updates
    if not valid(update)
)

# invalid_updates = ((75,97,47,61,53),)

fixed = []
for update in invalid_updates:
    while not valid(update):
        update = fix(update)

    fixed.append(update)
    print('got')
    # print(update)

print('\n\n\n')

total = 0
for update in fixed:
    print(update)

    i = len(update) // 2
    total += update[i]
    # print(update[i])

print(total)
