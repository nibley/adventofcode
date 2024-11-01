positions = []
velocities = []
while True:
    try:
        line = input()
    except EOFError:
        break

    left_side, right_side = line.split(' velocity=')
    position = tuple(
        int(piece.strip())
        for piece in left_side.split('position=')[1][1 : -1].split(',')
    )
    positions.append(position)

    velocity = tuple(
        int(piece.strip())
        for piece in right_side[1 : -1].split(',')
    )
    velocities.append(velocity)

min_y, *_, max_y = sorted(y for _, y in positions)
turns = 0
while max_y - min_y > 10: # bound determined by observation
    turns += 1
    positions = tuple(
        (x + velocity_x, y + velocity_y)
        for (x, y), (velocity_x, velocity_y) in zip(positions, velocities)
    )
    min_y, *_, max_y = sorted(y for _, y in positions)

print(turns)
