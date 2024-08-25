from math import floor

def simulate_race(seconds):
    for second in range(seconds):
        for reindeer_name in reindeer_names:
            flight_speed = flight_speeds[reindeer_name]
            flight_time = flight_times[reindeer_name]
            rest_time = rest_times[reindeer_name]

            remaining_rest = remaining_rests[reindeer_name]
            remaining_flight = remaining_flights[reindeer_name]

            if remaining_flight == -1: # resting
                if remaining_rest == 0: # exit rest
                    remaining_flights[reindeer_name] = flight_time - 1 # fly one second now
                    distances[reindeer_name] += flight_speed
                else:
                    remaining_rests[reindeer_name] -= 1
            else: # flying
                if remaining_flight == 0: # enter rest
                    remaining_rests[reindeer_name] = rest_time - 1 # rest one second now
                    remaining_flights[reindeer_name] = -1 # mark resting
                else:
                    remaining_flights[reindeer_name] -= 1
                    distances[reindeer_name] += flight_speed

        max_distance = sorted(distances.items(), key=lambda item: item[1])[-1][1]
        for reindeer_name in reindeer_names:
            if distances[reindeer_name] == max_distance:
                scores[reindeer_name] += 1
        
    for item in scores.items():
        print(item)
    return sorted(scores.items(), key=lambda item: item[1])[-1]

flight_speeds = {}
flight_times = {}
rest_times = {}

remaining_flights = {}
remaining_rests = {}

distances = {}
scores = {}

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

reindeer_names = sorted(flight_speeds.keys())
for reindeer_name in reindeer_names:
    remaining_rests[reindeer_name] = 0
    remaining_flights[reindeer_name] = flight_times[reindeer_name]
    distances[reindeer_name] = 0
    scores[reindeer_name] = 0

print(*simulate_race(2503))
