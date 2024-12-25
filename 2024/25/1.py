from itertools import product as cartesian_product

HEIGHT = 7

locks = []
keys = []
while True:
    grid = []

    try:
        line = input()
    except EOFError:
        break

    while line:
        grid.append(line)

        try:
            line = input()
        except EOFError:
            line = ''

    assert len(grid) == HEIGHT
    heights = tuple( column.count('#') for column in zip(*grid) )

    if grid[0][0] == '#':
        locks.append(heights)
    else:
        keys.append(heights)

print(
    sum(
        all(
            lock_height + key_height <= HEIGHT
            for lock_height, key_height in zip(lock, key)
        )
        for lock, key in cartesian_product(locks, keys)
    )
)
