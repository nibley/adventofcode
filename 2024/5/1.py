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

    update = tuple(map(int, line.split(',')))
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

print(
    sum(
        update[ len(update) // 2 ]
        for update in updates
        if valid(update)
    )
)
