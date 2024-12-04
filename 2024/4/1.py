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
width = sum( x == 0 for x, _ in grid )

# print(height, width)

# TODO wrong height on small

print(
    (
    # sum(
    # tuple(
        sum(
            # horizontal
            sum(
                ''.join( grid[(x, y)] for x in range(width) ).count(xmas)
                for xmas in {'XMAS', 'SAMX'}
            )
            for y in range(height)
        )
        + sum(
            # vertical
            sum(
                ''.join( grid[(x, y)] for y in range(height) ).count(xmas)
                for xmas in {'XMAS', 'SAMX'}
            )
            for x in range(width)
        )
        + sum(
            # diagonal down/right
            sum(
                ''.join( grid[(x + y, y)] for y in range(-1 * height, height) ).count(xmas)
                for xmas in {'XMAS', 'SAMX'}
            )
            for x in range(-1 * width, width)
        )
        + sum(
            # diagonal down/left
            # ''.join( grid[(x + y, y)] for y in range(height, -1 * height, -1) )
            sum(
                ''.join( grid[(x + (height - y), y)] for y in range(height, -1 * height, -1) ).count(xmas)
                for xmas in {'XMAS', 'SAMX'}
            )
            for x in range(width, -1 * width, -1)
        )
    )
)
