# from collections import defaultdict
# grid = defaultdict(lambda: '_')

grid = {}
y = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, char in enumerate(line):
        grid[ (x, y) ] = char

    y += 1

height = y
width = sum( x == 0 for x, _ in grid )

# TODO wrong height on small test

total = 0
for (x, y), cell in grid.items():
    if cell != 'A':
        continue

    if (
        all(
            diagonal == {'S', 'M'}
            for diagonal in (
                set(
                    (
                        grid.get((x - 1, y - 1), '_'),
                        grid.get((x + 1, y + 1), '_')
                    )
                ),
                set(
                    (
                        grid.get((x + 1, y - 1), '_'),
                        grid.get((x - 1, y + 1), '_')
                    )
                )
            )
        )
    ):
        total += 1

print(total)
