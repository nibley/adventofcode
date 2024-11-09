sensors = []
beacons = []
while True:
    try:
        line = input()
    except EOFError:
        break

    sensor, beacon = (
        tuple(
            int(coord.split('=')[1])
            for coord in piece.split(', ')
        )
        for piece in line.split(': ')
    )

    sensors.append(sensor)
    beacons.append(beacon)

def get_x_neighborhood(position, radius):
    sensor_x, sensor_y = position

    delta_y = radius
    if sensor_y - delta_y <= desired_row <= sensor_y + delta_y + 1:
        delta_x = radius - abs(sensor_y - desired_row)
        for x in range(sensor_x - delta_x, sensor_x + delta_x + 1):
            yield x

desired_row = 2_000_000
x_values_without_beacons = set()

for sensor, beacon in zip(sensors, beacons):
    distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    x_values_without_beacons.update(get_x_neighborhood(sensor, distance))

# actual beacon positions got marked as
# not being able to contain beacons above
for beacon_x, beacon_y in beacons:
    if beacon_y == desired_row:
        x_values_without_beacons.discard(beacon_x)

print(len(x_values_without_beacons))
