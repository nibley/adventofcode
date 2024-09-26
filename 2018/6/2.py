from math import inf
from collections import defaultdict

locations = []
while True:
    try:
        line = input()
    except EOFError:
        break
    
    locations.append(tuple(map(int, line.split(', '))))

sorted_by_x = sorted(locations, key=lambda location: location[0])
low_x, high_x = sorted_by_x[0][0], sorted_by_x[-1][0]

sorted_by_y = sorted(locations, key=lambda location: location[1])
low_y, high_y = sorted_by_y[0][1], sorted_by_y[-1][1]

width, height = high_x + 1, high_y + 1

grid = []
for row in range(0, height + 1):
    grid.append(['.'] * (width + 1))

def get_distance(first_location, second_location):
    return abs(first_location[0] - second_location[0]) + \
        abs(first_location[1] - second_location[1])

safe_cells = 0
for x in range(width):
    for y in range(height):
        cell = (x, y)

        distances = [get_distance(cell, location) for location in locations]
        cell_is_safe = sum(distances) < 10_000

        if cell_is_safe:
            grid[y][x] = '#'
            safe_cells += 1

for row in grid:
    print(''.join(row))

print()
print(safe_cells)

