from itertools import combinations

positions = []
while True:
    try:
        line = input()
    except EOFError:
        break

    pieces = line[1:-1].split(',')
    position = [ int(piece.split('=')[1]) for piece in pieces ]
    positions.append(position)

velocities = [ [0, 0, 0] for _ in positions ]

for _ in range(1000):
    # gravity effects velocity
    for first_index, second_index in combinations(range(len(positions)), 2):
        first_planet = positions[first_index]
        second_planet = positions[second_index]

        for axis_index, (first_position, second_position) \
                in enumerate(zip(first_planet, second_planet)):
            if first_position == second_position:
                continue

            if first_position > second_position:
                velocities[first_index][axis_index] -= 1
                velocities[second_index][axis_index] += 1
            else:
                velocities[first_index][axis_index] += 1
                velocities[second_index][axis_index] -= 1

    # velocity effects position
    for planet_index, velocity in enumerate(velocities):
        for axis_index, component in enumerate(velocity):
            positions[planet_index][axis_index] += component

total = 0
for position, velocity in zip(positions, velocities):
    position_total = sum(map(abs, position))
    velocity_total = sum(map(abs, velocity))

    total += position_total * velocity_total

print(total)
