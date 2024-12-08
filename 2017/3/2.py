goal_square = int(input())

def spiral_position_generator():
    x = 0
    y = 0

    side_length = 1
    while True:
        side_length += 2

        x += 1 # step right into the next spiral layer
        yield (x, y)

        for _ in range(side_length - 2): # go up
            y -= 1
            yield (x, y)

        for _ in range(side_length - 1): # go left
            x -= 1
            yield (x, y)

        for _ in range(side_length - 1): # go down
            y += 1
            yield (x, y)

        for _ in range(side_length - 1): # go right
            x += 1
            yield (x, y)

def generate_cell(position):
    x, y = position
    return sum(
        grid.get(neighbor, 0)
        for neighbor in (
            (x - 1, y - 1),
            (x    , y - 1),
            (x + 1, y - 1),
            (x - 1, y    ),
            (x + 1, y    ),
            (x - 1, y + 1),
            (x    , y + 1),
            (x + 1, y + 1)
        )
    )

grid = {}
positions = spiral_position_generator()

position = (0, 0)
last_square = 1

grid[position] = last_square
while not last_square > goal_square:
    position = next(positions)
    last_square = generate_cell(position)
    grid[position] = last_square

print(last_square)
