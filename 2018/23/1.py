def get_distance(first_position, second_position):
    return sum(
        abs(first_coord - second_coord)
        for first_coord, second_coord in zip(first_position, second_position)
    )

nanobots = []
while True:
    try:
        line = input()
    except EOFError:
        break

    left_side, right_side = line.split(', ')
    radius = int(right_side.split('=')[1])
    position = tuple(
        int(n)
        for n in left_side.split('=<')[1][:-1].split(',')
    )

    nanobots.append( (radius, position) )

base_radius, base_position = max(nanobots)
print(
    sum(
        get_distance(base_position, position) <= base_radius
        for _, position in nanobots
    )
)