from math import prod
from itertools import combinations

f = open('input.txt', 'r')
f = iter(f.readlines())

ps = []
vs = []
while True:
    try:
        # line = input()
        line = next(f)
    except (EOFError, StopIteration):
        break

    p, v = line.split()

    p = p.split('=')[1]
    v = v.split('=')[1]

    ps.append(tuple(map(int, p.split(','))))
    vs.append(tuple(map(int, v.split(','))))

height = 103
width = 101

# height = 7; width = 11

assert height % 2
assert width % 2

def step(ps):
    cells_with_robots = {}
    new_ps = []

    for p, v in zip(ps, vs):
        p_x, p_y = p
        v_x, v_y = v

        p_x = (p_x + v_x) % width
        p_y = (p_y + v_y) % height

        new_p = (p_x, p_y)
        new_ps.append(new_p)
        cells_with_robots.setdefault(p_x, set()).add(p_y)

    return new_ps, cells_with_robots

half_height = height // 2
half_width = width // 2

# print(height, half_height)
# print(width, half_width)

# for _ in range(100):
    # ps = step(ps)

def visualize(ps):
    for y in range(height):
        for x in range(width):
            if y == half_height or x == half_width:
                print('.', end='')
            else:
                n = sum( p == (x, y) for p in ps )
                print(n or '.', end='')
        print()
    print()

def get_hotness(vals):
    # sorted_vals = sorted(vals)
    # sorted_vals = set(sorted(vals))

    low, *_, high = sorted(vals)

    misses = sum(
        i not in vals
        # for i in range(sorted_vals[0], sorted_vals[-1] + 1)
        for i in range(low, high + 1)
    )

    return misses < 60

t = 0
while True:
    # visualize(ps)
    print(t)

    ps, cells_with_robots = step(ps)
    t += 1

    hot_cols = tuple(
        x_key
        for x_key, y_vals in cells_with_robots.items()
        if len(y_vals) > 30
    )

    if hot_cols and any(
        get_hotness(cells_with_robots[col])
        # sorted(cells_with_robots[col])
        for col in hot_cols
    ):

    # if any(
        # len(y_vals) > 30
        # for x_key, y_vals in cells_with_robots.items()
    # ):

    # if hot_cols:

        visualize(ps)
        print(t, 'hot')
        input()
    else:
        print(t)

    # input()

# scanned to 1150
