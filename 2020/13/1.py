departure_time = int(input())
routes = [
    int(route)
    for route in filter(
        lambda route: route != 'x',
        input().split(','))
]

wait_times = {
    route : route - (departure_time % route)
    for route in routes
}

next_bus, wait_time = sorted(
    wait_times.items(),
    key=lambda item: item[1]
)[0]

print(next_bus * wait_time)
