instructions = []
for instruction in input().split(', '):
    instructions.append( (instruction[0], int(instruction[ 1 : ])) )

directions = ('north', 'east', 'south', 'west')
facing = 0 # index into directions

x, y = (0, 0)
for direction, distance in instructions:
    facing = (facing + (1 if direction == 'R' else -1)) % 4

    if facing == 0:
        y += distance
    elif facing == 1:
        x += distance
    elif facing == 2:
        y -= distance
    elif facing == 3:
        x -= distance

print(abs(x) + abs(y))
