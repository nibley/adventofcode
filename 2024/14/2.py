from itertools import groupby

positions = []
velocities = []
while True:
    try:
        line = input()
    except EOFError:
        break

    position, velocity = (
        tuple( int(n) for n in vector.split('=')[1].split(',') )
        for vector in line.split()
    )

    positions.append(position)
    velocities.append(velocity)

HEIGHT = 103
WIDTH = 101

def has_long_vertical(y_values):
    TARGET_LENGTH = 10

    if len(y_values) < TARGET_LENGTH:
        return False

    min_y, *_, max_y = sorted(y_values)
    for key, group in groupby(
        range(min_y, max_y + 1),
        key=y_values.__contains__
    ):
        if key and sum( 1 for _ in group ) > TARGET_LENGTH:
            return True

    return False

t = 0
while True:
    t += 1

    positions = tuple(
        ((p_x + v_x) % WIDTH, (p_y + v_y) % HEIGHT)
        for (p_x, p_y), (v_x, v_y) in zip(positions, velocities)
    )

    robots_by_column = {}
    for p_x, p_y in positions:
        robots_by_column.setdefault(p_x, set()).add(p_y)

    if any(map(has_long_vertical, robots_by_column.values())):
        break

def visualize():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print('o' if (x, y) in positions else '.', end='')
        print()
    print()
# visualize()

print(t)
