directions = input()
assert not len(directions) % 2

x_human = 0
y_human = 0
x_robot = 0
y_robot = 0
visited = set([ (x_human, y_human) ])

for direction_human, direction_robot in zip(
    directions[ : -1 : 2],
    directions[ 1 : : 2]
):
    if direction_human == '<':
        x_human -= 1
    elif direction_human == '>':
        x_human += 1
    elif direction_human == 'v':
        y_human -= 1
    elif direction_human == '^':
        y_human += 1

    if direction_robot == '<':
        x_robot -= 1
    elif direction_robot == '>':
        x_robot += 1
    elif direction_robot == 'v':
        y_robot -= 1
    elif direction_robot == '^':
        y_robot += 1

    visited.add( (x_human, y_human) )
    visited.add( (x_robot, y_robot) )

print(len(visited))
