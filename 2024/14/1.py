from math import prod

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

assert HEIGHT % 2
assert WIDTH % 2

for _ in range(100):
    positions = tuple(
        ((p_x + v_x) % WIDTH, (p_y + v_y) % HEIGHT)
        for (p_x, p_y), (v_x, v_y) in zip(positions, velocities)
    )

HALF_HEIGHT = HEIGHT // 2
HALF_WIDTH = WIDTH // 2
quadrant_totals = [0, 0, 0, 0]
for p_x, p_y in positions:
    if p_x < HALF_WIDTH and p_y < HALF_HEIGHT:
        quadrant_totals[0] += 1
    elif p_x > HALF_WIDTH and p_y < HALF_HEIGHT:
        quadrant_totals[1] += 1
    elif p_x < HALF_WIDTH and p_y > HALF_HEIGHT:
        quadrant_totals[2] += 1
    elif p_x > HALF_WIDTH and p_y > HALF_HEIGHT:
        quadrant_totals[3] += 1

print(prod(quadrant_totals))
