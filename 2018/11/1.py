from itertools import product as cartesian_product

serial = int(input())

grid = {
    (x, y) :
    ((x + 10) * (y * (x + 10) + serial) // 100) % 10 - 5
    for x, y in cartesian_product(
        range(1, 300 + 1),
        repeat=2
    )
}

SIDE_LENGTH = 3

def get_positions(corner):
    x, y = corner
    for y_offset in range(SIDE_LENGTH):
        for x_offset in range(SIDE_LENGTH):
            yield (x + x_offset, y + y_offset)

best_position = max(
    cartesian_product(
        range(1, 300 + 1 - (SIDE_LENGTH - 1) ),
        repeat=2
    ),
    key=lambda corner: sum(map(grid.get, get_positions(corner)))
)
print('{},{}'.format(*best_position))
