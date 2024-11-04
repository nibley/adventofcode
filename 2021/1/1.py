readings = []
while True:
    try:
        line = input()
    except EOFError:
        break

    readings.append(int(line))

print(
    sum(
        readings[i + 1] > reading
        for i, reading in enumerate(readings[ : -1 ])
    )
)
