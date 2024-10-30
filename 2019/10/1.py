from itertools import product as cartesian_product
from math import gcd
from functools import cache

asteroids = set()
grid = {}
y = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, cell in enumerate(line):
        position = (x, y)
        cell = cell == '#'
        grid[position] = cell
        if cell:
            asteroids.add(position)

    y += 1

height = y
width = x + 1

def in_bounds(x, y):
    return 0 <= x < width and 0 <= y < height

get_gcd = cache(gcd)

most_asteroids_seen = 0
for x, y in asteroids:
    asteroids_seen = 0
    for run, rise in cartesian_product(
        range(-width + 1, width),
        range(-height + 1, height)
    ):
        if get_gcd(run, rise) != 1:
            continue

        scan_x = x + run
        scan_y = y + rise
        while in_bounds(scan_x, scan_y):
            if grid[ (scan_x, scan_y) ]:
                asteroids_seen += 1
                break

            scan_x += run
            scan_y += rise

    if asteroids_seen > most_asteroids_seen:
        most_asteroids_seen = asteroids_seen

print(most_asteroids_seen)
