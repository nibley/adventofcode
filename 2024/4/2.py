from collections import defaultdict

grid = defaultdict(lambda: '_')
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
width = len(line)

print(
    sum(
        cell == 'A'
        and all(
            set( grid[corner] for corner in diagonal ) == {'S', 'M'}
            for diagonal in (
                (
                    (x - 1, y - 1), (x + 1, y + 1)
                ),
                (
                    (x + 1, y - 1), (x - 1, y + 1)
                )
            )
        )
        # tuple because of defaultdict key insertion
        for (x, y), cell in tuple(grid.items())
    )
)
