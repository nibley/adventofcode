from itertools import product as cartesian_product

grid = dict.fromkeys(
    cartesian_product(range(1000), repeat=2),
    False
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
        None if line.startswith('toggle')
        else line.startswith('turn on')
    )
    commands.append( (command, start, end) )

for command, (start_x, start_y), (end_x, end_y) in commands:
    for position in cartesian_product(
        range(start_x, end_x + 1),
        range(start_y, end_y + 1)
    ):
        if command is None:
            grid[position] ^= True
        else:
            grid[position] = command

print(sum(grid.values()))
