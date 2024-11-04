readings = []
while True:
    try:
        line = input()
    except EOFError:
        break

    readings.append(int(line))

print(
    sum(
        sum(readings[ i + 1 : i + 4 ]) > sum(readings[ i : i + 3 ])
        for i, _ in enumerate(readings[ : -3 ])
    )
)
