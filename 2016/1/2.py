instructions = []
for instruction in input().split(', '):
    instructions.append( (instruction[0], int(instruction[ 1 : ])) )

def walk(position, facing, distance):
    x, y = position

    for _ in range(distance):
        if facing == 0:
            y += 1
        elif facing == 1:
            x += 1
        elif facing == 2:
            y -= 1
        elif facing == 3:
            x -= 1

        yield (x, y)

directions = ('north', 'east', 'south', 'west')
facing = 0 # index into directions

x, y = (0, 0)
visited = set()
done = False
for direction, distance in instructions:
    facing = (facing + (1 if direction == 'R' else -1)) % 4

    for position in walk((x, y), facing, distance):
        if position in visited:
            done = True
            break
        else:
            visited.add(position)

    x, y = position # the last position from walk

    if done:
        break

print(abs(x) + abs(y))
