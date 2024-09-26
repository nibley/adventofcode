from math import inf
from collections import defaultdict

locations = []
while True:
    try:
        line = input()
    except EOFError:
        break
    
    locations.append(tuple(map(int, line.split(', '))))
location_labels = [chr(32 + i) for i in range(len(locations))]

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

area_sizes = defaultdict(lambda: 0)
for x in range(width):
    for y in range(height):
        cell = (x, y)
        closest_location = None
        shortest_distance = inf
        distance_tied = False

        distances = [(label, get_distance(cell, location)) \
            for label, location in zip(location_labels, locations)]

        for label, distance in distances:
            if distance < shortest_distance:
                closest_location = label
                shortest_distance = distance

        distance_tied = len([item for item in distances \
            if item[1] == shortest_distance] ) > 1

        if distance_tied:
            grid[y][x] = '.'
        else:
            grid[y][x] = closest_location
            area_sizes[closest_location] += 1

for row in [0, height]:
    for column in [0, width]:
        for x in range(0, column):
            area_sizes.pop(grid[row][x], None)
        
        for y in range(0, row):
            area_sizes.pop(grid[y][column], None)

for row in grid:
    print(''.join(row))

print()
largest_area, largest_area_size = sorted(area_sizes.items(), \
    key=lambda item: item[1]
)[-1]
print(f'Largest area is {largest_area} with size:')
print(f'{largest_area_size}')
