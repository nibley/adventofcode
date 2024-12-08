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
            nodes.setdefault(char, set()).add(
                (x, y)
            )

    y += 1

HEIGHT = y
WIDTH = len(line)

def antinode_is_in_bounds(antinode_x, antinode_y):
    return antinode_x in range(WIDTH) and antinode_y in range(HEIGHT)

antinodes = set()
for frequency, positions in nodes.items():
    for (first_x, first_y), (second_x, second_y) in combinations(positions, 2):
        delta_x = second_x - first_x
        delta_y = second_y - first_y

        antinode_x, antinode_y = first_x, first_y
        while antinode_is_in_bounds(antinode_x, antinode_y):
            antinodes.add(
                (antinode_x, antinode_y)
            )

            antinode_x -= delta_x
            antinode_y -= delta_y

        antinode_x, antinode_y = second_x, second_y
        while antinode_is_in_bounds(antinode_x, antinode_y):
            antinodes.add(
                (antinode_x, antinode_y)
            )

            antinode_x += delta_x
            antinode_y += delta_y

print(len(antinodes))
