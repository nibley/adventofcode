instructions = []
while True:
    try:
        line = input()
    except EOFError:
        break

    command, steps = line[0], line[1:]
    steps = int(steps)
    instructions.append( (command, steps) )

ship_x = ship_y = 0
waypoint_x, waypoint_y = 10, 1

for command, steps in instructions:
    if command == 'F':
        ship_x += steps * waypoint_x
        ship_y += steps * waypoint_y
    elif command in 'LR':
        offset = 1 if command == 'R' else -1
        for _ in range(steps // 90):
            waypoint_x *= -1 * offset
            waypoint_y *= offset
            waypoint_x, waypoint_y = waypoint_y, waypoint_x
    elif command == 'N':
        waypoint_y += steps
    elif command == 'S':
        waypoint_y -= steps
    elif command == 'E':
        waypoint_x += steps
    elif command == 'W':
        waypoint_x -= steps
    
print(abs(ship_x) + abs(ship_y))
