the_input = input()

visited = {}
x = 0
y = 0

for c in the_input:
    visited[(x, y)] = True

    if c == '<': x -= 1
    if c == '>': x += 1
    if c == 'v': y -= 1
    if c == '^': y += 1

visited[(x, y)] = True

print(len(visited))
