from itertools import combinations

nodes = {}
y = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, char in enumerate(line):
        if char != '.':
            nodes.setdefault(char, set()).add( (x, y) )

    y += 1

height = y
width = len(line)

for k, v in nodes.items():
    print(k, v)

anti = set()

for char, positions in nodes.items():
    for pair in combinations(positions, 2):
        (first_x, first_y), (second_x, second_y) = pair
        delta_x = second_x - first_x
        delta_y = second_y - first_y

        x, y = first_x, first_y
        while x in range(width) and y in range(height):
            anti.add( (x, y) )
            x -= delta_x
            y -= delta_y

        x, y = second_x, second_y
        while x in range(width) and y in range(height):
            anti.add( (x, y) )
            x += delta_x
            y += delta_y

        # first_anti = (second_x + delta_x, second_y + delta_y)
        # if first_anti[0] in range(width) and first_anti[1] in range(height):
        #     anti.add(first_anti)

        # second_anti = (first_x - delta_x, first_y - delta_y)
        # if second_anti[0] in range(width) and second_anti[1] in range(height):
        #     anti.add(second_anti)

    for position in positions:
        if len(positions) > 2:
            anti.add(position)

print(len(anti))
