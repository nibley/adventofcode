from collections import defaultdict

grid = defaultdict(lambda: '#')
y = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, char in enumerate(line):
        grid[ (x, y) ] = char # y is distance from north edge

    y += 1

height = y
width = len(grid) // height

for y in range(1, height):
    for x in range(width):
        stone_y = y
        while (
           grid[ (x, stone_y) ] == 'O'
           and grid[ (x, stone_y - 1) ] == '.'
        ):
           grid[ (x, stone_y - 1) ] = 'O'
           grid[ (x, stone_y) ] = '.'
           stone_y -= 1

print(
    sum(
        (height - y) * sum(grid[ (x, y) ] == 'O' for x in range(width))
        for y in range(height)
    )
)
