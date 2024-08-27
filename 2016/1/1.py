raw = input()
pieces = raw.split(', ')
instructions = []
for piece in pieces:
    left_or_right = piece[0]
    distance = int(piece[1:])
    instructions.append((left_or_right, distance))

directions = ['north', 'east', 'south', 'west']
def turn(left_or_right):
    offset = 1 if left_or_right == 'R' else -1
    facing_index = directions.index(facing)
    return directions[(facing_index + offset) % 4]

x = y = 0
facing = 'north'
for left_or_right, distance in instructions:
    facing = turn(left_or_right)
    if facing == 'north':
        y += distance
    elif facing == 'east':
        x += distance
    elif facing == 'south':
        y -= distance
    elif facing == 'west':
        x -= distance

print(abs(x) + abs(y))
