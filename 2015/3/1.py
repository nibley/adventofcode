directions = input()

x = 0
y = 0
visited = set([ (x, y) ])

for direction in directions:
    if direction == '<':
        x -= 1
    elif direction == '>':
        x += 1
    elif direction == 'v':
        y -= 1
    elif direction == '^':
        y += 1

    visited.add( (x, y) )

print(len(visited))
