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

    reindeer.append(map(int, (flight_speed, flight_time, rest_time)))

RACE_LENGTH = 2503
distances = []
for flight_speed, flight_time, rest_time in reindeer:
    cycle_time = flight_time + rest_time
    complete_cycles, remainder_time = divmod(RACE_LENGTH, cycle_time)
    remainder_time = min(flight_time, remainder_time)

    seconds_flown = flight_time * complete_cycles + remainder_time
    distance_flown = flight_speed * seconds_flown

    distances.append(distance_flown)

print(max(distances))
