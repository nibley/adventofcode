instructions = []
while True:
    try:
        line = input()
    except EOFError:
        break

    command, steps = line[0], line[1:]
    steps = int(steps)
    instructions.append( (command, steps) )

cardinal_directions = 'NESW'
facing = 'E'
x = y = 0

for command, steps in instructions:
    if command == 'F':
        command = facing

    if command in 'LR':
        turn = (steps // 90) * (1 if command == 'R' else -1)
        facing = cardinal_directions[
            (cardinal_directions.index(facing) + turn) % 4
        ]
    elif command == 'N':
        y += steps
    elif command == 'S':
        y -= steps
    elif command == 'E':
        x += steps
    elif command == 'W':
        x -= steps

print(abs(x) + abs(y))
