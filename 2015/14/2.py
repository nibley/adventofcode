reindeer = []
while True:
    try:
        line = input()
    except EOFError:
        break

    (
        _, _, _,
        flight_speed, _, _,
        flight_time, _, _, _, _, _, _,
        rest_time, _
    ) = line.split()

    reindeer.append(
        tuple( int(stat) for stat in (flight_speed, flight_time, rest_time) )
    )

all_zeros = [ 0 for _ in reindeer ]
distances = all_zeros[ : ]
scores = all_zeros[ : ]
remaining_rests = all_zeros[ : ]
remaining_flights = [ flight_time for _, flight_time, _ in reindeer ]

RACE_LENGTH = 2503
for _ in range(RACE_LENGTH):
    for i, (remaining_flight, remaining_rest, current_reindeer) in enumerate(
        zip(remaining_flights, remaining_rests, reindeer)
    ):
        flight_speed, flight_time, rest_time = current_reindeer

        if remaining_flight == -1:
            # resting
            if remaining_rest == 0:
                # exit rest
                remaining_flights[i] = flight_time - 1 # fly one second now
                distances[i] += flight_speed
            else:
                # continue resting
                remaining_rests[i] -= 1
        else:
            # flying
            if remaining_flight == 0:
                # enter rest
                remaining_rests[i] = rest_time - 1 # rest one second now
                remaining_flights[i] = -1 # mark resting
            else:
                # continue flying
                remaining_flights[i] -= 1
                distances[i] += flight_speed

    max_distance = max(distances)
    for i, distance in enumerate(distances):
        if distance == max_distance:
            scores[i] += 1

print(max(scores))
