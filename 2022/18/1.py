from collections import defaultdict

cubes = []
while True:
    try:
        line = input()
    except EOFError:
        break

    x, y, z = map(int, line.split(','))
    cubes.append( (x, y, z) )

sorted_x_values = sorted(set(cube[0] for cube in cubes))
low_x, high_x = sorted_x_values[0], sorted_x_values[-1]

sorted_y_values = sorted(set(cube[1] for cube in cubes))
low_y, high_y = sorted_y_values[0], sorted_y_values[-1]

sorted_z_values = sorted(set(cube[2] for cube in cubes))
low_z, high_z = sorted_z_values[0], sorted_z_values[-1]

arrangement = {}
for x in range(low_x - 1, high_x + 2):
    arrangement[x] = {}
    for y in range(low_y - 1, high_y + 2):
        # true means air
        arrangement[x][y] = defaultdict(lambda: True)

for x, y, z in cubes:
    # false means no air
    arrangement[x][y][z] = False

surface_area = 0
for x, y, z in cubes:
    neighbors = [
        arrangement[x][y + 1][z],
        arrangement[x][y - 1][z],
        arrangement[x - 1][y][z],
        arrangement[x + 1][y][z],
        arrangement[x][y][z + 1],
        arrangement[x][y][z - 1]
    ]

    # true values for air count in the sum
    surface_area += sum(neighbors)

print(surface_area)
