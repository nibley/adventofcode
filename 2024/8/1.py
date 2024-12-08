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

        first_antinode_x = second_x + delta_x
        first_antinode_y = second_y + delta_y
        if antinode_is_in_bounds(first_antinode_x, first_antinode_y):
            antinodes.add(
                (first_antinode_x, first_antinode_y)
            )

        second_antinode_x = first_x - delta_x
        second_antinode_y = first_y - delta_y
        if antinode_is_in_bounds(second_antinode_x, second_antinode_y):
            antinodes.add(
                (second_antinode_x, second_antinode_y)
            )

print(len(antinodes))
