from collections import defaultdict
from itertools import product as cartesian_product

regions = []
while True:
    try:
        line = input()
    except EOFError:
        break

    left_side, right_side = line.split(' ')

    operation = left_side == 'on' # True for on, False for off
    axes = []
    for axis in right_side.split(','):
        range_start, range_end = map(int, axis.split('=')[1].split('..'))
        axes.append(range(max(-50, range_start), min(50, range_end) + 1))

    regions.append( (operation, cartesian_product(*axes)) )

grid = defaultdict(lambda: False)
for operation, cubes in regions:
    for cube in cubes:
        grid[cube] = operation

print(sum(grid.values()))
