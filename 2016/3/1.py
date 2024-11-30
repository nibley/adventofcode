triangles = []
while True:
    try:
        lines = tuple( input() for _ in range(3) )
    except EOFError:
        break

    for line in lines:
        triangles.append(sorted(map(int, line.split())))

print(
    sum(
        first_side + second_side > third_side
        for first_side, second_side, third_side in triangles
    )
)
