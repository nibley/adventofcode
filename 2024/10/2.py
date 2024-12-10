from math import inf

starts = []
grid = {}
y = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    for x, digit in enumerate(line):
        position = (x, y)
        if digit == '0':
            starts.append(position)

        grid[position] = int(digit)

    y += 1

def get_score(start):
    visited = set([start])
    while True:
        x, y = start
        height = grid[start]

        if height == 9:
            return 1

        subtotal = 0
        for x_offset, y_offset in (
            ( 0, -1),
            ( 1,  0),
            (-1,  0),
            ( 0,  1)
        ):
            neighbor = (x + x_offset, y + y_offset)
            neighbor_height = grid.get(neighbor, inf)

            if neighbor_height - height == 1:
                subtotal += get_score(neighbor)

        return subtotal

print(sum(map(get_score, starts)))
