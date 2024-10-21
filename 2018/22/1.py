from functools import cache
from itertools import product as cartesian_product

# surprisingly, caching this slows down the solution!
def get_geologic_index(position):
    x, y = position

    if position in ( (0, 0), goal ):
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        return get_erosion_level( (x - 1, y) ) * get_erosion_level( (x, y - 1) )

@cache
def get_erosion_level(position):
    return (get_geologic_index(position) + depth) % 20183

depth = int(input().split(': ')[1])
goal = tuple(map(int, input().split(': ')[1].split(',')))

print(
    sum(
        get_erosion_level(position) % 3
        for position in cartesian_product(range(goal[0] + 1), range(goal[1] + 1))
    )
)
