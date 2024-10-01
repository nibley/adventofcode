from collections import defaultdict

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

while True:
    old_num_particles = len(positions)

    # reevalute the number of particles after
    # several cycles to get some regression to the mean
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
        
        particles_by_position = defaultdict(list)
        for particle_id, position in positions.items():
            particles_by_position[position].append(particle_id)

        for position, particle_ids in particles_by_position.items():
            if len(particle_ids) < 2:
                continue

            for particle_id in particle_ids:
                del positions[particle_id]
                del velocities[particle_id]
                del accelerations[particle_id]
    
    if len(positions) == old_num_particles:
        break
    old_num_particles = len(positions)

print(len(positions))
