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

def walk(distance):
    steps = range(1, distance + 1)
    if facing == 'north':
        return [(x, y + i) for i in steps]
    elif facing == 'east':
        return [(x + i, y) for i in steps]
    elif facing == 'south':
        return [(x, y - i) for i in steps]
    elif facing == 'west':
        return [(x - i, y) for i in steps]

x = y = 0
locations = [(x, y)]
facing = 'north'
for left_or_right, distance in instructions:
    facing = turn(left_or_right)
    new_locations = walk(distance)

    solution = None
    for new_location in new_locations:
        if new_location in locations:
            solution = new_location
            break
    
    if solution:
        x, y = solution
        break

    x, y = new_locations[-1]
    locations.extend(new_locations)

print(abs(x) + abs(y))
