from functools import cache

adapters = []
while True:
    try:
        line = input()
    except EOFError:
        break

    adapters.append(int(line))

adapters = tuple([0] + sorted(adapters))

@cache
def count_choices(adapter, adapters):
    candidates = [
        candidate for candidate in adapters[ : 3 ]
        if candidate - adapter <= 3
    ]

    if not candidates:
        return 1

    return sum(
        count_choices(
            candidate,
            tuple(
                other_candidate for other_candidate in adapters[ : 3 ]
                if other_candidate > candidate
            ) + adapters[ 3 : ]
        )
        for candidate in candidates
    )

print(count_choices(adapters[0], adapters[ 1 : ]))
