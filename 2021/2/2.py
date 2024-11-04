horizontal = 0
depth = 0
aim = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    command, distance = line.split(' ')
    distance = int(distance)

    if command == 'forward':
        horizontal += distance
        depth += aim * distance
    elif command == 'down':
        aim += distance
    elif command == 'up':
        aim -= distance

print(depth * horizontal)
