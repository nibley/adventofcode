target_value = int(input())

'''
37  36  35  34  33  32  31
38  17  16  15  14  13  30
39  18   5   4   3  12  29
40  19   6   1   2  11  28
41  20   7   8   9  10  27
42  21  22  23  24  25  26
43  44  45  46  47  48  49
'''

def spiral_position_generator():
    x = 0
    y = 0
    yield (x, y)
    side_length = 1
    
    while True:
        side_length += 2

        x += 1 # step right
        yield (x, y)

        for _ in range(side_length - 2): # go up
            y += 1
            yield (x, y)

        for _ in range(side_length - 1): # go left
            x -= 1
            yield (x, y)

        for _ in range(side_length - 1): # go down
            y -= 1
            yield (x, y)

        for _ in range(side_length - 1): # go right
            x += 1
            yield (x, y)

def generate_cell(position):
    x, y = position
    return sum(map(
        lambda position: grid.get(position, 0),
        [
            (x - 1, y + 1),
            (x    , y + 1),
            (x + 1, y + 1),
            (x - 1, y    ),
            (x + 1, y    ),
            (x - 1, y - 1),
            (x    , y - 1),
            (x + 1, y - 1),
        ]))

grid = { (0, 0): 1 }
g = spiral_position_generator()
next(g) # filled in first cell manually

while True:
    cell = next(g)
    cell_value = generate_cell(cell)

    if cell_value > target_value:
        print(cell_value)
        break

    grid[cell] = cell_value
