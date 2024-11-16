from itertools import chain, product as cartesian_product
from functools import cache

serial = int(input())

grid = {
    (x, y) :
    ((x + 10) * (y * (x + 10) + serial) // 100) % 10 - 5
    for x, y in cartesian_product(
        range(1, 300 + 1),
        repeat=2
    )
}

@cache
def get_square_total(x, y, side_length):
    if side_length == 1:
        return grid[ (x, y) ]

    return sum(
        (
            # square with one less side length
            get_square_total(x, y, side_length - 1),
            # extended right edge, not including bottom-right corner
            sum(
                grid[ (x + side_length - 1, y_extended) ]
                for y_extended in range(y, y + side_length - 1)
            ),
            # extended bottom edge, including bottom-right corner
            sum(
                grid[ (x_extended, y + side_length - 1) ]
                for x_extended in range(x, x + side_length)
            )
        )
    )

side_lengths = iter(range(1, 300 + 1))
previous_best_total = 0
previous_best_position = None
best_total = 1
best_position = None
while best_total >= previous_best_total:
    previous_best_total = best_total
    previous_best_position = best_position

    side_length = next(side_lengths)
    best_total, *best_position = max(
        (
            get_square_total(*corner, side_length),
            *corner,
            side_length
        )
        for corner in cartesian_product(
            range(1, 300 - (side_length - 1) + 1),
            repeat=2
        )
    )

print('{},{},{}'.format(*previous_best_position))
