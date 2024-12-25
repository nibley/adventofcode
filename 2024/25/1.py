from itertools import product as cartesian_product

grids = []
grid = []
while True:
    try:
        line = input()
        if line:
            grid.append(tuple(line))
        else:
            grids.append(tuple(grid))
            grid = []
    except EOFError:
        break
    finally:
        pass

grids.append(tuple(grid))

def visualize(grid):
    for row in grid:
        print(''.join(row))
    print()

locks = tuple(
    grid
    for grid in grids
    if all( cell == '#' for cell in grid[0] )
)

keys = tuple(
    grid
    for grid in grids
    if all( cell == '.' for cell in grid[0] )
)

print(len(locks), 'locks')
print(len(keys), 'keys')

def valid(lock, key):
    assert len(lock[0]) == len(key[0])
    total_height = len(lock)

    for x in range(len(lock[0])):
        y = 0
        while y < total_height and lock[y][x] == '#':
            y += 1

        lock_height = y - 1

        y = total_height - 1
        while y > 0 and key[y][x] == '#':
            # print('    key', y)
            y -= 1

        key_height = y + 1

        if not key_height > lock_height:
            return False

    return True

print(
    sum(
        valid(lock, key)
        for lock, key in cartesian_product(locks, keys)
    )
)
