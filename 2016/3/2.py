triangles = []
while True:
    try:
        lines = tuple( input() for _ in range(3) )
    except EOFError:
        break

    triangles.extend(
        sorted(triangle)
        for triangle in zip(
            *( map(int, line.split()) for line in lines )
        )
    )

print(
    sum(
        first_side + second_side > third_side
        for first_side, second_side, third_side in triangles
    )
)
