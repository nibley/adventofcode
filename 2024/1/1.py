lines = []
while True:
    try:
        line = input()
    except EOFError:
        break

    lines.append(map(int, line.split()))

first_list, second_list = zip(*lines)
print(
    sum(
        abs(first - second)
        for first, second in zip(
            sorted(first_list),
            sorted(second_list)
        )
    )
)
