from math import floor

flight_speeds = {}
flight_times = {}
rest_times = {}

def simulate_race(seconds):
    distances = {}
    for reindeer_name in sorted(flight_speeds):
        flight_speed = flight_speeds[reindeer_name]
        flight_time = flight_times[reindeer_name]
        rest_time = rest_times[reindeer_name]

        print(f'{reindeer_name} ({flight_speed} for {flight_time} then {rest_time})')

        cycle_time = flight_time + rest_time
        print(f'\t{cycle_time} seconds per cycle')
        complete_cycles = floor(seconds / cycle_time)
        print(f'\t{complete_cycles} complete cycles')
        remainder_time = min(flight_time, seconds - (cycle_time * complete_cycles))
        print(f'\t{remainder_time} seconds in partial')
        seconds_flown = flight_time * complete_cycles + remainder_time
        print(f'\t{seconds_flown} seconds flown')
        distance_flown = flight_speed * seconds_flown
        distances[reindeer_name] = distance_flown

        print(f'\t{distance_flown} total distance')
        print()
    
    return sorted(distances.items(), key=lambda item: item[1])[-1]

while True:
    try:
        line = input()
    except EOFError:
        break
    
    left_side, right_side = line.split(' seconds, but then must rest for ')
    reindeer_name, flight_info = left_side.split(' can fly ')
    flight_speed, _, _, flight_time = flight_info.split(' ')
    rest_time = right_side.split(' ')[0]
    flight_speeds[reindeer_name] = int(flight_speed)
    flight_times[reindeer_name] = int(flight_time)
    rest_times[reindeer_name] = int(rest_time)

race_length = 2503
print(*simulate_race(race_length))
