positions = {}
accelerations = {}
velocities = {}
particle_id = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    pieces = line.split('>, ')

    positions[particle_id] = tuple(map(int, pieces[0][3:].split(',')))
    velocities[particle_id] = tuple(map(int, pieces[1][3:].split(',')))
    accelerations[particle_id] = tuple(map(int, pieces[2][3:-1].split(',')))

    particle_id += 1

def get_ordering():
    return {
        particle_id : i
        for i, particle_id in enumerate(
            sorted(
                positions.keys(),
                key=lambda particle_id: sum(map(abs, positions[particle_id]))
            )
        )
    }

ordering = get_ordering()

while True:
    # reevalute the ordering after several cycles
    # to get some regression to the mean
    for _ in range(50):
        for particle_id, position in positions.items():
            velocities[particle_id] = tuple(
                acceleration_component + velocity_component
                for acceleration_component, velocity_component
                in zip(accelerations[particle_id], velocities[particle_id])
            )

            positions[particle_id] = tuple(
                velocity_component + position_component
                for velocity_component, position_component
                in zip(velocities[particle_id], position)
            )

    new_ordering = get_ordering()
    for particle_id in tuple(positions.keys()):
        if new_ordering[particle_id] > ordering[particle_id]:
            # assume particle won't stay closest
            del new_ordering[particle_id]
            del positions[particle_id]
            del velocities[particle_id]
            del accelerations[particle_id]

    if len(new_ordering) == len(ordering):
        # didn't eliminate any particles, so call it done
        break

    ordering = new_ordering

print(
    next(
        particle_id
        for particle_id in ordering
        if ordering[particle_id] == 0
    )
)
