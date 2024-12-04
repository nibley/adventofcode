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

def count_matches(positions):
    text = ''.join(positions)
    return sum( text.count(xmas) for xmas in {'XMAS', 'SAMX'} )

horizontal = sum(
    count_matches( grid[ (x, y) ] for x in range(width) )
    for y in range(height)
)

vertical = sum(
    count_matches( grid[ (x, y) ] for y in range(height) )
    for x in range(width)
)

down_and_right = sum(
    count_matches(
        grid[ (x + y, y) ] for y in range(-1 * height, height)
    )
    for x in range(-1 * width, width)
)

down_and_left = sum(
    count_matches(
        grid[ (x + (height - y), y) ] for y in range(height, -1 * height, -1)
    )
    for x in range(width, -1 * width, -1)
)

print(horizontal + vertical + down_and_right + down_and_left)
