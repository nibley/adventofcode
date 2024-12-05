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
        tuple(map(int, line.split(',')))
    )

for update in updates:
    assert len(update) % 2

def valid(update):
    for first, second in zip(
        update[:-1], update[1:]
    ):
        for before, after in rules:
            if set((before, after)) == set((first, second)):
                print(1)
                if not (before == first and after == second):
                    print('bad', first, second, ' | ', before, after)
                    return False

    return True

valid_updates = tuple(
    update
    for update in updates
    if valid(update)
)

for update in valid_updates:
    print(update)

total = 0
for update in valid_updates:
    i = len(update) // 2
    total += update[i]
    # print(update[i])

print(total)
