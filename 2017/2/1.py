extrema = []
while True:
    try:
        line = input()
    except EOFError:
        break

    minimum, *_, maximum = sorted(map(int, line.split()))
    extrema.append(
        (minimum, maximum)
    )

print(
    sum(
        maximum - minimum
        for minimum, maximum in extrema
    )
)
