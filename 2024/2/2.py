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

def valid(line, exclude, predicate):
    line = list(line)
    del line[exclude]

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
            valid(line, exclude, predicate)
            for exclude in range(len(line))
            for predicate in (
                lambda first, second: first > second,
                lambda first, second: first < second
            )
        )
        for line in lines
    )
)
