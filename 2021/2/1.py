horizontal = 0
depth = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    command, distance = line.split(' ')
    distance = int(distance)

    if command == 'forward':
        horizontal += distance
    elif command == 'down':
        depth += distance
    elif command == 'up':
        depth -= distance

print(depth * horizontal)
