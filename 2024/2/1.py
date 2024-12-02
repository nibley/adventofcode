lines = []
while True:
    try:
        line = input()
    except EOFError:
        break

    lines.append(
        tuple(
            int(item) for item in line.split()
        )
    )

def valid(line, predicate):
    for first, second in zip(
        line[    : -1 ],
        line[  1 :    ]
    ):
        if (
            not 1 <= abs(second - first) <= 3
            or not predicate(first, second)
        ):
            return False

    return True

print(
    sum(
        any(
            valid(line, predicate)
            for predicate in (
                lambda first, second: first > second,
                lambda first, second: first < second
            )
        )
        for line in lines
    )
)
