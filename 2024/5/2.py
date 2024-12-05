from itertools import permutations

rules = []
line = input()
while line:
    rules.append(tuple(map(int, line.split('|'))))
    line = input()

updates = []
while True:
    try:
        line = input()
    except EOFError:
        break

    update = list(map(int, line.split(',')))
    assert len(update) % 2

    updates.append(update)

def valid(update):
    for first, second in zip(
        update[    : -1 ],
        update[ 1  :    ]
    ):
        for before, after in rules:
            if (
                set( (before, after) ) == set( (first, second) )
                and not (before == first and after == second)
            ):
                return False

    return True

def fix(update):
    print('fix')

    for (i, first), (j, second) in zip(
        enumerate(update[    : -1 ]),
        enumerate(update[ 1  :    ], start=1)
    ):
        for before, after in rules:
            if (
                set( (before, after) ) == set( (first, second) )
                and not (before == first and after == second)
            ):
                update[i], update[j] = update[j], update[i]

invalid_updates = tuple(
    update
    for update in updates
    if not valid(update)
)

fixed_updates = []
for update in invalid_updates:
    while not valid(update):
        # update = fix(update)
        fix(update)

    fixed_updates.append(update)
    print(len(fixed_updates))
    print()

print(
    sum(
        update[ len(update) // 2 ]
        for update in fixed_updates
    )
)
