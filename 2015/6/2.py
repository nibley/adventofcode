from itertools import product as cartesian_product

grid = dict.fromkeys(
    cartesian_product(range(1000), repeat=2),
    0
)

commands = []
while True:
    try:
        line = input()
    except EOFError:
        break

    *_, start, _, end = line.split()
    start, end = (
        map(int, position.split(','))
        for position in (start, end)
    )

    command = (
        None if line.startswith('turn off')
        else 2 if line.startswith('toggle')
        else 1
    )
    commands.append( (command, start, end) )

for command, (start_x, start_y), (end_x, end_y) in commands:
    for position in cartesian_product(
        range(start_x, end_x + 1),
        range(start_y, end_y + 1)
    ):
        if command is None:
            grid[position] = max(grid[position] - 1, 0)
        else:
            grid[position] += command

print(sum(grid.values()))
