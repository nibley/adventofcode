from math import prod

ps = []
vs = []
while True:
    try:
        line = input()
    except EOFError:
        break

    p, v = line.split()

    p = p.split('=')[1]
    v = v.split('=')[1]

    ps.append(tuple(map(int, p.split(','))))
    vs.append(tuple(map(int, v.split(','))))

height = 103
width = 101

# height = 7; width = 11

assert height % 2
assert width % 2

def step(ps):
    new_ps = []

    for p, v in zip(ps, vs):
        p_x, p_y = p
        v_x, v_y = v

        p_x = (p_x + v_x) % width
        p_y = (p_y + v_y) % height

        new_ps.append(
            (p_x, p_y)
        )

    return new_ps

half_height = height // 2
half_width = width // 2

# print(height, half_height)
# print(width, half_width)

for _ in range(100):
    ps = step(ps)

for y in range(height):
    for x in range(width):
        if y == half_height or x == half_width:
            print('o', end='')
        else:
            n = sum( p == (x, y) for p in ps )
            print(n or '.', end='')
    print()


quads = [0, 0, 0, 0]

for x, y in ps:
    if x < half_width and y < half_height:
        quads[0] += 1
    elif x > half_width and y < half_height:
        quads[1] += 1
    elif x < half_width and y > half_height:
        quads[2] += 1
    elif x > half_width and y > half_height:
        quads[3] += 1

print(quads)

print()
print(prod(quads))
