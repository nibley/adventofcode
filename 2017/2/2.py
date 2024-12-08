from itertools import combinations

rows = []
while True:
    try:
        line = input()
    except EOFError:
        break

    rows.append(
        # sort so that combinations will only produce (a, b) where a < b
        sorted(map(int, line.split()))
    )

print(
    sum(
        next(
            dividend // divisor
            for divisor, dividend in combinations(row, 2)
            if not dividend % divisor
        )
        for row in rows
    )
)
